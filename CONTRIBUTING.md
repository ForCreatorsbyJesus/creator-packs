# Contributing to Creator Packs

Creator Packs should solve real creator jobs with practical, evidence-aware support.

## Before proposing a pack

Open a discussion or issue that defines:

1. The creator audience and maturity range
2. The concrete job the pack performs
3. Three realistic requests that should trigger it
4. What a useful finished artifact looks like
5. What the pack must not do

Do not begin with a list of AI roles or agents. Begin with the creator's problem.

## Required development method

- Capture unassisted baseline outputs before authoring or expanding a skill.
- Store exact evaluation prompts and unaltered raw outputs.
- Forward-test with fresh contexts that cannot see expected answers.
- Keep community-facing language understandable and nontechnical.
- Use official sources for platform rules, eligibility, features, metrics, and specifications that may change.
- Label creator experience, public observation, community reports, and hypotheses accurately.
- Preserve creator voice; do not imitate named creators or reproduce signature packaging.
- Never promise growth, reach, revenue, virality, or algorithmic preference.
- Never add autonomous publishing or credential use without a separately reviewed design.

## Validation

Run:

```bash
python3 -m pytest
python3 scripts/validate_repository.py .
python3 /root/.codex/skills/oai/skill-creator/scripts/quick_validate.py \
  plugins/everyday-streamer-creator-pack/skills/creator-copilot
python3 /root/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py \
  plugins/everyday-streamer-creator-pack
```

The final two commands use Codex's local authoring tools. Pull requests from environments without those tools must still pass the repository tests and CI; maintainers will run the Codex-specific validators before release.

## Pull requests

Explain:

- What creator problem changed
- Which baseline or forward case motivated the change
- What files were changed
- What validation ran
- Any remaining uncertainty or platform-freshness concern

Do not include private creator analytics, transcripts, credentials, or personal information in commits, issues, or pull requests.
