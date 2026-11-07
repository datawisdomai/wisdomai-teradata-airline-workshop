# WisdomAI technical workshop for the Teradata field

A reusable, one-day technical workshop for 25 sales engineers, built around the TD-AirlineDemo domain and Airline Command Cockpit. The story moves from an executive scorecard to route economics, operational reliability, customer experience, and verifiable answers.

## Start here

1. Read [Instructor guide](INSTRUCTOR_GUIDE.md) for the agenda, preparation and team setup.
2. Follow [Domain deployment guide](DOMAIN_DEPLOYMENT_GUIDE.md) to adapt the assets to your own connection.
3. Run the eight [labs](WORKSHOP_LABS.md), using the [prompt bank](PROMPTS.md).
4. Rehearse the [prospect talk track](PROSPECT_TALK_TRACK.md).
5. Check [validation evidence](evidence/validation-summary.json) and [capability coverage](CAPABILITY_COVERAGE.md).

## Reference domain status

Verified from the November 6, 2026 evening build (export timestamp November 7 UTC):

| Asset | Verified count |
| --- | ---: |
| Teradata tables and views / source columns | 45 / 1,168 |
| Relationships | 49 |
| Knowledge entries / synonym sets | 23 / 23 |
| Metrics / business entities / skills | 43 / 11 / 6 |
| Reviewed SQL queries | 31 |
| Training questions with accepted matches | 30 |
| Synthetic storage table / derived summary / derived column | 1 / 1 / 1 |
| Invented practice document uploaded | 1 (processing not yet verified) |
| Semantic holdout, Thinking mode | 16/16 |
| Numerical and storage checks, Thinking mode | 5/5 |

These are bounded checks on this demonstration, not a general accuracy guarantee. See the evidence log for limitations and changes made after the evaluation runs.

## Repository layout

- `context/`: source metadata, business knowledge, metrics, terminology, entities, relationships, custom instructions and reviewed SQL.
- `training/`: candidate questions and SQL guidance, kept separate from holdouts.
- `evaluations/`: semantic and numerical/storage regression inputs.
- `skills/`: six analytical playbooks and the native CSV import format.
- `storage/`: eight explicitly invented notes and a scenario summary query.
- `evidence/`: source checks, run screenshots and configuration counts. The complete native instance backup stays local and is excluded from Git.

Use `context/metrics-complete.csv` for all 43 metrics. The original `metrics.csv` and `additional-metrics.csv` describe the staged build; do not import both the complete file and the staged files into the same clean domain.

## Reuse and distribution

Replace the `Ali-TD` connection label and `wisdomai` database bindings before importing into another environment. This kit contains configuration and aggregate demonstration checkpoints, not the airline warehouse itself. It cannot recreate the underlying data or grant attendees access.

Run `python3 validate_assets.py` to check asset structure, references and expected coverage. Live SQL execution, source reconciliation and evaluations are still required in each new environment.

The local Git repository is the prepared source. Publishing to the user's personal and WisdomAI GitHub repositories requires the exact destination repositories. Keep one upstream and mirror it to the second destination to prevent drift. No license or public-release policy is assumed.

## Seed generators

The four `build_*.py` scripts generate the initial authoring assets using only Python's standard library. They were run successfully in an isolated copy. Run them in a fresh copy: they can overwrite deployment status and staged assets. Final verified imports such as `metrics-complete.csv` and reviewed SQL are retained separately. The relationship checklist requires UI configuration; this repository does not claim an undocumented domain API.
