# Creator Packs Marketplace Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a public-ready `creator-packs` repository containing a valid Codex marketplace, an installable Everyday Streamer Creator Pack plugin, and the first usable `creator-copilot` skill.

**Architecture:** The repository is a marketplace root. `.agents/plugins/marketplace.json` catalogs independently installable creator-pack plugins; the first plugin is `everyday-streamer-creator-pack`, which contains one `creator-copilot` skill with internally routed specialist workflows. Repository validation is deterministic, while skill behavior is developed through baseline and forward-test scenarios.

**Tech Stack:** Markdown, JSON, Python 3.11+, pytest 8+, PyYAML 6+, jsonschema 4+, Codex plugin/skill manifests, GitHub Actions.

## Global Constraints

- Public repository name: `creator-packs`.
- Marketplace name: `creator-packs` with display name `Creator Packs`.
- Initial plugin name: `everyday-streamer-creator-pack`.
- Initial skill name: `creator-copilot`.
- Community-facing copy uses “AI creator support team,” “Creator Pack,” or “creator companion”; never “operating system,” “agent architecture,” or “workflow engine.”
- Deep platform scope is Twitch and YouTube; TikTok, Instagram Reels, and Discord are secondary destinations.
- V1 drafts assets but never uploads, schedules, publishes, authenticates, or operates creator accounts.
- Preserve creator identity; do not imitate named creators or infer private traits from public channels.
- Use test-first development for executable behavior and baseline-before-skill forward testing for skill behavior.
- Generated manifest/configuration files are validated immediately after scaffolding; all hand-written executable behavior follows RED–GREEN–REFACTOR.
- Stage only repository files belonging to Creator Packs.
- The current GitHub connection cannot create a repository and `gh` is unavailable; remote publication requires an empty public `creator-packs` repository URL from the user or an authenticated `gh` installation.

---

## Delivery decomposition

This plan implements the marketplace foundation and first usable skill. The approved design's larger deterministic analytics, recommendation-ranking, 24-profile evaluation, public-case holdouts, and consented pilot remain separate follow-on plans:

1. `creator-packs-marketplace-foundation` — this plan
2. `creator-copilot-deterministic-engines` — schemas, context merge, transcript/analytics normalization, ranking, and fixture suites
3. `creator-copilot-public-evaluation` — frozen GamingWithMeech, DebodBeezy, and non-gaming cases
4. `creator-copilot-external-pilot` — consented creator validation and behavioral proof

## Target file map

```text
creator-packs/
├── .agents/plugins/marketplace.json
├── .github/workflows/validate.yml
├── docs/
│   ├── design/2026-07-11-everyday-streamer-creator-pack-design.md
│   └── plans/2026-07-11-creator-packs-marketplace-foundation.md
├── plugins/everyday-streamer-creator-pack/
│   ├── .codex-plugin/plugin.json
│   └── skills/creator-copilot/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       ├── references/
│       │   ├── routing-and-context.md
│       │   ├── prepare-and-stream.md
│       │   ├── repurpose-and-publish.md
│       │   ├── review-and-improve.md
│       │   ├── insight-engine.md
│       │   └── safety-and-rights.md
│       └── assets/
│           ├── creator-profile.template.json
│           ├── tonight-stream-packet.template.md
│           └── context-capsule.template.md
├── evals/
│   ├── baseline/
│   ├── forward/
│   └── rubrics/creator-output-rubric.json
├── scripts/validate_repository.py
├── tests/test_repository_validation.py
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── SECURITY.md
└── pyproject.toml
```

### Ownership boundaries

- Marketplace and plugin manifests define discovery and installation only.
- `SKILL.md` owns routing, context precedence, core guardrails, and progressive-disclosure instructions.
- Workflow references own job-specific procedures and output contracts.
- Assets are creator-visible draft templates, not hidden memory.
- `scripts/validate_repository.py` owns deterministic repository and metadata checks; it does not score creative quality.
- `evals/` owns skill pressure scenarios and human scoring records; it does not ship inside the plugin.

---

### Task 1: Scaffold the repository marketplace and plugin

**Files:**
- Create: `.agents/plugins/marketplace.json`
- Create: `plugins/everyday-streamer-creator-pack/.codex-plugin/plugin.json`
- Create: `plugins/everyday-streamer-creator-pack/skills/`
- Create: `pyproject.toml`

