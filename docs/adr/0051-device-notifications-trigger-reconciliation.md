# ADR-0051: Device notifications trigger reconciliation

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Native device notifications differ in registration races, coalescing, ordering, callback constraints, overflow visibility, property readiness, and behavior across suspend or service restart. Replaying callback payloads as a portable journal would publish impossible intermediate states and conceal loss.

## Decision

Device notifications are bounded invalidation hints. They mark observation state dirty and trigger re-enumeration; only coherent revisioned snapshots and diffs between them are published as portable state. Loss, overflow, source restart, and lifecycle transitions force full reconciliation.

## Consequences

- Consumers are idempotent and snapshot-driven.
- Debounce improves burst behavior but remains bounded and observable.
- Native callbacks remain minimal; property I/O and product callbacks run outside them.
