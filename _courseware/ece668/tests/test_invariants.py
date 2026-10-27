"""Check scientific invariants and split boundaries, not only CLI execution."""

import json
import random
import unittest

from ece668 import project1 as p1, project2 as p2, project3 as p3, project4 as p4


class NetworkTests(unittest.TestCase):
    def test_packet_conservation_and_queue_bound(self):
        for scenario in ("steady", "burst", "degraded"):
            report, trace, packets = p1.simulate(p1.DEFAULT, scenario, 4, p1.queue_aware)
            self.assertEqual(report["generated"], report["dropped"] + len(packets))
            self.assertEqual(sum(report["routed"]), report["generated"])
            self.assertTrue(all(row[f"queue_{i}"] <= p1.DEFAULT["buffer"] for row in trace for i in (0, 1)))
            self.assertTrue(all(p["delay"] > 0 for p in packets))

    def test_paired_traffic_does_not_depend_on_policy_randomness(self):
        a = p1.simulate(p1.DEFAULT, "burst", 6, p1.shortest)[1]
        b = p1.simulate(p1.DEFAULT, "burst", 6, lambda obs, rng: rng.randrange(len(obs)))[1]
        slots = p1.DEFAULT["slots"]
        self.assertEqual([r["arrivals"] for r in a[:slots]], [r["arrivals"] for r in b[:slots]])

    def test_fifo_and_no_traffic(self):
        _, _, packets = p1.simulate(p1.DEFAULT)
        for path in (0, 1):
            arrivals = [p["arrival"] for p in packets if p["path"] == path]
            self.assertEqual(arrivals, sorted(arrivals))
        report, _, _ = p1.simulate(dict(p1.DEFAULT, arrival_rate=0))
        self.assertEqual(report["generated"], 0)
        self.assertIsNone(report["p95_delay"])


class ForecastTests(unittest.TestCase):
    def test_episode_disjointness_and_causality(self):
        rows = p2.dataset()
        groups = {s: {r["episode"] for r in rows if r["split"] == s} for s in ("train", "validation", "test", "shift")}
        for a in groups:
            for b in groups:
                if a != b:
                    self.assertTrue(groups[a].isdisjoint(groups[b]))
        for row in rows[::47]:
            values = p2.episode(row["episode"], row["split"] == "shift")
            t = row["target_slot"]
            self.assertEqual(p2.history_of(row), values[t-p2.HISTORY:t])
            self.assertEqual(row["target"], values[t])

    def test_training_fits_known_relationship_and_roundtrips(self):
        x = [[i/10] for i in range(40)]
        y = [3*row[0]+2 for row in x]
        model = p2.train(x, y, penalty=0)
        restored = json.loads(json.dumps(model))
        self.assertAlmostEqual(p2.predict(restored, [2.5]), 9.5, places=4)


class AllocationTests(unittest.TestCase):
    def test_capacity_and_packet_conservation(self):
        env, rng = p3.AllocationEnv(seed=1), random.Random(9)
        done = False
        while not done:
            capacity, previous = env.observe()["capacity"], sum(env.served)
            _, _, done = env.step(rng.randrange(5))
            self.assertLessEqual(sum(env.served)-previous, capacity)
            for i in (0, 1):
                self.assertEqual(env.arrived[i], env.served[i]+env.expired[i]+len(env.queues[i]))

    def test_reset_replays_and_rejects_invalid_action(self):
        env = p3.AllocationEnv(seed=1)
        start = env.observe()
        first = env.step(2)
        self.assertEqual(start, env.reset())
        self.assertEqual(first, env.step(2))
        with self.assertRaises(ValueError):
            env.step(8)

    def test_saved_policy_matches_in_memory_policy(self):
        q = p3.train(5)
        restored = json.loads(json.dumps(q))
        self.assertEqual(p3.evaluate(lambda obs: p3.greedy(q, obs), 10001),
                         p3.evaluate(lambda obs: p3.greedy(restored, obs), 10001))


class AgentTests(unittest.TestCase):
    def test_no_initial_fault_label_and_bounded_unknown_tools(self):
        one, two = p4.Incident(1), p4.Incident(2)
        self.assertEqual(one.observation(), two.observation())
        for _ in range(8):
            one.call("not_a_tool")
        self.assertTrue(one.done)
        self.assertEqual(one.errors, 8)
        self.assertFalse(one.verified)

    def test_rules_require_verification_and_fail_on_two_faults(self):
        for seed in range(12):
            result, log = p4.evaluate(p4.expert, seed)
            self.assertEqual(result["verified_success"], 1)
            self.assertEqual(log[-1]["tool"], "verify")
            result, _ = p4.evaluate(p4.expert, seed, shifted=True)
            self.assertEqual(result["verified_success"], 0)

    def test_train_and_load_agent_without_hidden_state(self):
        demos = p4.collect(48)
        tree = p4.train_tree([d["features"] for d in demos], [d["action"] for d in demos])
        tree = json.loads(json.dumps(tree))
        successes = [p4.evaluate(lambda obs: p4.tree_action(tree, obs), seed)[0]["verified_success"]
                     for seed in range(20000, 20020)]
        self.assertGreaterEqual(sum(successes), 18)


if __name__ == "__main__":
    unittest.main()
