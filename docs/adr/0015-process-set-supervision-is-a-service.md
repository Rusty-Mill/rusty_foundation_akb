# ADR-0015: Process-set supervision is a platform service

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

Applications need to stop, wait for, and account for groups of related processes. Parent/child ancestry is mutable and not a stable control object. Windows jobs, POSIX process groups/sessions, Linux cgroups/service scopes, and macOS service facilities differ in automatic membership, escape, nesting, signaling, accounting, and behavior after supervisor failure.

## Decision

Race-safe control of one owned child is `rm.process.control`. Supervision of a changing process set is a platform service that composes spawn, control, cancellation, deadlines, membership policy, and native containment. Providers claim scoped containment levels P0–P3 and cannot call observed ancestry a contained tree.

Restricted execution may compose supervision but remains distinct: containment governs membership/lifecycle, while restricted execution governs authority and isolation.

## Options considered

### Treat descendants as a property of spawn

Simple but cannot handle dynamic membership, escape, or independent service lifecycles.

### One cross-platform process-group capability

Suggests false equivalence between jobs, POSIX groups, cgroups, and service managers.

### Composed supervision service with containment claims

Makes policy and lifecycle explicit while retaining narrow child control.

## Consequences

- Group completion and root completion are distinct.
- Profiles request containment outcomes rather than a named native mechanism.
- Strong levels may require launch-time setup and fail in an incompatible parent job/session.
- Accounting and forced termination retain exact membership scope.

## Verification

Tests race descendant creation and exit against group control, attempt breakaway, nest under existing containment, kill the supervisor, and verify membership/accounting/terminal claims at each declared level.

