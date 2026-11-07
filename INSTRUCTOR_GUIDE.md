# Instructor guide

## Audience and operating model
25 sales engineers, five groups of five. Use the existing Airline Command Cockpit as the shared business story. Give each group one subject: network profitability, operational reliability, commercial mix, loyalty/co-brand, or customer experience.

## Prerequisites
Confirm attendee access and a safe editing arrangement before the session. Use attendee/group domains where possible, or assign non-overlapping exercises in the shared domain. Do not distribute connection credentials through GitHub. Confirm source timezone and currency separately from the application display defaults.

## Teaching sequence
1. Explore the schema and state grains.
2. Inspect business context and terminology.
3. Explain governed metric formulas and denominator traps.
4. Train questions; inspect SQL and accept verified matches.
5. Run separate holdouts and investigate a failure.
6. Invoke reusable analytical skills.
7. Upload synthetic text, configure RAG, and inspect citations.
8. Teach back a validated answer and a reusable customer adaptation plan.

## Instructor checkpoints
- Show passenger-count versus distance-weighted load factor.
- Show NPS versus mean recommendation score.
- Show miles balances versus flows.
- Show booking, travel, purchase, survey and service-case event dates.
- Show why cardholder spend cannot be added to airline revenue.
- Show unsupported named-account and FX questions being handled explicitly.
- Show separate facts combined only after aggregation.
- Keep synthetic notes visibly distinct from actual airline data.

## Recovery
Keep the metadata-before export and all import assets. If a participant falls behind, use the configured instructor domain and continue with validation rather than skipping the reasoning. Do not reset shared data or overwrite other groups' work during the session.

## Reuse in another workshop
Replace connection/table bindings and reporting periods. Revalidate key uniqueness, date coverage, eligibility flags, currencies and timezone semantics. Run both evaluation sets and inspect failures. Export final assets and capture the application version/date. Link the two GitHub copies to a single upstream source so fixes do not drift.

## Suggested one-day timing

Technical time below totals 6 hours 15 minutes, plus breaks and lunch. Adjust around the separate sales session.

| Time | Activity | Deliverable |
| --- | --- | --- |
| 09:00–09:20 | Story, access and baseline cockpit | Shared business question |
| 09:20–10:05 | Lab 1: schema, grain, joins and keys | Source/grain map |
| 10:05–10:45 | Lab 2: knowledge, terminology and ambiguity | Context correction |
| 10:45–11:00 | Break | |
| 11:00–11:45 | Lab 3: metrics and denominator traps | Validated formula |
| 11:45–12:30 | Lab 4: training and reviewed SQL | Accepted checked example |
| 12:30–13:15 | Lunch | |
| 13:15–14:00 | Lab 5: evaluations and failure diagnosis | Regression result and explanation |
| 14:00–14:30 | Lab 6: analytical skills | Evidence-backed answer |
| 14:30–14:45 | Break | |
| 14:45–15:25 | Lab 7: storage, derived data and citations | Retrieved and checked evidence |
| 15:25–16:10 | Lab 8: five team teach-backs | Reproducible prospect demo |
| 16:10–16:30 | Customer adaptation, questions and next steps | Individual application plan |

The timetable contains 6 hours 15 minutes of technical activity (including opening and wrap-up); shorten demonstrations to accommodate a sales module. Assign roles within each team: business question owner, domain author, SQL reviewer, evaluation reviewer, and presenter. Rotate them so all attendees practice beyond watching the instructor.

Score each teach-back out of 10: correct grain/date (2), formula and denominator (2), checked source evidence (2), explicit limitations (2), clear prospect story and handoff (2). Treat 8/10 plus no material factual error as readiness for a supervised customer demonstration; this is a workshop rubric, not a product certification.
