# Instructor cheat sheet — keep open during class

**Duration:** 3 hours, including a 10-minute break. **Students follow:** [README](README.md) → [WORKSHOP_LABS](WORKSHOP_LABS.md). **Definitions:** [GLOSSARY](GLOSSARY.md). **Detailed teaching/recovery notes:** [INSTRUCTOR_GUIDE](INSTRUCTOR_GUIDE.md).

**Opening line:** “Today you will learn how to give WisdomAI the right business meaning, review its work, and test whether it behaves as expected. The airline is our practice scenario.”

## Live clock and cues

| Elapsed | Say / show | Have students do | Check before moving on |
| --- | --- | --- | --- |
| 00:00–00:10 | Domain/context → question → answer/SQL → review → evaluation | Pick a question; start their workbook log; confirm creation access/source | They know the source and planned domain name. |
| 00:10–00:30 | Create New Domain first; then grain before joins | Create own named domain; map source/grain/date; propose metadata | New domain uses the right source; grains differ. |
| 00:30–01:00 | Knowledge = interpretation; synonym = vocabulary | Build/draft one atomic knowledge entry and one synonym; spot-test | The rule is meaningful, scoped, and not conflicting. |
| 01:00–01:25 | Metric = calculation; entity = object; skill = procedure | Specify/test a metric; inspect Route; draft a short skill | Explain formula, denominator, units, zero handling. |
| 01:25–01:35 | **Break** | Save logs | Check access and pending jobs. |
| 01:35–02:05 | Training proposes; review decides what to accept | One question → candidate SQL → evidence → accept/reject/revise | SQL execution alone is not semantic validation. |
| 02:05–02:35 | Evaluation = repeatable expectations; inspect answer and judge | Design numeric, behavior, and holdout cases; run or inspect; diagnose one failure | They can explain what a test checks and why a failure occurred. |
| 02:35–02:50 | Row calculation vs summary; retrieval with evidence | Inspect storage objects; open a baggage citation | SYN-002 / SYN-007 support the answer; synthetic disclosure. |
| 02:50–03:00 | Reproduce and explain, not just present | Selected 60-second teach-backs; collect everyone's log/cases | One context choice, checked result, regression test, limitation. |

## Answers to keep at hand

- **NPS:** promoters 9–10; passives 7–8; detractors 0–6; valid 0–10 denominator. 60% promoters − 20% detractors = **40**. Not average rating.
- **Margin:** 100 × total operating income / total revenue; undefined if denominator is zero; can be negative. Routes 10/100 and 90/300 combine to **25%**, not the **20%** average of margins.
- **Snapshot:** a month-end miles balance is a state, not a flow to add across months.
- **Storage:** eight notes → six summary rows: baggage **2**, service **2**, accessibility/cabin/weather/wifi **1** each. Derived column labels each row; derived table summarizes.
- **Brief WS-BRIEF-001:** question, exact prompt, source/period, checked number, metric definition, limitations, follow-up. Complete when another group reproduces the answer and explains the evidence/limits.
- **Training ≠ model fine-tuning. Reviewed query ≠ correct forever. Passing judge ≠ universal accuracy.**

## Five questions to ask repeatedly

1. What does one row represent, and which date applies?
2. Does this belong in knowledge, synonyms, metrics, entities, skills, reviewed queries, or evaluations—and why?
3. What independent evidence supports acceptance?
4. What would make this fail after a change?
5. What remains uncertain?

## Guardrails and recovery

- Prepare **one shared connection and one facilitator domain**, not 25 domains. Confirm attendee creation/source permissions before class. Students create `CSA Workshop - <first-name>-<last-name>` during Module 1.
- Creation: **Domains → Add domain → Domain Name → Select Data Source → wisdomai under Partner Lab → Create Domain**. Use the confirmed connection/database pair; another wisdomai may be listed under a different connection.
- Students edit/test in their own new domains. Inspect completed examples and storage in the facilitator domain. If access is blocked, resolve it and use draft-and-observe temporarily; do not have everyone edit the reference.
- If a job runs long, review a completed example and record the new job as pending. Do not call a queued job a pass.
- If time slips, cut the optional app tour and extra demo prompts; preserve SQL review and evaluation diagnosis.
- Close inspection editors with **Cancel → Discard changes** if prompted. Do not save by accident.
- Treat archived figures and pass rates as reference evidence. Label any fallback or archived example accurately.

**Collect:** each student's source map, context entries, metric/skill specifications, reviewed-query decision, three test designs, and checked citation or result.
