# ADR-0035: Configuration notifications trigger reconciliation

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Registry, filesystem, and preferences notifications have different payloads, ordering, scope, lifetime, overflow, and cross-process behavior. None provides a universal lossless record of configuration writes.

## Decision

Native notifications are invalidation hints. Providers re-read explicitly scoped sources, resolve and validate a candidate, and publish a replacement snapshot or structured rejection. Lost continuity produces an explicit resynchronization state. Portable events describe snapshot transitions, not every native write.

## Options considered

- Normalize native write events: attractive but semantically false under coalescing, overflow, replacement, and cache behavior.
- Poll only: portable but needlessly latent and expensive where native observation exists.
- Observe, reconcile, and resynchronize: truthful common semantics with native efficiency.

## Consequences

- Consumers respond to effective configuration transitions rather than storage mechanics.
- Providers must bound coalescing and prove convergence after loss.
- Applications cannot depend on observing every intermediate external edit.

