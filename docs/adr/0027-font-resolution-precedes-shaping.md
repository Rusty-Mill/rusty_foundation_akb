# ADR-0027: Font resolution precedes reproducible shaping

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

Family names and platform fallback rules are mutable environment policy. Shaping output depends on exact font bytes, face index, variations, features, engine, and Unicode data. Allowing a shaping call to discover fonts internally makes results non-reproducible and hides fallback, licensing, trust, and privacy decisions.

## Decision

Font discovery/resolution is a capability that converts policy and a versioned collection snapshot into an immutable ordered plan of exact artifact-digest/face/variation instances. Shaping consumes that plan and performs no ambient discovery or network access. Collection changes create new plans; existing layout identity does not mutate silently.

## Consequences

- Conformance fixtures and caches have complete font identity.
- Fallback and synthetic styling are observable.
- Downloaded/untrusted font policy can be isolated from shaping semantics.
- Applications that want live system-font changes explicitly re-resolve and re-layout.

