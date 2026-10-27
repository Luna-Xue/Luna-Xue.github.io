# Project 1 · Paths, Queues, and Delay

**Weeks 1–3 · 20% of the proposed course grade · Core environment: local Python**

A campus edge service can reach its destination through a short, low-capacity
path or a longer, higher-capacity path. Investigate when choosing the smaller
propagation delay makes end-to-end performance worse. Your deliverable is a
measured routing policy and an explanation of its operating limits.

## Concept notes

Propagation delay is only one component of delivery time. In this model,
`delivery delay = waiting time + transmission time + propagation time`.
A queue grows when arrivals exceed departures over an interval. Increasing
its storage can absorb a burst, but also allows admitted packets to wait longer.
The queue does not create service capacity.

A useful accounting identity is `generated = delivered + dropped + pending`.
After an experiment drains all queues, pending is zero. A throughput measurement
over the original observation window is different from a delivery count obtained
after draining. Both are reported here so the distinction is visible.

## Model and units

- One slot is an abstract interval; each packet has equal size.
- Each path contains one FIFO bottleneck and a propagation delay. These are
  parallel path abstractions, not a multi-hop protocol implementation.
- Default path capacities are 5 and 9 packets/slot; propagation is 1 and 4 slots.
- Each queue holds at most 24 packets by default. Arrivals happen before service;
  a full queue drops the arriving packet even if service follows in that slot.
- Each experiment generates traffic for 240 slots, then drains admitted packets.
- `steady` uses a Poisson mean of 10 packets/slot; `burst` raises that mean for
  part of the run; `degraded` temporarily reduces the first path to 1 packet/slot.
- Policies see current queue lengths, capacities, and propagation delays.
  This instantaneous knowledge is an assumption to investigate, not a free
  capability of a real distributed router.

There is no TCP feedback, retransmission, variable packet size, or routing protocol.
Use the results to explain this model, not to claim Internet-wide behavior.

## Prelab

1. At a mean arrival rate of 10, which individual path can sustain all traffic?
2. For a deterministic constant rate, estimate how quickly an initially empty
   24-packet queue fills if arrivals are 10 and service is 5 packets/slot.
3. Predict how increasing the buffer changes loss and the delay of delivered packets.
4. Explain why mean latency alone is insufficient for an interactive service.
5. Identify one observation available to the simulator that would cost time to collect in a real network.

## Run the supplied experiment

From the package root:

```sh
python3 -m ece668.project1 --out runs/p1-baseline
python3 -m ece668.project1 --config configs/p1-small-buffer.json --out runs/p1-small
python3 -m ece668.project1 --config configs/p1-large-buffer.json --out runs/p1-large
```

The runner compares a minimum-propagation baseline with a queue-aware estimate
on the same traffic seeds. `metrics.csv` contains one row per method, scenario,
and seed. For seed zero, the package also writes packet records, queue traces,
and SVG plots. Trace queue sizes are measured immediately before service.

`throughput_in_window` counts packets completing delivery by slot 240, divided
by 240. `delivered_after_drain` includes packets delivered later. `p95_delay`
uses all delivered packets; dropped packets have no delivery delay. Always show
loss beside delay to avoid rewarding a policy for dropping difficult packets.

## Student implementation

Edit `choose_path(observation, rng)` in `student/policies.py`. Return one valid
path index. The working starter chooses a random path; replace it with a policy
that expresses a hypothesis about queue load, capacity, or telemetry quality.

```sh
python3 -m ece668.project1 --student --seeds 10 --out runs/p1-student
```

Start with a stateless policy. A stateful or delayed-telemetry extension must
explicitly reset its state between experiments; add that reset in your runner.
Never use future arrival samples or private queues beyond the observation API.

## Required investigation

1. Reproduce the two supplied baselines on all three scenarios.
2. Implement a new path-selection rule and state what it should improve.
3. Change at least one condition: buffer size, capacity ratio, propagation delay,
   or offered load. Keep a comparison table of every configuration.
4. Report paired differences across at least 10 seeds. Use the same traffic seed
   for each policy comparison; report both averages and variation across runs.
5. Analyze one failure: excessive delay, overload, unbalanced use, or a poor decision
   caused by stale information. A negative result with a sound explanation is valid.

## Submit and assessment

Submit your code diff, configurations, metrics CSV, two explanatory figures, and
a 3–4 page report using the shared template. Include a command that reproduces
one figure and a brief explanation of packet conservation.

| Criterion | Points |
| --- | --- |
| Network reasoning and prelab | 20 |
| Policy implementation and interface correctness | 25 |
| Controlled experiments and reproducibility | 30 |
| Interpretation, uncertainty, and failure analysis | 25 |

Optional extensions include a third path, delayed observations, heterogeneous
packet sizes, or a separate Mininet experiment. Added realism must come with
explicit assumptions and a working small example.
