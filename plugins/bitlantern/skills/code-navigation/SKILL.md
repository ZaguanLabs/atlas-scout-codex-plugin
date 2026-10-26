---
name: bitlantern-code-navigation
description: Use Bit Lantern for local structural code navigation involving definitions, symbols, callers, references, dependency paths, architecture, traces, or edit impact. Use when asked where a symbol is defined, who calls or uses a function, what implements an interface, what breaks if code changes, or how a codebase is organized.
---

# Bit Lantern code navigation

Use Bit Lantern as the primary path for structural code navigation when its tools are available.
Check the MCP or deferred-tool catalog before assuming they are unavailable. Choose the matching
capability for the requested evidence:

- For a broad task or unfamiliar subsystem, call compact `fast_context` once for a source/test
  shortlist and exact ranges when exposed. If it is absent (for example in Free), begin with
  `symbol_search` using a short code concept, then `symbol_outline` on relevant returned files.
  For example, search `cache` to locate cache types and functions before reading their files.
  Outline accepts a source file, not a directory.
- `symbol_outline` lists declarations and exact ranges in a known file.
- `symbol_search` locates definitions and returns stable symbol ids.
- `symbol_references` returns indexed callers, references, and implementations.
- Graph, trace, path, architecture, and edit-impact tools return their corresponding bounded
  structural evidence.
- Omit `detail` and `limit` on initial discovery. Read useful cited ranges before another broad
  navigation call, and stop when the evidence is sufficient.

Text search remains useful for literals, regular expressions, generated or malformed code,
unsupported or partial language coverage, and focused completeness checks. Other development tools
remain appropriate for builds, tests, package managers, Git, servers, metrics, and runtime
diagnostics. Check Bit Lantern's coverage and trust metadata before treating an empty result as
exhaustive, and choose whichever available tool best fits the user's request.
