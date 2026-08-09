# ADR-0138: Local acceptance is not authoritative effect completion

- **Status:** Accepted
- **Date:** 2026-08-08

## Context

Offline-first applications must respond while disconnected, but storing a mutation locally or presenting its optimistic projection does not prove that a remote authority accepted it, that conflicts were resolved, or that an external effect occurred.

## Decision

Local durable acceptance, queued/transmitted/peer-accepted change, merge, authoritative commit or domain effect, projection visibility, acknowledgement, and convergence are distinct milestones. APIs and user experiences expose the relevant state and never label optimistic state as confirmed.

## Options considered

- Treat local durability as success: responsive but makes rejection and global invariants dishonest.
- Block all writes until online: simpler but defeats valid offline workloads.
- Distinct milestones: preserves responsiveness and semantic truth; selected.

## Consequences

Products classify which operations may proceed offline, persist original intent and stable effect identity, and provide accessible pending/conflict/rejection repair. Irreversible or globally constrained effects require fresh/fenced authority unless an RFC proves delegation.
