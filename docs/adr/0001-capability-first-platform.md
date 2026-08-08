# ADR-0001: Capability-first platform model

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

Windows, Linux, and macOS expose different names, boundaries, semantics, and performance mechanisms. Wrapping their APIs directly would leak OS identity upward and encourage a lowest-common-denominator design.

## Decision

Rusty Mill models application needs as versioned capabilities with behavioral contracts. Applications and common services depend on capabilities, not OS APIs. Backends implement the contracts using native mechanisms and expose variance, emulation, degradation, or unavailability explicitly.

## Alternatives considered

- Thin one-for-one OS wrappers: simple initially, but not a stable cross-platform model.
- POSIX as the common model: excludes or distorts important Windows and macOS semantics.
- Lowest common denominator: portable but prevents native quality and advanced behavior.

## Consequences

- Domain analysis and contract design precede APIs.
- Capability discovery and negotiation become core architecture.
- Platform-specific extensions remain possible but explicit.
- Conformance work is substantial and mandatory.

## Verification

Each stable capability must be implemented and pass the same contract-derived suite on Windows, Linux, and macOS.
