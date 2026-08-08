# ADR-0053: Cancellation does not end operation lifetime

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Native cancellation is often best effort and races with successful or partial completion. Kernels and drivers may retain pointers to buffers and operation control blocks after cancellation is requested. Reclaiming them at request time creates memory-safety and ABA hazards.

## Decision

Cancellation changes operation intent but does not end its lifetime. All operation-owned memory, resource-generation references, and native control state remain valid until exactly one terminal completion is observed or the provider proves an equivalent terminal acknowledgement. Timeout is a cancellation policy, not a distinct magical completion.

## Consequences

- Dropped futures need explicit cancel-or-detach supervision.
- Shutdown continues draining completions after cancellation requests.
- APIs expose progress and the race between cancellation and normal completion.
