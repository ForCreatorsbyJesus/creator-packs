# Everyday Streamer Creator Pack — Product and Skill Design

**Date:** July 11, 2026  
**Status:** Approved design; ready for implementation planning  
**Working skill name:** `creator-copilot`

## 1. Executive definition

The Everyday Streamer Creator Pack is an AI-powered support team for solo and small-team livestream creators. It helps creators decide what to stream, prepare it, turn each broadcast into useful content for YouTube and social platforms, understand what worked, and know what to do next.

The product promise is:

> Your AI creator support team: plan stronger streams, get more content from every broadcast, and improve each week—without doing everything alone.

Community-facing language must describe practical help rather than technical architecture. Use **Creator Pack**, **AI creator support team**, **creator companion**, or the specific job being performed. Do not market the product as an “operating system,” “agent architecture,” “workflow engine,” or similar technical abstraction. Terms such as module, router, schema, and workflow are reserved for implementation documentation.

The product is delivered as one installable ChatGPT/Codex skill in V1. It presents a Creator Copilot and several specialist modes, but routes among those modes internally to preserve context and avoid competing skill triggers.

The creator-facing loop is:

> **Prepare → Create → Multiply → Learn**

The more detailed lifecycle—Position → Plan → Prepare → Stream → Repurpose → Publish → Review → Improve—remains an internal design model rather than required navigation.

## 2. Intended users

### 2.1 Primary audience

V1 serves everyday streamers across:

- Gaming
- IRL
- Education
- Commentary
- Creative content
- Variety content

Recommendations adapt from emerging through growing creators. The default experience is optimized for a solo creator who streams at least once a week, has limited time and budget, and lacks a formal content or analytics team.

### 2.2 Maturity adaptation

The system classifies the creator's operating stage from confirmed inputs rather than follower count alone:

- **Starting:** little or no content history; needs positioning, setup, and first-stream support.
- **Emerging:** publishes or streams but lacks consistent systems and sufficient evidence.
- **Growing:** has repeat viewers and useful analytics but needs repeatability, experimentation, and leverage.
- **Team-supported:** has moderators, editors, or partners; receives collaboration-aware outputs without making team operations the V1 default.

### 2.3 Platform scope

V1 provides deep support for:

- Twitch livestream preparation, community engagement, clips, and stream review
- YouTube Live, VOD packaging, long-form content, Shorts, and channel review

It provides lighter destination-specific support for:

- TikTok
- Instagram Reels
- Discord community follow-up

V1 does not claim feature parity across all destinations. Platform-specific advice must be versioned and reverified when it may have changed.

## 3. Product principles

1. **Minimize decisions.** Recommend one default action and provide alternatives only when useful.
2. **Fit the creator's moment.** Support “now,” “tonight,” “after my stream,” and “this week” instead of forcing a lifecycle.
3. **Produce work, not just advice.** Deliver editable stream briefs, asset packages, and reviews.
4. **Use evidence with humility.** Show provenance, applicability, effort, uncertainty, and limitations.
5. **Learn from the creator's baseline.** Prefer longitudinal comparison with the creator's own history over universal benchmarks.
6. **Optimize for sustainable leverage.** Rank expected impact against creator hours, budget, energy, safety, and enjoyment.
7. **Preserve creator identity.** Adapt lessons without imitating another creator's voice, likeness, or recognizable packaging.
8. **Keep humans in control.** Draft and recommend; never publish or operate an account in V1.

## 4. User-facing experience

### 4.1 Entry points

The creator may begin with natural requests such as:

- “I go live in 90 minutes.”
- “Plan my creator week.”
- “Turn this VOD into content.”
- “Review my last stream.”
- “What should I do next?”
- “What are successful streamers learning?”
- “Help me improve my Twitch and YouTube presence.”

The skill identifies the requested job, checks whether material context is missing, and either proceeds with labeled assumptions or asks one concise question.

### 4.2 First-value experience

The target first-run flow is:

1. Capture a minimum viable creator profile in no more than five minutes.
2. Ask for the immediate job, time available, and relevant links or artifacts.
3. Deliver one useful artifact within ten minutes.
4. End with one recommended next action and a compact context capsule.

The skill must remain useful when the creator has no integrations or analytics. More evidence improves confidence and specificity; it is not a prerequisite for first value.

