# ADR-0079: Background triggers are reconciliation hints, not work authority

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Service managers and schedulers trigger on time, boot/login, devices, network, filesystem, sockets, notifications, idle state, and provider events. Registrations race with changes; events can duplicate, coalesce, reorder, overflow, carry stale or hostile payloads, or vanish across broker restart and sleep.

## Decision

A background trigger is generation- and source-scoped at-least-once invalidation evidence. It admits a bounded execution attempt only after current definition, principal, authority, policy, resources, freshness, and authoritative domain state are revalidated. Trigger payload is an untrusted hint, never an exactly-once journal entry or authority to perform the work.

## Consequences

- Providers converge through snapshot-plus-generation reconciliation.
- Duplicate triggers are normal and work claims are idempotent or transactional.
- Wake, network, device, credential, and side-effect authority remain separate.
- Overflow and broker restart are explicit loss states rather than invented event history.
