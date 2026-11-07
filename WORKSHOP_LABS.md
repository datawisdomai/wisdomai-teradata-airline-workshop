# Technical workshop labs

Work on a dedicated attendee copy when available. Keep a known instructor domain as the reference.

## 1. Understand the data
Find route-month, flight, ticket-segment and survey grains. Explain why joining surveys to tickets and route financials can multiply revenue. Compare base fact and enriched view and identify the preferred source.
Checkpoint: each team can state the grain, date basis, and eligible denominator for its analysis.

## 2. Teach business context
Inspect the domain knowledge, metadata and synonyms. Ask about booking month versus travel month, miles outstanding, and unsupported corporate commitments.
Checkpoint: answers distinguish dates, balances and unsupported questions.

## 3. Govern metrics
Inspect passenger-count and distance-weighted load factors. Compare ratio-of-sums against average-of-ratios. Compute NPS from individual valid scores and distinguish it from mean recommendation score.
Checkpoint: teams can explain formula, grain, filter and denominator.

## 4. Train and review
Use a candidate question, inspect generated SQL, execute it, compare reference results and accept only verified matches. Record an incorrect example and the correction that fixes it.
Checkpoint: an executed reviewed-query example and a documented reason for accepting or rejecting a match.

## 5. Evaluate
Run the separate semantic holdout. Inspect both answers and judge explanations. Add numerical SQL ground truth to one independently validated case.
Checkpoint: record pass rate and one failure investigation; do not train on holdout wording.

## 6. Reuse skills
Invoke route profitability, operations, commercial performance, customer experience, and loyalty/co-brand playbooks. Inspect whether the intended skill is retrieved and whether its procedure is followed.
Checkpoint: evidence-backed summary with sample sizes, correct dates, and limitations.

## 7. Storage and RAG
Retrieve baggage-related feedback from the explicitly synthetic notes table. Expected note IDs: SYN-002 and SYN-007. Inspect citations and filter behavior. Explain why these notes cannot substantiate actual flight incidents.
Create or inspect the derived classification column and the scenario summary table, then explain row calculations versus aggregation. Inspect the invented facilitator brief in Files; after processing, retrieve its required handoff and check the document citation.
Checkpoint: correct citations, matching scenario counts, explicit synthetic-data disclosure, and a reproducible handoff.

## 8. Capstone and teach-back
Each team selects an executive question, explains source selection and grain, demonstrates the answer, validates one number, and hands another team a reproducible prompt and check procedure.
