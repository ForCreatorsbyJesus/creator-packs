# Review and improve

## Inputs

- Creator's question and objective
- Comparable stream or video metrics with dates, counts, rates, and definitions
- Changes made, cadence, capacity, and known external factors

## Procedure

1. Separate `observation`, `hypothesis`, and `result`. Treat a single mixed-variable comparison as observation, not causation.
2. Align baselines by platform, format, game or topic, day and time, duration, audience size, and metric definition where possible. Compare both counts and rates when denominator changes can mislead.
3. List confounders, including simultaneous title, timing, topic, distribution, seasonality, recommendations, outages, and missing data.
4. Choose one primary metric tied to the objective and one guardrail metric. Define a practical decision rule without claiming statistical certainty from a small sample.
5. Return `keep`, `change`, and `stop` decisions. Recommend one low-workload experiment that changes one target variable while holding known controllable variables steady when feasible and fits the creator's actual cadence. Describe a one-stream comparison as directional or quasi-experimental, never as isolating or proving that variable while uncontrolled platform, distribution, recommendation, day, duration, or other confounders remain.
6. State what the current evidence cannot establish. Label proposed explanations as `hypothesis` and completed tests as `creator experiment`.
7. When creator baseline data is missing, label any numeric guardrail or decision threshold a `provisional heuristic` and require calibration against the creator's later baseline; otherwise use a qualitative directional rule.

## Output contract

Return a concise review card: observations, hypotheses, confounders, aligned baseline, keep/change/stop, one directional or quasi-experimental test, primary success signal, guardrail, review point, and one next action inside the complete seven-field context capsule.

## Graceful degradation

If metric definitions, absolute values, or comparable baselines are missing, do not diagnose a cause. Explain the ambiguity, offer the safest reversible change, and ask for only the missing metric that would materially alter it.

## Example

Observation: chat participation fell on a live illustration lesson after both a denser overlay and stronger microphone processing were introduced, while average watch time stayed similar. Hypothesis: the overlay reduced visual clarity, but the two simultaneous changes prevent attribution. Restore only the simpler overlay next session while holding known controllable inputs steady, use chatters per 100 live viewers as primary and average watch time as guardrail, then treat the one-session result as directional because uncontrolled distribution and audience factors remain.
