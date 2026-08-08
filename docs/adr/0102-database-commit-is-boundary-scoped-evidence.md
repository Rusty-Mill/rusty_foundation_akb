# ADR-0102: Database commit is boundary-scoped evidence

## Status

Accepted

## Context

Databases can acknowledge transactions after different logging, flush, replication, quorum, and storage boundaries. A committed transaction may not yet be visible on replicas, captured by archive logs, included in a backup, published to a broker, observed by a client, or reflected in an external physical system. Network loss can also hide a successful commit from the caller.

## Decision

Rusty Mill treats logical commit, requested durability satisfaction, replica visibility, archive/PITR inclusion, change-feed publication, caller observation, and external/domain effects as separate evidence. Every transaction profile names its exact durability and failure assumptions. Ambiguous commit remains unknown and is reconciled by stable transaction/idempotency/domain identity rather than unsafe automatic replay.

## Consequences

- Applications select durability and visibility appropriate to each operation.
- Backups and change streams cannot be inferred from commit success.
- Failover and timeout handling retain unknown outcomes.
- Provider performance comparisons must use equal completion boundaries.

