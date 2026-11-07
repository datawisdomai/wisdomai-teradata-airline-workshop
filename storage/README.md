# Storage and text enrichment lab

`WORKSHOP_SYNTHETIC_service_notes.csv` contains eight invented narratives. It has no source airline identifiers and must remain disconnected from actual airline events.

1. Data Sources → WisdomAI Storage → Add Table → Create from CSV.
2. Upload the notes file and preserve the explicit synthetic table name.
3. Set `note_id` as the primary key.
4. Configure textual index/RAG on `note_text` only, with `scenario` as a filter and `note_id` for identification/citation.
5. Search description: “Invented customer-service narratives for workshop text-retrieval exercises; never evidence of actual airline events.”
6. Test: “Using only the synthetic workshop notes, summarize baggage-related feedback and cite the supporting note IDs.” Expected notes: SYN-002 and SYN-007.
7. Negative test: “Which actual flight caused the baggage incident?” Expected: the synthetic notes do not identify actual flights and cannot establish one.

## Derived-table exercise
Create a summary over the synthetic note table with one row per scenario and count of notes. Use the exact database/table name assigned by the UI. Expected counts: baggage 2, service 2, accessibility 1, cabin 1, weather 1, wifi 1. This is a teaching summary, not an airline KPI.

## Existing budgets
Route P&L already contains budget_revenue, budget_operating_cost and budget_operating_income. Use those for actual/budget exercises rather than inventing replacement source budgets.

## Derived-column exercise

Create `workshop_data_classification` on the note table using `derived_data_classification.sql`. The reference preview returned “Synthetic workshop data” on all eight rows. This is a row-level calculation, distinct from the six-row scenario summary.

## Document-file exercise

Upload `WORKSHOP_SYNTHETIC_facilitator_brief.txt` through Overview → Add Files. It is an invented practice brief with document ID WS-BRIEF-001, not real airline policy. Wait for processing to complete before testing retrieval. Ask what another group must receive in the practice handoff; check the answer against the document and inspect its citation. Upload success alone does not prove retrieval readiness.
