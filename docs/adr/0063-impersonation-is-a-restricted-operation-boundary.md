# ADR-0063: Impersonation is a restricted operation boundary

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Windows impersonation is thread-context state; Linux credential facilities are process/thread and subsystem sensitive; macOS commonly uses operation-oriented authorization or privileged helpers rather than a universal equivalent. Rust futures can move between executor threads, and pooled threads outlive tasks. An ambient guard spanning `await` can leak or apply the wrong principal to unrelated work.

## Decision

Portable impersonation is exposed only as a bounded restricted operation. A dedicated provider validates an attenuated delegated context, enters the native context, performs one synchronous operation, restores the prior context on every exit path, and only then completes the caller's async result. Impersonation never implicitly propagates across `await`, callbacks, plugins, executors, or unrelated I/O.

## Consequences

- General application code cannot run arbitrary futures “as user.”
- Providers must prove restoration, nesting policy, stale-context rejection, and thread-pool isolation.
- Long-lived privilege separation uses restricted processes/services rather than impersonation scope.
