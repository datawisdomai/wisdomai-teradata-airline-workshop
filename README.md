# WisdomAI concepts workshop — three-hour student guide

**Students: start here, then follow the [step-by-step workbook](WORKSHOP_LABS.md).** Keep GitHub open beside the [Teradata WisdomAI instance](https://teradata.wisdom.ai). Your instructor will explain and demonstrate each concept, then pause for you to complete the corresponding exercise.

This workshop teaches you to **design a domain, build business context, define calculations and analytical procedures, review generated SQL, and test answers**. You will build small, meaningful examples and explain why they belong in the domain. The airline scenario supplies the data; a product demo is one application of what you learn.

## What to open

1. **This README:** the class agenda and navigation.
2. **[Student workbook](WORKSHOP_LABS.md):** numbered actions, examples, checks, and what to record for every exercise.
3. **[Glossary](GLOSSARY.md):** plain-language definitions and airline examples. Keep it available throughout.
4. **Teradata WisdomAI:** sign in and find **CSA Workshop - Facilitator**, the prepared reference domain, or the domain your instructor assigns.

No Git installation or Python is required. Read Markdown files directly on GitHub. To read a CSV, click its filename in the file list; **Raw** shows the original text when GitHub's table preview is inconvenient. Downloading a ZIP is optional until you want an offline copy.

## How we will work

Each module follows **explain → inspect → build → test → explain back**. Work individually or with your assigned group, and record your own decisions and results using the workbook's copyable exercise log.

**Each student creates a uniquely named domain during Module 1. You do not need 25 domains created in advance.** The instructor provides one working Teradata connection and the prepared `CSA Workshop - Facilitator` reference domain. Students reuse the connection; they do not create database accounts, copy the warehouse, or enter connection credentials.

Before class, the instructor must confirm that attendee roles can use **Domains → Add domain** and access the workshop source. In the inspected instance the source is **wisdomai under Partner Lab**; another connection also exposes a database named wisdomai, so use the connection/database pair the instructor confirms. This workflow was inspected using the facilitator's account; attendee permissions still need a pre-work check.

In Module 1, create `CSA Workshop - <first-name>-<last-name>` (add a suffix if needed), then use that domain for your edits and chat tests. Keep `CSA Workshop - Facilitator` unchanged as the reference. If permissions prevent creation, tell the instructor and temporarily draft artifacts in your log while the access issue is resolved; this is a fallback, not an assumption that the instructor has prebuilt your domain.

The connection is already provisioned. Domain building includes creating your workspace, choosing the existing source, inspecting grains and relationships, and adding the context needed for a business question. You are not expected to configure all 45 source objects or mark every table with a primary key during class.

## Three-hour agenda

Times are relative to the workshop start. The schedule includes a ten-minute break.

| Time | Module | What you will produce |
| --- | --- | --- |
| 00:00–00:10 | Orientation and the learning model | Your business question and exercise log |
| 00:10–00:30 | 1. Domains and data meaning | Your new domain plus a source/grain/date map |
| 00:30–01:00 | 2. Context building | One metadata improvement, knowledge entry, and synonym set |
| 01:00–01:25 | 3. Metrics, entities, and skills | A checked metric, entity explanation, and short analytical skill |
| 01:25–01:35 | Break | Instructor checks progress and pending jobs |
| 01:35–02:05 | 4. Training and reviewed queries | One reviewed question/SQL decision with evidence |
| 02:05–02:35 | 5. Evaluation sets | Three test-case designs and a failure investigation |
| 02:35–02:50 | 6. Storage, derived data, and retrieval | A grain explanation and checked document/note citation |
| 02:50–03:00 | 7. Teach-back and recap | A reproducible answer and explanation of how you would improve it |

**At each time block, follow the matching module in [WORKSHOP_LABS.md](WORKSHOP_LABS.md).** The instructor will tell you when to move on. Keep optional extensions for after class if an exercise or background job takes longer than expected.

## Concepts you must be able to distinguish

| Concept | Its purpose | Question it answers |
| --- | --- | --- |
| Domain | Select data and context for a subject | What information belongs in scope? |
| Metadata and knowledge | Describe structure and business meaning | What does this data mean, and how should it be used? |
| Synonym | Connect alternative names for a concept | Does “NPS” mean “Net Promoter Score”? |
| Metric | Specify a business calculation | How do we calculate NPS or margin? |
| Entity | Identify and name a business object | Which route, aircraft, or product are we discussing? |
| Skill | Specify a reusable analytical procedure | What steps should a route review follow? |
| Training examples | Generate and inspect candidate matches for example questions | Is this a suitable answer or SQL example to review? |
| Reviewed query | Retain an approved question/SQL example | Which query have we checked and accepted? |
| Evaluation set | Test expected results and behaviors | Does the system handle these cases correctly after changes? |

**Training is not the same as evaluation.** Training examples support setup and review; they do not retrain the underlying language model. Keep separate holdouts to test beyond the examples used during preparation. An accepted query or passing evaluation label still needs a defensible review process.

See [GLOSSARY.md](GLOSSARY.md) for the complete working glossary, including grain, cardinality, snapshots, ground truth, assertions, RAG, and citations.

## Your end-of-class checklist

You should be able to:

- State a source's grain and choose an appropriate event date.
- Write useful knowledge and a synonym without confusing either with a metric.
- Explain a metric's numerator, denominator, units, and zero handling.
- Distinguish an entity from an analytical skill.
- Inspect generated SQL and justify accepting or rejecting it.
- Design an evaluation case and investigate a failure without changing the expectation just to get a pass.
- Check a citation and distinguish synthetic teaching material from actual business evidence.
- Hand another student a prompt, source/date basis, checked result, and limitation they can reproduce.

## If something is missing or fails

| Situation | Next action |
| --- | --- |
| GitHub shows 404 | Use an account granted access, or the copy supplied by the instructor. |
| The domain or an editing control is missing | Ask the instructor to check your assigned domain and role; continue drafting in your exercise log. |
| A prompt returns unexpected figures | Check domain, period, source, grain, and filters. Record the discrepancy; do not force the reference numbers. |
| Training/evaluation is still running | Save the job/reference, continue designing your checks, and inspect an existing completed example with the instructor. |
| A metric inspection asks to discard changes | If you were only inspecting, choose Cancel, then Discard changes. Do not save unintentionally. |
| A prepared asset is absent | Tell the instructor which module and asset; use the linked repository example while the issue is resolved. |

## Repository map

| File or folder | Use |
| --- | --- |
| [WORKSHOP_LABS.md](WORKSHOP_LABS.md) | Student workbook for the three-hour class |
| [INSTRUCTOR_CHEAT_SHEET.md](INSTRUCTOR_CHEAT_SHEET.md) | Quick instructor clock, cues, answers and recovery |
| [INSTRUCTOR_GUIDE.md](INSTRUCTOR_GUIDE.md) | Detailed instructor teaching cards and preparation |
| [GLOSSARY.md](GLOSSARY.md) | Definitions used in class; expanded from our walkthrough draft |
| [DEMO_WALKTHROUGH.md](DEMO_WALKTHROUGH.md) | Optional short demo rehearsal after the concept workshop |
| [PROMPTS.md](PROMPTS.md) and [PROSPECT_TALK_TRACK.md](PROSPECT_TALK_TRACK.md) | Extra questions and customer-facing storytelling |
| `context/` and `skills/` | Metadata, knowledge, metrics, synonyms, entities, relationships, reviewed SQL, and skill examples |
| `training/` and `evaluations/` | Example inputs and test cases; choose the small subset assigned in class |
| `storage/` | Invented service notes, a facilitator brief, and derived-data SQL |
| [DOMAIN_DEPLOYMENT_GUIDE.md](DOMAIN_DEPLOYMENT_GUIDE.md) | Detailed builder reference for preparing or adapting an environment |
| `evidence/` and [CAPABILITY_COVERAGE.md](CAPABILITY_COVERAGE.md) | Historical source checks, validation results, scope, and limitations |
| `build_*.py` and `validate_assets.py` | Maintainer tools; not required for students |

Use **September 2026** for the fixed airline exercises. Dates, counts, and evaluation pass rates recorded from the original proddemo environment are reference evidence, not a guarantee about every workshop copy. Use the assigned Teradata instance; a second proddemo login is not required.

Edits are maintained in [ali-wisdom's working repository](https://github.com/ali-wisdom/wisdomai-teradata-airline-workshop) and synchronized to [the shared WisdomAI repository](https://github.com/datawisdomai/wisdomai-teradata-airline-workshop). The instructor will identify the class version.
