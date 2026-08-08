# ADR-0040: Resolution results are candidates, not authority or identity

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Resolvers return time- and network-dependent address candidates. DNS aliases, search policy, split horizons, DNS64, proxies, cache expiry, and attacker influence prevent an address from serving as durable service identity or authorization.

## Decision

Resolution returns an immutable expiring candidate set with provenance. Network authority is supplied separately, and peer authentication binds the original service identity at connection/use time. Resolved addresses are never silently promoted to trusted identity or persistent authorization data.

## Options considered

- Treat resolved address as identity: simple but insecure and stale.
- Require numeric endpoints only: explicit but unsuitable for service identity and modern dual-stack policy.
- Preserve service intent through resolution and connection: explicit and secure.

## Consequences

- Connection reports retain both original intent and selected endpoint.
- Rebinding and redirect policy are reviewable rather than accidental.
- Caches must honor expiry/network epochs and cannot confer authority.

