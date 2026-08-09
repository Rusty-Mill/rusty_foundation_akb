# ADR-0124: Consent is a revocable purpose-scoped grant, not universal processing authority

## Status

Accepted

## Context

Applications frequently collapse platform permission, terms acceptance, feature activation, cookie choices, marketing preferences, and consent into a Boolean. This loses what was presented, which purposes/data/actions/recipients were chosen, who could grant, expiry, and withdrawal. It also incorrectly implies consent is the only possible product-policy basis or that it legalizes unrelated future processing.

## Decision

Rusty Mill models consent as one issuer- and product-policy-defined, granular, affirmative, versioned, purpose/data/action/recipient-scoped, expiring and revocable grant. It records offer and interaction evidence plus nonclaims. Every processing action still requires a current product policy decision; other counsel-approved bases are opaque policy evidence outside portable semantics. Withdrawal invalidates future consent-dependent authority and initiates scoped reconciliation without claiming reversal of prior effects.

## Consequences

- Platform permissions and privacy consent remain distinct and composable.
- Products can support refusal, granular choice, withdrawal, and preference conflicts honestly.
- Background/headless systems cannot fabricate consent.
- Legal applicability and sufficiency remain product/counsel decisions rather than framework claims.