### 4.3 Signature artifact: Tonight's Stream Packet

The defining V1 output contains:

- One recommended concept and creator-fit rationale
- One primary title and two alternatives
- One thumbnail direction
- Opening hook
- Timed run of show
- Segment beats and transitions
- Audience prompts and CTA
- Technical and moderation preflight
- A fallback plan for dead air, technical trouble, or failed segments
- Planned moments that can become clips
- Post-stream capture instructions
- The active experiment and success signal

The packet must be concise enough to use immediately and opinionated enough to reduce decisions.

### 4.4 V1 input-acquisition contract

V1 may use public web browsing to inspect accessible channel pages, public metadata, official guidance, creator interviews, and available transcripts. It does not authenticate, bypass access controls, scrape continuously, download protected media, or assume that a Twitch or YouTube URL exposes captions or a usable transcript.

Supported creator-supplied inputs are:

- UTF-8 `.txt`, `.md`, `.csv`, `.tsv`, and `.json`
- Platform analytics exports matching a versioned supported schema
- Transcript text containing timestamps in `HH:MM:SS`, `MM:SS`, seconds, or ISO-8601 duration form
- Screenshots that the active ChatGPT/Codex surface can inspect
- Public URLs that the active surface can browse without authentication
- Creator-written timestamps, stream notes, chat-spike notes, and clip candidates

V1 accepts up to five source files per workflow, 10 MB per text/tabular file, 25 MB combined, 200,000 transcript words, 100,000 analytics rows, and ten screenshots. Larger inputs require creator-approved chunking with a manifest that records coverage. A workflow must reject inputs it cannot process reliably rather than silently truncate them. A target runtime may impose a lower documented limit, which must be surfaced before processing.

Acquisition precedence is:

1. User-supplied export or transcript
2. Publicly accessible platform transcript or metadata
3. User-supplied screenshots and notes
4. Public page observation
5. Labeled assumptions

If a URL cannot be read, the skill explains the limitation and requests a transcript, export, screenshot, or notes. “Turn this VOD into content” is considered fully supported only when timestamped source material is available; without it, the skill may create an untimestamped repurposing plan but must not invent moments or timestamps.

## 5. V1 architecture

V1 ships as one installable skill named `creator-copilot`. Its main instruction file routes work to internal workflow and reference files using progressive disclosure.

| Internal module | Owns | Primary output |
|---|---|---|
| Route and Context | Intent classification, context checks, workflow composition, state updates | Selected workflow, assumptions, context capsule |
| Position and Plan | Audience promise, channel role, content pillars, cadence, goals, bounded experiments | Weekly Growth Plan |
| Prepare and Stream | Stream concept, run of show, preflight, engagement design, contingencies | Tonight's Stream Packet |
| Repurpose and Publish | Transcript/VOD analysis, clip candidates, platform transformation, draft packaging | Content Multiplier Package |
| Review and Improve | Analytics interpretation, retrospective, experiment review, next-action ranking | Post-Stream Review |
| Creator Insight Engine | Source management, Insight Cards, relevance filtering, evidence ranking, freshness | Sourced recommendations used by all modules |

“Improve” is the output of Review and an input to Plan. “Publish” means generating draft-ready packaging and a checklist; the skill does not upload, schedule, or publish.

### 5.1 Routing rules

Routing classifies the creator's job rather than matching lifecycle terms. Precedence is:

> Explicit request → current stream/project context → confirmed creator profile → labeled defaults

Examples:

| Request | Workflow |
|---|---|
| “What should my channel focus on?” | Position and Plan |
| “Plan Friday's stream.” | Prepare and Stream |
| “Find clips in this transcript.” | Repurpose and Publish |
| “Why did this underperform?” | Review and Improve |
| “Review yesterday and plan next week.” | Review and Improve → Position and Plan |
| “What should I do next?” | Read latest review; otherwise create a bounded weekly plan |

For compound requests, the router creates one workflow graph so outputs share the same experiment and creator context.

## 6. Creator context and continuity

The skill must not imply durable hidden memory. It maintains explicit, user-visible artifacts that can be reused across ChatGPT or Codex sessions.

### 6.1 Context scopes

| Scope | Examples | Update rule |
|---|---|---|
| Creator | Niche, audience, goals, voice, resources, guardrails | Update only from user confirmation or direct statement |
| Project | Series, recurring format, active experiment, assets | Update during project work |
| Session | Immediate task, temporary assumptions, draft decisions | Expire or promote explicitly |

