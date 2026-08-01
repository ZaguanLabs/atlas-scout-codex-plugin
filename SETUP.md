# Setup and troubleshooting

## Install the runtime

Read <https://atlasscout.dev/docs> before installing Atlas Scout. If you approve the installation,
download the supported installer for inspection and run it only after review:

```bash
curl -fsSL https://atlasscout.dev/install.sh -o install.sh
less install.sh
bash install.sh
```

Verify the runtime in the workspace you intend to use:

```bash
atlas-scout --version
atlas-scout doctor --workspace /absolute/path/to/project
```

## Install the Codex plugin

```bash
codex plugin marketplace add ZaguanLabs/atlas-scout-codex-plugin
codex plugin add atlas-scout@atlas-scout
```

Start a new Codex thread. The plugin starts the server with `atlas-scout mcp` and uses the workspace
chosen by Codex.

## Troubleshooting

- If Codex reports that `atlas-scout` is missing, add the installer-reported executable directory
  to the environment that launches Codex, then start a new thread.
- Run `atlas-scout doctor --workspace /absolute/path/to/project` for runtime, index, daemon,
  language-coverage, and integration diagnostics.
- If Atlas Scout appears twice, remove or disable the older manual MCP registration and keep the
  plugin-provided server.
- Scout is intentionally not the right tool for every query. Use text search for literals and
  regexes, and builds or tests for runtime evidence.

## Remove the plugin

```bash
codex plugin remove atlas-scout
codex plugin marketplace remove atlas-scout
```

Removing the plugin does not delete the Atlas Scout runtime or disposable workspace indexes. Follow
the product documentation if you also want to remove those components.
