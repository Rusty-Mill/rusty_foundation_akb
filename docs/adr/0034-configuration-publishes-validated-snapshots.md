# ADR-0034: Configuration publishes validated immutable snapshots

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Platform stores differ in hierarchy, typing, caching, persistence, notification, and policy behavior. A mutable global key/value facade would expose torn reads, hide precedence, and make validation/reload races part of every consumer.

## Decision

Configuration resolution publishes immutable, monotonically revisioned, validated snapshots with per-value provenance. Candidate changes replace a complete snapshot atomically or leave the active revision unchanged. Dynamic activation follows each key's live, coordinated, restart-required, or immutable policy.

## Options considered

- Direct mutable reads from native stores: freshest-looking but incoherent, platform-shaped, and difficult to test.
- Mutable process-global map: convenient but hides authority, ordering, and update races.
- Immutable validated snapshots: explicit coherence and evidence at modest copy/reconciliation cost.

## Consequences

- Consumers can reason about one coherent revision and retain it safely.
- Source acquisition, resolution, validation, and activation are separable and replayable.
- Very large configurations may require structurally shared snapshots, but this cannot weaken immutability.
- Cross-process global atomicity is not promised.

