# ADR-0103: Schema migration is a compatibility rollout

## Status

Accepted

## Context

Application versions, database replicas, read models, caches, queues, change consumers, analytics, backups, and offline clients rarely change atomically. A one-shot DDL or migration script can lock or rewrite large data, break old readers/writers, invalidate rollback, amplify replication logs, and leave partially backfilled semantics after cancellation or failure.

## Decision

Every schema change is an immutable staged compatibility plan: expand, deploy compatible readers/writers, backfill, validate, switch authority, contract, and verify. The plan includes all consumers and recovery artifacts, provider-specific DDL/lock/rewrite behavior, resumable concurrent-write-safe backfills, mixed-version evidence, explicit points of no return, and roll-forward/restore strategy.

## Consequences

- Schema and application deployment are coordinated without requiring simultaneous rollout.
- Destructive contraction waits for proof that old representations are no longer needed.
- Migration state becomes observable, resumable, and auditable.
- Small deployments carry more ceremony for changes that affect compatibility or data meaning.

