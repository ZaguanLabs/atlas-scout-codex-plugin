# Reviewer test cases

These cases are written for OpenAI's Plugins Directory review. For navigation cases, install Atlas
Scout Free, register the local MCP server through this repository's plugin, and use any ordinary
source repository with a completed index. No account, private network, or proprietary fixture is
required.

## Positive cases

### 1. Find a definition

- Prompt: `Find the definition of the function that handles MCP symbol_search requests and show its exact source range.`
- Expected behavior: Use `symbol_search`, resolve ambiguity if necessary, and read the returned source range.
- Expected result: A file path, symbol identity, exact line range, and a source-grounded explanation.
- Fixture: Any indexed repository containing a named function; Atlas Scout itself may be used by an authorized reviewer.

### 2. Find callers and references

- Prompt: `Show every indexed caller and reference for this function, grouped by relationship.`
- Expected behavior: Resolve the selected symbol, call `symbol_references`, and report coverage or truncation limits.
- Expected result: Grouped callers/references with source locations and an explicit completeness caveat when needed.
- Fixture: An indexed repository with at least one called function.

### 3. Trace a static path

- Prompt: `Trace the static path from the request handler to the database query used for symbol search.`
- Expected behavior: Resolve both endpoints, use the path or trace capability, then inspect cited ranges.
- Expected result: An ordered structural path with symbol and file evidence, or a bounded no-path result.
- Fixture: An indexed repository with a multi-function call chain.

### 4. Summarize architecture

- Prompt: `Summarize the indexed module architecture and identify the strongest cross-module dependencies.`
- Expected behavior: Use Atlas Scout's architecture or graph evidence and state the index coverage boundary.
- Expected result: A concise module-level summary grounded in indexed dependency counts and cited code locations.
- Fixture: Any indexed multi-module repository.

### 5. Estimate edit impact

- Prompt: `Estimate the edit impact of changing this public function and identify the most likely tests to run.`
- Expected behavior: Resolve the symbol, use `edit_impact`, inspect returned references, and separate static evidence from recommendations.
- Expected result: A bounded affected-symbol/file list, likely tests, and caveats about runtime behavior not visible statically.
- Fixture: An indexed repository with source and test files.

## Negative cases

### 1. Literal or regular-expression search

- Prompt: `Find every occurrence matching the regular expression TODO\([A-Z]+-[0-9]+\).`
- Expected behavior: Use a text or regex search tool instead of Atlas Scout.
- Why: Atlas Scout is a structural symbol index, not the correct source of exhaustive literal or regex matches.

### 2. Runtime-only claim

- Prompt: `Prove this function never fails in production using only the Atlas Scout index.`
- Expected behavior: Explain that static navigation cannot prove runtime behavior and recommend tests, telemetry, or logs.
- Why: Claiming runtime certainty from a bounded structural index would be misleading.

### 3. Unapproved installation

- Scenario: Atlas Scout is not installed and the user asks only a code-navigation question.
- Expected behavior: State that Scout is unavailable and ask before downloading, executing, or changing Codex configuration; offer available local alternatives.
- Why: Installing software and changing configuration require explicit user approval.
