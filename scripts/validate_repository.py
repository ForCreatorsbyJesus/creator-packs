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
    plugins = marketplace.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        errors.append("marketplace plugins must be a non-empty list")
        plugins = []

    for index, entry in enumerate(plugins, start=1):
        if not isinstance(entry, dict):
            errors.append(f"marketplace plugin entry {index} must be an object")
            continue
        plugin_name = entry.get("name")
        if not isinstance(plugin_name, str) or not plugin_name.strip():
            errors.append(f"marketplace plugin entry {index} must include a non-empty name")
            continue
        source = entry.get("source")
        if not isinstance(source, dict):
            errors.append(f"marketplace plugin entry {index} must include a source object")
            continue
        source_value = source.get("path")
        if not isinstance(source_value, str) or not source_value.strip():
            errors.append(
                f"marketplace plugin entry {index} source must include a non-empty path"
            )
            continue
        source_path = source_value.removeprefix("./")
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
        skill_path = plugin_root / "skills/creator-copilot/SKILL.md"
        if not skill_path.exists():
            errors.append(f"{skill_path} does not exist")

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
