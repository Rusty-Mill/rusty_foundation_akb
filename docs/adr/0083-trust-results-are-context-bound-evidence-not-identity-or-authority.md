# ADR-0083: Trust results are context-bound evidence, not identity or authority

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Certificate evaluation depends on purpose, reference identity, time, trust anchors/distrust and enterprise/user/application policy, path choice, algorithm rules, revocation/network mode, cache, overrides, and provider behavior. A boolean “trusted” encourages reuse across hosts, protocols, times, store changes, and authorization decisions.

## Decision

A trust result is immutable context-bound evidence identifying exact certificate bytes/path/anchor, validation policy and purpose, typed reference identity, verification time/clock quality, trust and algorithm-policy generations, status/freshness/network/cache evidence, provider/version, pins/overrides, warnings, unknowns, expiration, and dependencies. It establishes only that this evidence satisfied that policy. Authentication additionally requires protocol proof-of-possession/channel binding and authorization remains a domain decision.

## Consequences

- Cached results expire or invalidate on any material dependency change.
- `unknown`, `not checked`, and `unavailable` revocation remain distinct from `good`.
- User/admin exceptions are narrow, time-bound, auditable policy inputs.
- APIs may project a boolean but cannot discard the evidence-bearing result.
