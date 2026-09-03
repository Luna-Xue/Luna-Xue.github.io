# ECE 362 — Discrete Math for Engineers
## Syllabus · Fall 2026

> **DRAFT.** Sections flagged with ⚠️ contain UH Mānoa policy language/offices you should verify against the current official templates (UHM boilerplate changes yearly). Everything else is ready to use.

---

### Course Information

| | |
|---|---|
| **Course** | ECE 362 — Discrete Math for Engineers |
| **Credits** | 3 |
| **Semester** | Fall 2026 (Aug 24 – Dec 10, 2026) |
| **Meetings** | M/W/F 11:30 AM – 12:20 PM |
| **Location** | Kuykendall Hall 310 |
| **Instructor** | Xiaochan Xue |
| **Email** | xxue@hawaii.edu |
| **Office / Hours** | *by appointment* |
| **Course site** | https://luna-xue.github.io/teaching/ece-362/ |
| **Course web tool** | https://ece362.147-224-57-207.sslip.io/ |

### Course Description

Fundamental discrete mathematics for engineering: **logic, proof techniques, sets, relations, functions, counting, recurrences, growth of functions, and discrete structures / models of computation.** These provide the mathematical foundations for analyzing algorithms — for both correctness and performance — and an introduction to models of computation including finite-state machines and Turing machines.

### Prerequisites

ECE 160 Completed w/C grade; ECE 260 Completed w/C grade; MATH 242 Completed w/C grade

### Learning Outcomes

By the end of the course, students will be able to:

1. Use propositional and predicate logic to express and evaluate statements, and construct valid arguments.
2. Produce rigorous proofs, including direct, contrapositive, contradiction, and **mathematical/strong induction**.
3. Work fluently with sets, functions, and relations (including equivalence relations and partial orders).
4. Apply counting techniques (permutations, combinations, inclusion–exclusion, pigeonhole) and generating functions.
5. Analyze the growth of functions and the time/space complexity of algorithms using asymptotic (Big-O/Θ/Ω) notation.
6. Set up and solve recurrence relations, including via the Master theorem.
7. Describe basic models of computation: formal languages, finite automata, and Turing machines.

### Textbook & Resources

- **Required:** Kenneth H. Rosen, *Discrete Mathematics and Its Applications*, **8th edition**, McGraw-Hill, 2019. ISBN 978-1-259-67651-2.
- **Optional (gentler on proofs):** Susanna S. Epp, *Discrete Mathematics with Applications*, 5th ed., 2020.
- Lecture slides, reading notes, homework, and an interactive Big-O explorer are posted on the course site.

---

### Grading

| Component | Weight | Notes |
|-----------|-------:|-------|
| Homework (weekly) | 25% | Lowest score dropped. |
| Quizzes | 10% | Short checkpoint quizzes during each module; lowest score dropped. |
| In-class exercises | 6% | |
| Midterm 1 | 17% | Fri Sep 25 (Week 5) |
| Midterm 2 | 17% | Wed Nov 4 (Week 11) |
| Final exam (comprehensive) | 25% | **Mon, Dec 14, 2026, 12:00–2:00 PM** |

**Grade scale:** A+ ≥ 95, A 90–94, B 80–89, C 70–79, D 60–69, F < 60. The scale may be adjusted downward (never up) at the instructor's discretion to reflect score variation.

#### Homework

- One assignment most weeks; posted on the course site with the due date.
- Submissions via **Lamaku** by the stated deadline. No email or paper submissions.
- **Format:** **Handwritten**, scanned as a single PDF. Typed submissions are not accepted. Write legibly and label each problem and part; illegible work cannot be graded.
- **Collaboration:** You may discuss the *meaning* of problems and possible *approaches*, but you must write up every solution entirely on your own and cite any person, book, or web source you consulted. Copying solutions (in whole or part) is a violation of academic integrity.
- **Prep Sets.** Before each exam a *Prep Set* is posted. It is **not collected and not graded**; it exists to cover material that is examinable but lands after the last homework was due, and it is worked at the board in the review session. Everything on a Prep Set is fair game on the exam.

#### Quizzes & Exercises

Short quizzes are given at checkpoints within a module — not after every lecture, and not on material an exam is about to cover in depth. All quizzes are closed-book. In-class exercises are open-book collaborative problem-solving practice; students may use the textbook, notes, and course materials. Lowest score in each category is dropped.

#### Exams

Two midterms during regular class time and one comprehensive final. All exams are closed-book, and no collaboration is permitted. Makeup exams only for documented, university-approved excuses arranged in advance.

### Late Work & Regrading

- **No late submissions accepted**; the dropped-lowest policy is your buffer for emergencies. On-time work is eligible for partial credit.
- **Regrade requests** must be submitted in writing (email) within **one week** of a graded item's return, with specific justification. Requests after that window are not honored.
- Work completed for a *university-approved excused absence* is makeup work, not late work.

---

### Tentative Course Schedule

✅ *Dates verified against the published UH Mānoa Fall 2026 academic calendar (manoa.hawaii.edu/registrar) and the official final-exam schedule.* No class on university holidays: **Labor Day (Mon 9/7)**, **Veterans Day (Wed 11/11)**, **Thanksgiving (Thu 11/26 + non-instructional Fri 11/27)**. Election Day (Tue 11/3) is a UH holiday but does not affect MWF meetings. UH Mānoa does **not** observe Discoverers' Day — Mon Oct 12 meets as usual.