Every material fact records one of these provenance types:

- `user_provided`
- `analytics_derived`
- `publicly_observed`
- `assumed`

The system never silently overwrites confirmed profile facts with inference.

### 6.2 Field-level provenance and merge contract

Context records use a field-value envelope for every mutable material fact:

```json
{
  "value": "example",
  "source_type": "user_provided",
  "source_ref": "conversation-or-artifact-reference",
  "observed_at": "2026-07-11T00:00:00Z",
  "confidence": "confirmed",
  "status": "active"
}
```

Allowed confidence values are `confirmed`, `derived`, `observed`, and `assumed`. Allowed status values are `active`, `superseded`, and `deleted`. Deletion is represented by a tombstone envelope; keys are not silently removed.

Merge precedence is:

1. A new direct user statement supersedes an older direct user statement.
2. User-confirmed values supersede analytics-derived, publicly observed, and assumed values.
3. Analytics-derived values may update only fields defined as analytical baselines; they cannot change identity, goals, voice, or guardrails.
4. Public observations and assumptions may fill empty fields but cannot overwrite confirmed values.
5. Conflicting values of equal precedence produce a conflict record and require creator confirmation before promotion.
6. Session facts are promoted to project or creator scope only after explicit confirmation, except generated artifact IDs and timestamps.

At the end of a workflow, the skill proposes a human-readable context diff. The creator must approve changes to creator-scope goals, identity, voice, guardrails, or platform roles. Project artifacts and session records may be written as drafts automatically. Asset status transitions are `draft → reviewed → approved`; only explicit creator confirmation may set `approved`.

### 6.3 Canonical records

Every machine-readable record includes `schema_version`, a stable ID, creation/update timestamps, and provenance.

#### CreatorProfile

- Creator maturity and niches
- Target audience and audience promise
- Primary and secondary platforms
- Cadence and available creator-hours
- Budget and team size
- Hardware/software constraints
- Voice preferences and prohibited styles
- Primary objective and guardrails
- Confirmed baselines and last confirmation date

#### ContentProject

- Project or series identity
- Concept and audience promise
- Format and platform roles
- Recurring segments
- Asset inventory
- Active experiment
- Project constraints

#### StreamBrief

- Objective and success signal
- Topic, game, or event
- Date, duration, and segment timeline
- Engagement moments and CTAs
- Technical/moderation checklist
- Contingency branches
- Planned repurposing targets

#### InsightCard

- Claim, lesson, or observed result
- Source type, source reference, and title when applicable
- Source date, review date, and `next_review_at`
- Source creator context when applicable
- Platform, niche, maturity, and resource applicability
- Adapted action
- Evidence class and confidence
- Effort/cost
- Expected mechanism and success signal
- Contradictions and limitations

Analytics-derived cards may reference an immutable AnalyticsSnapshot instead of an external URL. Hypothesis cards may have no external source but must cite the observations and reasoning that produced them.

#### Recommendation

- Action
- Rank: `do_now`, `test_next`, `watch`, or `ignore`
- Creator-fit rationale
- Linked Insight Cards
- Expected effort and reversibility
- Success metric and decision window
- Confidence and uncertainty

#### AssetManifest

- Source stream or transcript
- Asset type and destination platform
- Draft content and creative brief
- Timestamp, crop, duration, or specification needs
- Rights, privacy, or policy flags
- Status: `draft`, `reviewed`, or `approved`
- Human approval requirement

#### ReviewRecord

- Immutable analytics snapshot reference
- Metric definitions, date window, and timezone
- Comparison baseline
- Observation, hypothesis, and experiment result
- Confounders
- Keep, change, and stop decisions
- Next action

#### AnalyticsSnapshot

- Platform and export format version
- Original immutable artifact hash
- Capture time, reporting window, and timezone
- Canonical metric names, definitions, values, and denominators
- Missing-data and normalization notes

#### ExperimentRecord

- Hypothesis and expected mechanism
- Creator goal and affected workflow artifacts
- Start/end window and baseline
- Success, failure, and inconclusive thresholds
- Confounders and creator workload
- Result and keep/change/stop decision

#### ContextCapsule

