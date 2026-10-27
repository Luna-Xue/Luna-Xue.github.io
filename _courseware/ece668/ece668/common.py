"""Small, dependency-free helpers shared by the four course projects."""

import csv
import html
import json
import math
from pathlib import Path


def save_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def save_csv(path, rows):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = list(rows)
    if not rows:
        return
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def percentile(values, q):
    if not values:
        return None
    ordered = sorted(values)
    return ordered[max(0, math.ceil(q * len(ordered)) - 1)]


def mean(values):
    values = list(values)
    return sum(values) / len(values) if values else 0.0


def poisson(rng, rate):
    """Knuth sampling; intended only for the small rates in these labs."""
    if rate < 0:
        raise ValueError("Arrival rate must be nonnegative")
    if rate == 0:
        return 0
    product, count = 1.0, 0
    threshold = math.exp(-rate)
    while product > threshold:
        product *= rng.random()
        count += 1
    return count - 1


def line_plot(path, series, title, ylabel):
    """Write a standalone SVG; each series is a list of numeric samples."""
    width, height, pad = 860, 360, 60
    samples = [v for values in series.values() for v in values]
    top = max(1.0, max(samples, default=1.0))
    count = max((len(v) for v in series.values()), default=1)
    colors = ["#086788", "#d1495b", "#408a56", "#8546a3"]
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img">',
             f'<title>{html.escape(title)}</title>', '<rect width="100%" height="100%" fill="white"/>',
             f'<text x="{pad}" y="25" font-family="sans-serif" font-size="18">{html.escape(title)}</text>',
             f'<path d="M{pad},45 V{height-pad} H{width-20}" fill="none" stroke="#777"/>']
    for i, (label, values) in enumerate(series.items()):
        points = " ".join(f"{pad+j*(width-pad-20)/max(1,count-1):.1f},{height-pad-v*(height-pad-50)/top:.1f}"
                          for j, v in enumerate(values))
        color = colors[i % len(colors)]
        parts.append(f'<polyline points="{points}" stroke="{color}" fill="none" stroke-width="1.6"/>')
        parts.append(f'<text x="{pad+i*190}" y="{height-12}" fill="{color}" font-size="12" font-family="sans-serif">{html.escape(label)}</text>')
    parts.extend([f'<text x="8" y="50" font-size="12">{top:.1f}</text>',
                  f'<text x="8" y="{height-pad}" font-size="12">0</text>',
                  f'<text x="{pad}" y="{height-37}" font-size="12" font-family="sans-serif">sample index · {html.escape(ylabel)}</text>', '</svg>'])
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(parts))
