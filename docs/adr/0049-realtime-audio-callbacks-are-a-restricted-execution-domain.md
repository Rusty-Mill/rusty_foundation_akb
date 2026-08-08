# ADR-0049: Realtime audio callbacks are a restricted execution domain

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Native audio callbacks run under small, device-driven budgets. General allocation, blocking synchronization, I/O, logging, runtime scheduling, and unbounded reclamation can cause audible failure even when functionally correct.

## Decision

Realtime audio callbacks are a distinct restricted execution domain. Their data plane is preallocated, bounded, nonblocking, panic-contained, and isolated from ordinary control-plane work. Implementations must prove callback-path constraints and measured deadline behavior before claiming realtime quality.

## Consequences

- Ordinary async or thread-safe code is not automatically callback-safe.
- Configuration and graph changes use bounded generation handoff and deferred retirement.
- Observability uses bounded counters/rings with export outside the callback.
