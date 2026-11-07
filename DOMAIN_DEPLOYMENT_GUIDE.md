# Deploy and adapt the domain

## Before importing

Use a dedicated workshop domain connected to the airline schema. Confirm source objects and column names against `context/schema-reference.json`. Replace database and connection labels in CSV/SQL assets for the target environment. Obtain attendee access through the normal organization process; the repository supplies no credentials or data connection.

Export the current domain through Overview → domain card More → Export metadata. Keep the native JSON as a local recovery artifact. This build's native export is excluded from Git because it includes instance and actor identifiers. Do not import a whole-domain backup into another domain without inspecting how the target instance maps objects and connections.

## 1. Source metadata and relationships

In Data Sources, use the source More menu → Import metadata with `context/metadata.csv`. Confirm the preview matches 45 tables/views and 1,168 columns before applying.

Use `context/relationships.csv` as the relationship checklist. In each source table choose Create Relationship, select the source and destination columns, and use the stated Many to One cardinality. The file is a checklist, not a claimed native bulk-import format. The reference build uses 49 relationships; the destination key checks are in `evidence/key-uniqueness.csv`. Recheck uniqueness in a new source. Cardinality does not establish referential completeness; inspect unmatched keys when relevant. INNER joins can exclude unmatched rows.

Mark verified keys through column advanced settings. The reference uses primary keys for 14 dimensions, base/view flight and ticket, and synthetic note ID. Format numeric identifier columns as strings when displayed. Do not mark a single column as unique in a fact with a composite grain unless a source test proves it.

## 2. Business context

In Context, use each section's Import CSV:

| Section | File | Required import header |
| --- | --- | --- |
| Knowledge | `context/knowledge.csv` | `Knowledge` |
| Synonyms | `context/synonyms.csv` | `Name,Synonyms` |
| Metrics | `context/metrics-complete.csv` | Use its exported multi-column structure |
| Entities | `context/entities.csv` | `Entity,ID Column,Name Column,Default Sort Column,Default Sort Order,Related Columns` |
| Skills | `skills/skills-import.csv` | `Skill Markdown` |

Use one complete metric import on a clean domain. Four standalone COUNT(*) metrics in the original build did not bind to a table; their corrected expressions count explicit key columns. Imported metric names are normalized with underscores. Confirm 43 included metrics and inspect staleness. Run financial, survey and operations checks before teaching.

Six individual skill Markdown files are also provided for reading and adaptation. The native import expects one complete frontmatter/body document per CSV cell; the human-readable `skills.csv` is not that import format.

In Advanced → WisdomAI Chat behavior, save `context/custom-instructions.md`. Preserve the distinction between source data, invented storage notes, and unsupported assumptions.

## 3. Train and review

Import `training/training-import.csv` into Training. Its columns are `Question,Answer`; Answer contains reference SQL guidance, not an independently certified response. Run training, inspect each match, execute/reconcile it and accept verified matches. Never accept solely because the generated SQL looks plausible.

The reference build has all 30 questions represented in the final reviewed SQL export. Twenty-nine generated matches were accepted after successful training execution; the loyalty tier monthly aggregate was executed in SQL Playground and reviewed separately. The additional coverage query produces 31 reviewed SQL entries. The Overview count of 32 also includes the pre-existing non-SQL app-building entry.

`context/reviewed-queries.csv` is the final SQL-only reference. Some exported queries use display names; apply the matching metadata first and inspect table resolution in the target instance. `training/candidate_queries.csv` retains the original physical-name guidance. A matched question does not imply the generated SQL is byte-identical to that guidance.

## 4. Storage, derived data and retrieval

Upload `storage/WORKSHOP_SYNTHETIC_service_notes.csv` into WisdomAI Storage as a table. Mark note_id as the primary key. Configure note_text for content retrieval, scenario as a filter, and note_id for identification/citation. Describe the table as eight invented workshop notes, one row per note, unrelated to actual customer incidents.

Create `WORKSHOP_SYNTHETIC_note_summary` from `storage/note_summary.sql`. Its description should state: one row per scenario with a synthetic note count; use the source notes for narratives and citations. It must not be joined to airline actuals as incident evidence.

Create the optional row-level `workshop_data_classification` column using `storage/derived_data_classification.sql`; preview all eight labels. Upload `storage/WORKSHOP_SYNTHETIC_facilitator_brief.txt` as a file and check processing status before testing its cited retrieval.

Validate counts: baggage 2, service 2, accessibility 1, cabin 1, weather 1, wifi 1. Baggage retrieval should cite SYN-002 and SYN-007 and explicitly disclose the invented nature of the notes.

## 5. Evaluate and inspect health

Create separate evaluation sets using `evaluations/holdout-import.csv` and `evaluations/numeric-storage-import.csv`. The native headers are `query,sql,assertions,no_ground_truth`. Assertions are JSON arrays of strings inside CSV cells. Run Thinking mode, inspect every failure and its judge explanation, and reconcile the answer with source SQL.

Keep training questions and semantic holdouts separate. Correct the business rule or presentation issue; do not weaken an expectation merely to obtain a passing score. The reference financial test initially failed because abbreviated labels omitted exact source-unit totals. The fix requested exact amounts alongside abbreviated charts. The currency test required an explicit request for missing currency and FX basis.

Health → Run Analysis may take time. Review both User-facing and Proactive categories. Accept only recommendations supported by the schema/business meaning. The final changes clarified customer-segment ambiguity and the synthetic summary's grain. Re-run analysis after changes; a resolved prior recommendation is not proof that future analyses find no issues.

## 6. Export, share and maintain

Export final metadata, metrics and reviewed SQL, plus run screenshots and aggregate source checks. Exclude native instance backups, credentials, raw customer records and session data from Git. Keep `evidence/validation-summary.json` current. Commit reusable assets and publish the same versioned content to the two identified GitHub repositories, with one documented upstream.

After a source refresh or context change, rerun affected SQL checks and both suites. Rehearse the LiveApp story. Do not assume that this kit automatically recreates the existing cockpit, configures organization permissions, or reproduces the separate Tera Analyze experience.
