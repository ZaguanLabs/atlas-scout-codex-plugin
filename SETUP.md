# Setup and troubleshooting

## Install the runtime

Read <https://atlasscout.dev/docs> before installing Bit Lantern. If you approve the installation,
download the supported installer for inspection and run it only after review:

```bash
curl -fsSL https://atlasscout.dev/install.sh -o install.sh
less install.sh
bash install.sh
```

Verify the runtime in the workspace you intend to use:

```bash
bitlantern --version
bitlantern doctor --workspace /absolute/path/to/project
```

## Install the Codex plugin

```bash
codex plugin marketplace add ZaguanLabs/atlas-scout-codex-plugin
codex plugin add bitlantern@bitlantern
```

Start a new Codex thread. The plugin starts the server with `bitlantern mcp` and uses the workspace
chosen by Codex.

## Troubleshooting

- If Codex reports that `bitlantern` is missing, add the installer-reported executable directory
  to the environment that launches Codex, then start a new thread.
- Run `bitlantern doctor --workspace /absolute/path/to/project` for runtime, index, daemon,
  language-coverage, and integration diagnostics.
- If Bit Lantern appears twice, remove or disable the older manual MCP registration and keep the
  plugin-provided server.
- Scout is intentionally not the right tool for every query. Use text search for literals and
  regexes, and builds or tests for runtime evidence.

## Remove the plugin

```bash
codex plugin remove bitlantern
codex plugin marketplace remove bitlantern
```

Removing the plugin does not delete the Bit Lantern runtime or disposable workspace indexes. Follow
the product documentation if you also want to remove those components.
