# Atlas Scout for Codex

Atlas Scout is a local, read-only MCP server that gives Codex indexed definitions, exact source
ranges, references, static call relationships, architecture summaries, and bounded edit impact for
source repositories.

This repository contains the inspectable Codex plugin wrapper. The separately installed Atlas
Scout runtime remains proprietary software under the Atlas Scout license. Installing the wrapper
does not download the runtime, run repository code, or send source code to Zaguán Labs.

## Requirements

- Codex with plugin support
- A supported Atlas Scout installation whose `atlas-scout` executable is on `PATH`
- A workstation permitted to run the Atlas Scout preview

Atlas Scout previews for macOS and Windows do not yet carry Apple or Microsoft publisher
signatures. Review the [installation and platform-safety documentation](https://atlasscout.dev/docs)
before installing the runtime. Do not weaken operating-system or organization security controls.

## Install

### OpenAI Plugins Directory

Atlas Scout is published in the universal Plugins Directory shared by ChatGPT and Codex:

<https://chatgpt.com/plugins/plugins_6a6e427dd300819196d41d5d1f24da50>

The directory entry installs the navigation and guarded setup skills. Atlas Scout remains a local
`stdio` MCP server, so users who want its structural tools must also install the runtime and the
MCP-enabled marketplace plugin below. This preserves local indexing instead of routing source code
through a hosted MCP service.

### Zaguán Labs Codex marketplace

Install and verify the Atlas Scout runtime first:

```bash
atlas-scout --version
atlas-scout doctor --workspace /absolute/path/to/project
```

Add the Zaguán Labs marketplace and install the plugin:

```bash
codex plugin marketplace add ZaguanLabs/atlas-scout-codex-plugin
codex plugin add atlas-scout@atlas-scout
```

Start a new Codex thread after installation. Remove or disable any duplicate manually registered
Atlas Scout MCP server so Codex starts only one copy. See [SETUP.md](SETUP.md) for troubleshooting
and removal instructions.

## What the plugin provides

- A local `stdio` MCP connection that runs `atlas-scout mcp`
- A code-navigation skill describing Scout's capabilities and coverage boundaries
- A guarded setup skill that never downloads or executes the runtime without explicit approval

The OpenAI directory package supplies the same navigation and setup skills but excludes `.mcp.json`
because its public **With MCP** flow requires a production HTTPS MCP URL. Users who want the local
server connection install this repository's plugin after installing the runtime.

## Example prompts

1. `Find the definition of reconcile_workspace and show me its exact source range.`
2. `Which functions call SymbolStore::replace_snapshot, and where are those calls?`
3. `Trace the static path from the MCP symbol_search handler to the SQLite query.`
4. `Summarize the indexed module architecture and the strongest cross-module dependencies.`
5. `Estimate the bounded edit impact of changing this public function and identify likely tests.`

Results are bounded by the languages and relationships present in the local index. Codex should
check returned health, coverage, trust, and truncation metadata before treating an empty result as
exhaustive.

## Data access

Atlas Scout reads source files in the workspace selected by Codex and writes a disposable SQLite
index beneath that workspace. It sends navigation results to Codex because that is the plugin's
requested function. Atlas Scout does not transmit source code, repository paths, symbols, queries,
tool calls, editor state, Git remotes, or index metrics to the Atlas Scout licensing service.

The runtime does not execute repository code, hooks, package scripts, builds, or tests. A Free
installation that has never been activated makes no licensing request. Previously activated
installations may perform asynchronous license refreshes as described in the
[privacy policy](https://atlasscout.dev/legal/privacy).

## Validate and build the directory package

The repository validates both the MCP-enabled Codex plugin and the skills-only archive in CI:

```bash
python3 scripts/check.py
```

The generated archive is written to `dist/atlas-scout-openai-skills-1.0.0-preview.25.zip`. Its
manifest intentionally omits `mcpServers`, and the archive contains no `.mcp.json` or `.app.json`.

## Support, privacy, and licensing

- Documentation: <https://atlasscout.dev/docs>
- Support and security reports: <support@atlasscout.dev>
- Privacy policy: <https://atlasscout.dev/legal/privacy>
- Atlas Scout EULA: <https://atlasscout.dev/legal/eula>

The Apache-2.0 license in this repository covers only the Codex plugin wrapper. The Atlas Scout
executable, product source, and other product materials remain governed by their separate EULA.
