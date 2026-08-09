# ADR-0154: Maturity promotion uses conjunctive gates, not scores

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Repository-scale scorecards make progress visible, but percentages and weighted scores can hide a missing safety, authority, verification, or ownership gate behind strong documentation elsewhere.

## Decision

Maturity promotion uses conjunctive required gates with explicit `pass`, `fail`, `unknown`, `not-applicable`, or governed-waiver states. Unknown blocks promotion. Generated scorecards are decision support; only an explicit reviewed promotion record changes maturity.

## Alternatives considered

- Weighted readiness score: rejected because unlike risks are not safely compensable.
- Document-count threshold: rejected because volume does not prove semantics or evidence.
- Reviewer judgment without gate records: rejected because the conclusion cannot be reproduced or invalidated precisely.

## Consequences

- Progress may look slower but blockers remain visible.
- Non-applicability and waivers require reviewable rationale.
- Automation can assemble evidence but cannot self-promote a capability.
