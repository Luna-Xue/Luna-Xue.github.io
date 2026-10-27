"""Project 4: train a small tool-selection agent in a synthetic network sandbox."""

import argparse
from collections import Counter
import json
import random
from pathlib import Path

from .common import mean, save_csv, save_json


FAULTS = ("congestion", "link", "route", "service")
FIXES = {"shape_traffic": "congestion", "restore_link": "link",
         "repair_route": "route", "restart_service": "service"}
READS = ("read_metrics", "inspect_path", "inspect_host")
TOOLS = READS + tuple(FIXES) + ("verify",)


class Incident:
    """All tools act on an in-memory model; no live network connection exists."""

    def __init__(self, seed=0, shifted=False, budget=8):
        if budget < 1:
            raise ValueError("Tool budget must be positive")
        rng = random.Random(seed)
        self._faults = set(rng.sample(FAULTS, 2 if shifted else 1))
        self._severity = rng.uniform(.7, 1) if shifted else rng.uniform(.4, .8)
        self.budget, self.calls, self.wrong_fixes, self.errors = budget, 0, 0, 0
        self.visible, self.log = {}, []
        self.verified, self.done = False, False

    def observation(self):
        return {"alarm": "service degradation", "results": dict(self.visible),
                "remaining_calls": self.budget-self.calls, "tools": list(TOOLS)}

    def call(self, tool):
        if self.done:
            raise RuntimeError("Incident finished")
        self.calls += 1
        if tool == "read_metrics":
            result = {"queue_load": self._severity if "congestion" in self._faults else .1,
                      "loss": .5 if "link" in self._faults else .02}
        elif tool == "inspect_path":
            result = {"link_up": "link" not in self._faults, "route_ok": "route" not in self._faults}
        elif tool == "inspect_host":
            result = {"service_ok": "service" not in self._faults}
        elif tool in FIXES:
            fault = FIXES[tool]
            if fault in self._faults:
                self._faults.remove(fault)
            else:
                self.wrong_fixes += 1
            # Acknowledgement never reveals whether the action was correct.
            result = {"accepted": True}
        elif tool == "verify":
            self.verified = not self._faults
            result = {"recovered": self.verified}
            self.done = True
        else:
            self.errors += 1
            result = {"error": "unknown tool"}
        self.visible[tool] = result
        self.log.append({"tool": tool, "result": result})
        self.done = self.done or self.calls >= self.budget
        return self.observation()


def features(observation):
    results = observation["results"]
    metrics, path, host = (results.get(name, {}) for name in READS)
    return [int(name in results) for name in READS] + [
        metrics.get("queue_load", 0), metrics.get("loss", 0),
        int(path.get("link_up", True)), int(path.get("route_ok", True)),
        int(host.get("service_ok", True))] + [int(tool in results) for tool in FIXES]


def expert(observation):
    """Visible-information policy used to collect demonstration trajectories."""
    results = observation["results"]
    for tool in READS:
        if tool not in results:
            return tool
    if any(tool in results for tool in FIXES):
        return "verify"
    if not results["inspect_path"]["link_up"]:
        return "restore_link"
    if not results["inspect_path"]["route_ok"]:
        return "repair_route"
    if not results["inspect_host"]["service_ok"]:
        return "restart_service"
    if results["read_metrics"]["queue_load"] > .3:
        return "shape_traffic"
    return "verify"


def collect(episodes=160):
    demonstrations = []
    for seed in range(episodes):
        env = Incident(seed)
        while not env.done:
            observation = env.observation()
            tool = expert(observation)
            demonstrations.append({"episode": seed, "observation": observation,
                                   "features": features(observation), "action": tool})
            env.call(tool)
    return demonstrations


def impurity(labels):
    counts = Counter(labels)
    return 1-sum((v/len(labels))**2 for v in counts.values()) if labels else 0


