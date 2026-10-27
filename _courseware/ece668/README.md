# ECE 668 Network Intelligence Lab

Four original programming projects for **ECE 668: Telecommunication Networks**,
University of Hawaiʻi at Mānoa. Maintained for Xiaochan Xue's Spring 2027 course.
Version **0.1.0 — instructor review edition**. Project weights and deadlines remain tentative.

The sequence connects network fundamentals to measurement, prediction, decision
making, and agents. AI-RAN and ISAC are optional applications of those methods.
The package is a complete runnable teaching baseline, with research extensions
left for students. It is not a reproduction of a production network stack.

## Start in five commands

Use Python **3.9 or later**. No pip dependencies, cloud account, API key, GPU,
Mininet, ns-3, or radio hardware is required for these core exercises.
Open a terminal in the extracted folder containing this README:

```sh
python3 -m unittest discover -s tests -v
python3 -m ece668.project1
python3 -m ece668.project2
python3 -m ece668.project3
python3 -m ece668.project4
```

On Windows, use `py -3` instead of `python3` if needed. Generated files appear in
`runs/p1` through `runs/p4`; repeated runs replace files with the same names.
Use a fresh `--out` directory to retain an experiment. Open SVG files in a browser;
CSV and JSON files can be inspected without additional packages.

## Four assignments

| Project | Weeks | Weight | Core question | Guide |
| --- | --- | --- | --- | --- |
| 1. Paths, queues, and delay | 1–3 | 20% | When does the shorter path lose? | [Project 1](docs/project1.md) |
| 2. Predicting network demand | 4–6 | 20% | Does a trained predictor survive a traffic shift? | [Project 2](docs/project2.md) |
| 3. Learning resource allocation | 7–10 | 25% | How do throughput and deadlines compete? | [Project 3](docs/project3.md) |
| 4. Training a diagnostic agent | 11–16 | 35% | Can a learned tool policy handle unfamiliar incidents? | [Project 4](docs/project4.md) |

Project 4 also serves as the final project. Its proposal, progress check, demo,
and report are milestones within that assignment. Other network intelligence
topics may replace the default diagnostic-agent track with instructor agreement.

## Class format

The course uses **eight core short lectures of 35–45 minutes**, two per project.
The rest of each 75-minute lecture meeting is practical work. Other scheduled
meetings are programming studios, student-led case discussions, project clinics,
peer reproduction, or demonstrations. Students prepare with the project notes and
prelabs; the instructor guides experiments and provides feedback during studios.
See the instructor guide for the eight lecture outlines and studio routine.

## What students receive

- Original concept notes, prelab questions, experiment tasks, and assessment rubrics.
- Synthetic traffic and incident generators with explicit units and assumptions.
- Working baselines, CPU-sized training routines, saved model artifacts, and evaluators.
- Editable interfaces in `student/policies.py`; add `--student` to a project command.
- A [report template](docs/report-template.md), tests, and GitHub contribution guidance.

The baseline solution is intentionally public. Credit comes from a new question,
implementation changes, fair comparisons, and evidence. Running a supplied baseline
without an extension is a prelab activity, not the completed assignment.

## File map

```text
ece668/                 Simulator, training code, evaluators, plotting helpers
student/policies.py     Four working extension hooks
configs/                Small/large buffer experiment configurations
docs/                   Student handouts and instructor preparation guide
tests/                  Conservation, isolation, serialization, and agent tests
examples/               Small recorded validation summary, not a grading target
.github/workflows/      Optional CI when this folder becomes its own repository
REFERENCES.md           Related teaching/research resources and provenance
LICENSE                 MIT license for this package's original files
```

## Scope and interpretation

All included data is synthetic. Slots and packets are abstract units. There is
no real TCP stack, PHY, CU/DU connection, live remediation, or hidden production
dataset. The agent model is a trained decision tree over tool observations,
not a fine-tuned language model. These choices keep a reproducible core available
to the whole class; advanced extensions can add realistic traces or larger models.

See [instructor preparation](docs/instructor-guide.md) for release checks,
extension design, workload calibration, and optional OpenISAC-Edge integration.

## Contributing and attribution

Use issues for reproducible bugs and research questions; use pull requests for
tested improvements. Include an experiment configuration and explain which result
changes. Students may follow OpenISAC-Edge releases and propose scoped contributions;
starring or subscribing to a repository is voluntary and is not a grading criterion.

The package's code and prose were independently written for this course; it does
not vendor the previously discussed courses or libraries. Related resources are
acknowledged in [REFERENCES.md](REFERENCES.md). Preserve this package's MIT notice
and any additional upstream notices if you later incorporate third-party work.
