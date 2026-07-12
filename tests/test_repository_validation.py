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


def test_missing_creator_copilot_skill_fails(tmp_path: Path) -> None:
    write_json(tmp_path / ".agents/plugins/marketplace.json", valid_marketplace())
    write_json(
        tmp_path / "plugins/everyday-streamer-creator-pack/.codex-plugin/plugin.json",
        {"name": "everyday-streamer-creator-pack"},
    )

    result = validate_repository(tmp_path)

    assert any("creator-copilot/SKILL.md does not exist" in error for error in result.errors)


def test_missing_marketplace_plugins_fails(tmp_path: Path) -> None:
    marketplace = valid_marketplace()
    del marketplace["plugins"]
    write_json(tmp_path / ".agents/plugins/marketplace.json", marketplace)

    result = validate_repository(tmp_path)

    assert any("plugins must be a non-empty list" in error for error in result.errors)


def test_empty_marketplace_plugins_fails(tmp_path: Path) -> None:
    marketplace = valid_marketplace()
    marketplace["plugins"] = []
    write_json(tmp_path / ".agents/plugins/marketplace.json", marketplace)

    result = validate_repository(tmp_path)

    assert any("plugins must be a non-empty list" in error for error in result.errors)


def test_malformed_plugin_entries_accumulate_errors(tmp_path: Path) -> None:
    marketplace = valid_marketplace()
    marketplace["plugins"] = [
        "not-an-object",
        {},
        {"name": "missing-source"},
        {"name": "missing-path", "source": {}},
    ]
    write_json(tmp_path / ".agents/plugins/marketplace.json", marketplace)

    result = validate_repository(tmp_path)

    assert result.errors == (
        "marketplace plugin entry 1 must be an object",
        "marketplace plugin entry 2 must include a non-empty name",
        "marketplace plugin entry 3 must include a source object",
        "marketplace plugin entry 4 source must include a non-empty path",
    )


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
