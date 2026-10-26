#!/usr/bin/env python3
"""Validate the Codex marketplace plugin and OpenAI skills-only archive."""

from __future__ import annotations

import json
import struct
import subprocess
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "bitlantern"
MANIFEST = PLUGIN / ".codex-plugin" / "plugin.json"
ARCHIVE = ROOT / "dist" / "bitlantern-openai-skills-1.0.0-preview.30.zip"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def png_dimensions(path: Path) -> tuple[int, int]:
    data = path.read_bytes()
    require(data.startswith(b"\x89PNG\r\n\x1a\n"), f"not a PNG: {path}")
    return struct.unpack(">II", data[16:24])


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    require(manifest["name"] == "bitlantern", "unexpected plugin name")
    require(manifest["version"] == "1.0.0-preview.30", "unexpected plugin version")
    require(manifest["mcpServers"] == "./.mcp.json", "missing MCP manifest reference")
    require(manifest["interface"]["category"] == "Developer Tools", "unexpected category")
    require(len(manifest["interface"]["shortDescription"]) <= 30, "short description is too long")
    require(len(manifest["interface"]["defaultPrompt"]) <= 3, "too many starter prompts")

    mcp = json.loads((PLUGIN / ".mcp.json").read_text(encoding="utf-8"))
    require(mcp["mcpServers"]["bitlantern"]["command"] == "bitlantern", "wrong MCP command")
    require(mcp["mcpServers"]["bitlantern"]["args"] == ["mcp"], "wrong MCP arguments")

    for relative in ("assets/icon.png", "assets/logo.png"):
        dimensions = png_dimensions(PLUGIN / relative)
        require(dimensions[0] == dimensions[1] >= 48, f"branding image is not a usable square: {relative}")

    skill_files = sorted((PLUGIN / "skills").glob("*/SKILL.md"))
    require(len(skill_files) == 2, "expected exactly two bundled skills")
    for skill in skill_files:
        contents = skill.read_text(encoding="utf-8")
        require(contents.startswith("---\n"), f"missing frontmatter: {skill}")
        require("\nname:" in contents and "\ndescription:" in contents, f"incomplete frontmatter: {skill}")
        require("[TODO:" not in contents, f"unfinished placeholder: {skill}")

    subprocess.run([sys.executable, str(ROOT / "scripts" / "build-skills-only.py")], check=True)
    with zipfile.ZipFile(ARCHIVE) as package:
        names = set(package.namelist())
        require(".codex-plugin/plugin.json" in names, "archive manifest is missing")
        require("skills/code-navigation/SKILL.md" in names, "navigation skill is missing")
        require("skills/setup/SKILL.md" in names, "setup skill is missing")
        require(not any(Path(name).name in {".mcp.json", ".app.json"} for name in names), "archive contains MCP or app configuration")
        uploaded_manifest = json.loads(package.read(".codex-plugin/plugin.json"))
        require("mcpServers" not in uploaded_manifest, "skills-only manifest references MCP")
        require("apps" not in uploaded_manifest, "skills-only manifest references an app")

    print("Bit Lantern Codex plugin validation passed")


if __name__ == "__main__":
    main()
