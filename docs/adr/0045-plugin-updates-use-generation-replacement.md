# ADR-0045: Plugin updates use immutable generation replacement

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Overwriting loaded code or relying on universal unload safety conflicts with mapped executables, outstanding calls, callbacks, TLS, threads, dependencies, allocator ownership, and platform loaders. State migration may also make binary rollback unsafe.

## Decision

Updates install immutable content-addressed generations, prepare and validate a new instance, atomically switch routing after readiness, quiesce the old generation, and retire it. In-process native replacement normally completes on host restart; unload is an optional evidenced optimization, never the contract.

## Consequences

- Failed activation leaves the prior generation available.
- Disk/memory budgets must allow bounded coexistence and cleanup.
- State migration and executable rollback compatibility are evaluated separately.

