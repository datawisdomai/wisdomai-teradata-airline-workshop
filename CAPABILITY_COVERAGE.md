# Capability coverage and scope

This inventory distinguishes demonstrated configuration from options that require a concrete workshop or source requirement. It prevents an untouched setting from being mistaken for a completed exercise.

| Area | Reference build and workshop treatment |
| --- | --- |
| Connection and data access | Existing Ali-TD Teradata connection reused. Credentials, connection grants and warehouse data are outside the repository. |
| Tables and views | 45 existing source objects; base facts and enriched views retained with source-selection guidance. ZAL_NUMS marked technical helper. |
| Display names and descriptions | 45 objects and 1,168 source columns populated. A schema reference supports adaptation. |
| Keys and relationships | 18 source key columns plus synthetic note ID marked; 49 relationships exported. Composite-grain facts are described without inventing a single-column key. |
| Column formatting | Selected numeric identifiers use String. Financial source units and ratio scales are explicit in context. Automatic presentation remains on many measures; inspect precision for the actual demo. |
| Lookup/enum behavior | Existing behavior retained. No custom enum-value mappings added. Use documented source values before introducing mappings. |
| Derived columns | One row-level synthetic classification column created; preview checked on all eight notes. Business aggregate calculations remain metrics. |
| Knowledge and instructions | 23 atomic entries plus domain instructions; ambiguity, dates, snapshots, currency and causal limits addressed. |
| Synonyms | 23 terminology sets. Distinct load-factor definitions remain separate. |
| Metrics | 43 metrics across finance, operations, customer experience, commercial, loyalty, maintenance, crew and weather. Full export provided; only listed source checkpoints are independently reconciled. |
| Entities | 11 business entities. Customer/crew identifiers are not exposed as additional entities for this executive workshop. |
| Reviewed queries | 31 SQL references, including all 30 training questions plus coverage check. Existing non-SQL app-building entry retained in the live domain. |
| Training | 30 questions loaded and matched; manual reviewed SQL completed the loyalty case. |
| Evaluations | 16 semantic holdouts and five numeric/storage cases. One final recorded run per suite passed; no claim of repeated-run stability. |
| Skills | Six analytical playbooks imported. Attendees inspect retrieval and procedure adherence during Lab 6; every possible skill invocation has not been independently scored. |
| Storage table | Eight invented notes with PK, content retrieval and scenario filtering. |
| Storage derived table | Six scenario counts; description distinguishes aggregate counts from source narratives. |
| Storage files | Invented facilitator brief processed successfully. A separate Thinking-mode chat returned the seven handoff requirements, correct completion criterion, synthetic disclosure, and citations to the actual document. This file check is separate from the five-case notes/numeric suite. |
| Health | Two surfaced recommendations addressed. Reanalysis is a maintenance step; no permanent clean-health guarantee. |
| Changelog | Available for inspecting changes and demonstrating traceability; not exported as an audit certification. |
| Calendar and timezone | Existing settings inspected and retained. No source timezone/currency or custom fiscal convention inferred from UI defaults. |
| Cache and crawl | Existing cache/crawl configuration retained. Refresh and cache management are instructor topics; this build does not benchmark freshness or performance. |
| RLS and column security | Existing policy unchanged. Use the approved organization roles and a separately designed policy exercise; synthetic permissions would not establish real access requirements. |
| Explorer/display settings | Existing experience retained. Confirm attendee roles before the event. |
| Recommended questions | Existing nine suggestions retained; some are generic/overlapping. Use the curated PROMPTS.md bank for the workshop; segment ambiguity now prompts clarification. |
| LiveApp | Existing Airline Command Cockpit reused. No claim that the repository exports/recreates its application code. |
| Tera Analyze in AI Studio | Separate environment and OEM demonstration required. Standalone WisdomAI results do not verify OEM capability or UI parity. |
| Distribution | Private working repository under ali-wisdom; shared copy under datawisdomai. Synchronize validated workshop revisions from the working copy before distribution. The earlier aalladin copy is historical. See README. |

For future extensions, add a feature only when it helps a business question or a learning objective, then record its validation. Do not manufacture currency definitions, historical attributes, security policies or customer evidence to fill a configuration field.
