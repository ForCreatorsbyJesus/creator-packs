# Creator Packs

Practical AI support teams for everyday creators.

Creator Packs turn a creator's goals, voice, available time, and real performance signals into useful work they can act on today. The first pack is built for emerging livestreamers across YouTube and Twitch, with support for repurposing into TikTok, Instagram, and Discord.

## Available packs

| Pack | What it helps with | Status |
|---|---|---|
| [Everyday Streamer Creator Pack](plugins/everyday-streamer-creator-pack) | Stream preparation, content repurposing, performance learning, and sourced creator insights | Early preview |

## Install from this marketplace

Add this repository as a Codex plugin marketplace, then install `everyday-streamer-creator-pack`.

```bash
codex plugin marketplace add https://github.com/ForCreatorsbyJesus/creator-packs
codex plugin install everyday-streamer-creator-pack@creator-packs
```

## What makes a Creator Pack trustworthy

- Recommendations identify whether evidence is confirmed, observed, derived, or assumed.
- Public creator examples use public information without implying endorsement.
- The creator stays in control of voice, boundaries, and final publishing decisions.
- The pack asks for the smallest useful amount of context and remains useful when analytics are incomplete.

## Project stage

This repository currently contains the marketplace foundation and the first usable Creator Copilot skill. Deterministic scoring, public-case evaluation, and a consenting creator pilot are separate delivery gates.

See [CONTRIBUTING.md](CONTRIBUTING.md) to help improve a pack or propose a new one.
Creator Packs turns common creator jobs into reusable ChatGPT and Codex skills. The first pack is designed for livestream creators who want useful help today—not a pile of generic growth tips.

## Available packs

| Pack | Status | Best for |
|---|---|---|
| Everyday Streamer Creator Pack | Alpha | Twitch and YouTube creators working alone or with a small team |

## Everyday Streamer Creator Pack

The pack helps a creator:

- Decide what to stream next
- Prepare a stream without exceeding the available time
- Turn a VOD or transcript into a few strong content opportunities
- Adapt each idea for Twitch, YouTube, and Shorts
- Review performance without pretending correlation proves causation
- Learn from successful creators without copying their identity or tactics blindly
- Carry decisions and experiments into the next creator session

Its main skill is `creator-copilot`, an AI creator support teammate that routes the request to the right kind of help.

## What can I ask it?

- “I go live in 90 minutes.”
- “Plan my creator week.”
- “Turn this stream into content.”
- “Review my last stream.”
- “What should I do next?”
- “What are successful streamers learning?”

## Example: Tonight's Stream Packet

A rapid stream-preparation request produces one usable packet:

```markdown
# Tonight's Stream Packet

## Recommended concept
One stream idea fitted to your audience, energy, time, and platform.

## Timed run of show
A hook, segment beats, audience prompts, CTA, and fallback.

## Planned clip moments
Moments designed to become useful content after the stream.

## Active experiment and success signal
One thing to test and a clear way to review it.
```

The result ends with one next action instead of an overwhelming list.

## Install from this marketplace

Clone the marketplace, add its local path, then install the pack:

```bash
git clone https://github.com/ForCreatorsbyJesus/creator-packs.git
codex plugin marketplace add "$(pwd)/creator-packs"
codex plugin add everyday-streamer-creator-pack@creator-packs
```

Confirm it appears with:

```bash
codex plugin list
```

Then start a new conversation and ask for `$creator-copilot`.

> The repository validates these commands against the Codex plugin-creator contract. This build environment does not include the Codex CLI, so end-to-end CLI installation remains a release verification item.

## How recommendations use evidence

Creator Copilot separates:

- Official platform guidance
- Firsthand creator experience
- Public observations
- Community reports
- Your own creator experiments
- Unproven hypotheses

Advice is adapted to the creator's niche, maturity, platform, available hours, budget, and current goal. A popular tactic is not treated as universally correct.

## Privacy and creator control

- Creator analytics and transcripts remain creator-controlled inputs.
- Public channel reviews use only observable information and do not imply endorsement.
- The pack drafts content but does not upload, schedule, publish, or operate creator accounts.
- Rights checks identify possible risks; they do not provide legal clearance.
- The creator approves assumptions, profile changes, and anything intended for publication.

## Development status

This alpha includes the validated marketplace, plugin, skill, baseline evaluations, and forward evaluations. Deterministic analytics adapters, larger public-channel evaluation sets, and a consented creator pilot are planned follow-on releases.

See the [product design](docs/design/2026-07-11-everyday-streamer-creator-pack-design.md) and [foundation implementation plan](docs/plans/2026-07-11-creator-packs-marketplace-foundation.md).

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing another creator pack or changing a creator workflow.

## License

MIT. See [LICENSE](LICENSE).