**Interfaces:**
- Consumes: approved product-and-skill design specification.
- Produces: a marketplace entry whose `source.path` resolves to the plugin directory and a plugin manifest whose name matches its folder.

- [ ] **Step 1: Initialize the local repository**

```bash
git init -b main
git status -sb
```

Expected: a new repository on `main` containing only the existing approved design and implementation-plan documents as untracked files.

- [ ] **Step 2: Run the canonical repository-marketplace scaffold**

Run from the plugin-creator skill directory:

```bash
python3 scripts/create_basic_plugin.py everyday-streamer-creator-pack \
  --path /workspace/scratch/3c3299a79a51/creator-packs/plugins \
  --marketplace-path /workspace/scratch/3c3299a79a51/creator-packs/.agents/plugins/marketplace.json \
  --marketplace-name creator-packs \
  --with-skills \
  --with-marketplace
```

Expected: plugin directory, `.codex-plugin/plugin.json`, `skills/`, and marketplace JSON are created without placeholders.

- [ ] **Step 3: Normalize marketplace metadata**

Set `.agents/plugins/marketplace.json` to:

```json
{
  "name": "creator-packs",
  "interface": {
    "displayName": "Creator Packs"
  },
  "plugins": [
    {
      "name": "everyday-streamer-creator-pack",
      "source": {
        "source": "local",
        "path": "./plugins/everyday-streamer-creator-pack"
      },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Productivity"
    }
  ]
}
```

- [ ] **Step 4: Normalize plugin metadata**

Set `plugins/everyday-streamer-creator-pack/.codex-plugin/plugin.json` to the validated scaffold shape, preserving every scaffold-required field and enforcing:

```json
{
  "name": "everyday-streamer-creator-pack",
  "version": "0.1.0",
  "description": "An AI creator support team for planning stronger streams, creating more from every broadcast, and improving each week."
}
```

If the scaffold validator rejects `version` or `description`, retain only the validated fields emitted by the scaffold and place version/description in marketplace or repository metadata instead; do not invent unsupported manifest fields.

- [ ] **Step 5: Add the development package contract**

Create `pyproject.toml`:

```toml
[build-system]
requires = ["setuptools>=75"]
build-backend = "setuptools.build_meta"

[project]
name = "creator-packs-validation"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
  "jsonschema>=4.23,<5",
  "PyYAML>=6.0,<7"
]

[project.optional-dependencies]
dev = ["pytest>=8.3,<9"]

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-q"
```

- [ ] **Step 6: Validate the generated plugin**

Run:

```bash
python3 /root/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py \
  plugins/everyday-streamer-creator-pack
```

Expected: validation succeeds with exit code 0.

- [ ] **Step 7: Commit the scaffold**

```bash
git add .agents/plugins/marketplace.json \
  plugins/everyday-streamer-creator-pack/.codex-plugin/plugin.json \
  pyproject.toml
git commit -m "chore: scaffold creator packs marketplace"
```

---

### Task 2: Build repository validation with TDD

**Files:**
- Create: `tests/test_repository_validation.py`
- Create: `scripts/validate_repository.py`

**Interfaces:**
- Consumes: repository root path.
- Produces: `ValidationResult(errors: tuple[str, ...])`, `validate_repository(root: Path)`, and a CLI exit code of 0 for valid or 1 for invalid.

- [ ] **Step 1: Write failing marketplace-layout tests**

Create `tests/test_repository_validation.py`:

