# ADR-0140: Entitlement is eligibility evidence, not effect authority

- **Status:** Accepted
- **Date:** 2026-08-08

## Context

Products often treat a paid subscription or billing-provider entitlement as a direct feature switch. That collapses commercial eligibility into actor authorization, tenant lifecycle, resource safety, capacity, privacy, and successful effects.

## Decision

Effective entitlement is a versioned derivation and supplies eligibility evidence only. Every effect still passes actor/resource authorization, policy, quota/capacity admission, platform capability, and effect-specific validation. Billing-provider state is one mapped input and cannot override security policy by itself.

## Options considered

- Billing state directly gates code paths: simple but creates a remote privileged authority and ambiguous outages.
- Entitlement equals authorization: centralizes checks but mixes commercial and security semantics.
- Separate eligibility evidence: explicit and composable; selected.

## Consequences

Applications can explain subscription eligibility separately from denial, unavailability, or quota exhaustion. Cached/offline grants need expiry and revocation semantics. Conformance tests precedence and stale-provider histories.
