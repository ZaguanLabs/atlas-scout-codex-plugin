# OpenAI Plugins Directory submission

This file is the reviewer-facing source of truth for the initial Atlas Scout submission.

## Submission shape

- Shape: **Skills only**
- Package: `dist/atlas-scout-openai-skills-1.0.0-preview.25.zip`
- Reason: Atlas Scout is deliberately local and uses `stdio`. OpenAI's public **With MCP** flow
  requires a public production HTTPS MCP URL, which would change Atlas Scout's privacy and
  deployment architecture. The public skill guides safe setup and correct use of the local tool.
- Public source: <https://github.com/ZaguanLabs/atlas-scout-codex-plugin>

The GitHub marketplace package includes `.mcp.json` for Codex users. The portal ZIP intentionally
excludes `.mcp.json` and `mcpServers`, as required for skills-only uploads.

## Listing fields

- Plugin name: `atlas-scout`
- Version: `1.0.0-preview.25`
- Display name: `Atlas Scout`
- Short description: `Local structural code maps`
- Developer: `Zaguán Labs`
- Category: `Developer Tools`
- Website: <https://atlasscout.dev>
- Support: <https://atlasscout.dev/docs>
- Privacy policy: <https://atlasscout.dev/legal/privacy>
- Terms: <https://atlasscout.dev/legal/eula>
- Availability: Global, subject to OpenAI's supported countries and regions
- Authentication: None for Atlas Scout Free
- Screenshots: None; the plugin has no custom UI

### Long description

Atlas Scout gives Codex local structural-index evidence for definitions, exact source ranges,
references, static call paths, architecture, and bounded edit impact. It helps coding agents inspect
large repositories without repeatedly scanning unrelated files. Source code stays on the user's
workstation; the separately installed runtime creates a disposable SQLite index inside the selected
workspace. The bundled skills guide safe setup, choose the right structural query, require source
range verification, and preserve text search, builds, and tests for the cases they handle best.

## Starter prompts

1. `Find this symbol and show its exact source range.`
2. `Show callers and references for this function.`
3. `Estimate this change's impact and likely tests.`

## Release notes

Initial public submission of Atlas Scout for Codex. This skills-only package provides guarded setup
instructions and structural code-navigation guidance for the separately installed local Atlas Scout
runtime. It has no custom UI, external actions, authentication requirement, or bundled remote MCP
server. Reviewers may use Atlas Scout Free with any local source repository; test cases and expected
results are documented in `TESTING.md`.

## Review materials

- Five positive and three negative cases: [TESTING.md](TESTING.md)
- Wrapper license: [LICENSE](LICENSE)
- Product terms: <https://atlasscout.dev/legal/eula>
- Data practices: <https://atlasscout.dev/legal/privacy>
- Security contact: <support@atlasscout.dev>

Before submitting, confirm in the OpenAI Platform portal that the selected publisher identity is
Zaguán Labs and that the submitter has Apps Management write access.