```python
import json
from pathlib import Path

from scripts.validate_repository import validate_repository


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value), encoding="utf-8")


def valid_marketplace() -> dict:
    return {
        "name": "creator-packs",
        "interface": {"displayName": "Creator Packs"},
        "plugins": [{
            "name": "everyday-streamer-creator-pack",
            "source": {
                "source": "local",
                "path": "./plugins/everyday-streamer-creator-pack",
            },
            "policy": {
                "installation": "AVAILABLE",
                "authentication": "ON_INSTALL",
            },
            "category": "Productivity",
        }],
    }


def test_valid_marketplace_and_plugin_pass(tmp_path: Path) -> None:
    write_json(tmp_path / ".agents/plugins/marketplace.json", valid_marketplace())
    write_json(
        tmp_path / "plugins/everyday-streamer-creator-pack/.codex-plugin/plugin.json",
        {"name": "everyday-streamer-creator-pack"},
    )
    skill = tmp_path / "plugins/everyday-streamer-creator-pack/skills/creator-copilot/SKILL.md"
    skill.parent.mkdir(parents=True)
    skill.write_text(
        "---\nname: creator-copilot\n"
        "description: Use when a livestream creator needs planning, repurposing, or review support.\n"
        "---\n\n# Creator Copilot\n",
        encoding="utf-8",
    )

    result = validate_repository(tmp_path)

    assert result.errors == ()


def test_missing_plugin_path_fails(tmp_path: Path) -> None:
    write_json(tmp_path / ".agents/plugins/marketplace.json", valid_marketplace())

    result = validate_repository(tmp_path)

    assert any("does not exist" in error for error in result.errors)


def test_manifest_name_must_match_folder(tmp_path: Path) -> None:
    write_json(tmp_path / ".agents/plugins/marketplace.json", valid_marketplace())
    write_json(
        tmp_path / "plugins/everyday-streamer-creator-pack/.codex-plugin/plugin.json",
        {"name": "wrong-name"},
    )

    result = validate_repository(tmp_path)

    assert any("must match folder" in error for error in result.errors)


def test_community_copy_rejects_operating_system(tmp_path: Path) -> None:
    write_json(tmp_path / ".agents/plugins/marketplace.json", valid_marketplace())
    write_json(
        tmp_path / "plugins/everyday-streamer-creator-pack/.codex-plugin/plugin.json",
        {"name": "everyday-streamer-creator-pack"},
    )
    readme = tmp_path / "README.md"
    readme.write_text("An AI creator operating system.", encoding="utf-8")

    result = validate_repository(tmp_path)

    assert any("community-facing banned term" in error for error in result.errors)
```

- [ ] **Step 2: Run the tests and verify RED**

Run:

```bash
python3 -m pytest tests/test_repository_validation.py -q
```

Expected: collection fails because `scripts.validate_repository` does not exist.

- [ ] **Step 3: Implement the minimal validator**

Create `scripts/validate_repository.py`:

```python
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ValidationResult:
    errors: tuple[str, ...]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_repository(root: Path) -> ValidationResult:
    errors: list[str] = []
    marketplace_path = root / ".agents/plugins/marketplace.json"
    if not marketplace_path.exists():
        return ValidationResult((f"{marketplace_path} does not exist",))

    marketplace = load_json(marketplace_path)
    for entry in marketplace.get("plugins", []):
        plugin_name = entry["name"]
        source_path = entry["source"]["path"].removeprefix("./")
        plugin_root = root / source_path
        if not plugin_root.exists():
            errors.append(f"plugin path {source_path} does not exist")
            continue
        manifest_path = plugin_root / ".codex-plugin/plugin.json"
        if not manifest_path.exists():
            errors.append(f"{manifest_path} does not exist")
            continue
        manifest = load_json(manifest_path)
        if manifest.get("name") != plugin_root.name or plugin_name != plugin_root.name:
            errors.append(f"plugin name must match folder {plugin_root.name}")

    banned = "operating system"
    for path in (root / "README.md",):
        if path.exists() and banned in path.read_text(encoding="utf-8").lower():
            errors.append(f"community-facing banned term found in {path.name}")

    return ValidationResult(tuple(errors))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", type=Path, default=Path.cwd())
    args = parser.parse_args()
    result = validate_repository(args.root.resolve())
    for error in result.errors:
        print(error)
    return 1 if result.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run the tests and verify GREEN**

Run:

```bash
python3 -m pytest tests/test_repository_validation.py -q
```

Expected: `4 passed`.

- [ ] **Step 5: Run the validator against the repository**

```bash
python3 scripts/validate_repository.py .
```

Expected at this point: failure identifying the missing `creator-copilot/SKILL.md`. This is the next task's required RED state.

- [ ] **Step 6: Commit the validator**

```bash
git add scripts/validate_repository.py tests/test_repository_validation.py
git commit -m "test: validate creator packs repository layout"
```

---

### Task 3: Establish baseline skill failures before authoring

**Files:**
- Create: `evals/baseline/go-live-soon.md`
- Create: `evals/baseline/repurpose-vod.md`
- Create: `evals/baseline/review-underperformance.md`
- Create: `evals/rubrics/creator-output-rubric.json`

**Interfaces:**
- Consumes: raw user requests without the new skill.
- Produces: baseline outputs and scored failure notes demonstrating what the skill must teach.

- [ ] **Step 1: Create the human rubric**

Create `evals/rubrics/creator-output-rubric.json`:

```json
{
  "scale": {"minimum": 1, "maximum": 5},
  "dimensions": [
    "creator_fit",
    "platform_fit",
    "actionability",
    "prioritization",
    "evidence_transparency",
    "workload_realism",
    "voice_preservation",
    "artifact_usefulness",
    "uncertainty_calibration"
  ],
  "release_target": {
    "average_minimum": 4.0,
    "dimension_floor": 3.5
  }
}
```

- [ ] **Step 2: Run three baseline pressure scenarios using fresh subagents**

Use these exact prompts without giving the design specification or intended answers:

```text
Scenario A: I am a solo gaming streamer with 90 minutes before I go live on Twitch. I have three hours total tonight and no editor. Help me make the stream useful for YouTube too.

