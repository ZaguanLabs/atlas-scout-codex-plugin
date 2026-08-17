# OpenAI Plugins Directory submission

This file is the reviewer-facing source of truth for Atlas Scout directory submissions.

## Publication status

- Status: **Preview 29 published**
- Last published: 2026-08-17
- Directory listing: <https://chatgpt.com/plugins/plugins_6a6e427dd300819196d41d5d1f24da50>
- Published version: `1.0.0-preview.29`
- Pending version: none
- Updated: 2026-08-17
- Prepared package SHA-256: `e96673f837ac41fd968916975f7c750f1ebe02cca3d2ded8431c37cface6d743`
- Local package validation: passed on 2026-08-17; five expected members, no MCP/app configuration
- Public GitHub marketplace validation: passed on 2026-08-17; an ephemeral Codex session loaded
  the Preview 29 skill, called `atlas-scout.symbol_search` once, and resolved the indexed probe to
  `src/lib.rs:1-3`
- Last published skill scans: `atlas-scout-code-navigation` passed; `atlas-scout-setup` passed
- Publisher identity shown by the directory: `Stig-Ørjan Smelror`
- Public developer brand used by the source package: `Zaguán Labs`

OpenAI approved the initial skills-only submission immediately after the publisher completed the
policy attestations. The publisher then published the approved version from the portal. The
Preview 26 skills-only package was uploaded and published through the same listing on 2026-08-03,
followed by Preview 27 on 2026-08-04. Preview 28 was uploaded, approved, and explicitly published
through the same listing on 2026-08-08. Preview 29 was uploaded, approved, and explicitly published
through that listing on 2026-08-17.

## Submission shape

- Shape: **Skills only**
- Package: `dist/atlas-scout-openai-skills-1.0.0-preview.29.zip`
- Reason: Atlas Scout is deliberately local and uses `stdio`. OpenAI's public **With MCP** flow
  requires a public production HTTPS MCP URL, which would change Atlas Scout's privacy and
  deployment architecture. The public skill guides safe setup and correct use of the local tool.
- Public source: <https://github.com/ZaguanLabs/atlas-scout-codex-plugin>

The GitHub marketplace package includes `.mcp.json` for Codex users. The portal ZIP intentionally
excludes `.mcp.json` and `mcpServers`, as required for skills-only uploads.

## Listing fields

- Plugin name: `atlas-scout`
- Version: `1.0.0-preview.29`
- Display name: `Atlas Scout`
- Short description: `Local structural code maps`
- Developer in source manifest: `Zaguán Labs`
- Verified publisher identity: `Stig-Ørjan Smelror`
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

Preview 29 quality and efficiency update for Atlas Scout for Codex. The navigation skill now starts
broad or unfamiliar work with one compact `fast_context` call, directs the agent to read the cited
exact ranges before further broad navigation, and adds an explicit stop condition once the evidence
is sufficient. It also keeps literal search, builds, tests, and focused completeness checks in their
proper roles and requires coverage and trust metadata before treating empty structural results as
exhaustive. This skills-only package continues to provide guarded setup guidance for the separately
installed local Atlas Scout runtime. It has no custom UI, external actions, authentication
requirement, or bundled remote MCP server. The update aligns the wrapper with the Preview 29 runtime
while preserving the published local-only architecture.
Reviewers may use Atlas Scout Free with any local source repository; test cases and expected results
are documented in `TESTING.md`.

## Review materials

- Five positive and three negative cases: [TESTING.md](TESTING.md)
- Wrapper license: [LICENSE](LICENSE)
- Product terms: <https://atlasscout.dev/legal/eula>
- Data practices: <https://atlasscout.dev/legal/privacy>
- Security contact: <support@atlasscout.dev>

Before submitting, confirm in the OpenAI Platform portal that the selected publisher identity is
Zaguán Labs and that the submitter has Apps Management write access.
