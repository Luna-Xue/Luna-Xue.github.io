"""Project 1: finite queues on two parallel abstract network paths."""

import argparse
from collections import deque
import json
import random
from pathlib import Path

from .common import line_plot, mean, percentile, poisson, save_csv, save_json


DEFAULT = {"slots": 240, "buffer": 24, "arrival_rate": 10,
           "capacities": [5, 9], "propagation": [1, 4]}


def shortest(observation, rng):
    return min(range(len(observation)), key=lambda i: observation[i]["propagation"])


def queue_aware(observation, rng):
    return min(range(len(observation)), key=lambda i:
               observation[i]["propagation"] +
               (observation[i]["queue"] + 1) / max(0.01, observation[i]["capacity"]))


def simulate(config, scenario="steady", seed=0, policy=shortest):
    if scenario not in ("steady", "burst", "degraded"):
        raise ValueError("Unknown traffic scenario")
    slots, buffer = config["slots"], config["buffer"]
    capacities, propagation = config["capacities"], config["propagation"]
    if (not isinstance(slots, int) or not isinstance(buffer, int) or
            slots <= 0 or buffer <= 0 or not capacities or
            len(capacities) != len(propagation) or min(capacities) <= 0 or
            any(not isinstance(c, int) for c in capacities) or min(propagation) < 0):
        raise ValueError("Require positive slots/buffer/integer capacities and nonnegative propagation")
    # Traffic has its own RNG so different policies see identical arrivals.
    traffic_rng, policy_rng = random.Random(seed), random.Random(seed + 917)
    queues = [deque() for _ in capacities]
    delivered, dropped, generated, trace = [], 0, 0, []
    routed = [0] * len(capacities)
    t = 0
    while t < slots or any(queues):
        current_capacity = list(capacities)
        if scenario == "degraded" and slots // 3 <= t < 2 * slots // 3:
            current_capacity[0] = 1
        rate = config["arrival_rate"]
        if scenario == "burst" and slots // 3 <= t < slots // 2:
            rate *= 2.2
        arrivals = poisson(traffic_rng, rate) if t < slots else 0
        for _ in range(arrivals):
            generated += 1
            observation = [{"queue": len(q), "capacity": c, "propagation": p}
                           for q, c, p in zip(queues, current_capacity, propagation)]
            choice = policy(observation, policy_rng)
            if not isinstance(choice, int) or not 0 <= choice < len(queues):
                raise ValueError("Policy must return a valid integer path index")
            routed[choice] += 1
            if len(queues[choice]) >= buffer:
                dropped += 1
            else:
                queues[choice].append(t)
        before_service = [len(q) for q in queues]
        for i, queue in enumerate(queues):
            for j in range(min(current_capacity[i], len(queue))):
                born = queue.popleft()
                completion = t + (j + 1) / current_capacity[i] + propagation[i]
                delivered.append({"arrival": born, "completion": completion,
                                  "delay": completion - born, "path": i})
        row = {"slot": t, "arrivals": arrivals}
        row.update({f"queue_{i}": size for i, size in enumerate(before_service)})
        trace.append(row)
        t += 1
    delays = [p["delay"] for p in delivered]
    report = {"generated": generated, "delivered_after_drain": len(delivered),
              "dropped": dropped, "loss_rate": dropped / max(1, generated),
              "throughput_in_window": sum(p["completion"] <= slots for p in delivered) / slots,
              "mean_delay": mean(delays), "p95_delay": percentile(delays, .95),
              "routed": routed, "seed": seed, "scenario": scenario}
    return report, trace, delivered


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default="runs/p1")
    parser.add_argument("--config", default=None)
    parser.add_argument("--seeds", type=int, default=5)
    parser.add_argument("--student", action="store_true")
    args = parser.parse_args()
    if args.seeds < 1:
        parser.error("--seeds must be positive")
    config = dict(DEFAULT)
    if args.config:
        config.update(json.loads(Path(args.config).read_text()))
    policies = {"shortest": shortest, "queue_aware": queue_aware}
    if args.student:
        from student.policies import choose_path
        policies["student"] = choose_path
    out, reports = Path(args.out), []
    for scenario in ("steady", "burst", "degraded"):
        for name, policy in policies.items():
            for seed in range(args.seeds):
                report, trace, packets = simulate(config, scenario, seed, policy)
                reports.append(dict(report, policy=name))
                if seed == 0:
                    prefix = out / f"{scenario}-{name}"
                    save_csv(str(prefix) + "-trace.csv", trace)
                    save_csv(str(prefix) + "-packets.csv", packets)
                    line_plot(str(prefix) + ".svg",
                              {f"path {i}": [r[f"queue_{i}"] for r in trace] for i in range(len(config["capacities"]))},
                              f"{scenario}: {name}", "queued packets before service")
    save_json(out / "config.json", config)
    save_csv(out / "metrics.csv", reports)
    print(f"Project 1: {len(reports)} experiments written to {out}")


if __name__ == "__main__":
    main()
