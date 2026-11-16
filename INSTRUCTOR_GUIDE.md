# Instructor guide — three-hour WisdomAI concepts workshop

Use [INSTRUCTOR_CHEAT_SHEET.md](INSTRUCTOR_CHEAT_SHEET.md) for quick cues during class; open these detailed teaching notes beside the [student workbook](WORKSHOP_LABS.md). The [README](README.md) is the students' entry point; [GLOSSARY.md](GLOSSARY.md) contains the definitions. The optional [short demo rehearsal](DEMO_WALKTHROUGH.md) is for after the concept workshop.

## What success looks like

Every student can explain the difference between domain/context, metric/entity/skill, and training/reviewed query/evaluation. Every student leaves with a log containing a context proposal, a metric specification, a reviewed-query decision, three evaluation case designs, and checked evidence. A fluent sales demo alone is not the assessment.

For 25 attendees, use five groups of five if practical. Roles: question owner, context author, SQL reviewer, evaluation reviewer, presenter. Rotate at the break. Students keep their own notes even when sharing an exercise.

## Before the room opens

- Confirm Teradata instance and GitHub/ZIP access. Use **CSA Workshop - Facilitator** as the prepared reference.
- Assign five editable group domains using the approved existing connection, or announce **draft-and-observe** mode. Do not let 25 students edit the reference simultaneously. Practice domains and permissions must be prepared separately; their existence is not guaranteed by the repository.
- In editable copies, decide which context items are intentionally absent or will use team-specific names. Retain a checked reference. Avoid conflicting duplicate rules in a complete clone.
- Rehearse one knowledge edit, one metric save, one training question, review/accept controls, and a three-case evaluation in the actual instance. UI controls and job duration can vary.
- Have one completed training example and evaluation run ready in case jobs outlast a module. Use only evidence you can show.
- Prepare a small failure example: wrong event date, NPS as average score, or abbreviated financial totals failing an exact-value assertion. Explain whether it is an archived failure or a live one; do not pretend the reference domain is broken.
- Keep September 2026 fixed. Confirm source units and date basis. The original full-suite passes in evidence/ are historical, not the current room's result.
- Check the synthetic note table, summary, classification column and processed brief. Print or keep the expected answers below available.

## Run of show — exactly 180 minutes, including break

| Elapsed | Module | Teach / demonstrate | Student output |
| --- | --- | --- | --- |
| 00:00–00:10 | Orientation | Explain the domain/context → question → SQL/answer → review → evaluation cycle. | Business question and log |
| 00:10–00:30 | 1. Domain design | Compare three grains; inspect one key/relationship. | Source/grain/date map, metadata improvement |
| 00:30–01:00 | 2. Context building | Demonstrate one atomic knowledge entry and synonym. | Knowledge + synonym + spot check |
| 01:00–01:25 | 3. Metric/entity/skill | Explain the distinctions; show NPS, Route and a route-review skill. | Metric specification, entity explanation, skill draft |
| 01:25–01:35 | Break | Check progress and background jobs. | Saved log |
| 01:35–02:05 | 4. Training/review | Generate or open a candidate; validate before accepting. | One review decision with evidence |
| 02:05–02:35 | 5. Evaluation | Inspect a case/run; design three cases; diagnose a failure. | Three case designs and diagnosis |
| 02:35–02:50 | 6. Storage/RAG | Compare row label and scenario summary; open a citation. | Grain explanation and checked citation |
| 02:50–03:00 | 7. Teach-back | Select brief presentations; collect every student's log. | Reproducible handoff |

Protect the training and evaluation blocks. If time slips, shorten the optional app tour, extra prompts and file-retrieval extension; do not remove the review decision or failure analysis.

## Teaching cards: what to say, ask, and watch

### Orientation — 10 minutes

**Say:** “We are learning how to give an analytics assistant the right business meaning and how to check its work. The airline story is our practice dataset.”

**Ask:** “Can SQL execute successfully and still answer the wrong question?” Expected: yes—wrong date, grain, denominator, population, or units.

**Do:** confirm domain assignments and editing rules, then have each student start the workbook log. Avoid a lengthy product/menu tour.

### 1. Domain design — 20 minutes

**Say:** “A domain brings relevant sources and business context into scope. Grain tells us what one row means before we combine data.”

**Show:** route-month P&L, flight and survey views. Use table/column descriptions rather than reading all 45 objects.

**Expected:** route-month financials use month-end period; flights use flight date; survey analysis can use survey date. A route key repeats across months. Primary keys are verified, not guessed; the original key checklist does not require every object to have a single-column key.

**Watch:** students equating relationships with permission to sum independently detailed facts. Ask which measure will be repeated after the proposed join.

**Recovery:** if metadata editing is unavailable, students submit the exact proposed description. If connectivity fails, use the repository's schema reference and an existing completed answer; label this as fallback evidence.

### 2. Context building — 30 minutes

**Say:** “Metadata describes the data; knowledge supplies the rule; synonyms connect the vocabulary.”

**Ask:** “For ‘September sales,’ is a synonym enough?” Expected: no; booking versus travel period needs a business rule or clarification.

**Show:** one focused knowledge item, not a paragraph mixing unrelated rules. Have students create/draft one meaningful entry and one synonym for their own question. Check whether existing context already covers the ambiguity.

**Watch:** conflicting duplicate knowledge, invented fiscal/currency assumptions, or treating two different load factors as synonyms. A single improved answer is a spot check, not broad proof.

**Recovery:** retain a baseline answer or use a clearly identified prepared before/after example. If no observable behavior changes, evaluate the quality of the rule and test rather than claiming a win.

### 3. Metric, entity, skill — 25 minutes

