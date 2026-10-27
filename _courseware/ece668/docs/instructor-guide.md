# Instructor Guide · ECE 668 Network Intelligence Lab

## Release intent

Version 0.1.0 is a runnable instructor-review edition of four original project
packages. It includes the reference baselines, student extension hooks, handouts,
evaluators, tests, and synthetic data generators. It does not include a full
semester's slide deck, a replacement textbook, live RAN adapters, or an LLM
fine-tuning deployment. The course website continues to label the syllabus
and assessment weights as preliminary.

## Teaching commitment: eight core short lectures

Prepare **two core short lectures per project**, eight across the semester.
Each lasts **35–45 minutes** within a 75-minute class meeting; total planned
core lecture time is **4 hours 40 minutes to 6 hours**. Use the rest of those
meetings for a practical exercise. Jan 11 is course orientation; the remaining
21 meetings are studios, student-led discussions, clinics, or demonstrations.
All scheduled class meetings remain in place, with the instructor providing
guidance and feedback.

Use Jan 11 for a **20-minute course overview**, 15 minutes of student background
and project-interest discussion, 30 minutes of repository navigation and supported
environment setup, and 10 minutes of questions. Reuse the syllabus and project
pages for the overview; no separate orientation slide deck is needed. This brief
overview is additional to the eight technical short lectures. Move core session 1
to Jan 13 and use its practical segment to trace a packet and run the baseline.
Core session 2 remains on Jan 20, preserving the four project windows.

Each short-lecture outline below contains one central question, one worked
example, and one exercise. An annotated notebook, whiteboard, or 6–8 slides is
sufficient. A separate slide deck for every meeting is not part of the plan.
Use the project handouts for background; deeper readings support student inquiry.

| Core session | Target | Central question | Worked example and exercise |
| --- | --- | --- | --- |
| 1 | Week 1, Jan 13, P1 | Why can the shorter path be slower? | Decompose one packet's delay; predict which path becomes overloaded and run the baseline. |
| 2 | Week 2, P1 | What changes when a queue grows? | Account for admitted, delivered, and dropped packets; compare two buffer sizes. |
| 3 | Week 4, P2 | What can a predictor know before the next slot? | Mark features and target on a seven-slot trace; audit one split for leakage. |
| 4 | Week 5, P2 | How do we know a trained model helps? | Walk through one loss calculation and update; fit, save, and compare a small model. |
| 5 | Week 7, P3 | What should a scheduler optimize? | Allocate one capacity budget across two queues; compare deadline and throughput outcomes. |
| 6 | Week 8, P3 | How does a policy learn from a decision? | Work through one Q-value update; inspect state compression and reward choices. |
| 7 | Week 11, P4 | What evidence should an agent gather before acting? | Trace a diagnostic tool sequence; distinguish repair acknowledgement from verified recovery. |
| 8 | Week 12, P4 | What does training teach a tool-using policy? | Inspect a demonstration and a tree split; train a policy and examine a multi-fault failure. |

## Studio routine and preparation limits

For a core-lecture meeting, plan approximately 40 minutes of explanation,
25 minutes of practical work, and 10 minutes of discussion. Keep the explanation
within 45 minutes by moving deeper background to the notes or an optional reading.

For studios and discussion meetings, use a 5-minute check-in, approximately 60 minutes of coding,
peer discussion, or demos, and a 10-minute recap. Students bring their current
code, plot, question, or failure case. The instructor circulates, gives targeted
help, and records common issues for a short written FAQ. Brief troubleshooting
does not require another prepared lecture.

- Reuse the four project packages, one rubric per project, and the shared report template.
- Keep proposed improvements, progress evidence, and reflection inside the four
  assignments; no separate weekly paper report or presentation deck is required.
- Student-led cases use a selected figure, code example, or project result. Rotate
  facilitators and keep the instructor's role to framing questions and feedback.
- AI-RAN, OCUDU, ISAC, and edge topics are student case choices or project clinics.
  They do not create additional instructor lecture commitments.
- If a new topic needs a prepared lecture, replace or narrow one of the eight
  planned sessions rather than adding another lecture to the schedule.

## Teaching sequence

