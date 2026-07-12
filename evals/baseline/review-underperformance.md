# Baseline: review underperformance

## Prompt

Scenario C: My last YouTube Live had more views but fewer returning viewers. I changed the title, streamed an hour later, and played a different game. Tell me why it happened and what to change next.

## Raw output

More views but fewer returning viewers usually means the stream attracted a broader, less familiar audience—or that fewer regulars showed up. But because three things changed at once, the result can’t be attributed confidently to any one cause.

Likely explanations:

- **Different game:** The strongest candidate. It may have generated more search/recommendation traffic, increasing total views, while appealing less to your established audience.
- **One-hour-later start:** Some regular viewers may have been unavailable, reducing returning viewers.
- **Changed title:** A stronger or broader title could have increased clicks from new viewers. If it overpromised or poorly matched the stream, those viewers may not return.
- **Metric effect:** More total views can lower the *percentage* of returning viewers even if their absolute number is similar. Compare both counts and rates.

For the next streams, change only one variable at a time:

1. Return to your usual game and start time, but reuse the new title style.
2. Then test the later time while holding the game and title style steady.
3. Test the different game again at your normal time with a title format your regulars recognize.

Track impressions, click-through rate, average watch time, unique viewers, returning-viewer count and share, subscriber gains, and traffic sources. Use at least two or three comparable streams per variation—one stream can be distorted by recommendations, competition, or day-of-week effects.

My initial hypothesis: the different game and/or broader title brought extra discovery traffic, while the later time or game mismatch reduced attendance from regulars. For the safest next move, restore the normal time, keep the improved title approach, and test the new game separately.

## Rubric scores

- **creator_fit — 3/5:** It responds to a live creator's discovery-versus-loyalty tradeoff but lacks channel size, cadence, audience, or historical-baseline context.
- **platform_fit — 4/5:** It uses relevant YouTube Live concepts including impressions, click-through rate, traffic sources, unique viewers, and returning-viewer counts and shares.
- **actionability — 4/5:** It provides a controlled test sequence and metrics, though the first test's exact title treatment and success threshold remain unspecified.
- **prioritization — 4/5:** It names a safest next move after presenting multiple hypotheses, but also proposes a longer three-variation sequence.
- **evidence_transparency — 5/5:** It explicitly identifies the three confounders, separates hypotheses from conclusions, and calls for both counts and rates.
- **workload_realism — 3/5:** Repeating each of three variations for two or three streams could require six to nine streams without acknowledging the creator's cadence or capacity.
- **voice_preservation — 3/5:** It avoids rewriting the creator's voice, but recommends a recognizable title format without first learning what that format is.
- **artifact_usefulness — 3/5:** The diagnostic checklist is useful, but it is not condensed into a reusable experiment card with fixed inputs, decision rule, and context capsule.
- **uncertainty_calibration — 5/5:** It consistently uses conditional language and warns that one observation cannot isolate a cause.

## Observed failure modes

- It calls the new title approach “improved” even though the prompt provides no evidence that the title itself improved.
- The proposed multi-stream test program is not calibrated to the creator's publishing cadence or available workload.
- It lists many success metrics but gives no primary metric or threshold for deciding whether the next test worked.
- It does not provide a compact experiment record or context capsule for the next review.
