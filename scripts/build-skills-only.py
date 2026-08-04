#!/usr/bin/env python3
"""Build the skills-only archive accepted by the OpenAI Plugins Directory."""

from __future__ import annotations

import json
import shutil
import tempfile
import zipfile
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
PLUGIN_ROOT = REPOSITORY_ROOT / "plugins" / "atlas-scout"
OUTPUT_DIR = REPOSITORY_ROOT / "dist"
ARCHIVE = OUTPUT_DIR / "atlas-scout-openai-skills-1.0.0-preview.27.zip"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="atlas-scout-openai-") as temporary:
        stage = Path(temporary)
        shutil.copytree(PLUGIN_ROOT / "skills", stage / "skills")
        (stage / "assets").mkdir()
        shutil.copy2(PLUGIN_ROOT / "assets" / "icon.png", stage / "assets" / "icon.png")
        shutil.copy2(PLUGIN_ROOT / "assets" / "logo.png", stage / "assets" / "logo.png")

        manifest = json.loads(
            (PLUGIN_ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8")
        )
        manifest.pop("mcpServers", None)
        manifest_dir = stage / ".codex-plugin"
        manifest_dir.mkdir()
        (manifest_dir / "plugin.json").write_text(
            json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

        forbidden = {".mcp.json", ".app.json"}
        if any(path.name in forbidden for path in stage.rglob("*")):
            raise SystemExit("skills-only stage contains an MCP or app configuration")
        if "mcpServers" in manifest or "apps" in manifest:
            raise SystemExit("skills-only manifest contains an MCP or app reference")

        with zipfile.ZipFile(ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for path in sorted(stage.rglob("*")):
                if path.is_file():
                    archive.write(path, path.relative_to(stage).as_posix())

    print(ARCHIVE)


if __name__ == "__main__":
    main()