def train_tree(x, y, depth=0, max_depth=8):
    """Small CART-style classifier for supervised tool-selection learning."""
    if not y or len(x) != len(y):
        raise ValueError("Nonempty aligned demonstrations required")
    majority = Counter(y).most_common(1)[0][0]
    leaf = {"action": majority, "samples": len(y)}
    if depth >= max_depth or len(set(y)) == 1:
        return leaf
    best, parent = None, impurity(y)
    for column in range(len(x[0])):
        values = sorted({row[column] for row in x})
        # Limit threshold candidates to bound cost for continuous observations.
        thresholds = [(a+b)/2 for a, b in zip(values, values[1:])]
        thresholds = thresholds[::max(1, len(thresholds)//24)]
        for threshold in thresholds:
            left = [i for i, row in enumerate(x) if row[column] <= threshold]
            right = [i for i, row in enumerate(x) if row[column] > threshold]
            cost = (len(left)*impurity([y[i] for i in left]) + len(right)*impurity([y[i] for i in right]))/len(y)
            if best is None or cost < best[0]:
                best = (cost, column, threshold, left, right)
    if best is None or best[0] >= parent-1e-12:
        return leaf
    _, column, threshold, left, right = best
    return {"column": column, "threshold": threshold,
            "left": train_tree([x[i] for i in left], [y[i] for i in left], depth+1, max_depth),
            "right": train_tree([x[i] for i in right], [y[i] for i in right], depth+1, max_depth)}


def tree_action(tree, observation):
    row = features(observation)
    while "action" not in tree:
        tree = tree["left"] if row[tree["column"]] <= tree["threshold"] else tree["right"]
    return tree["action"]


def naive(observation):
    return "verify" if "restart_service" in observation["results"] else "restart_service"


def evaluate(policy, seed, shifted=False):
    env = Incident(seed, shifted)
    while not env.done:
        env.call(policy(env.observation()))
    return {"verified_success": int(env.verified), "tool_calls": env.calls,
            "wrong_fixes": env.wrong_fixes, "tool_errors": env.errors}, env.log


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default="runs/p4")
    parser.add_argument("--episodes", type=int, default=160)
    parser.add_argument("--eval-episodes", type=int, default=40)
    parser.add_argument("--student", action="store_true")
    args = parser.parse_args()
    if not 1 <= args.episodes <= 10000 or not 1 <= args.eval_episodes <= 10000:
        parser.error("--episodes and --eval-episodes must be 1..10000 to keep splits disjoint")
    demos, out = collect(args.episodes), Path(args.out)
    tree = train_tree([d["features"] for d in demos], [d["action"] for d in demos])
    save_json(out / "agent.json", tree)
    out.mkdir(parents=True, exist_ok=True)
    with (out / "demonstrations.jsonl").open("w") as stream:
        for demo in demos:
            stream.write(json.dumps(demo) + "\n")
    # Load the saved artifact for evaluation, as students must do for submissions.
    tree = json.loads((out / "agent.json").read_text())
    policies = {"naive": naive, "rules": expert, "trained_tree": lambda obs: tree_action(tree, obs)}
    if args.student:
        from student.policies import agent_action
        policies["student"] = agent_action
    rows = []
    for split, seed_start, shifted in (("validation", 10000, False), ("test", 20000, False), ("shift", 30000, True)):
        for name, policy in policies.items():
            for i in range(args.eval_episodes):
                result, log = evaluate(policy, seed_start+i, shifted)
                rows.append(dict(result, split=split, policy=name, seed=seed_start+i))
                if i == 0:
                    save_json(out / f"{split}-{name}-trajectory.json", log)
    save_csv(out / "metrics.csv", rows)
    save_json(out / "summary.json", [{"split": split, "policy": name,
        "success_rate": mean(r["verified_success"] for r in rows if r["split"] == split and r["policy"] == name)}
        for split in ("validation", "test", "shift") for name in policies])
    save_json(out / "config.json", {"training_episodes": args.episodes, "eval_episodes": args.eval_episodes,
              "training_seed_start": 0, "validation_seed_start": 10000, "test_seed_start": 20000,
              "shift_seed_start": 30000, "model": "supervised decision-tree tool policy",
              "synthetic": True, "tool_budget": 8})
    print(f"Project 4: demonstrations, trained agent, and evaluations written to {out}")


if __name__ == "__main__":
    main()
