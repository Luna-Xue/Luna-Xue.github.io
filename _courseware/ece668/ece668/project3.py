"""Project 3: deadline-aware allocation and tabular Q-learning."""

import argparse
from collections import deque
import random
from pathlib import Path

from .common import mean, percentile, poisson, save_csv, save_json


SHARES = (.1, .3, .5, .7, .9)


class AllocationEnv:
    """Two FIFO service classes; one slot is an abstract scheduling interval."""

    def __init__(self, seed=0, shifted=False, horizon=120):
        if horizon < 1:
            raise ValueError("horizon must be positive")
        rng = random.Random(seed)
        self.horizon = horizon
        # Precompute exogenous events so all policies face the same experiment.
        self.events = []
        for t in range(horizon):
            rates = (7, 3) if shifted else (3, 7)
            burst = 4 if 35 <= t % 80 < 50 else 0
            self.events.append(([poisson(rng, rates[0]+burst), poisson(rng, rates[1])],
                                rng.choice((10, 12, 14))))
        self.reset()

    def reset(self):
        self.t = 0
        self.queues = [deque(), deque()]
        self.arrived, self.served, self.expired = [0, 0], [0, 0], [0, 0]
        self.delays = []
        self.total_reward = 0
        self._arrive()
        return self.observe()

    def _arrive(self):
        for i, count in enumerate(self.events[self.t][0]):
            self.queues[i].extend([self.t] * count)
            self.arrived[i] += count

    def observe(self):
        return {"queues": [len(q) for q in self.queues],
                "head_age": [self.t-q[0] if q else 0 for q in self.queues],
                "capacity": self.events[self.t][1] if self.t < self.horizon else 0}

    def step(self, action):
        if self.t >= self.horizon:
            raise RuntimeError("Episode ended; reset before stepping")
        if not isinstance(action, int) or not 0 <= action < len(SHARES):
            raise ValueError("Action must be an integer from 0 to 4")
        capacity = self.events[self.t][1]
        first = round(capacity * SHARES[action])
        allocations = [first, capacity-first]
        completed, expired_now = 0, 0
        for i, (queue, budget, deadline) in enumerate(zip(self.queues, allocations, (4, 20))):
            # A packet whose end-of-slot delay would exceed the deadline is lost.
            while queue and self.t-queue[0]+1 > deadline:
                queue.popleft()
                self.expired[i] += 1
                expired_now += 1
            for _ in range(min(budget, len(queue))):
                born = queue.popleft()
                self.delays.append(self.t-born+1)
                self.served[i] += 1
                completed += 1
        reward = completed - 2 * expired_now - .02 * sum(map(len, self.queues))
        self.total_reward += reward
        self.t += 1
        done = self.t == self.horizon
        if not done:
            self._arrive()
        return self.observe(), reward, done

    def report(self):
        pending = [len(q) for q in self.queues]
        total, squares = sum(self.served), sum(v*v for v in self.served)
        return {"throughput": total/self.horizon, "p95_delay_served": percentile(self.delays, .95),
                "expired_fraction": sum(self.expired)/max(1, sum(self.arrived)),
                "pending_fraction": sum(pending)/max(1, sum(self.arrived)),
                "jain_served": total*total/(2*squares) if squares else 0,
                "reward": self.total_reward, "arrived_0": self.arrived[0], "arrived_1": self.arrived[1],
                "served_0": self.served[0], "served_1": self.served[1],
                "expired_0": self.expired[0], "expired_1": self.expired[1],
                "pending_0": pending[0], "pending_1": pending[1]}


def state(observation):
    bins = [min(3, q//6) for q in observation["queues"]]
    urgent = int(observation["head_age"][0] >= 2)
    return ":".join(map(str, bins + [urgent, observation["capacity"]]))


def greedy(q, observation):
    values = q.get(state(observation), [0.0] * len(SHARES))
    # Prefer the central allocation on ties, including unseen states.
    return max(range(len(SHARES)), key=lambda a: (values[a], -abs(a-2)))


def train(episodes=100, seed=7):
    q, rng = {}, random.Random(seed)
    for episode in range(episodes):
        env = AllocationEnv(seed=episode)
        observation, done = env.observe(), False
        epsilon = max(.05, .8*(1-episode/max(1, episodes)))
        while not done:
            key = state(observation)
            values = q.setdefault(key, [0.0]*len(SHARES))
            action = rng.randrange(len(SHARES)) if rng.random() < epsilon else greedy(q, observation)
            next_observation, reward, done = env.step(action)
            future = 0 if done else max(q.get(state(next_observation), [0.0]*len(SHARES)))
            values[action] += .12*(reward + .9*future - values[action])
            observation = next_observation
    return q


def equal_share(observation):
    return 2


def demand_share(observation):
    first, second = observation["queues"]
    share = first/max(1, first+second)
    return min(range(len(SHARES)), key=lambda a: abs(SHARES[a]-share))


def evaluate(policy, seed, shifted=False):
    env = AllocationEnv(seed, shifted)
    observation, done = env.observe(), False
    while not done:
        observation, _, done = env.step(policy(observation))
    return env.report()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default="runs/p3")
    parser.add_argument("--episodes", type=int, default=100)
    parser.add_argument("--train-seed", type=int, default=7)
    parser.add_argument("--eval-episodes", type=int, default=20)
    parser.add_argument("--student", action="store_true")
    args = parser.parse_args()
    if not 1 <= args.episodes <= 10000 or args.eval_episodes < 1:
        parser.error("--episodes must be 1..10000 and --eval-episodes must be positive")
    q, out = train(args.episodes, args.train_seed), Path(args.out)
    save_json(out / "qtable.json", q)
    policies = {"equal": equal_share, "demand": demand_share, "q_learning": lambda obs: greedy(q, obs)}
    if args.student:
        from student.policies import allocate
        policies["student"] = allocate
    rows = []
    for scenario, shifted in (("test", False), ("shift", True)):
        for name, policy in policies.items():
            for episode in range(args.eval_episodes):
                seed = 10000+episode
                rows.append(dict(evaluate(policy, seed, shifted), policy=name, scenario=scenario, seed=seed))
    save_csv(out / "metrics.csv", rows)
    summary = [{"scenario": scenario, "policy": policy,
                "mean_throughput": mean(r["throughput"] for r in rows if r["scenario"] == scenario and r["policy"] == policy)}
               for scenario in ("test", "shift") for policy in policies]
    save_json(out / "summary.json", summary)
    save_json(out / "config.json", {"episodes": args.episodes, "eval_episodes": args.eval_episodes,
              "training_episode_seeds": [0, args.episodes-1], "training_policy_seed": args.train_seed,
              "test_seed_start": 10000,
              "action_shares": SHARES, "deadlines": [4, 20], "synthetic": True})
    print(f"Project 3: Q-table and paired policy evaluations written to {out}")


if __name__ == "__main__":
    main()