- Current objective
- Confirmed creator constraints
- Decisions made
- Active experiment
- Assets created
- Open questions
- Recommended next action

## 7. Creator Insight Engine

The Creator Insight Engine is shared infrastructure, not a user-facing tips scraper.

### 7.1 Source hierarchy

The engine prioritizes:

1. The creator's own fixed analytics and experiment history
2. Current official Twitch and YouTube guidance
3. Firsthand interviews, streams, videos, podcasts, and postmortems from thriving creators
4. Credible creator educators and platform specialists
5. Publicly observable channel patterns
6. Community experience from sources such as r/Twitch and r/NewTubers

Frequency of repetition does not determine evidence quality. Creator interviews are experiential evidence, not universal rules.

For V1, a **thriving creator** is a source creator with a sustained, publicly observable body of relevant work and either documented operating experience or attributable firsthand lessons; follower count alone is insufficient. A **credible educator** must use attributable sources, distinguish evidence from opinion, and demonstrate current platform-specific expertise. These labels qualify a source for review but do not automatically raise confidence.

Official Twitch resources establish that channel analytics, stream summaries, clips, branding, engagement, accessibility, collaboration, events, and social strategy are distinct creator jobs. Official YouTube resources establish separate Live, long-form, Shorts, community, and analytics surfaces whose metrics and uses must not be conflated.

### 7.2 Evidence classes

| Evidence class | Meaning | Maximum default confidence |
|---|---|---|
| Creator experiment | Result from the creator's own controlled or bounded test | High, subject to sample and confounders |
| Official platform guidance | Current documented platform behavior or recommended practice | High for the documented claim |
| Firsthand creator experience | A creator explains what worked in their context | Medium until adapted and tested |
| Public observation | A visible pattern in public content or packaging | Medium-low; cannot establish causality |
| Community report | Anecdotal report from an identified community source | Low to medium after triangulation |
| Hypothesis | Reasoned but untested proposal | Experimental |

### 7.3 Relevance filter

Before presenting a lesson, the engine compares:

- Creator maturity
- Niche and format
- Audience size and behavior
- Primary objective
- Available time, energy, team, and budget
- Platform and destination
- Cadence
- Creator strengths and current bottleneck
- Safety, privacy, rights, and burnout constraints

It then adapts the lesson and classifies it as:

- **Do now:** high-fit and sufficiently supported
- **Test next:** plausible and measurable with bounded cost
- **Watch:** promising but currently weak or inapplicable
- **Ignore for now:** valid advice that does not fit the current stage or objective

V1 recommendation ranking uses a documented 0–3 rubric for creator fit, source quality, freshness, expected value, effort, risk, and reversibility. “High-fit” requires no material mismatch on niche, platform, maturity, objective, or time budget. “Bounded cost” means the action fits the creator's confirmed weekly time and budget without displacing a higher-priority commitment. Confidence may be reduced by contradictions, poor freshness, weak sample size, or confounders; it may never exceed the maximum allowed by its strongest supporting evidence class without a creator-specific experiment.

### 7.4 Freshness

Platform guidance stores a source date, review date, and next review date. The skill must browse current official sources before relying on rules, eligibility thresholds, feature availability, asset specifications, or platform metrics that could have changed.

Durable principles and volatile tactics are stored separately. Stale guidance may be retained for history but cannot support a current high-confidence recommendation without verification.

### 7.5 V1 runtime and storage boundary

V1 combines three evidence modes:

- **Bundled baseline:** a versioned source registry containing official starting sources, metric dictionaries, and durable principles.
- **Runtime verification:** browsing current official sources when a recommendation depends on volatile rules, features, specifications, or metrics.
- **Creator-local cards:** Insight Cards created for the current creator from consented analytics, public observations, and sourced lessons.

The source registry records source ID, URL, platform, source type, topics, retrieved/reviewed dates, next review date, and status. Creator-local cards remain explicit user artifacts; V1 does not maintain a hidden global creator-surveillance database. `check_source_freshness.py` evaluates registry dates and status but does not crawl the web. Browsing retrieves current evidence; the skill then proposes updated registry/card records for user-visible storage.

## 8. Workflow specifications

### 8.1 Creator Copilot and onboarding

Minimum onboarding asks only for information that changes the first output:

- Channel links or creator description
- Niche and typical format
- Primary platform and intended role of YouTube/Twitch
- Primary objective: reach, retention, community, consistency, craft, or income
- Weekly time budget and stream cadence
- Immediate job

