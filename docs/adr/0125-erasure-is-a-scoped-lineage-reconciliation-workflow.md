# ADR-0125: Erasure is a scoped lineage-reconciliation workflow

## Status

Accepted

## Context

Personal data spreads into normalized stores, replicas, object versions, caches, search indexes, queues, messages, reports, logs, exports, recipients, processors, backups, features, and trained models. A database delete can leave usable copies, allow restoration, conflict with holds, or erase audit/security evidence improperly. Some boundaries support only expiry, access revocation, cryptographic erasure, retraining, or unverifiable notification.

## Decision

Rusty Mill models erasure as an immutable, authority- and policy-bound plan over an authenticated inventory and lineage snapshot. Each named system applies an explicit method, records outcome and residuals, installs resurrection guards/tombstones, and participates in recovery/rebuild/restore reconciliation. Completion is scoped to measured boundaries; universal disappearance and rollback of prior disclosure are prohibited claims.

## Consequences

- Products must maintain usable inventories and lineage rather than bolt deletion onto one database.
- Holds, exceptions, recipients, backups, logs, and models remain explicit rather than silently ignored.
- Partial, delayed, unverifiable, and unsupported outcomes are first-class.
- Recovery systems must consume correction/restriction/erasure state before republishing data.
