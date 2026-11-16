# WisdomAI workshop: attendee demo guide

**Start here. Follow the numbered steps on this page, in order.** This is a hands-on demo using an already prepared airline domain. You do not need to build a domain, configure a connection, import CSVs, install Git or Python, or run the repository's scripts.

The story you will demonstrate: **The airline is filling seats. Where should leadership focus to protect profit and passenger trust?**

By the end, you will have asked business questions, followed an investigation, checked the evidence behind an answer, used cited text, and explained how context, skills, training and evaluations support the demo.

## Before you begin — two browser tabs

1. Keep this GitHub page open in **Tab 1**. You can copy every prompt directly from this README; downloading a ZIP is optional.
2. In **Tab 2**, sign in to [the Teradata WisdomAI instance](https://teradata.wisdom.ai).
3. Open **Domains → CSA Workshop - Facilitator**. Use a different domain only if your facilitator assigns it.
4. Confirm that you can open **Context** and see the prepared airline material. If the domain or Context is unavailable, ask the facilitator to check your access. A successful application login alone does not grant domain access.
5. For the exercises below, use **New chat**, keep **Ask** selected, select **CSA Workshop - Facilitator** in the chat's domain selector, and choose **Thinking** if that mode is available. Recheck the selected domain each time you start a new chat.

**Use September 2026 throughout.** “Latest month” and “this month” can give different results as time passes. Wait for each answer to finish before asking its follow-up.

This is a shared, prepared domain. Inspect existing context and runs; leave configuration changes and training/evaluation execution to the facilitator unless you have been assigned your own editable copy.

## Step 1 — establish the financial baseline

**Do:** In a new chat scoped to the workshop domain, copy and send:

```text
For September 2026, show total route revenue, operating income,
operating margin, passenger-count load factor, and distance-weighted
load factor. Use the route-month financial view. State the reporting
date basis and formulas. Include exact financial totals to two decimal
places and explain any limitations on the monetary units.
```

**Check:** The answer names a source and reporting period, distinguishes the two load factors, and explains the calculations. Use the following as reference checkpoints for the original demonstration data, not as numbers to force into an answer:

| Measure | September 2026 reference |
| --- | ---: |
| Route revenue | 64,612,818.33 source monetary units |
| Operating income | 6,860,708.98 source monetary units |
| Operating margin | About 10.62% |
| Passenger-count load factor | About 85.0% |
| Distance-weighted load factor | About 85.3% |

If your answer differs, check the selected domain, month, source and filters with the facilitator before continuing. A currency symbol alone does not establish the source currency.

**Explain:** “A full aircraft and a profitable route are different questions. These measures establish the starting point for our investigation.”

## Step 2 — identify where to investigate

**Do:** Stay in the same conversation and send:

```text
For September 2026, show the five routes with the lowest operating
income. Include route code, revenue, operating cost, operating income,
operating margin, passenger-count load factor, RASM, and CASM.
Use the route-month view and explain the units.
```

**Check:** There are up to five routes, ordered by lowest operating income. RASM is revenue per available seat mile; CASM is operating cost per available seat mile. Neither is automatically expressed in cents.

Copy one **route code actually returned**. In the next prompt, replace `[ROUTE]` with that code; do not send the square-bracket placeholder unchanged:

```text
For [ROUTE], compare September 2026 with August 2026 and September 2025.
Show revenue, operating income, operating margin, and passenger-count
load factor. Describe the observed changes and identify questions
that require more evidence. Do not infer causes from the comparison alone.
```

**Explain:** “We have moved from a network total to a specific investigation. The comparison shows what changed; it does not prove why.”

## Step 3 — examine customer experience separately

**Do:** Start a **new chat**, select the workshop domain again, and send:

```text
For September 2026 using survey date, show the valid NPS response count,
promoter count, passive count, detractor count, NPS, and average
recommendation score. Use the passenger survey view. Explain the
eligibility rules and why NPS is different from an average score.
```

**Check:** Scores 9–10 are promoters, 7–8 are passives, and 0–6 are detractors. Valid scores 0–10 form the NPS denominator. In the original demonstration data, reference counts were 7,029 survey records, 3,705 promoters and 1,146 detractors, with NPS about 36.4. Confirm the answer's valid-response count rather than assuming every record is eligible.

NPS is a score between −100 and +100. It is not the mean recommendation score. Survey-date responses and route-month financials describe different populations; do not join their detail rows to add up revenue.

**Explain:** “NPS is the percentage of promoters minus the percentage of detractors. Passives are included in the denominator.”

## Step 4 — inspect how the domain knows what you mean

**Do:** Open **Domains → CSA Workshop - Facilitator → Context**. Inspect these existing items:

1. **Knowledge:** find **Travel versus booking period**. Read why flight date and booking date answer different questions.
2. **Synonyms:** find **Net Promoter Score** and confirm **NPS** is listed.
3. **Metrics:** open **Survey_NPS** and **Operating_Margin_%**, one at a time. Inspect the formulas. Exit using **Cancel**; if prompted, choose **Discard changes**. Do not select Save during this inspection.

**Check:** NPS uses valid survey responses. Operating margin is `100 × SUM(operating_income) / SUM(total_revenue)`, with a zero-denominator guard. Margin can be negative for losses. Combine totals before dividing; do not simply average route margins.

**Explain:** “Synonyms identify the concept. Metrics define the calculation. Knowledge explains how to interpret and use the data.”

**Glossary:** A **grain** is what one row represents. A **denominator** is the total or eligible population underneath a ratio. A **ratio of sums** adds the relevant values first, then divides their totals.

## Step 5 — use an analytical skill

**Do:** In **Context → Skills**, open **Airline route profitability review** and read its procedure. Close without saving, then return to a new, domain-scoped chat and send:

```text
Use the Airline route profitability review skill to review September
2026 route profitability against budget. Show the five largest negative
operating-income gaps in source monetary units. Include actual income,
budget income, the gap, and relevant revenue and margin context.
State the source, period basis, and limitations.
```

**Check:** The answer compares actuals with budget and distinguishes the size of a gap from a percentage rate. Where the interface shows skill usage, inspect it. An answer that merely follows similar steps is not proof that a particular skill was retrieved.

**Explain:** “A skill is a reusable analytical procedure: the steps we want followed for this kind of investigation.”

The readable version is in [the route profitability skill](skills/airline-route-profitability-review.md).

## Step 6 — retrieve and check cited text

**Do:** Start a new, domain-scoped chat and send:

```text
Using only the WORKSHOP_SYNTHETIC service notes, summarize
baggage-related feedback. Cite the supporting note IDs and clearly
state that the notes are invented workshop material, not actual
passenger evidence.
```

**Check:** Open the citations. The baggage notes should be **SYN-002** and **SYN-007**. Confirm the cited text supports the summary. Do not attribute these invented notes to the route selected in Step 2.

Then send:

```text
Using only WORKSHOP_SYNTHETIC_facilitator_brief.txt (WS-BRIEF-001),
what must each group hand to the next group, and what defines completion
of the practice exercise? Cite the document and state that it is
invented workshop material, not real airline policy.
```

**Check:** The handoff includes the business question, exact prompt, source and period basis, one checked number, metric definition, limitations, and suggested follow-up. Completion means another group can reproduce the answer and explain the evidence and limitations. Open the document citation.

**Explain:** “Retrieval brings relevant source text into the answer. A citation lets us inspect whether that text actually supports the claim.”

**Optional storage inspection:** In the domain's **Data Sources → Tera Storage**, inspect the existing note table, derived summary and file. The SQL database name may still be `wisdom_storage`. One source row represents one note; one summary row represents one scenario. The summary counts should be baggage 2, service 2, and accessibility, cabin, weather and wifi 1 each. Do not upload duplicate copies.

## Step 7 — see how answers are reviewed and tested

**Do:** Return to the workshop domain and inspect these three areas:

1. **Context → Reviewed Queries:** open an existing September 2026 route or survey example. Compare the question with its SQL. Check the source table, date filter, aggregation and denominator. Close without saving.
2. **Training:** inspect an existing question, its reference guidance and its accepted SQL match. Notice that a candidate and the accepted SQL can differ. Do not start training or accept new matches in the shared facilitator domain.
3. **Evaluation → Evaluation Sets:** open a set and read one test's question and expectation. In the inspected facilitator domain, **Evaluation Set 1** had 16 cases and **Evaluation Set 2** had 5; names may differ in an attendee copy. Use the contents to identify the suite. Then open **Run History → View Group** for that set and inspect a completed case, its answer, score and explanation.

**Check:** A reviewed query is a vetted question/SQL example. Training examples support setup and review; they do not retrain the underlying language model. Evaluation cases test expected results or behavior. A passing judge score should still be checked against the answer and source evidence.

If no runs are present in your assigned copy, review the repository's [evaluation protocol](evaluations/README.md) and [recorded reference evidence](evidence/validation-log.md) with the facilitator. You do not need to create or run a suite to finish this demo flow. Original proddemo pass rates are historical evidence, not a claim about a new environment.

**Explain:** “Training examples help establish expected behavior. Separate holdout evaluations check behavior beyond those examples and help catch regressions.”

## Step 8 — demonstrate a sensible boundary

**Do:** In a new, domain-scoped chat, send:

```text
Convert September 2026 route revenue to euros.
```

**Check:** Without a documented source currency and exchange-rate basis, the answer should ask for those inputs before presenting converted figures. If it assumes either, flag the response for the facilitator. Do not accept relabeled source amounts as a currency conversion.

**Explain:** “A useful answer includes knowing what additional information is needed.”

## Step 9 — deliver your five-minute demo

**Do:** Present this sequence to another attendee:

1. Open with the business question at the top of this page.
2. Show your financial baseline from Step 1.
3. Show one actual route result from Step 2 and explain the next investigation question.
4. Show one metric definition or checked citation as evidence of how the answer was produced.
5. Close with one question you would validate with a customer and the data needed to answer it.

Use the [prospect talk track](PROSPECT_TALK_TRACK.md) for presenter wording. Its original cockpit references describe the proddemo reference environment; for this attendee exercise, use the Teradata domain and the chat results you just produced.

**Done means:** another attendee can repeat your prompt, find the same source and period, check one number or citation, and explain one limitation. Record your exact prompt, source/date basis, checked result and limitation. Flag a mismatch rather than inventing the expected answer.

## Optional — explore the prepared app

In the Teradata instance, open **Apps → Passenger Experience Scorecard**, the app observed for this facilitator domain. Explore its available views and identify one question it makes you want to ask in chat. If the facilitator provides a different app name, use that app. An app is not required for Steps 1–9.

The original **Airline Command Cockpit** lives in the proddemo reference environment. Do not switch to proddemo or assume you need a second login to complete the attendee flow.

## If you get stuck

| Problem | What to do |
| --- | --- |
| GitHub 404 or sign-in screen | Sign in with an account granted repository access, or use the workshop ZIP supplied by the facilitator. |
| Domain is missing or Context is unavailable | Ask the facilitator to check your domain access; do not create a replacement domain. |
| Chat answers an unrelated subject | Start a new chat and explicitly select CSA Workshop - Facilitator. |
| Numbers differ from the checkpoints | Check September 2026, source, date basis and filters with the facilitator. |
| Notes/file cannot be found | Check the selected domain and ask the facilitator to confirm the prepared storage content and file processing. |
| A section, run or app is missing | Tell the facilitator which step and item is missing; do not rebuild it mid-exercise. |
| Inspection opens an editor | Exit with Cancel, then Discard changes if prompted. |

## Where the other repository files fit

| Material | When to use it |
| --- | --- |
| [PROMPTS.md](PROMPTS.md) | Additional questions after this numbered flow. |
| [WORKSHOP_LABS.md](WORKSHOP_LABS.md) | Deeper technical exercises led by the facilitator. |
| [INSTRUCTOR_GUIDE.md](INSTRUCTOR_GUIDE.md) | Instructor agenda, team roles and preparation. |
| [DOMAIN_DEPLOYMENT_GUIDE.md](DOMAIN_DEPLOYMENT_GUIDE.md) | Instructor/builder reference for creating a domain; not an attendee prerequisite. |
| `context/`, `training/`, `evaluations/`, `skills/`, `storage/` | Reusable reference/import assets; not files every attendee must upload. |
| [CAPABILITY_COVERAGE.md](CAPABILITY_COVERAGE.md) and `evidence/` | Recorded scope, checks and limitations. |
| `build_*.py`, `validate_assets.py` | Maintainer tools; not needed to follow the demo. |

Make revisions in [ali-wisdom's working repository](https://github.com/ali-wisdom/wisdomai-teradata-airline-workshop), then synchronize reviewed content to [the shared WisdomAI repository](https://github.com/datawisdomai/wisdomai-teradata-airline-workshop). Students should use the version supplied by the facilitator. Repository visibility and access can change; a ZIP download does not grant application or domain access.
