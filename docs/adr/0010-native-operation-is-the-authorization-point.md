# ADR-0010: The native operation is the authorization point

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

Access checks are often requested for UI planning, diagnostics, or provider selection. Between a check and use, credentials, policy, object identity, namespace bindings, labels, sandbox state, or revocation state can change. Cross-platform mechanisms also expose different subsets of authorization logic.

## Decision

Portable policy evaluation is advisory. It returns permit, deny, indeterminate, or not-applicable with provenance and freshness, but never guarantees that a later operation will succeed. The protected native operation remains the authorization point and its denial is a normal typed outcome.

A contract may claim atomic authorization only when its native mechanism performs the check and operation as one protected action and conformance evidence proves the scoped claim.

## Consequences

- Applications must handle denial even after a permit result.
- Providers cannot implement authorization as check-then-use when an operation-time mechanism exists.
- Diagnostics distinguish policy advice from actual enforcement outcomes.
- UI preflight can explain likely denial but cannot promise access.

## Verification

Adversarial tests change policy, identity, namespace, and sandbox-relevant state between evaluation and operation and verify that native denial is preserved.

