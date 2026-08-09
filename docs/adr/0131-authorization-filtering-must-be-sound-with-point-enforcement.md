# ADR-0131: Authorization filtering must be sound with point enforcement

## Status

Accepted

## Context

Applications need lists, search, counts, facets, batch checks, and available-action hints. Calling a remote point decision for every candidate can be prohibitively expensive, but filtering after unrestricted retrieval can leak existence, metadata, ordering, counts, or content. Independently implemented filter and point-check semantics also drift.

## Decision

Rusty Mill requires authorization filters to declare semantic equivalence and consistency with the point-check contract. Sound filters never return a resource that the corresponding point check would deny or classify indeterminate under the named frontier. Optimizations may be incomplete and omit allowed resources only when that limitation is explicit. The resource boundary still performs point enforcement before disclosure or effect.

## Consequences

- Search/index/query integrations must carry authorization generations and leakage tests.
- Counts, facets, snippets, and pagination are protected outputs, not harmless metadata.
- Optimizers can trade completeness for bounded work but never safety.
- Differential conformance compares filtering, batching, and point decisions under mutation.
