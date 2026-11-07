# Evaluation protocol

Keep holdout cases separate from training/reviewed examples. `holdout-import.csv` uses the application's exported format: query,sql,assertions,no_ground_truth. Each semantic case has an explicit expectation and no invented numeric ground truth.

Run the semantic set in Thinking mode. Inspect individual answers and judge explanations; a judge pass is not proof of numeric correctness. For numerical regression, add SQL ground truth only after executing it and checking grain, filters, currency, and period semantics.

Track: scored pass rate, incorrect-answer rate, unsupported-question handling, SQL execution success, source selection, denominator correctness, fanout avoidance, sample-size disclosure, and latency. Record mode and run date with every comparison.

Acceptance: no unsupported claims or fact multiplication; all priority numeric cases agree with executed reference SQL; all failed cases investigated. Do not train on holdouts merely to improve the displayed score.
