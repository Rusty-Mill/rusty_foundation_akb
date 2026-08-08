# ADR-0052: Portable asynchronous I/O is completion-oriented

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Windows commonly reports completed overlapped operations, Linux supports both io_uring completion and epoll readiness, and macOS commonly exposes kqueue/dispatch readiness or callback mechanisms. Readiness means an operation may now make progress; it is not the result of a requested operation and can be stale or concurrently consumed.

## Decision

Portable domain-facing asynchronous I/O contracts are completion-oriented. Providers may use native completion, readiness translated through bounded retries, or disclosed blocking adapters. Readiness state and rearm policy remain behind the backend contract and never substitute for exact terminal operation results.

## Consequences

- Domain capabilities share one lifecycle and cancellation vocabulary.
- Readiness providers perform additional bounded bookkeeping.
- Provider evidence is per operation/resource/mechanism, not merely per OS.