Scenario B: Turn this timestamped livestream transcript into content for YouTube and Shorts. I can spend 60 minutes editing and only want the two best opportunities. [Attach a small synthetic transcript fixture.]

Scenario C: My last YouTube Live had more views but fewer returning viewers. I changed the title, streamed an hour later, and played a different game. Tell me why it happened and what to change next.
```

Expected baseline failure signals:

- Generic creator advice not tied to time, platform role, or creator maturity
- Too many options without one default recommendation
- Missing stream packet or ranked artifact contract
- Causal claims despite confounders
- No explicit next experiment or success signal
- No context capsule for the next interaction

- [ ] **Step 3: Save baseline evidence**

For each scenario, create a Markdown file containing:

```markdown
# Baseline: <scenario name>

## Prompt
<exact prompt>

## Raw output
<unaltered subagent output>

## Rubric scores
<one score and one-sentence evidence per rubric dimension>

## Observed failure modes
<only failure modes evidenced by the raw output>
```

- [ ] **Step 4: Commit the baseline suite**

```bash
git add evals/baseline evals/rubrics/creator-output-rubric.json
git commit -m "test: capture creator copilot baselines"
```

---

### Task 4: Author the first installable Creator Copilot skill

**Files:**
- Create: `plugins/everyday-streamer-creator-pack/skills/creator-copilot/SKILL.md`
- Create: `plugins/everyday-streamer-creator-pack/skills/creator-copilot/agents/openai.yaml`
- Create: six files under `plugins/everyday-streamer-creator-pack/skills/creator-copilot/references/`
- Create: three files under `plugins/everyday-streamer-creator-pack/skills/creator-copilot/assets/`

**Interfaces:**
- Consumes: user request, optional CreatorProfile, content artifacts, and the appropriate reference file.
- Produces: one routed creator artifact, a prioritized next action, and a context capsule.

- [ ] **Step 1: Write `SKILL.md` with the exact trigger contract**

Use this frontmatter:

```yaml
---
name: creator-copilot
description: Use when a livestream creator needs help planning a Twitch or YouTube stream, turning a broadcast or transcript into content, reviewing creator analytics, choosing what to do next, or adapting advice from successful creators to their own channel and constraints.
---
```

The body must remain under 500 lines and contain, in imperative form:

1. Identify the job: `go_live_soon`, `plan_week`, `repurpose`, `review`, `next_action`, or `creator_insights`.
2. Read only the matching reference file plus `safety-and-rights.md` when needed.
3. Apply context precedence: explicit request → current project → confirmed creator profile → labeled assumptions.
4. Ask only for missing information that materially changes the artifact.
5. Recommend one default action before alternatives.
6. Preserve the creator's time budget, voice, goal, safety, and platform roles.
7. Label evidence as official guidance, creator experience, public observation, community report, creator experiment, or hypothesis.
8. Never promise outcomes, infer private traits, imitate named creators, or publish.
9. End meaningful work with a context capsule and one next action.

- [ ] **Step 2: Create the workflow references**

Each reference must define inputs, procedure, output contract, graceful-degradation behavior, and one concise example:

- `routing-and-context.md`: job mapping, compound-route ordering, field provenance, and context capsule.
- `prepare-and-stream.md`: Tonight's Stream Packet and rapid 90-minute mode.
- `repurpose-and-publish.md`: timestamp normalization expectations, two-best-opportunities mode, platform-native transformations, and abstention when no clip is strong.
- `review-and-improve.md`: observation/hypothesis/result separation, aligned baselines, confounders, keep/change/stop, and one experiment.
- `insight-engine.md`: source hierarchy, relevance filter, Do Now/Test Next/Watch/Ignore, freshness, and confidence limits.
- `safety-and-rights.md`: privacy, disclosure, copyright-risk screening, creator well-being, and no-clearance language.

- [ ] **Step 3: Create the creator profile template**

Create `assets/creator-profile.template.json`:

```json
{
  "schema_version": "0.1.0",
  "creator_id": "creator-local-id",
  "niches": [],
  "audience_promise": null,
  "primary_platform": null,
  "secondary_platforms": [],
  "primary_objective": null,
  "weekly_creator_hours": null,
  "stream_cadence": null,
  "team_size": 1,
  "voice_preferences": [],
  "guardrails": [],
  "provenance": {}
}
```

- [ ] **Step 4: Create the Tonight's Stream Packet template**

Create `assets/tonight-stream-packet.template.md` with these required headings:

```markdown
# Tonight's Stream Packet

