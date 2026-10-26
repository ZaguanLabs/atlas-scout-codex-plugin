# Bit Lantern Preview 30 Codex acceptance

Verified on 2026-10-26 with Codex CLI/app-server 0.164.0 against the public
`1.0.0-preview.30` Linux x86-64 runtime. Native executable SHA-256:
`9931347ef4a2d0215e701bd5245a28b0e32a3fb12928a9cb86682e1c1c780dee`.

The local marketplace plugin loaded both `bitlantern-code-navigation` and
`bitlantern-setup` skills in a fresh ephemeral thread. The server reported Preview 30 and
six unactivated Free tools. Direct host calls found a fixture definition at `src/cache.rs:6-8`
and its three callers. One bounded model turn completed successfully in 24.202 seconds,
used `symbol_search`, `symbol_references`, and `symbol_schema`, read the returned source,
and explained the function from that source. It also stated the setup approval requirement;
no installation or configuration change was requested or performed by that turn.

The workstation already had a manually registered MCP connection named `bitlantern` pointing
to an earlier development runtime. It shadowed the plugin connection in initial checks.
The successful test used a disposable local marketplace copy with the exact released executable,
a clean unactivated state, and a test-only connection alias. Per-thread overrides disabled
other connections for that test; the user's global registrations were preserved. The published
plugin keeps the standard `bitlantern` command. Users should remove or disable duplicate manual
registrations as described in [SETUP.md](SETUP.md).

The skills-only portal ZIP is frozen at
`dist/bitlantern-openai-skills-1.0.0-preview.30.zip`, SHA-256
`2ff3cc12423aebcb4aaccc20e6325a5ee4c840a996ca7f70232778754c0d35ca`.
It contains exactly the manifest, two skills, and two square PNG assets, with no MCP or app
configuration. This live test covers the GitHub plugin; it does not establish portal scanning,
submission, approval, or publication. Those steps remain pending because the signed-in
publication browser was unavailable. The existing listing's last observed publication remains
Atlas Scout Preview 29; see [OPENAI_SUBMISSION.md](OPENAI_SUBMISSION.md).
