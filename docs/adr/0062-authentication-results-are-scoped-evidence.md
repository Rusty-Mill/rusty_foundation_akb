# ADR-0062: Authentication results are scoped evidence

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Native brokers may authenticate with passwords, biometrics, device keys, cached login state, enterprise providers, or future methods. Returning a boolean, password, or universal assurance score would erase purpose, audience, freshness, method, provider, and interaction differences and encourage authentication to be treated as authorization.

## Decision

An authentication result is purpose-, audience-, principal-, provider-, method-, assurance-, and time-scoped evidence. It contains no reusable secret and grants no capability authority. Protected operations independently validate explicit authority and native policy at use time. Cached or silent satisfaction is acceptable only when declared and when it meets the request.

## Consequences

- Products use trusted native brokers where available and do not design around collecting passwords.
- Evidence can expire or be revoked independently of credentials, sessions, and authority.
- Protocol-specific tokens and remote federation require separate contracts.
