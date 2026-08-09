# ADR-0139: Conflict resolution is typed domain policy

- **Status:** Accepted
- **Date:** 2026-08-08

## Context

Concurrent changes may represent counters, sets, ordered text, authorization, uniqueness, deletion, money, or human intent. Arrival order and wall-clock last-write-wins discard different meanings and fail under skew or malicious clocks.

## Decision

Conflict detection and resolution are versioned per domain type, field, relation, and invariant. Each policy declares causal/order inputs, algebra or resolver, authority, loss, metadata bounds, garbage collection, schema evolution, and unresolved states. Last-write-wins, CRDTs, OT, three-way merge, authoritative-side wins, rejection, or human resolution are mechanisms selected only when their assumptions match.

## Options considered

- Universal last-write-wins: operationally cheap but semantically destructive and clock-dependent.
- Universal CRDT model: convergent for designed datatypes but not a general invariant or authority solution.
- Typed policy: more design work but explicit and testable; selected.

## Consequences

Conformance requires history/permutation tests and validates hidden causal metadata as well as visible state. Resolutions create new provenance-bearing changes; deterministic display winners cannot silently erase losing intent.