## Recommended concept
## Title and thumbnail direction
## Opening hook
## Timed run of show
## Audience prompts and CTA
## Technical and moderation preflight
## Fallback plan
## Planned clip moments
## Active experiment and success signal
## Post-stream capture
```

- [ ] **Step 5: Create the context capsule template**

Create `assets/context-capsule.template.md`:

```markdown
# Creator Context Capsule

## Current objective
## Confirmed constraints
## Decisions made
## Active experiment
## Assets created
## Open questions
## Recommended next action
```

- [ ] **Step 6: Generate skill UI metadata**

Run from `/root/.codex/skills/oai/skill-creator`:

```bash
python3 scripts/generate_openai_yaml.py \
  /workspace/scratch/3c3299a79a51/creator-packs/plugins/everyday-streamer-creator-pack/skills/creator-copilot \
  --interface display_name="Creator Copilot" \
  --interface short_description="Plan stronger streams and create more from every broadcast." \
  --interface default_prompt="Help me choose the most useful next action for my Twitch or YouTube creator work."
```

- [ ] **Step 7: Validate the skill and repository**

Run:

```bash
python3 /root/.codex/skills/oai/skill-creator/scripts/quick_validate.py \
  plugins/everyday-streamer-creator-pack/skills/creator-copilot
python3 /root/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py \
  plugins/everyday-streamer-creator-pack
python3 scripts/validate_repository.py .
```

Expected: all three commands exit 0.

- [ ] **Step 8: Commit the first skill**

```bash
git add plugins/everyday-streamer-creator-pack/skills/creator-copilot
git commit -m "feat: add creator copilot skill"
```

---

### Task 5: Forward-test and refine Creator Copilot

**Files:**
- Create: `evals/forward/go-live-soon.md`
- Create: `evals/forward/repurpose-vod.md`
- Create: `evals/forward/review-underperformance.md`
- Modify: skill/reference files only when a forward test exposes a demonstrated failure.

**Interfaces:**
- Consumes: the same raw scenarios used for baseline plus the installed skill path.
- Produces: directly comparable forward outputs and a documented RED–GREEN skill cycle.

- [ ] **Step 1: Run fresh forward-test agents**

Dispatch each scenario in a fresh context using this form:

```text
Use @creator-copilot at /workspace/scratch/3c3299a79a51/creator-packs/plugins/everyday-streamer-creator-pack/skills/creator-copilot to solve this request:

