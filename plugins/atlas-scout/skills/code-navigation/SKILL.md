---
name: atlas-scout-code-navigation
description: Use Atlas Scout for local structural code navigation involving definitions, symbols, callers, references, dependency paths, architecture, traces, or edit impact. Use when asked where a symbol is defined, who calls or uses a function, what implements an interface, what breaks if code changes, or how a codebase is organized.
---

# Atlas Scout code navigation

Atlas Scout provides local, read-only structural-index evidence. Before relying on it, confirm that
the Atlas Scout MCP tools are available in the active session. If they are absent, explain that the
runtime and MCP connection need setup; never pretend that Scout produced a result.

Choose the narrowest matching Scout capability:

- If the file and range are already known, read that range directly.
- If a file is known but the relevant range is not, use `symbol_outline` before reading the file.
- If the location is unknown, use `symbol_search`, then `symbol_resolve` when exact metadata is
  needed.
- Use `symbol_references`, `symbol_graph`, `symbol_trace`, `symbol_path`, `symbol_architecture`, or
  `edit_impact` for the corresponding structural question.
- Read the exact source ranges returned by Atlas Scout before drawing conclusions or editing.

Use text search for literals, regular expressions, generated or malformed code, unsupported or
partial language coverage, an explicit user request, or after focused Atlas Scout queries miss.
Use builds, tests, package managers, Git, servers, metrics, and runtime diagnostics for their own
purposes. Check Scout's health, coverage, trust, and truncation metadata before treating an empty
or partial result as exhaustive.
