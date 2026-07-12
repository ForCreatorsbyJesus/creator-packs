# Forward: repurpose VOD

## Prompt

Use @creator-copilot at /workspace/scratch/3c3299a79a51/creator-packs/plugins/everyday-streamer-creator-pack/skills/creator-copilot to solve this request:

Scenario B: Turn this timestamped livestream transcript into content for YouTube and Shorts. I can spend 60 minutes editing and only want the two best opportunities.

Transcript:
[00:00] Welcome back—tonight I’m trying the new survival mode without a guide.
[03:18] I wasted all my coins on armor, then realized the storm damages metal gear twice as fast.
[05:02] Wait, the map warning literally says that. I skipped it. That is painfully on brand.
[08:41] If I sell the armor now, I can afford one fire charm—but the next boss is probably ice.
[10:12] Chat says keep the armor. I’m trusting chat, which has never gone wrong.
[14:27] The storm starts; the armor breaks, but the broken metal attracts lightning and stuns the hidden boss.
[15:06] That accident unlocked the Stormbreaker badge. I cannot believe the bad decision was the solution.
[18:33] Here’s the lesson: read the warning, ignore it, and apparently discover a secret.

## Raw output

Primary job: `repurpose`

Assumptions: one YouTube highlight plus one Short; transcript-only evidence, so visuals, audio, and continuity remain unverified.

## 1. Short — “The bad decision was the solution”

Why it wins: The mistake-to-secret-badge reversal is understandable without broader game context and has the sharpest payoff. Audience response is a `hypothesis`; the story beats are `source-observed`.

Normalized selects:

- `00:03:18` — wasted coins on metal armor
- `00:05:02` — realizes the warning was explicit
- `00:10:12` — trusts chat and keeps it
- `00:14:27` — broken armor attracts lightning and stuns the hidden boss
- `00:15:06` — unlocks the Stormbreaker badge
- Optional button: `00:18:33` — “read the warning, ignore it…”

Target: 35–45 seconds, vertical.

Structure:

1. Cold open: “I cannot believe the bad decision was the solution.”
2. Compress setup: bought metal armor; storm destroys metal twice as fast.
3. Escalate: “Chat says keep it. I’m trusting chat…”
4. Payoff: armor breaks, attracts lightning, stuns hidden boss.
5. End on the badge reaction; use the `00:18:33` line only if pacing allows.

Packaging:

- Title: **My Worst Survival-Mode Decision Unlocked a Secret Badge**
- First-screen text: **I ignored the warning—and unlocked a secret**
- Caption: **Apparently the optimal strategy was making every wrong decision.**
- Cover text: **BAD CHOICE = SECRET?**

Time box: 18 minutes for cut, vertical crop, readable captions, and one punch-in on the badge. Avoid extra effects.

## 2. YouTube — “I ignored the warning and found a secret”

Why it wins: The full transcript contains a complete setup, dilemma, audience decision, reversal, and closing lesson. It supports a compact 4–6 minute highlight rather than an 18-minute lightly trimmed upload. Story beats are `source-observed`; title and thumbnail appeal are a `hypothesis`.

Normalized selects:

- `00:00:00` — survival mode without a guide
- `00:03:18–00:05:02` — armor mistake and skipped warning
- `00:08:41–00:10:12` — sell-or-keep dilemma and chat vote
- `00:14:27–00:15:06` — lightning, hidden boss, badge
- `00:18:33` — closing lesson

Structure:

1. Open with 3–5 seconds of the badge reaction from `00:15:06`.
2. Reset to `00:00:00`: first survival run without a guide.
3. Establish the costly armor mistake and warning.
4. Preserve the sell-or-keep decision so chat’s choice matters.
5. Let the storm sequence breathe; show the lightning stun clearly.
6. Resolve with the badge and the `00:18:33` lesson.

Packaging:

- Title: **I Ignored the Survival Mode Warning—and Found a Secret**
- Alternate title: **My Worst Decision Accidentally Beat the Hidden Boss**
- Thumbnail text: **THE MISTAKE WORKED**
- Description opener: **I went into the new survival mode blind, ignored the clearest warning imaginable, and somehow turned the mistake into a secret badge.**

Time box: 24 minutes for a clean narrative cut with simple jump cuts and minimal graphics.

## 60-minute edit budget

| Work | Time |
|---|---:|
| Check footage, audio, continuity, and mark shared selects | 8 min |
| Short edit, crop, and captions | 18 min |
| YouTube highlight edit | 24 min |
| Review both cuts | 5 min |
| Export and handoff | 5 min |
| **Total** | **60 min** |

Dependency and rights check: confirm the badge and lightning stun are visually legible. Blur chat usernames unless participants have consented to display. Rights or permission for game footage and any background music are not confirmed; verify the publisher/platform terms and mute or replace uncleared music before publishing.

## Creator Context Capsule

### Current objective
Turn one timestamped livestream transcript into the two strongest YouTube/Shorts opportunities.

### Confirmed constraints
60 total editing minutes; exactly two opportunities; transcript-only source.

### Decisions made
Create one 35–45 second Short and one 4–6 minute YouTube highlight using the same narrative spine and shared selects.

### Active experiment
Test whether the immediate “bad decision unlocked a secret” reversal earns enough viewer interest to support both formats.

### Assets created
Two ranked edit briefs, normalized selects, packaging drafts, dependency checks, and a 60-minute allocation.

### Open questions
Visual continuity, audio quality, game-footage rights, music clearance, and chat-name visibility are unverified.

### Recommended next action
Open `00:14:27–00:15:06` first and confirm the lightning stun plus badge unlock are clearly visible; if they are, edit the Short first.

## Rubric scores

- **creator_fit — 5/5:** It honors the 60-minute ceiling and exactly-two request while using shared selects and an explicit transcript-only assumption.
- **platform_fit — 5/5:** It distinguishes a compact vertical Short from a narrative YouTube highlight with format-specific structure and packaging.
- **actionability — 5/5:** Both opportunities include normalized selects, sequence, packaging, dependency checks, and complete edit allocations.
- **prioritization — 5/5:** It ranks the Short first, provides exactly two opportunities, and places one footage-verification action in the capsule.
- **evidence_transparency — 5/5:** Transcript beats are tagged `source-observed`, audience/packaging appeal is labeled a hypothesis, and visual claims remain conditional.
- **workload_realism — 5/5:** The full 60-minute plan reserves time for source checks, both edits, review, exports, and handoff.
- **voice_preservation — 5/5:** It builds hooks and copy from the creator’s supplied self-deprecating mistake-to-solution language.
- **artifact_usefulness — 5/5:** It delivers two complete edit briefs, a production budget, dependency checks, and all seven context fields.
- **uncertainty_calibration — 5/5:** It makes visuals, audio, continuity, rights, and audience response explicitly unverified and conditions the first action on footage quality.

**Average: 5.00/5.**

## Threshold checks

- Correct workflow route: pass (`repurpose`)
- One prioritized default action inside the capsule: pass
- All seven context-capsule fields: pass
- Average at least 4.0: pass
- No dimension below 3.5: pass (lowest: 5)
