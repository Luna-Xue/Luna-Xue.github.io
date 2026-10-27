"""Project 2: causal traffic forecasting with independent episode splits."""

import argparse
import math
import random
from pathlib import Path

from .common import line_plot, mean, poisson, save_csv, save_json


HISTORY = 6


def features(history):
    return list(history[-HISTORY:]) + [mean(history), max(history) - min(history)]


def episode(seed, shifted=False, length=120):
    rng = random.Random(seed)
    phase = rng.uniform(0, 2 * math.pi)
    period = 19 if shifted else 48
    values = []
    for t in range(length):
        rate = 8 + 4 * math.sin(2 * math.pi * t / period + phase)
        if shifted and 40 <= t < 65:
            rate += 9
        values.append(poisson(rng, max(0.5, rate)))
    return values


def dataset():
    rows = []
    for split, seeds in (("train", range(12)), ("validation", range(100, 104)),
                         ("test", range(200, 206)), ("shift", range(300, 306))):
        for seed in seeds:
            values = episode(seed, shifted=split == "shift")
            for t in range(HISTORY, len(values)):
                row = {"split": split, "episode": seed, "target_slot": t,
                       "target": values[t]}
                row.update({f"lag_{i+1}": values[t-HISTORY+i] for i in range(HISTORY)})
                rows.append(row)
    return rows


def history_of(row):
    return [row[f"lag_{i+1}"] for i in range(HISTORY)]


def train(x, y, epochs=300, rate=.04, penalty=.01):
    if not x or len(x) != len(y):
        raise ValueError("Nonempty aligned training data required")
    n, width = len(x), len(x[0])
    center = [mean(row[j] for row in x) for j in range(width)]
    scale = [max(1e-8, math.sqrt(mean((row[j]-center[j])**2 for row in x))) for j in range(width)]
    z = [[(v-m)/s for v, m, s in zip(row, center, scale)] for row in x]
    weights, bias = [0.0] * width, mean(y)
    for _ in range(epochs):
        errors = [bias + sum(w*v for w, v in zip(weights, row)) - label for row, label in zip(z, y)]
        bias -= rate * 2 * mean(errors)
        gradient = [2 * sum(e*row[j] for e, row in zip(errors, z))/n + 2*penalty*weights[j]
                    for j in range(width)]
        weights = [w-rate*g for w, g in zip(weights, gradient)]
    return {"center": center, "scale": scale, "weights": weights, "bias": bias,
            "epochs": epochs, "rate": rate, "penalty": penalty}


def predict(model, row):
    if len(row) != len(model["weights"]):
        raise ValueError("Feature dimensions do not match the saved model")
    return max(0.0, model["bias"] + sum(w*(v-m)/s for w, v, m, s in
               zip(model["weights"], row, model["center"], model["scale"])))


def score(actual, predictions):
    return {"mae": mean(abs(y-p) for y, p in zip(actual, predictions)),
            "rmse": math.sqrt(mean((y-p)**2 for y, p in zip(actual, predictions)))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default="runs/p2")
    parser.add_argument("--epochs", type=int, default=300)
    parser.add_argument("--student", action="store_true")
    args = parser.parse_args()
    if args.epochs < 1:
        parser.error("--epochs must be positive")
    extractor = features
    if args.student:
        from student.policies import forecast_features
        extractor = forecast_features
    rows, out = dataset(), Path(args.out)
    training = [r for r in rows if r["split"] == "train"]
    model = train([extractor(history_of(r)) for r in training], [r["target"] for r in training], args.epochs)
    save_json(out / "model.json", model)
    save_csv(out / "dataset.csv", rows)
    results, forecasts = [], []
    for split in ("validation", "test", "shift"):
        selected = [r for r in rows if r["split"] == split]
        actual = [r["target"] for r in selected]
        guesses = {"persistence": [history_of(r)[-1] for r in selected],
                   "moving_mean": [mean(history_of(r)) for r in selected],
                   "trained_linear": [predict(model, extractor(history_of(r))) for r in selected]}
        for name, values in guesses.items():
            results.append(dict(score(actual, values), split=split, method=name, samples=len(actual)))
            forecasts.extend({"split": split, "method": name, "episode": r["episode"],
                              "target_slot": r["target_slot"], "actual": y, "prediction": p}
                             for r, y, p in zip(selected, actual, values))
        line_plot(out / f"{split}.svg", {"actual": actual[:114], "trained": guesses["trained_linear"][:114],
                  "persistence": guesses["persistence"][:114]}, f"Traffic prediction: {split}", "packets / slot")
    save_csv(out / "metrics.csv", results)
    save_csv(out / "predictions.csv", forecasts)
    save_json(out / "manifest.json", {"history": HISTORY, "target": "next-slot packet arrivals",
              "training_episodes": sorted({r["episode"] for r in training}),
              "feature_function": "student" if args.student else "default",
              "split_unit": "independently generated episode", "synthetic": True})
    print(f"Project 2: trained model and held-out predictions written to {out}")


if __name__ == "__main__":
    main()
