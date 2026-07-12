# Insight engine

## Inputs

- Creator's objective, channel context, constraints, and decision horizon
- For `next_action`: current candidate actions or backlog, dependencies, deadlines, creator-hours, and safety or rights constraints
- For `creator_insights`: candidate official sources, creator accounts, public observations, community reports, creator experiments, and publication or access dates when available

## Next-action procedure (`next_action`)

1. Derive candidate actions from the explicit request, current project, and confirmed profile. Do not require external creator-advice sources.
2. Remove actions that violate a hard time, safety, rights, voice, or platform constraint.
3. Score each remaining action on creator-goal alignment, expected value, urgency, dependency unlock, creator-hours required, and risk/reversibility. Use relative ratings such as low/medium/high; label expected value as a hypothesis unless creator evidence supports it.
4. Prefer actions with strong goal alignment and dependency value that fit available hours and remain reversible. Treat high urgency as meaningful only when a real deadline or loss exists.
5. Select one feasible default action. State why it outranks the rest, its time box, completion condition, and the first concrete step. Mention an alternative only when a distinct constraint could invalidate the default.

## Creator-insights procedure (`creator_insights`)

1. Use the source hierarchy: current official platform guidance; direct creator experience with stated context; verifiable public observation; aggregated community report; then hypothesis. Do not turn popularity into authority.
2. Apply a relevance filter: same platform role, creator stage, content format, audience relationship, resources, objective, and risk tolerance. Reject advice that conflicts with explicit constraints.
3. Preserve the underlying principle without copying a named creator's wording, persona, visual identity, signature format, or claims.
4. Sort findings into `Do Now`, `Test Next`, `Watch`, or `Ignore`. Recommend one item in `Do Now`; keep the rest brief.
5. Record source date and retrieval date where known. Mark stale or undated material and prefer current official guidance for platform mechanics.
6. Calibrate confidence to source quality, relevance, consistency, and recency. State evidence limits; never promise an outcome.

## Output contract

- For `next_action`, return a compact action scorecard, one default action, selection rationale, creator-hours and completion condition, known risk, and a context capsule.
- For `creator_insights`, return one default action, its relevance rationale, evidence label, confidence and freshness note, a bounded test or implementation step, and a context capsule.
- Add alternatives only when they address distinct constraints.

## Graceful degradation

- For `next_action`, if the backlog is unclear, compare the actions named in the request; if none are named, choose the smallest action that unblocks the stated objective and label assumptions. If creator-hours are unknown, time-box a reversible first step rather than inventing capacity.
- For `creator_insights`, if sources are unavailable or weak, label the recommendation `hypothesis`, propose a reversible creator experiment, and avoid attributing the idea to consensus. If the creator lacks time to test, choose a no-regret maintenance action.

## Example

A music educator has 45 minutes and is choosing among fixing captions, designing a new series, or clipping yesterday's lesson. Caption repair scores high on goal alignment and urgency, unlocks the ready upload, fits the available time, and is reversible; choose it as the default without consulting external advice.
