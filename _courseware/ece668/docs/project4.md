# Project 4 · Training a Diagnostic Agent

**Weeks 11–16 · 35% of the proposed course grade · Includes final demo and report**

This is the default capstone track. You may instead propose a network controller,
edge offloading system, scheduling study, AI-RAN application, or ISAC experiment
with a comparable baseline, evaluation plan, and feasible environment.

In the default track, train an agent to choose diagnostic tools and a remediation
action. Then investigate why a policy trained on single incidents fails when
multiple faults coexist. The core package trains a small decision-tree policy
from demonstrations; no language model or paid API is required.

## Concept notes

An agent receives observations, selects actions, and evaluates their consequences.
A tool call is an action even when it only reads a metric: it consumes time or
budget and changes what the agent knows. Tool access alone does not imply that
the policy is trained, nor does a fluent explanation prove that a repair worked.

Here, supervised imitation learning maps observed diagnostic state to the next
tool. A rule policy generates demonstrations using the same public observations
available to the student. A decision tree learns splits that reduce class-label
impurity. The saved tree is then loaded and executed on new incidents.

Action-prediction accuracy and incident-resolution success are different metrics.
An early tool error can change every subsequent observation. Evaluate full
episodes, not only classification accuracy on demonstration rows.

## Sandbox contract

Each incident initially exposes the same generic degradation alarm. Hidden faults
belong to congestion, link availability, routing configuration, or service health.
The agent can discover symptoms only through tool results.

| Tool | Result or simulated action |
| --- | --- |
| `read_metrics` | Queue-load indicator and packet-loss indicator |
| `inspect_path` | Link availability and routing validity |
| `inspect_host` | Service health |
| `shape_traffic` | Remove the simulated congestion fault if present |
| `restore_link` | Remove the simulated link fault if present |
| `repair_route` | Remove the simulated route fault if present |
| `restart_service` | Remove the simulated service fault if present |
| `verify` | Check full recovery and end the episode |

Every call consumes one of eight allowed calls. Unknown tools also consume a call
and produce an error. Repair acknowledgements do not reveal whether a repair was
appropriate. `verify` is terminal even when recovery fails. Existing read results
are snapshots; call a read tool again to observe the updated simulated system.

There is no live command execution, CU/DU connection, external API, or production
network. The faults and tool outputs are intentionally simple teaching models.

## Prelab

1. Which tools distinguish a broken link from an incorrect route?
2. Explain why a repair acknowledgement is not evidence of recovery.
3. Compare training from expert actions with optimizing a task-level reward.
4. Why must all steps of an incident remain in the same data split?
5. Estimate how many reads, repairs, and verification calls a two-fault case needs.

## Train and evaluate the baseline agent

```sh
python3 -m ece668.project4 --out runs/p4-baseline
```

The default run generates 160 single-fault demonstration episodes, trains a tree,
reloads `agent.json`, and compares it with a naive restart policy and the supplied
rule policy. `demonstrations.jsonl` includes episode ID, visible observations,
derived features, and expert actions. No hidden fault labels are included in the
policy input. `metrics.csv` contains incident-level results, and selected
`*-trajectory.json` files show complete tool sequences.

Training seeds start at 0, validation at 10000, test at 20000, and shift at 30000.
The shifted setting has two simultaneous faults and changed severity. The baseline
rule policy repairs only one fault before verification; its demonstrations
therefore do not teach multi-fault recovery. This intentionally exposes a
limitation of the training data and workflow.

## Student implementation

Edit `agent_action(observation)` in `student/policies.py` and run:

```sh
python3 -m ece668.project4 --student --out runs/p4-student
```

For a trained-agent submission, also change the demonstration collection or
training pipeline and submit the learned artifact. An entirely hand-written
workflow is a useful comparison but does not satisfy the trained-agent track.
Do not inspect `Incident` private state or provide hidden labels to the policy.

Choose a focused investigation, for example:

- Teach multi-fault diagnosis with new training episodes and a revised expert.
- Reduce tool calls while preserving resolution success.
- Add noisy or missing observations, then train and test a robust policy.
- Compare the decision tree with a small classifier or a language-model policy.
- Transfer the tool interface to replayed telemetry with a documented schema.

If using a small language model, keep the sandbox and evaluator, export tool
trajectories to an appropriate training format, and document the model, license,
token budget, hardware, and training procedure. Language-model fine-tuning and
OCUDU integration are extensions; they are not implemented in this core package.

## Milestones within this assignment

| Target | Deliverable |
| --- | --- |
| Weeks 8–9 | Informal topic and resource exploration |
| Week 11 | One-page proposal: question, baseline, data, metrics, compute plan |
| Week 13 | Working prototype, early evaluation, and one observed failure |
| Weeks 15–16 | Final demo, repository, frozen model, and 5–7 page report |

Exact dates will be assigned in the course schedule. These are milestones within
Project 4, not additional major assignments.

## Required evidence and assessment

Compare against at least one simple rule policy and the relevant supplied
baseline. Keep independent validation and final test incidents. Report verified
success, tool calls, wrong repairs, invalid tool calls, and at least one changed
condition. Include failures in both aggregate metrics and trajectory analysis.
When your dataset changes, state which faults and combinations were seen in training.

| Criterion | Points |
| --- | --- |
| Problem definition and feasible proposal | 15 |
| Implementation, model training, and artifact | 30 |
| Baselines, held-out evaluation, and failure analysis | 35 |
| Reproducibility, demo, and communication | 20 |

For an OpenISAC-Edge direction, begin with recorded telemetry and a read-only
adapter. Establish units, timestamps, labels, and independent recording splits.
Observing a RAN does not establish the ability to control it; demonstrate each
required interface before making a live-network claim.