Everything else may be inferred as a labeled assumption or requested later. The first response ends with one useful artifact, not an onboarding report.

### 8.2 Weekly Growth Planner

Inputs:

- Creator profile
- Available creator-hours
- Recent content or performance evidence when available
- Current goal and constraints

Output:

- One weekly priority
- One bounded hypothesis
- One major experiment
- Planned stream and content outputs
- Expected effort
- Success signal and review window
- Tasks to stop, defer, or substitute

### 8.3 Stream Prep Studio

Inputs:

- Stream concept or request for a recommendation
- Time before stream
- Planned duration
- Platform and format
- Creator energy/resources
- Current experiment

Output:

- Tonight's Stream Packet
- Compact one-screen preflight
- Optional moderator or collaborator brief

If the creator is going live soon, the skill prioritizes speed and omits nonessential strategy work.

### 8.4 Content Multiplier

Inputs may include:

- VOD link
- Timestamped transcript
- Chat log or chat-spike markers
- Creator notes
- Existing clips
- Analytics snapshots

Output:

- Ranked moments with timestamps and selection rationale
- One recommended primary asset
- Platform-native transformations rather than copy-pasted resizing
- Hooks, edit decisions, captions, titles, descriptions, and thumbnail briefs
- Community follow-up
- Asset manifest with declared or observable rights/privacy risk indicators

If the supplied content contains no strong clip, the system says so and may suggest a recap, compilation, or future stream-design change instead of manufacturing false highlights.

### 8.5 Post-Stream Review

Inputs:

- Creator observations
- Stream summary or analytics export
- Published asset results when available
- Active experiment and baseline

Output separates:

- What was observed
- What may explain it
- What remains uncertain
- Whether the experiment was supported, inconclusive, or contradicted
- What to keep, change, and stop
- One change carried into the next plan

Metrics are stored with definitions, platform, window, denominator, and timezone. Twitch and YouTube metrics are never treated as interchangeable merely because they have similar names.

### 8.6 V1 analytics contract

V1 guarantees deterministic analytics only for:

1. The canonical `AnalyticsSnapshot` JSON schema included with the skill.
2. Versioned Twitch and YouTube fixture formats explicitly listed in the platform references.
3. CSV/TSV data that the creator maps to canonical fields and confirms before calculation.

Screenshots and prose may support qualitative review but cannot enter deterministic calculations until values and definitions are extracted and confirmed.

The canonical metric dictionary records platform, surface (`live`, `vod`, `short`, `video`, or `community`), metric ID, platform label, definition, unit, aggregation type, denominator, reporting window, and export version. V1 calculations are limited to validated absolute deltas, percentage changes with nonzero baselines, rates with explicit denominators, and period comparisons using aligned windows. Weighted metrics require the documented weight. Zero denominators produce `undefined`, not zero. Missing values remain missing. All timestamps normalize to UTC while preserving the source timezone.

An unknown export version or metric label fails closed: the skill requests mapping or treats the value as qualitative evidence. The 100% analytics-correctness threshold applies only to frozen supported fixtures and formulas, not to arbitrary screenshots or undocumented platform exports.

## 9. Data-flow and failure behavior

### 9.1 Evidence levels

| Level | Input available | Expected behavior |
|---|---|---|
| 1 | Creator description only | Useful first artifact with explicit assumptions and low/medium confidence |
| 2 | Public channel and content | Observable content and packaging analysis without private inference |
| 3 | Transcript, VOD notes, screenshots, or analytics export | Timestamped assets and creator-specific findings |
| 4 | Several weeks of records | Creator-baseline comparisons and experiment learning |

### 9.2 Graceful degradation

- Missing public metadata: request screenshots/exports or proceed with creator-provided description.
- Missing analytics: use content evidence and label outcome claims as hypotheses.
- No viable clip: explain why and recommend a different artifact or stream-design change.
- Conflicting advice: show the conflict, evidence type, and contextual reason for selecting or rejecting each option.
- Stale source: verify against an official current source or lower confidence and warn.
- Ambiguous route: state the selected workflow; ask only if alternatives would materially change the output.
- Invalid metrics: stop the calculation, identify the issue, and request corrected definitions or data.
- Unrealistic workload: reduce, substitute, or defer work before adding more tasks.

