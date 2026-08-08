# ADR-0047: Poisoning is consistency policy, not lock semantics

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Some Rust locks expose panic poisoning, while native primitives generally do not; robust cross-process mutexes detect different owner-death cases. Treating all abnormal exits as one lock state confuses synchronization with application invariant recovery.

## Decision

Mutual exclusion and memory synchronization remain the base contract. Poisoning/owner-death is optional advisory evidence. Application policy decides whether to validate/recover, replace state, or fail; a lock cannot prove protected data consistent.

## Consequences

- Native and Rust-backed providers can report truthful differences.
- Recovery logic is explicit and testable.
- Cross-process robust synchronization remains a separate capability.

