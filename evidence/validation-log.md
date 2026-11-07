# Reference build validation log

Reference: TD-AirlineDemo, proddemo.askwisdom.ai. Build date: November 6, 2026 Pacific time. Export timestamps fall on November 7 UTC.

## Configuration evidence

The final pre-file native domain export confirmed 45 source objects, 1,168 source columns, 49 relationships, 23 knowledge entries, 43 metrics, 11 entities, six skills and 31 SQL reviewed queries. The UI shows 32 reviewed entries including the original non-SQL app-building request. All 30 training questions appear among the SQL entries.

The original baseline had no knowledge, metrics, synonyms, entities, skills, training or evaluation sets. Its existing LiveApp and airline warehouse were reused. The repository does not create that warehouse or export the app code.

The 49 relationships were checked against context/relationships.csv. An interrupted save had omitted the ticket-to-sales-channel relationship; the final export confirmed its correction. Four COUNT(*) metrics did not bind during import; explicit table-qualified key counts saved successfully, bringing the exported metric total to 43. The offline integrity check validates referenced columns, not the numerical correctness of every metric.

After that export, a derived classification column was added to the synthetic note table; its preview showed “Synthetic workshop data” for all eight rows. An invented facilitator brief was uploaded successfully as a file. Its initial status was Waiting. The Mac initially locked before the processing/retrieval recheck; after unlocking, the file still showed Waiting. Do not equate upload success with file retrieval readiness.

## Executed source checks

- Route-month coverage: first 2024-10-31, last 2026-09-30; 1,920 rows; recorded all-period revenue 1,544,614,175.33 in source monetary units.
- September 2026 route-month: 80 rows; revenue 64,612,818.33; operating income 6,860,708.98; passenger-count load factor about 85.0%, distance-weighted load factor about 85.3%.
- September scheduled flight legs: 1,938; cancellations 27; diversions four; eligible-arrival OTP about 81.6%; cancellation rate about 1.4%.
- September survey-date records: 7,029 responses; 3,705 promoters; 1,146 detractors; NPS about 36.4; mean score about 8.4. Mean score and NPS are distinct.
- Eighteen uniqueness checks: count equals distinct key count for 14 dimensions and base/view flight and ticket sources. See key-uniqueness.csv. This does not prove referential completeness or every fact's uniqueness.
- Loyalty monthly tier aggregate executed successfully (five rows, 2.6 seconds) and saved as reviewed SQL, completing coverage of the 30 training questions.

A combined numerical export uses one-decimal numeric rendering due to Teradata UNION type inference; the separate financial evaluation checks exact amounts. No source currency or timestamp timezone was established from these results.

## Training and reviewed SQL

Thirty candidate questions were imported with reference SQL guidance. Twenty-nine generated successful matches were accepted. The missing loyalty tier aggregate was executed and reviewed separately. Candidate files preserve the original guidance; exported reviewed SQL can differ. Accepted-match coverage is not a claim of exhaustive result-by-result independent auditing of all generated queries.

## Semantic holdout

Sixteen separate cases, Thinking mode. Initial run: 15/16. The currency case avoided an unsupported conversion but failed to explicitly request the missing source currency and FX basis. Domain instructions were corrected. Final recorded run: 16/16. See semantic-holdout-pass.png.

## Numerical and storage suite

Five cases: exact route financial totals; scheduled flights/cancellations/diversions; survey/promoter/detractor counts; synthetic baggage-note retrieval with citations; synthetic scenario counts. Initial run: 4/5. Financial output abbreviated the totals (64.61M and 6.86M); exact-source-unit expectations were not satisfied by the presentation. Instructions were changed to include exact financial totals to two decimals alongside chart abbreviations.

A date-filter assumption was saved only for that question: September records in the monthly source have month_end_date 2026-09-30, making the tested range and equality filters equivalent. It was not generalized to all datasets.

Final recorded Thinking run group ET_JOB_RUN_bb211ed230ab47a9a8122deda8fecef0: 5/5 consistently passing across the single run. See numeric-storage-pass.png. “Consistently” is the product's label; there is no repeated-run stability evidence here.

The final skill/relationship/segment-description additions and later derived-column/file extension were not all included in those earlier runs. Re-run affected cases after further edits and before the event. No latency or broad accuracy benchmark was performed.

## Health

The completed analysis surfaced two high-priority recommendations. One was a missing description separating synthetic note narratives from their scenario summary. The suggested accurate description was accepted. The other was an ambiguous “customer segment” term. A new knowledge entry requires clarification of the intended attribute and revenue/date basis rather than inventing a canonical hierarchy. Overview subsequently showed Health (0), “All caught up.” Future analysis can surface new issues.

## Distribution and remaining dependencies

Portable assets exclude the full native instance backup and actor metadata. The private GitHub destinations are aalladin/wisdomai-teradata-airline-workshop and datawisdomai/wisdomai-teradata-airline-workshop. The WisdomAI copy was pushed with Git; the personal copy uses its separate authenticated browser session. Attendee access, isolated exercise domains, source currency/timezone confirmation, complete talk-track rehearsal and the separate Tera Analyze environment remain event-preparation tasks.