## 10. Safety, trust, and creator well-being

The skill must:

- Avoid promises of virality, growth, revenue, sponsorships, or algorithmic preference
- Avoid fake engagement, spam, harassment, deceptive packaging, impersonation, or unsafe stunt recommendations
- Avoid inferring private traits, income, relationships, motivations, or business arrangements from public content
- Avoid copying recognizable creator wording, thumbnail designs, identity, or brand expression
- Screen for declared or observable music, footage, guest, chat-log, likeness, privacy, and disclosure risk indicators in draft assets
- State that risk screening does not establish ownership, permission, or legal clearance; request creator confirmation when evidence is unavailable
- Treat private analytics as creator-controlled data and use only consented records
- Respect weekly time, energy, enjoyment, accessibility, and burnout guardrails
- Keep all publishing assets in draft status until human approval
- Distinguish observation, hypothesis, and causal evidence
- Recommend one major experiment at a time unless the creator explicitly accepts a more complex test

## 11. Validation design

### 11.1 Validation layers

1. **Synthetic regression suite:** at least 24 profiles across niches, maturity, team size, budget, cadence, accessibility needs, and platform mix.
2. **Public realism cases:** observation-only reviews of GamingWithMeech and DebodBeezy, plus non-gaming cases. These creators are evaluation subjects, not endorsements or templates.
3. **Prospective pilot:** one or more consenting creators using fixed, redacted analytics and an explicit baseline.
4. **Adversarial suite:** requests involving fabricated sources, stale rules, unsupported facts, private inference, unsafe tactics, copyright problems, unrealistic workload, and autonomous publishing.

Development and holdout observations must be separated. Public creator cases used to tune prompts cannot also be the sole scored test set.

Each public-case fixture records the channel URL, observation timestamp, accessible artifacts, source hashes where possible, excluded/private fields, development-or-holdout assignment, and reviewer notes. The analysis may describe only content visible in that frozen fixture. It may not imply creator consent or endorsement.

A private pilot requires written creator consent, a declared retention period, a redaction checklist, a fixed baseline of at least four comparable creator-weeks when available, and a minimum set of creator goal, workload, stream/content outputs, and platform-defined outcome metrics. A missing publication or incomplete week is recorded as noncompletion with a reason; it does not become an automatic product failure when external events prevented use. The pilot is a post-build validation gate, not a prerequisite for producing the core package.

### 11.2 Baselines

Compare V1 against:

- A generic model response without the skill
- A single large static “creator expert” prompt
- Creator Copilot without the Insight Engine
- Creator Copilot without persisted context
- Creator Copilot without effort ranking
- A creator's existing manual workflow when available

Comparisons must reward better decisions and usable artifacts, not longer outputs.

### 11.3 Objective release thresholds

| Test | V1 threshold |
|---|---:|
| Skill trigger precision | ≥95% |
| Skill trigger recall | ≥90% |
| Internal routing accuracy | ≥95% |
| Schema validation | 100% |
| Constraint adherence | ≥98% |
| Source entailment in sampled claims | ≥95% |
| Expired official guidance used without warning | 0 |
| Correct use of supplied context | ≥98% |
| Unsupported creator facts introduced | <1% |
| Deterministic analytics calculations | 100% |
| No autonomous publishing | 100% |
| Excluded-data leakage | 0 |

### 11.4 Human evaluation rubric

Two independent reviewers score each output from 1–5 on:

- Creator fit
- Platform fit
- Actionability
- Prioritization
- Evidence transparency
- Workload realism
- Voice preservation
- Artifact usefulness
- Cross-artifact consistency
- Accuracy and uncertainty calibration
- Likelihood the creator would use the result

V1 targets an average of at least 4.0, no dimension below 3.5, and tracked reviewer agreement.

Reviewer agreement is measured using weighted Cohen's kappa for two reviewers, with a target of at least 0.60. Disagreements larger than one point require adjudication but retain the original scores.

### 11.5 Behavioral proof

Initial pilot success requires:

- First useful artifact in under ten minutes
- At least one recommendation or asset accepted or meaningfully edited
- At least one repurposed asset published within 48 hours
- One bounded weekly experiment completed and reviewed
- The review causes a concrete change to the next stream
- Creator-reported time savings without increased burnout

The north-star metric is:

