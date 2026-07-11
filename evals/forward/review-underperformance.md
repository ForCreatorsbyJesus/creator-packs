# Forward: review underperformance

## Prompt

Use @creator-copilot at /workspace/scratch/3c3299a79a51/creator-packs/plugins/everyday-streamer-creator-pack/skills/creator-copilot to solve this request:

Scenario C: My last YouTube Live had more views but fewer returning viewers. I changed the title, streamed an hour later, and played a different game. Tell me why it happened and what to change next.

## Raw output

Primary job: `review`

## Review card

Most plausible explanation: the stream reached a broader, less familiar audience while fitting your regular audience less well.

- **Observation:** Total views increased, while returning viewers decreased.
- **Hypotheses:**
  - `hypothesis` The different game attracted more first-time or game-specific viewers.
  - `hypothesis` The one-hour-later start made some regular viewers unavailable.
  - `hypothesis` The new title improved discovery or clicks, bringing in more new viewers without increasing core-audience turnout.
- **Confounders:** Title, start time, and game all changed together. YouTube recommendations, stream duration, day/date, traffic sources, and post-live replay views may also have contributed.
- **What the evidence cannot establish:** A single mixed-variable stream cannot tell us which change caused either result. “More views” may also include repeat or replay views, so it is not directly comparable with returning-viewer count.

**Aligned baseline:** Compare this stream with 3–5 recent YouTube Lives at your usual time, using the same game if possible. Check unique viewers, returning-viewer count and share, live peak/concurrent viewers, replay views, and traffic sources.

**Keep:** The clearer or more curiosity-driven title approach, provided it accurately represents the stream.

**Change:** Restore your usual game and start time for the next comparison.

**Stop:** Changing title, timing, and game in the same test.

**Directional creator experiment:** Next stream, use your usual game and usual start time, but apply the new title structure to that game. This creates a cleaner, still imperfect comparison with your earlier usual streams.

- **Primary success signal:** Returning-viewer count rebounds toward your 3–5-stream baseline.
- **Guardrail:** Total views do not materially fall below that baseline.
- **Decision rule:** If returning viewers rebound while views remain stronger, keep testing the title style. If views or returning viewers weaken, do not conclude from one stream; repeat once before changing another variable.
- **Review point:** 48–72 hours after the stream, so live and early replay performance can be separated.
- Any numeric threshold would be a `provisional heuristic` until calibrated against your channel’s baseline.

## Context capsule

**Current objective:** Explain the rise in views alongside the fall in returning viewers and choose what to change next.

**Confirmed constraints:** One stream changed three variables simultaneously: title, start time, and game.

**Decisions made:** Treat the outcome as broader discovery plus weaker regular-audience fit or availability, not as proof that any single change caused it. Keep the title concept; restore the familiar content and schedule for the next test.

**Active experiment:** Usual game + usual start time + new title structure; compare with 3–5 similar prior streams.

**Assets created:** Review card, hypotheses, keep/change/stop decisions, and a directional test.

**Open questions:** Unique-viewer count, returning-viewer rate, live-versus-replay views, traffic sources, and the comparable 3–5-stream baseline are unknown.

**Recommended next action:** Run the next stream with your usual game and usual start time while keeping only the new title structure as the changed variable.

## Rubric scores

- **creator_fit — 4/5:** It directly addresses discovery versus returning viewers, while the creator’s actual baseline values, cadence, and capacity remain unknown.
- **platform_fit — 5/5:** It uses relevant YouTube Live measures and separates live, replay, recommendation, and traffic-source effects.
- **actionability — 5/5:** It supplies aligned-baseline guidance, keep/change/stop decisions, one directional test, primary signal, guardrail, rule, and review point.
- **prioritization — 5/5:** It chooses the familiar game/time plus the new title structure as the single next comparison and puts that action inside the capsule.
- **evidence_transparency — 5/5:** It separates observation from labeled hypotheses, names all known and additional confounders, and explicitly states what one mixed-variable result cannot establish.
- **workload_realism — 4/5:** It uses one next stream and existing historical comparisons, but may require one repeat and does not know the creator’s cadence.
- **voice_preservation — 4/5:** It avoids drafting replacement copy, but characterizes the unknown new title as clearer or curiosity-driven without evidence that this describes it.
- **artifact_usefulness — 5/5:** The review card includes a bounded decision framework and a complete seven-field context capsule.
- **uncertainty_calibration — 5/5:** It calls the test directional and imperfect, avoids isolation or causal claims, retains uncontrolled factors, and marks unsupported numeric thresholds provisional.

**Average: 4.67/5.**

## Threshold checks

- Correct workflow route: pass (`review`)
- One prioritized default action inside the capsule: pass
- All seven context-capsule fields: pass
- Explicit confounders and no causal/isolation overclaim: pass
- Numeric thresholds without baseline labeled provisional: pass
- Average at least 4.0: pass
- No dimension below 3.5: pass (lowest: 4)
