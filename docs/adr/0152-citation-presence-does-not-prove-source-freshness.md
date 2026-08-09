# ADR-0152: Citation presence does not prove source freshness

**Status:** Accepted  
**Date:** 2026-08-08

## Context

The knowledge base cites hundreds of standards and platform/provider documents. URLs may remain reachable while content changes, standards are superseded, errata appear, or applicability shifts by product/version/region.

## Decision

External links are inventory records only. A freshness claim separately binds authority class, source version/status, review date, applicability scope, affected propositions, reviewer, expiry/trigger, and findings. Unknown remains explicit.

## Alternatives considered

- Treat successful link checks as freshness: rejected because reachability says nothing about content or applicability.
- Pin every page snapshot immediately: rejected because licensing, mutable documentation, and the current Draft scope require a reviewed prioritization process.
- Avoid external sources: rejected because native platform and standards semantics require primary evidence.

## Consequences

- The generated index can expose the review backlog without overclaiming it.
- High-risk sources receive shorter review cadences and specialist review.
- Provider trials and releases must bind source/version evidence rather than only URLs.