> **Percentage of active creator-weeks that complete one prepared stream, one accepted repurposed asset, one reviewed experiment, and one evidence-based improvement to the next plan.**

Creator outcome measures include publishing consistency, output per creator-hour, returning-viewer behavior, relevant retention, packaging performance, audience interaction, creator confidence, and sustainability. Followers, raw views, posting volume, and peak concurrent viewers are contextual outcomes rather than sole optimization targets.

### 11.6 Evaluation operation definitions

- **Useful artifact:** a complete contracted output that satisfies all required fields, creator constraints, and safety checks and receives a human usefulness score of at least 4/5.
- **Ten-minute target:** measured from receipt of the final required creator input to artifact delivery; user response time, platform upload/download time, and unavailable third-party pages are excluded and reported separately.
- **Accepted asset:** explicitly approved for use by the creator. **Meaningfully edited** means the creator retains the asset's concept and at least half of its substantive structure while changing wording or execution.
- **Source-entailment sample:** all high-confidence claims plus a seeded random sample of at least 20 remaining externally supported claims per release candidate.
- **Context-correctness denominator:** all fixture facts required by the selected workflow. Unsupported-fact rate uses all factual creator claims generated by the skill.
- **Abstention:** correct when required evidence is unavailable or an action is outside scope; abstentions are scored separately from failures.
- **Invalid case:** a fixture that violates its own schema or lacks required gold labels; it is excluded only with a recorded reason before results are calculated.

## 12. Skill package design

The intended implementation structure is:

```text
creator-copilot/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── routing-and-context.md
│   ├── position-and-plan.md
│   ├── prepare-and-stream.md
│   ├── repurpose-and-publish.md
│   ├── review-and-improve.md
│   ├── insight-engine.md
│   ├── schemas.md
│   ├── evidence-rubric.md
│   ├── platform-youtube.md
│   ├── platform-twitch.md
│   ├── metric-dictionary.md
│   ├── source-registry.json
│   └── safety-and-rights.md
├── scripts/
│   ├── validate_records.py
│   ├── merge_context.py
│   ├── normalize_transcript.py
│   ├── normalize_analytics.py
│   ├── calculate_metrics.py
│   ├── validate_insight_cards.py
│   ├── validate_asset_manifest.py
│   ├── check_source_freshness.py
│   ├── rank_recommendations.py
│   └── score_evaluations.py
└── assets/
    ├── creator-profile.template.json
    ├── content-project.template.json
    ├── stream-brief.template.json
    ├── insight-card.template.json
    ├── recommendation.template.json
    ├── asset-manifest.template.json
    ├── analytics-snapshot.template.json
    ├── experiment-record.template.json
    ├── review-record.template.json
    ├── context-capsule.template.md
    ├── weekly-growth-plan.template.md
    ├── tonight-stream-packet.template.md
    ├── content-multiplier-package.template.md
    └── post-stream-review.template.md
```

The implementation workspace also contains a non-shipping validation surface:

```text
evals/
├── README.md
├── contracts/
│   ├── case.schema.json
│   ├── expected-output.schema.json
│   └── human-rubric.schema.json
├── fixtures/
│   ├── synthetic-profiles/
│   ├── routing-positive/
│   ├── routing-negative/
│   ├── compound-workflows/
│   ├── transcripts/
│   ├── analytics/
│   ├── stale-and-conflicting-sources/
│   ├── adversarial/
│   └── public-cases/
├── gold/
│   ├── routes.jsonl
│   ├── calculations.jsonl
│   ├── constraints.jsonl
│   └── source-entailment.jsonl
└── holdout-manifest.json
```

`SKILL.md` remains concise and contains the routing workflow, core rules, context precedence, and instructions for loading the appropriate reference. Detailed platform material, schemas, rubrics, and workflow examples live in references. Deterministic scripts handle validation, dates, schema merging, transcript normalization, metric calculations, and evaluation scoring.

Each evaluation case records a case ID, task prompt, creator/artifact inputs, allowed assumptions, expected route, required and forbidden output properties, applicable objective checks, and reviewer rubric. Gold labels are versioned and immutable within a release candidate. `holdout-manifest.json` identifies fixtures that implementation authors must not use for prompt tuning. `score_evaluations.py` consumes per-case machine results and human rubric files and emits numerator, denominator, exclusions, confidence intervals where appropriate, and failed-case IDs.

