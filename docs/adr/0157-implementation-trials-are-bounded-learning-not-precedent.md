# ADR-0157: Implementation trials are bounded learning, not precedent

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill architecture governance

## Context

Native implementation evidence is needed before stable design, but prototypes can accidentally dictate public APIs, crate boundaries, provider choices, or support claims.

## Decision

An implementation trial is an exact, bounded, generation-linked learning authority. Its code and results establish no architecture, maturity, provider, compatibility, production, or release precedent. Those changes require ordinary ADR, RFC, promotion, and release decisions.

## Options considered

Treat prototypes as the starting implementation, authorize from Experimental status alone, or prohibit pre-Stable implementation. Each either creates accidental commitment, omits essential controls, or prevents necessary native learning.

## Consequences

Trials require explicit questions, limits, nonclaims, evidence, isolation, and disposal. Successful code may be discarded. Negative and inconclusive results retain value.

## Verification

Audit every trial record for bound inputs, nonclaims, evidence, outcome, and a separate decision for any downstream adoption.

## Follow-up

- Apply [RFC-0002](../rfc/0002-implementation-trial-governance.md) before selecting a trial candidate.

