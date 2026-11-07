# From a monthly scorecard to the next business question

## Presenter brief

Audience: business leader with a data or technology partner. Length: 15–20 minutes. Use the Airline Command Cockpit in TD-AirlineDemo, then a domain-scoped conversation. This is a demonstration dataset, not a customer success story. September 2026 is the fixed reporting period. Rehearse each prompt before presenting; follow-up rankings depend on the live answer and are not preclaimed here.

The central question: **The airline is filling seats. Where should leadership focus to protect profit and passenger trust?**

Success for the meeting is agreeing on one customer question, its trusted source, its business definition, and an owner who can validate the answer.

## Opening: the question behind the dashboard — 90 seconds

“Imagine it is the September business review. The commercial leader sees a healthy load factor. Operations has a service reliability report. Customer experience has survey scores. Finance has route profitability.

Each report can be correct, yet the leadership team still needs to decide where to focus. Which routes deserve attention? Is the issue revenue, cost, reliability, or the passenger experience? And when someone asks a follow-up, can we answer it while the discussion is still happening?

Today we will start with a familiar scorecard and follow the questions it creates. We will also show you the definitions and source evidence behind the answers.”

Open the cockpit's About page briefly. Establish that it covers several airline subjects and that the demonstration uses a fixed month. Move to Executive Overview. Do not spend the opening touring menus.

## Act 1: establish an agreed starting point — 3 minutes

“Let us agree on the month before interpreting the business. For September 2026, the route-month source records 64,612,818.33 in revenue and 6,860,708.98 in operating income, in the source's monetary units. Passenger-count load factor is about 85.0%.

Those totals establish scale. They do not tell us which routes need attention. A full aircraft and a profitable route are different questions.”

Ask:

> For September 2026, show total route revenue, operating income, operating margin, passenger-count load factor, and distance-weighted load factor. State the source, period basis, formulas, and monetary-unit limitations. Include exact financial totals alongside any abbreviated labels.

Show the result and available SQL/source explanation. If the answer differs from the recorded checkpoint, reconcile the source and filters before continuing. A currency symbol on a chart does not establish the dataset's currency.

Transition:

“We now have a shared starting point. Let us find where an investigation would be most useful.”

## Act 2: turn a total into a focused investigation — 4 minutes

Ask:

> For September 2026, rank the ten routes with the lowest operating income. Include revenue, operating cost, operating margin, passenger-count load factor, RASM, and CASM. Use the route-month view and explain the metric units.

“Rather than assuming that more passengers fix every problem, we can compare how much revenue a route generates with its operating cost. The useful result is a shortlist for investigation.”

Choose one route actually returned. Say its name and the observed figures; do not use an invented route or prewritten ranking.

Ask, replacing the bracketed route with that live result:

> For [route], compare September 2026 with August 2026 and September 2025. Show revenue, operating income, passenger-count load factor, and RASM versus CASM. Describe the observed changes and separate them from explanations that would need additional evidence.

“A comparison helps us frame the next question. It does not, by itself, prove why the change happened.”

## Act 3: bring operational and customer evidence into the conversation — 4 minutes

Move to Operations, then CX, keeping the reporting period fixed.

“The operations source records 1,938 scheduled flight legs for September, including 27 cancellations and four diversions. Eligible-arrival on-time performance is about 81.6%. The survey source contains 7,029 responses; NPS is about 36.4.

These measures describe different populations. We should preserve those differences as we investigate the selected route.”

Ask:

> For [route] in September 2026, summarize scheduled flight legs, cancellations, diversions, and eligible-arrival on-time performance from the flight view. Separately summarize survey response count and NPS from the survey view using survey date. Explain why the populations and date bases differ. Avoid a raw fact-to-fact join that duplicates records.

“Notice the discipline here: we can place the evidence side by side without pretending that every survey is the same thing as a flight, or that an association proves a cause.”

If no route-level survey evidence is available, state that limitation and retain the separate network summary. Do not fill the gap with speculation.

## Act 4: show how trust is built — 3 minutes

“The business conversation is useful only if the answer means what your organization expects it to mean. Here is the context behind this demo.”

Open domain Context. Show three items, briefly:

1. A metric: NPS uses promoters minus detractors over valid responses; it is not an average score. Load factor is a ratio of sums, with two explicitly different definitions.
2. A knowledge item or skill: event dates, monthly snapshots, and joining subjects at compatible grains.
3. A reviewed query and the evaluation evidence: examples establish expected behavior; separate holdouts check questions beyond those examples.

“The reusable work is the business meaning, the tested questions, and the evidence. That is what lets another team member reproduce the demonstration and assess an answer.”

Optional boundary prompt:

> Convert September 2026 route revenue to euros.

Expected behavior: ask for the source currency and exchange-rate basis. Use this only after rehearsal confirms that behavior.

“A useful assistant should also surface what it needs to know before answering.”

## Optional extension: structured results and cited notes — 2 minutes

Use only if relevant to the prospect. This is a separate teaching extension, not evidence about the airline's actual customers.

> In the WORKSHOP_SYNTHETIC service notes only, summarize the baggage feedback. Cite the note IDs and clearly label the material as invented workshop data.

“The numbers can tell us where to investigate. Written evidence can add context. Here we use explicitly invented notes to demonstrate retrieval and citations without presenting fictional feedback as actual passenger evidence.”

Do not attribute these notes to the selected route, real flights, or real passengers.

## Close: connect the demonstration to their business — 2 minutes

“We started with a monthly scorecard. We identified a focused investigation, compared relevant evidence, and checked the definitions behind the answer.

For your business, the starting point might be branch profitability, service reliability, inventory, or customer retention. The next step is to choose one important question, identify the trusted data and business definitions, and agree on how your team will judge the answer.

Which recurring decision currently sends your team away to assemble another analysis? Let us use that decision to define a focused technical validation.”

Capture: decision and audience; source and owner; grain and period; metric definition; approved access; a small set of expected answers and difficult questions; validation owner. Agree on these before promising a timeline or outcome.

## Five-minute version

- Open with the September leadership-review scenario.
- Show the executive scorecard and ask the Act 1 prompt.
- Ask the lowest-income route prompt and inspect one actual result.
- Show one metric definition and its reviewed SQL evidence.
- Close by selecting one prospect decision and agreeing on validation criteria.

## Presenter boundaries

- Demo figures are source checkpoints, not customer benefits or promised ROI.
- Route financial totals, flight operations, survey-date responses, and monthly loyalty snapshots have distinct grains and time bases.
- Preserve source monetary units until currency and conversion policy are documented.
- Describe associations and investigation priorities; do not claim causal attribution, automatic optimization, forecasting, or actions this demonstration has not shown.
- Do not claim Tera Analyze or AI Studio parity from this standalone demo. Use the actual OEM environment for that part of the workshop and verify the available capabilities there.
- The semantic holdout achieved 16/16 in the recorded Thinking-mode run. This is a bounded regression result, not a general accuracy guarantee. The numerical/storage suite also passed 5/5 in its checked run. Later extensions have separate validation limits documented in the evidence log.

## Rehearsal checklist

Confirm domain access and source availability; open the cockpit and domain conversation; set September 2026; run the exact sequence; record the route selected in Act 2; reconcile financial and survey checkpoints; inspect citations and SQL; check the latest evaluations; retain screenshots for a connection outage. If a result fails, explain the observed limitation and switch to the verified evidence instead of improvising an answer.
