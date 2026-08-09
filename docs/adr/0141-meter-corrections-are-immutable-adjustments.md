# ADR-0141: Meter corrections are immutable adjustments

- **Status:** Accepted
- **Date:** 2026-08-08

## Context

Usage arrives late, duplicated, out of order, or wrong. Rewriting raw events or closed aggregates destroys provenance and makes disputes, rerating, invoice reconciliation, and audit irreproducible.

## Decision

Accepted meter events are immutable observations. Corrections, reversals, credits, late data, rerating, allocation changes, and dispute outcomes create new adjustment records referencing the displaced evidence. Derived views may supersede prior results while preserving lineage.

## Options considered

- Mutate or delete incorrect events: easy current-state queries but no reliable history.
- Rebuild without adjustment records: reproducible only if all inputs and rules remain available and closed-period effects are ignored.
- Immutable events plus adjustments: auditable and reconcilable; selected.

## Consequences

Storage and query models carry lineage and effective/accounting periods. Idempotency and deduplication become mandatory. Rusty Mill reports evidence but does not decide accounting or tax treatment.
