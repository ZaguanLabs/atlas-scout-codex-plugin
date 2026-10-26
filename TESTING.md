# Reviewer test cases

These cases are written for OpenAI's Plugins Directory review. For navigation cases, install Bit Lantern Free, register the local MCP server through this repository's plugin, and use any ordinary
source repository with a completed index. No account, private network, or proprietary fixture is
required.

## Positive cases

### 1. Find a definition

- Prompt: `Find the definition of the function that handles MCP symbol_search requests and show its exact source range.`
- Expected behavior: Use `symbol_search`, resolve ambiguity if necessary, and read the returned source range.
- Expected result: A file path, symbol identity, exact line range, and a source-grounded explanation.
- Fixture: Any indexed repository containing a named function; Bit Lantern itself may be used by an authorized reviewer.

### 2. Find callers and references

- Prompt: `Show every indexed caller and reference for this function, grouped by relationship.`
- Expected behavior: Resolve the selected symbol, call `symbol_references`, and report coverage or truncation limits.
- Expected result: Grouped callers/references with source locations and an explicit completeness caveat when needed.
- Fixture: An indexed repository with at least one called function.

### 3. Outline a known file

- Prompt: `List the top-level declarations in this source file and show their exact ranges.`
- Expected behavior: Use `symbol_outline` on the known file and read relevant ranges.
- Expected result: Source-ordered declarations, with a continuation cursor when truncated.
- Fixture: An indexed source file with multiple declarations.

### 4. Inspect coverage

- Prompt: `Check whether this directory is indexed and explain its coverage gaps.`
- Expected behavior: Use scoped `symbol_schema` and state reported health and language limits.
- Expected result: Coverage and freshness evidence with no unsupported completeness claim.
- Fixture: An indexed repository with a supported source file and a partial-coverage file.

### 5. Resolve a selected symbol

- Prompt: `Show the full metadata for this symbol and inspect its definition.`
- Expected behavior: Copy the stable identifier from search or outline into `symbol_resolve`, then read the returned source range.
- Expected result: The exact selected symbol and a source-grounded explanation.
- Fixture: An indexed repository with at least one named function.

Trace, architecture, and impact scenarios require those tools to be exposed by the connected edition.
Do not ask a Free reviewer to invoke unavailable tools or treat their absence as a product failure.

## Negative cases

### 1. Literal or regular-expression search

- Prompt: `Find every occurrence matching the regular expression TODO\([A-Z]+-[0-9]+\).`
- Expected behavior: Use a text or regex search tool instead of Bit Lantern.
- Why: Bit Lantern is a structural symbol index, not the correct source of exhaustive literal or regex matches.

### 2. Runtime-only claim

- Prompt: `Prove this function never fails in production using only the Bit Lantern index.`
- Expected behavior: Explain that static navigation cannot prove runtime behavior and recommend tests, telemetry, or logs.
- Why: Claiming runtime certainty from a bounded structural index would be misleading.

### 3. Unapproved installation

- Scenario: Bit Lantern is not installed and the user asks only a code-navigation question.
- Expected behavior: State that Scout is unavailable and ask before downloading, executing, or changing Codex configuration; offer available local alternatives.
- Why: Installing software and changing configuration require explicit user approval.