| Weeks | Meeting format | In-class activity | Project milestone |
| --- | --- | --- | --- |
| 1 | Jan 11 orientation + Jan 13 core 1 | Review the course and project roadmap; set up the environment, then trace a packet and run the baseline | P1 prelab and baseline |
| 2 | Holiday + core 2 | Buffer sweep and conservation check | P1 policy design |
| 3 | Programming studio + student results | Compare path policies and explain failures | P1 report |
| 4 | Core 3 + data studio | Audit windows, episode splits, and simple predictors | P2 data audit |
| 5 | Core 4 + model clinic | Fit, reload, and compare a small model | P2 feature experiment |
| 6 | Holiday + student results | Diagnose forecast failures under traffic shift | P2 report |
| 7 | Core 5 + programming studio | Step through allocation; run rule baselines | P3 baselines |
| 8 | Core 6 + training studio | Train and inspect a policy | P3 method; P4 topic exploration |
| 9 | Student-led case discussion + project clinic | Map the model to wireless cases; assess optional RAN/ISAC extensions | P3 progress; P4 feasibility |
| 10 | Evaluation studio + student results | Compare policies across seeds and traffic conditions | P3 report |
| 11 | Core 7 + proposal workshop | Inspect tool trajectories; discuss student proposals | P4 proposal |
| 12 | Core 8 + integration studio | Train a tool policy; develop the chosen system | P4 implementation |
| 13 | Project clinic + midpoint demonstrations | Debug failures and review early evidence | P4 midpoint demo |
| 14 | Student-led topic exchange + robustness studio | Share relevant findings and run ablations | P4 robustness studies |
| 15 | Peer reproduction studio + final demonstrations | Reproduce a small example and present results | Final integration |
| 16 | Final demonstrations + project retrospective | Discuss evidence, limitations, and next steps | Final report |

## Preparation before student release

1. Run every command in README on the intended lab platform. The current local
   validation uses Python 3.9.6; additional Python versions in CI are configured
   but are not claimed as tested until that workflow runs.
2. Have a student unfamiliar with the package perform one prelab. Adjust the
   instructions based on observed setup and interpretation difficulties.
3. Freeze a release version. Assign deadlines, collaboration rules, late policy,
   and accessibility accommodations through normal course channels.
4. Keep the public synthetic seeds for examples. Prepare additional independent
   grading episodes after freezing the student-facing simulator specification.
5. Confirm any optional GPU, dataset, or testbed availability before approving
   a project that depends on it. The core package requires none of those resources.

## Instructor checks and expected reasoning

P1: The short path alone is overloaded at the default mean arrival rate.
Queue-aware routing can use spare capacity on the longer path. Larger buffers
can reduce loss while increasing delay. Check definitions and packet accounting;
do not grade against an exact preferred throughput number.

P2: Check that targets are absent from features and preprocessing fits training
data only. Holdout units are episodes, not overlapping windows. The small trained
model may improve ordinary test error while retaining failures on changed traffic.
A student must explain why an error metric is appropriate for a network use case.

P3: Resource allocation never exceeds current capacity. Lost and pending packets
must accompany survivor-delay statistics. A learned policy can lose to a demand
rule, especially after a change in offered load. Reward design, state compression,
and exploration are appropriate explanations to investigate experimentally.

P4: A rule teacher and learned policy can both solve a simple single-fault
distribution. The default workflow terminates after one repair; dual-fault
recovery therefore fails. Reward careful workflow/data changes and independent
evaluation, not merely replacing the baseline with a larger model.

## Workload and assessment

Each early project should contain one baseline-reproduction session, one focused
implementation task, and one controlled investigation. Treat the handout rubrics
as proposed 100-point breakdowns within the 20/20/25/35 course weighting.
Avoid adding every optional extension as a requirement. Checkpoints support the
four assignments and should not become extra major submissions.

Use short code walkthroughs and small unseen scenarios to assess understanding.
Do not use repository stars, follows, or promotional activity as evidence of
technical achievement. Reproducible upstream fixes can be recognized as technical
contributions when they meet the same documented assessment criteria.

## Repository and release process

The package can be copied unchanged into a dedicated course repository. Its
internal `.github/workflows/ci.yml` is intended for that repository root.
Within the website checkout it is data, not an active GitHub workflow.
Preserve LICENSE and REFERENCES.md. Announce a tagged release only after the
instructor chooses the repository and reviews the package.

The website build helper packages the files and generates handout pages. Keep
source changes in `_courseware/ece668`; regenerate the download and pages rather
than independently editing two copies. Generated runs and Python caches are
excluded from the archive.

## Optional OpenISAC-Edge track

Start with a documented offline recording and a read-only observation interface.
Require a data dictionary, recording IDs, units, timestamp interpretation, and
the origin of any labels. Use held-out recording sessions, not adjacent windows
from one capture, for generalization claims. Separate recorded measurements from
synthetic demonstrations and separate observation from implemented control.

Possible scoped contributions include a replay evaluator, a reproducible anomaly
study, a telemetry adapter, or improved experiment documentation. A live RAN
controller needs a demonstrated control interface, meaningful action constraints,
and an evaluation plan beyond the synthetic agent included here.
