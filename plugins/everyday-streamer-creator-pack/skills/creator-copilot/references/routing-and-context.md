# Routing and context

## Inputs

- User request and stated deadline or budget
- Current project context, if present
- Confirmed CreatorProfile fields, if present
- Available artifacts and their provenance

## Procedure

1. Map the dominant deliverable to `go_live_soon`, `plan_week`, `repurpose`, `review`, `next_action`, or `creator_insights`.
2. For compound requests, order routes by dependency: diagnose before choosing; choose before planning; plan before producing; repurpose after source material exists. Deliver one primary artifact and fold in only secondary work that fits the budget.
3. Resolve fields in this order: explicit request → current project → confirmed creator profile → labeled assumption. Never let an older profile override the current request.
4. Mark important fields with provenance such as `user-stated`, `project`, `profile-confirmed`, `source-observed`, or `assumed` when the distinction affects the recommendation. Treat these as field-origin tags, not evidence labels; apply the canonical evidence labels from `SKILL.md` separately to claims and recommendations.
5. Ask a question only if different answers would materially change the artifact. Otherwise use a reversible assumption and include a fallback.
6. Close with a context capsule that uses all seven explicit headings: `Current objective`, `Confirmed constraints`, `Decisions made`, `Active experiment`, `Assets created`, `Open questions`, and `Recommended next action`. Put the one prioritized next action inside the capsule; do not omit a heading or place the action only outside it. Use `None` or `Unknown` when needed rather than dropping a field, and keep unknowns unknown.

## Output contract

Return one named primary job, one usable creator artifact, one default action, and a complete seven-field context capsule whose `Recommended next action` contains that one action. Keep the total workload within the creator's stated budget.

## Graceful degradation

When context is sparse, avoid inventing channel history or audience preferences. Produce the smallest reversible artifact, label assumptions, and identify the single missing fact most worth confirming later.

## Example

Request: “I have an hour to edit last night's VOD and want Shorts plus a review.” Route to `repurpose` first because it produces the immediate artifact; include only a brief observed performance note if data is supplied. Assumption: export time must fit inside the hour. Next action: confirm the top clip after viewing its footage.