**Say:** “Metric: how to calculate. Entity: which object. Skill: which analytical steps.”

**Show:** Survey_NPS, Operating_Margin_%, Route, and Airline route profitability review. Close editors without saving during inspection; Cancel can trigger a Discard changes confirmation.

**Expected calculations:**

- NPS: valid 0–10 denominator; 9–10 promoters, 7–8 passives, 0–6 detractors. 60% promoters − 20% detractors = NPS 40. Do not call it the mean rating.
- Margin: 100 × SUM(income) / SUM(revenue), with zero-denominator handling. Income/revenue 10/100 and 90/300 gives combined margin **25%**, not an unweighted **20%**. Margin can be negative.
- Route entity: inspect the configured ID and name columns; do not infer that a route-month financial row is the route entity itself.
- Skill draft: period → source/grain → measures → comparison → limitations. Similar prose alone does not establish that a named skill was retrieved; inspect usage if exposed.

**Recovery:** each student submits a metric specification and skill draft even if controls or runtime prevent saving/testing everything.

### 4. Training and reviewed queries — 30 minutes

**Say:** “Training proposes examples and matches. Review is the acceptance decision. Neither replaces source validation or evaluation.”

**Do:** choose one question per group from training/candidate_queries.csv. Demonstrate **Training → Add queries**, generation, inspection, execution/reconciliation, and the actual review action available in this instance. Keep full 30-question imports outside this timed exercise.

**Review checklist:** correct subject/source; event date and boundaries; grain and joins; eligible denominator; units; null/zero behavior; source reconciliation; explainable output.

**Ask before acceptance:** “What evidence would make you reject this query?” Expected: a concrete semantic or numerical mismatch, not merely a preference for different SQL formatting.

**Watch:** accepting because SQL ran, copying the answer as its own ground truth, or implying model fine-tuning.

**Recovery:** while training runs, review a completed candidate. Record the new job as pending. Students can hand in an accept/reject/revise decision even without a saved match. Do not label unexecuted SQL as validated.

### 5. Evaluation sets — 30 minutes

**Say:** “An evaluation set makes expected behavior explicit and repeatable. It helps us catch regressions; it is not a claim that every possible answer is correct.”

**Show:** Evaluation Sets → a case → Run History → View Group → answer and judge explanation. The inspected facilitator domain used generic names Evaluation Set 1 (16 cases) and Evaluation Set 2 (5); identify by contents, not name alone.

**Students design:** one numerical case with independently checked reference SQL, one behavior/ambiguity case, and one holdout. If execution is enabled, create a small team-named practice suite; otherwise review their designs and an existing completed run.

**Use this failure discussion:** exact financial totals may be required even when charts show rounded millions. Ask whether the answer, presentation, expectation or judge is at fault. A date-basis error needs a semantic correction; an incorrect assertion needs a justified test correction.

**Watch:** weakening a valid assertion to obtain a pass, using training wording as the only test, or quoting old 16/16 and 5/5 results as current workshop accuracy.

**Recovery:** use an archived failure and final correction from evidence/validation-log.md. If all current cases pass, students should still explain a plausible regression and which case would detect it. Background runtime must not consume the entire discussion.

### 6. Storage, derived data and retrieval — 15 minutes

**Say:** “A row-level derived column calculates something for each row. A derived table can change the grain. A file supplies document content. Retrieval and citations give us evidence to inspect.”

**Answer key:**

- Source: eight invented notes, one row per note.
- Classification column: Synthetic workshop data on the eight reference rows.
- Summary: six rows—baggage 2, service 2, accessibility 1, cabin 1, weather 1, wifi 1.
- Baggage citations: **SYN-002** and **SYN-007**. Require synthetic disclosure; the notes do not establish real flight incidents.
- Brief: **WS-BRIEF-001**. Handoff = business question, exact prompt, source/period, checked number, metric definition, limitations, follow-up. Completion = another group reproduces the answer and explains evidence and limits.

**Watch:** treating upload success as successful retrieval, assuming a derived table is necessarily physically materialized, or attributing invented notes to an actual route.

**Recovery:** inspect the CSV/file text locally and an existing cited answer. State explicitly that this does not prove a new retrieval request worked.

### 7. Teach-back — 10 minutes

Select a few 60-second presentations and collect all logs/case designs. Ask:

1. What is your question, source grain and event date?
2. Which context feature did you choose, and why?
3. What did you check before accepting the SQL or answer?
4. Which evaluation catches a future failure?
5. What remains uncertain?

Use five checks, 0–2 points each: scope/grain/date, context placement, calculation/procedure, evidence/review decision, evaluation/limitations. A useful outcome is a reasoned, reproducible artifact—not a perfect score or a product certification.

## Quick distinction card

| If a student asks… | Short answer |
| --- | --- |
| “Where should this rule go?” | Meaning/convention → knowledge; vocabulary → synonym; calculation → metric; procedure → skill; checked example → reviewed query; expected behavior/result test → evaluation. |
| “Is training a model retrain?” | No. Here it supports generating and reviewing example question matches. |
| “Does ACCEPTED mean correct forever?” | No. Ask what checks were performed and whether the source/definition changed. |
| “Does a passing judge prove the answer?” | No. Inspect the answer, expectation and source evidence. |
| “Do I need all 45 primary keys?” | No. Inspect relevant grains and verified keys; do not invent a single-column key for a composite grain. |
| “Can we skip straight to a demo?” | The optional rehearsal is available after the concept exercises; retain the learning artifacts and checks first. |

Keep [GLOSSARY.md](GLOSSARY.md) available for longer explanations. Use the [builder guide](DOMAIN_DEPLOYMENT_GUIDE.md) outside class for connection/domain provisioning details.
