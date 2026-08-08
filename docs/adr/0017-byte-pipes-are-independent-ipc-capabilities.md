# ADR-0017: Byte pipes are independent IPC capabilities

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

Pipes are commonly introduced as process-standard-stream plumbing, but they have independent resource, transfer, buffering, EOF, broken-peer, backpressure, atomicity, sync/async, and cancellation semantics. Treating them as files would import false seek/durability assumptions; embedding them in spawn would prevent reuse and hide Windows async variance.

## Decision

`rm.ipc.byte-pipe` is an independent unidirectional anonymous IPC capability. Process spawn binds compatible endpoints through its stdio model. Pipeline composition is a service/framework concern that owns multiple children, pipe ends, drainage, failure, and supervision.

Buffer capacity, non-interleaving write size, and async realization are provider claims. Basic Windows anonymous-pipe APIs cannot claim overlapped completion; providers may use a named-pipe mechanism internally while preserving anonymous semantics.

## Consequences

- IPC becomes an explicit taxonomy domain.
- Process contracts depend on byte-stream semantics rather than filesystem files.
- EOF correctness requires rigorous duplicate/inheritance cleanup.
- Text, terminal, and message framing remain separate adapters/capabilities.

## Verification

Tests cover all endpoint close permutations, concurrent inheritance, full-buffer backpressure, partial I/O, broken-peer host survival, atomicity boundaries, cancellation races, and Q0–Q3 async evidence.