<exact baseline scenario prompt and the same fixture>
```

Do not include baseline outputs, expected answers, diagnoses, or prior conclusions.

- [ ] **Step 2: Score and compare**

Use the same rubric. Require:

- Average score ≥4.0
- No dimension below 3.5
- Correct workflow route in all three cases
- One prioritized default action in all three cases
- Explicit confounders and no causal overclaim in Scenario C
- Context capsule in all three cases

- [ ] **Step 3: Refine only evidenced failures**

For each failed requirement:

1. Record the raw failure.
2. Add the minimum imperative instruction or example to the matching reference.
3. Rerun only that scenario with a fresh agent.
4. Confirm the original passing scenarios remain materially compliant.

- [ ] **Step 4: Save forward results and commit**

```bash
git add evals/forward plugins/everyday-streamer-creator-pack/skills/creator-copilot
git commit -m "test: forward validate creator copilot"
```

---

### Task 6: Add public repository documentation

**Files:**
- Create: `README.md`
- Create: `CONTRIBUTING.md`
- Create: `SECURITY.md`
- Create: `LICENSE`
- Copy: approved design and this plan into `docs/design/` and `docs/plans/`.

**Interfaces:**
- Consumes: actual repository structure and validated install commands.
- Produces: community-facing discovery, installation, contribution, and security guidance.

- [ ] **Step 1: Write the README**

Required sections:

```markdown
# Creator Packs

Practical AI support teams for everyday creators.

## Available packs
## Everyday Streamer Creator Pack
## What it helps with
## Install from this marketplace
## Example requests
## How recommendations use evidence
## Privacy and creator control
## Contributing
## License
```

The first screen must explain outcomes, not schemas or agents. Include the six community entry points and a sample Tonight's Stream Packet excerpt. Document the exact marketplace-add/install commands verified in Task 8; do not publish guessed CLI syntax.

- [ ] **Step 2: Write CONTRIBUTING.md**

Require contributors to:

- Propose a creator job and concrete examples before adding a pack
- Add baseline and forward scenarios
- Keep community copy nontechnical
- Use official sources for volatile platform facts
- Avoid imitation, unsupported public inference, and guaranteed-growth claims
- Run repository, plugin, and skill validation

- [ ] **Step 3: Write SECURITY.md**

Cover private analytics, transcripts, accidental personal information, untrusted URLs/files, prompt injection in retrieved creator content, and responsible reporting. State that public issues must not contain private creator data.

- [ ] **Step 4: Add the MIT license**

Create `LICENSE` using the standard MIT text with copyright year 2026 and the repository owner name confirmed before publication.

- [ ] **Step 5: Copy approved project documentation**

```bash
mkdir -p docs/design docs/plans
cp docs/superpowers/specs/2026-07-11-everyday-streamer-creator-pack-design.md \
  docs/design/2026-07-11-everyday-streamer-creator-pack-design.md
cp docs/superpowers/plans/2026-07-11-creator-packs-marketplace-foundation.md \
  docs/plans/2026-07-11-creator-packs-marketplace-foundation.md
```

- [ ] **Step 6: Validate community language and commit**

```bash
python3 scripts/validate_repository.py .
git add README.md CONTRIBUTING.md SECURITY.md LICENSE docs/design docs/plans
git commit -m "docs: explain creator packs marketplace"
```

Expected: validator exits 0 and README contains no banned community-facing terms.

---

### Task 7: Add continuous validation

**Files:**
- Create: `.github/workflows/validate.yml`

**Interfaces:**
- Consumes: repository contents and Python development dependencies.
- Produces: a required validation workflow for pushes and pull requests.

- [ ] **Step 1: Create the GitHub Actions workflow**

Create `.github/workflows/validate.yml`:

```yaml
name: Validate Creator Packs

on:
  push:
  pull_request:

permissions:
  contents: read

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
          cache: pip
      - run: python -m pip install --upgrade pip
      - run: python -m pip install -e '.[dev]'
      - run: python -m pytest
      - run: python scripts/validate_repository.py .
```

- [ ] **Step 2: Run all locally available checks**

```bash
python3 -m pytest
python3 scripts/validate_repository.py .
python3 /root/.codex/skills/oai/skill-creator/scripts/quick_validate.py \
  plugins/everyday-streamer-creator-pack/skills/creator-copilot
python3 /root/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py \
  plugins/everyday-streamer-creator-pack
