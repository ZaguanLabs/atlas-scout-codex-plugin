---
name: bitlantern-setup
description: Install, configure, verify, troubleshoot, or remove the Bit Lantern runtime and Codex integration when the user asks for Bit Lantern setup help.
---

# Set up Bit Lantern for Codex

Bit Lantern requires a separately installed `bitlantern` executable. Never download or execute a
binary, alter operating-system security controls, or change the user's Codex configuration without
their explicit approval.

1. Check whether `bitlantern` is already on `PATH` with `bitlantern --version`.
2. If it is absent, ask the user to review <https://atlasscout.dev/docs>, including the preview and
   platform-safety disclosures. The supported installer is <https://atlasscout.dev/install.sh>.
3. After approval, download the installer to a temporary file for inspection before running it.
4. Verify the runtime and workspace:

   ```bash
   bitlantern --version
   bitlantern doctor --workspace /absolute/path/to/project
   ```

5. When this plugin was installed from the Zaguán Labs Codex marketplace, its bundled `.mcp.json`
   starts `bitlantern mcp`. Start a new Codex thread and confirm the Bit Lantern tools are present.
6. If the server cannot start, check the executable path and run `bitlantern doctor`. If Bit Lantern
   was also registered manually, remove or disable the duplicate so only one server starts.

Installing or removing this open plugin wrapper does not install or remove the proprietary Bit Lantern runtime, and removing the runtime does not delete workspace indexes unless the product
documentation explicitly says so.