## 13. V1 exclusions

V1 explicitly excludes:

- Autonomous uploading, scheduling, publishing, messaging, or account operation
- Credentials, OAuth, or direct platform integrations
- Acting as a real-time co-host or operating streaming software
- Real-time moderation or safety enforcement
- Guaranteed growth, virality, monetization, revenue, or sponsorship outcomes
- Automated scraping or continuous surveillance of creators and communities
- Full competitive intelligence or creator ranking
- Rights clearance or legal conclusions
- Tax, financial, medical, or mental-health advice
- Paid media buying, sponsorship negotiation, merch, and business operations
- Full multilingual or local-market optimization
- TikTok, Instagram, and Discord parity with Twitch and YouTube
- Agency and multi-channel enterprise workflows
- Fine-grained causal attribution from observational analytics
- Automatic imitation of another creator's identity, voice, thumbnails, or formats
- Eight independently installable lifecycle skills before routing reliability is proven

## 14. Expansion path

After V1 validates routing and the closed loop, potential additions are:

- Separate niche playbooks
- Live incident-recovery and technical troubleshooting
- Moderator and community operations
- Collaboration and guest-stream planning
- Editor/moderator handoffs
- Direct analytics connectors
- Longitudinal creator benchmarking
- Sponsorship and monetization workflows
- Optional independently installable specialists when trigger boundaries are empirically reliable

## 15. Source baseline

The initial reference baseline should prioritize official sources, including:

- [YouTube Live](https://www.youtube.com/creators/create/live/)
- [YouTube: Optimize and evolve your content](https://www.youtube.com/creators/grow/optimize-your-content/)
- [YouTube: Live stream metrics](https://support.google.com/youtube/answer/2853833)
- [YouTube: Shorts analytics](https://support.google.com/youtube/answer/12942217)
- [YouTube Creator updates](https://support.google.com/youtube/answer/9072033)
- [Twitch Creator Camp](https://www.twitch.tv/creatorcamp/en/level1/)
- [Twitch Analytics Overview](https://help.twitch.tv/s/article/channel-analytics)
- [Twitch Stream Summary](https://help.twitch.tv/s/article/stream-summary)
- [Twitch Featured Clips](https://help.twitch.tv/s/article/featured-clips)
- [Twitch Research Analytics](https://help.twitch.tv/s/article/research)

Community posts, thriving-creator interviews, and educator content may complement this baseline only when captured as provenance-rich Insight Cards with explicit context and uncertainty.

## 16. Staged delivery gates

The design is delivered through four sequential gates rather than one undifferentiated implementation plan:

1. **Core skill package:** initialize `creator-copilot`; implement routing, schemas, templates, deterministic utilities, official source baseline, and all five user workflows using synthetic fixtures.
2. **Deterministic validation:** complete positive/negative routing, schema, merge, transcript, analytics, freshness, ranking, safety, and cross-workflow tests; meet applicable objective thresholds.
3. **Public-case evaluation:** freeze public observations for GamingWithMeech, DebodBeezy, and non-gaming creators; run blinded human review without using holdout cases for tuning.
4. **External pilot:** run the consented creator pilot, measure behavioral proof, and decide whether the system is ready for wider use or requires iteration.

Gates 1–2 constitute the build plan. Gate 3 is the pre-release realism evaluation. Gate 4 validates external usefulness and may complete after the installable V1 exists.

## 17. Completion and readiness criteria

The installable V1 build is complete when Gates 1–2 pass. Pre-release readiness additionally requires Gate 3 and the following criteria:

1. The skill initializes and passes structural validation.
2. All canonical record schemas validate valid fixtures and reject failure fixtures.
3. The router passes the labeled intent suite.
4. Each workflow produces its contracted artifact.
5. Cross-workflow fixtures preserve the same creator goal and active experiment.
6. Source freshness and evidence labels appear correctly.
7. Analytics fixtures produce exact expected calculations.
8. Public creator cases avoid unsupported inference and imitation.
9. Adversarial cases do not publish, invent evidence, expose excluded data, or recommend unsafe tactics.
10. Forward tests demonstrate a meaningful preference over generic and static-prompt baselines.

Gate 4 produces the external-usefulness decision. A pilot failure triggers iteration but does not retroactively mean the installable artifact was structurally incomplete.