```

Expected: every command exits 0 with no warnings attributable to repository files.

- [ ] **Step 3: Commit CI**

```bash
git add .github/workflows/validate.yml
git commit -m "ci: validate creator packs"
```

---

### Task 8: Verify marketplace installation locally

**Files:**
- Modify: `README.md` only if verified commands differ from the draft.

**Interfaces:**
- Consumes: completed marketplace and plugin.
- Produces: verified installation and sharing instructions.

- [ ] **Step 1: Validate exact CLI syntax in the installed runtime**

Run:

```bash
codex plugin marketplace --help
codex plugin --help
```

Expected: help output identifies the supported marketplace-add and plugin-install commands. Record the exact commands; do not infer them.

- [ ] **Step 2: Add the repository marketplace locally**

Run the exact marketplace-add command returned by help against:

```text
/workspace/scratch/3c3299a79a51/creator-packs
```

Expected: marketplace `creator-packs` is discoverable.

- [ ] **Step 3: Install the Everyday Streamer Creator Pack**

Run the exact install command returned by help for:

```text
everyday-streamer-creator-pack@creator-packs
```

Expected: plugin installs and exposes `creator-copilot`.

- [ ] **Step 4: Run one smoke request in a fresh thread**

```text
Use @creator-copilot. I go live on Twitch in 90 minutes, have no editor, and want the stream to create one useful YouTube Short. Give me the most useful packet you can.
```

Expected: Tonight's Stream Packet, one prioritized concept, one active experiment, and a context capsule; no publishing action.

- [ ] **Step 5: Replace README install commands with verified syntax and commit**

```bash
git add README.md
git commit -m "docs: verify marketplace installation"
```

---

### Task 9: Initialize Git, create the public remote, and publish

**Files:**
- Create: `.gitignore`
- Modify: `LICENSE` owner only if not already confirmed.

**Interfaces:**
- Consumes: a validated local repository and an empty public GitHub repository named `creator-packs`.
- Produces: a public default branch with all marketplace files and no private evaluation data.

- [ ] **Step 1: Add repository ignore rules**

Create `.gitignore`:

```gitignore
__pycache__/
*.py[cod]
.pytest_cache/
.venv/
dist/
build/
*.egg-info/
.DS_Store
private-evals/
creator-data/
```

- [ ] **Step 2: Inspect publication scope**

```bash
git status -sb
git diff --stat
git ls-files
```

Expected: only Creator Packs repository files; no private creator data, credentials, unrelated files, or temporary evaluation output.

- [ ] **Step 3: Create or connect the public GitHub repository**

Preferred when authenticated `gh` is available:

```bash
gh repo create creator-packs --public --source=. --remote=origin --description \
  "Practical AI support teams for everyday creators." 
```

Current-environment fallback: the user creates an empty public repository named `creator-packs` and provides its HTTPS URL. Then run:

```bash
git remote add origin "$CREATOR_PACKS_REMOTE_URL"
```

Expected: `git remote -v` shows only the intended public repository.

- [ ] **Step 4: Run the final verification suite**

```bash
python3 -m pytest
python3 scripts/validate_repository.py .
python3 /root/.codex/skills/oai/skill-creator/scripts/quick_validate.py \
  plugins/everyday-streamer-creator-pack/skills/creator-copilot
python3 /root/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py \
  plugins/everyday-streamer-creator-pack
```

Expected: all checks pass.

- [ ] **Step 5: Commit any final publication metadata**

```bash
git add .gitignore LICENSE README.md
git commit -m "chore: prepare public creator packs repository"
```

If there is nothing new to commit, do not create an empty commit.

- [ ] **Step 6: Push the default branch**

```bash
git branch -M main
git push -u origin main
```

Expected: public `main` branch is available on GitHub.

- [ ] **Step 7: Verify public contents**

Inspect the repository through the GitHub connection and confirm:

- Marketplace JSON is visible
- Plugin and skill files are visible
- README installation steps render correctly
- GitHub Actions validation runs
- No private creator or evaluation data was published

---

## Plan self-review checklist

- Every file in the foundation target map is created by a task.
- Skill behavior receives baseline tests before `SKILL.md` is authored.
- Executable validator behavior follows RED–GREEN–REFACTOR.
- Marketplace, plugin, and skill validation commands are explicit.
- The first release is useful without direct platform integration.
- GitHub publication has a documented current-environment fallback.
- Public-case evaluation and private pilot are deliberately separated from the foundation build.
- No task promises autonomous publishing, guaranteed growth, or private inference.
