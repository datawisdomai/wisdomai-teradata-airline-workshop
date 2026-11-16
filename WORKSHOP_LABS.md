# Student workbook — three-hour WisdomAI concepts workshop

Follow the timing in [README.md](README.md). Keep [GLOSSARY.md](GLOSSARY.md) open. Your instructor will explain each module, demonstrate one example, then give you time to build or draft your own.

## Before the clock starts

1. Sign in to [teradata.wisdom.ai](https://teradata.wisdom.ai).
2. Find **CSA Workshop - Facilitator**, the reference domain.
3. Confirm your assigned editable practice domain with the instructor. Make changes only there. If no practice copy is assigned, use the **draft-and-observe path**: write the artifacts below in your log and watch the instructor save and test a selected example. Do not overwrite the reference domain.
4. Choose a business question: route profitability, flight reliability, or customer experience. Use September 2026 for the fixed exercises.
5. Copy the following log into your own notes. Each student keeps a log even when working in a group.

```text
Student/group:
Assigned practice domain, or draft-and-observe:
Business question:
Module / artifact name:
Source and grain:
Period and event-date basis:
Definition, context, or SQL I proposed:
Test question and expected behavior/result:
Observed result and evidence:
Accept / reject / revise, and why:
One limitation / next question:
```

## Orientation — 00:00–00:10

Read the concept table in the README. In your log, write one business question and one way an answer could be misleading even if the SQL executes successfully.

**Checkpoint:** explain why “the query ran” and “the answer is correct for the business” are different claims.

## 1. Design a domain — 00:10–00:30

**Learn:** domain, data source, metadata, grain, key, relationship, and cardinality. See the first two glossary sections.

**Inspect** (about 5 minutes):

1. Open **Domains → your assigned domain → Data Sources**.
2. Locate `ZAL_VW_ROUTE_PNL_MONTHLY`, `ZAL_VW_FLIGHT`, and `ZAL_VW_PASSENGER_SURVEY` in the airline source. Display names may be friendlier; match the physical names.
3. Inspect descriptions and columns. Identify the reporting date and what one row represents for each.

**Build or draft** (about 8 minutes):

4. Write a small domain design for your business question: which of those sources belong in scope, their grains and date bases, and one tempting but unsafe join.
5. Inspect one existing key or relationship with the instructor. Explain why a route key alone is not unique in a route-month table. You do not need to mark keys on all 45 objects.
6. Propose one table or column description that would help another engineer choose the correct source. Save it only in your practice domain if the instructor has enabled this exercise; otherwise record the proposed text.

**Check and explain back** (about 7 minutes): your map should distinguish route-month financials, one flight leg, and one survey response. A Many to One relationship describes key matching; it does not make every detail-fact join safe for summing revenue. Combining subjects often requires separate aggregation first.

**Deliver:** source/grain/date map and one metadata improvement.

## 2. Build business context — 00:30–01:00

**Learn:** metadata describes data structure; knowledge supplies interpretation rules; synonyms connect vocabulary. None is a substitute for a metric formula.

**Inspect** (about 5 minutes):

1. Open **Context → Knowledge** and find **Travel versus booking period** and **Snapshot measures**.
2. Open **Synonyms** and find **Net Promoter Score → NPS**.
3. Read [context/knowledge.csv](context/knowledge.csv) and [context/synonyms.csv](context/synonyms.csv) as examples, not as files to re-import into the reference domain.

**Build or draft** (about 12 minutes):

4. Write one atomic knowledge entry for a real ambiguity in your chosen question. Use this pattern: **when the user asks X, use Y, because Z; clarify if A is missing**.
5. Write one synonym set. State the canonical concept and its alternative wording. Do not merge distinct concepts, such as passenger-count and distance-weighted load factor, into interchangeable synonyms.
6. Save those two items in your assigned practice domain using the corresponding Context section's add control, or write their exact text in your log. Use a team-specific name for any new item; do not duplicate or edit an existing reference entry accidentally.

Example knowledge draft:

> For travel-period ticket revenue, filter by flight_date. For booking-period revenue, filter by booking_date. If the user only says “September sales,” clarify which period basis they mean.

**Test** (about 8 minutes): in a new chat, select your practice domain and ask:

```text
For September 2026, show ticket passenger revenue by sales channel.
Explain whether you are using booking date or flight date, and clarify
what you need to know if “September sales” is ambiguous.
```

7. Inspect the chosen date basis and source. Compare with your intended rule. If testing a change, retain the earlier answer or use a prepared baseline from the instructor; do not invent a before/after difference.

**Explain back** (about 5 minutes): what changed, why it belongs in knowledge rather than a synonym, and what evidence shows the rule was followed. One answer is a spot check, not a general guarantee.

**Deliver:** metadata improvement, one knowledge entry, one synonym set, and a test observation.

## 3. Define calculations, objects, and procedures — 01:00–01:25

**Learn:** metric = calculation; entity = identifiable business object; skill = analytical procedure.

1. **Metrics:** inspect `Survey_NPS` and `Operating_Margin_%` in Context. Opening a metric can open an editor; use **Cancel → Discard changes** to exit an inspection without saving.
2. Write NPS in business terms: promoters 9–10 minus detractors 0–6, divided by all valid 0–10 responses, multiplied by 100. Passives 7–8 remain in the denominator. It is a score, not the average rating.
3. Write operating margin as `100 × SUM(operating_income) / NULLIF(SUM(total_revenue), 0)`. State its grain, date filter, units, and zero-denominator behavior. It can be negative for losses.
4. **Build or draft one metric specification:** name, source, formula, eligible records, period basis, unit/scale, and a simple test. If building it in a practice domain, use the instructor's assigned name and an expression based on one source table. Do not overwrite a reference metric.
5. **Entities:** open the existing Route entity. Identify its ID and name columns. Explain why a route is an entity and operating margin is a metric. If the entity is absent, inspect [context/entities.csv](context/entities.csv).
6. **Skills:** open **Airline route profitability review**, or read [its Markdown](skills/airline-route-profitability-review.md). Draft a short skill for your question: resolve the period; select the source/grain; calculate the measures; compare; state limitations. Save only in your practice domain if assigned.
7. In a domain-scoped chat, test your metric question or skill. Where the answer exposes skill usage, inspect it; similar prose alone does not prove a skill was retrieved.

**Check:** 20 units of operating income over 100 units of revenue gives 20% margin. For routes with income/revenue 10/100 and 90/300, combined margin is 25%, not the 20% unweighted average of their margins. With 60% promoters and 20% detractors, NPS is 40.

**Deliver:** one metric specification and test, an entity explanation, and a short skill draft. You do not need to build every entity or skill during this block.

## Break — 01:25–01:35

Save your log. The instructor checks access, progress and any pending jobs. Do not use the break to change shared configuration.

## 4. Train a question and review its SQL — 01:35–02:05

**Learn:** a training example proposes a question and guidance; generated candidate SQL must be inspected; a reviewed query records an accepted example. Training is not language-model fine-tuning.

**Inspect** (about 5 minutes):

1. Open **Training** in the reference domain. Inspect a question, its reference guidance, candidate SQL and status with the instructor.
2. Open **Context → Reviewed Queries** and inspect the corresponding question/SQL where available. A candidate and an accepted query need not be identical. Do not treat an ACCEPTED label alone as proof that a careful review occurred.

**Build and test one example** (about 15 minutes):

3. In your practice domain, open **Training → Add queries** and add one question, or draft the question and guidance in your log. Choose one example from [training/candidate_queries.csv](training/candidate_queries.csv); do not import all 30 during this exercise.

Example:

```text
For September 2026, show scheduled flight counts and cancellations
by route code using flight date.
```

4. Start training only in the assigned practice domain when instructed. If it is still running, continue the review exercise using an existing completed example. Do not resubmit the same job repeatedly.
5. Inspect source tables, date filters, aggregation and cancellation logic in the candidate SQL. Execute and compare with a trusted source query or instructor-provided checked result. **SQL that executes can still use the wrong date, denominator or grain.**
6. Accept/save the match as reviewed only if the evidence supports it, using the available review action. Otherwise reject or revise it and explain the issue. If you are drafting, record the decision and evidence rather than pretending a save occurred.

**Explain back** (about 10 minutes): why your example belongs in training/reviewed queries, what you checked, and which new questions it does not establish correctness for.

**Deliver:** one question, candidate SQL, checked evidence, and accept/reject/revise decision. In draft-and-observe mode, the instructor demonstrates the save/review controls on one selected example.

## 5. Design an evaluation set and investigate a failure — 02:05–02:35

**Learn:** evaluation set, test case, assertion, ground truth, holdout, judge, regression, and pass rate. Read the glossary definitions before treating a score as a verdict.

**Inspect** (about 5 minutes):

1. Open **Evaluation → Evaluation Sets**. In the inspected facilitator domain, **Evaluation Set 1** contained 16 cases and **Evaluation Set 2** contained 5. Names can differ in other copies; identify a suite by its questions.
2. Read one question and its expectation. Then open **Run History → View Group** and inspect a completed case: answer, reference SQL/assertions, score, and explanation.

**Build or draft three cases** (about 10 minutes):

3. Use [evaluations/holdout_cases.csv](evaluations/holdout_cases.csv) and [evaluations/numeric-storage-import.csv](evaluations/numeric-storage-import.csv) as examples. Write:
   - **One numerical case:** a question with reference SQL whose result you have checked independently.
   - **One behavior case:** for example, converting revenue to euros without a documented source currency or FX basis should request missing inputs.
   - **One holdout case:** different wording, period or grouping from your training question. Define the expected handling and validate any numeric ground truth separately.
4. For each case, record the question, source/date scope, expected result or behavior, and how you will judge it. Do not invent a number because the model returned it.
5. In an assigned editable domain, use **Evaluation → Add Evaluation** to create a small, team-named set and add/import your cases with the instructor. Do not overwrite the reference suites. If time or permissions prevent execution, hand in the case designs and inspect a completed reference run.

**Run, diagnose, explain** (about 15 minutes):

6. Run the small set in the instructor-specified mode where available. While it runs, compare your expectations with another student's cases.
7. Investigate one failure or the instructor's prepared example. Is the issue the answer, source selection, date/denominator, missing context, output formatting, or the test itself?
8. Propose a justified correction and which cases to rerun. Do not weaken a valid expectation simply to turn a score green. Explain why a training wording and a holdout wording should stay separate.

**Deliver:** three case designs, an observed run/case or explicit pending status, and one failure analysis. A queued run is not a pass.

## 6. Understand storage and check retrieved evidence — 02:35–02:50

**Learn:** storage table, derived column, derived table, file, retrieval/RAG, and citation.

1. Open **Data Sources → Tera Storage** in the reference domain. Inspect **Workshop Synthetic Service Notes**, **Workshop Synthetic Note Summary**, and the facilitator brief file. Display names differ from physical SQL names.
2. Explain the grain change: one row per note becomes one row per scenario in the summary. Inspect its SQL; `WHERE synthetic_flag = 1` filters records and `GROUP BY scenario` with `COUNT(*)` aggregates them. Expected counts are baggage 2, service 2, and accessibility, cabin, weather and wifi 1 each.
3. If present, inspect the row-level `workshop_data_classification` derived column. It labels each note; it does not summarize multiple rows. A derived-table definition alone does not tell you whether results are physically materialized.
4. In a new, domain-scoped chat, send:

```text
Using only the synthetic workshop service notes, summarize baggage
feedback. Cite note IDs and state that the material is invented,
not evidence about actual passengers or flights.
```

5. Open the citations. Check support from **SYN-002** and **SYN-007**, and confirm the synthetic disclosure. The filter flag alone does not independently prove the notes are invented; their provenance and labeling matter.
6. Inspect the file's processing status. If time permits, ask what the synthetic facilitator brief **WS-BRIEF-001** requires in a group handoff, and open its document citation. Upload success alone does not establish processing or retrieval readiness.

**Deliver:** explanation of table versus derived column versus derived table versus file, plus one checked citation. Do not upload duplicates into the reference domain.

## 7. Teach back and recap — 02:50–03:00

Each student or group gives a concise handoff; the instructor selects a few for a 60-second verbal teach-back.

1. State the business question and domain scope.
2. Explain one context choice, one calculation/procedure, and why they belong in different features.
3. Show one checked query result or citation.
4. Explain a reviewed-query decision and one evaluation case that would catch a future regression.
5. State a limitation or pending check.

**Done means:** another student can reproduce your example and explain why it is appropriate. Hand in your completed log and the three test-case designs. A polished customer demo is an optional next step, not the sole learning outcome.

## After class

Use [DEMO_WALKTHROUGH.md](DEMO_WALKTHROUGH.md) for the short demo rehearsal and [PROSPECT_TALK_TRACK.md](PROSPECT_TALK_TRACK.md) to adapt the story for a prospect. Use [DOMAIN_DEPLOYMENT_GUIDE.md](DOMAIN_DEPLOYMENT_GUIDE.md) if you need to build or adapt a complete environment.
