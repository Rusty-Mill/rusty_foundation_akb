# ADR-0129: Account recovery is an authenticator replacement ceremony

## Status

Accepted

## Context

Recovery frequently bypasses normal authentication through email, phone, support staff, security questions, or an existing session. If that alternate path is materially weaker or depends on the compromised factor, the advertised authentication strength is illusory. Recovery also changes security state beyond proving a one-time login.

## Decision

Rusty Mill models recovery as a high-risk, policy-versioned identity re-establishment and authenticator lifecycle ceremony. It evaluates independent evidence, creates new authenticator and security generations, reconciles existing authenticators/sessions/tokens, applies notifications and optional delay/restriction, and records exceptions. Recovery evidence does not become general authentication or resource authority.

## Consequences

- Products must threat-model recovery alongside primary authentication.
- Circular dependencies on a lost or compromised channel are visible.
- Support and administrative exceptions require explicit bounded authority and audit.
- Successful recovery cannot silently preserve potentially compromised sessions or credentials.
