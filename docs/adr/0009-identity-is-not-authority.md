# ADR-0009: Identity is not authority

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

Windows tokens and SIDs, Linux credentials and capabilities, and macOS identities, entitlements, and sandbox rules encode different dimensions of security. Treating a principal identifier or process credential as portable authority would create confused-deputy risks, ambient privilege, namespace collisions, and false cross-platform equivalence.

## Decision

Rusty Mill models principal claims, security-context snapshots, authority, grants, and constraints as distinct concepts. Security-sensitive operations accept explicit resource- and operation-scoped authority where practical. Portable authority derivation is attenuation-only. Constraints compose by intersection, and missing required evidence fails closed.

Authority is opaque unless a contract defines inspection. It is not serializable or transferable unless a capability explicitly defines authenticity, confidentiality, replay, audience, lifetime, and restoration semantics.

## Consequences

- Convenient ambient-authority APIs require explicit policy and disclosure.
- Native identities retain issuer/type information instead of collapsing into strings.
- Delegation and process isolation require separate specifications.
- Some native rights cannot be represented portably and remain provider extensions.

## Verification

Conformance tests attempt authority amplification, cross-namespace identity confusion, use after close, and fail-open behavior under absent evidence.