| Wk | Monday | Wednesday | Friday | Rosen | Milestones |
|---|---|---|---|---|---|
| 1 · Aug 24–28 | **No class** | **Course introduction, syllabus, and course tools** | Propositional logic + inference rules (M1·L1–2) | Ch. 1 | — |
| 2 · Aug 31–Sep 4 | Predicate logic (M1·L3) | Proof techniques (M1·L4) | Sets (M2·L1) | Ch. 1–2 | **M1 quiz 9/4 · HW1 assigned 9/1** |
| 3 · Sep 7–11 | **Labor Day — no class** | Set operations, identities, Cartesian products (M2·L2) | Relations and their properties (M2·L3) | Ch. 2, 9 | **HW1 due 9/9 · HW2 assigned 9/9** |
| 4 · Sep 14–18 | Functions (M2·L4) | Floor/ceiling and cardinality (M2·L5) | Equivalence relations (M2·L6) | Ch. 2, 9 | **Quiz 2 (checkpoint) 9/14 · HW2 due 9/18 · Prep Set out 9/18** |
| 5 · Sep 21–25 | Partial orders and Hasse diagrams (M2·L7) | **Prep Set worked at the board** | **★ Midterm 1** | Ch. 1–2, 9 | **Midterm 1 on 9/25** |
| 6 · Sep 28–Oct 2 | Induction I (M3·L1) | Strong induction (M3·L2) | Recursion and sums (M3·L3–4) | Ch. 5, 2.4 | **HW3 assigned 9/28** |
| 7 · Oct 5–9 | Big-O definition (M4·L1) | Big-Ω and Big-Θ (M4·L2) | Little-o and growth hierarchy (M4·L3) | Ch. 3 | **M3 quiz 10/5 · HW4 assigned 10/5 · HW3 due 10/9** |
| 8 · Oct 12–16 | Bounding sums (M4·L3) | Algorithm analysis and cases (M4·L4) | Complexity classes; linear vs. binary search (M4 wrap) | Ch. 3 | — |
| 9 · Oct 19–23 | Product and sum rules (M5·L1) | Pigeonhole principle (M5·L2) | Permutations and combinations (M5·L3) | Ch. 6 | **M4 quiz 10/19 · HW4 due and HW5 assigned 10/19** |
| 10 · Oct 26–30 | Binomial theorem and Pascal's identity (M5·L4) | Inclusion–exclusion (M5·L5) | Generating functions (M5·L6) | Ch. 6, 8 | — |
| 11 · Nov 2–6 | **Review M3–M5 + M5 quiz** | **★ Midterm 2** | Recurrences: modeling (M6·L1) | Ch. 8 | **HW5 due 11/2 · Midterm 2 on 11/4 · HW6 assigned 11/6** |
| 12 · Nov 9–13 | Linear homogeneous recurrences and characteristic equations (M6·L2) | **Veterans Day — no class** | Repeated roots and Binet's formula (M6·L2) | Ch. 8 | — |
| 13 · Nov 16–20 | Nonhomogeneous recurrences + Master theorem (M6·L3–4) | Formal languages (M7·L1) | Grammars and the Chomsky hierarchy (M7·L2) | Ch. 8, 13 | **M6 quiz and HW7 assigned 11/18 · HW6 due 11/20** |
| 14 · Nov 23–27 | Regular expressions (M7·L3) | Finite automata: DFA and NFA (M7·L4) | **Thanksgiving break — no class** | Ch. 13 | — |
| 15 · Nov 30–Dec 4 | NFA and Kleene's theorem (M7·L4) | Turing machines and the halting problem (M7·L5) | Course synthesis and connections (M7 wrap) | Ch. 13 | **HW7 due and M7 quiz 12/4** |
| 16 · Dec 7–10 | **Review M1–M4** | **Review M5–M7** | No meeting; study period begins 12/11 | — | Comprehensive review |
| **Final** | **Mon Dec 14, 12:00–2:00 PM — Comprehensive final examination** | | | All | — |

**Exam dates:** Midterm 1 — Fri **Sep 25**; Midterm 2 — Wed **Nov 4**; Final — Mon **Dec 14, 12:00–2:00 PM**.
**No class:** Mon Aug 24 (before the first course meeting); Labor Day (Mon 9/7); Veterans Day (Wed 11/11); Thanksgiving (Thu 11/26–Fri 11/27). *(Verified against the published UH Mānoa Fall 2026 academic calendar; see CALENDAR_AUDIT.md for sources.)*

---

### University Policies

⚠️ *The four sections below must use UH Mānoa's current official language. Paste the up-to-date text from the UHM syllabus-template / Manoa Catalog. The summaries here are placeholders.*

**Academic Integrity.** All work submitted must be your own. Cheating, plagiarism, and unauthorized collaboration are violations of the UH Mānoa **Student Conduct Code** and will be reported. *[Insert current UHM Student Conduct Code statement + link.]*

**Disability Access (KOKUA).** Students with disabilities who need accommodations should contact the **KOKUA Program** (Student Services, UH Mānoa) and share their approved accommodations with the instructor as early as possible. *[Insert current KOKUA contact + link.]*

**Title IX / Nondiscrimination.** UH Mānoa prohibits sex/gender-based discrimination and harassment. Faculty are generally mandatory reporters. Students seeking confidential support should contact *[UHM confidential advocate / counseling]*. *[Insert current Title IX statement + Office contact.]*

**Attendance & Makeup Work.** Regular attendance and participation are expected. Makeup work is available only for documented, university-approved excused absences. *[Confirm UHM wording.]*

**Mental Health & Student Support.** *[Optional but recommended: UHM Counseling and Student Development Center (CSDC) statement + contact.]*

---

*Draft prepared 2026-07-09. Schedule and materials derived from the instructor's ECE 362 teaching-logic plan (backbone: Rosen 8e).*
