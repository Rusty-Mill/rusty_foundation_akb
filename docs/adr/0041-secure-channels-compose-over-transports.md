# ADR-0041: Secure channels compose over transports

**Status:** Accepted  
**Date:** 2026-08-08

## Context

TCP establishment, proxy tunnels, TLS handshakes, certificate validation, application-protocol negotiation, and higher-level readiness have different failure, timing, identity, and authority semantics. Baking TLS into a socket abstraction would conflate those milestones while excluding other secure transports.

## Decision

Byte-stream/datagram transports own movement semantics. A secure-channel service composes transport with protocol, trust, credential, service-identity, resumption, and application-protocol policy. It publishes cryptographic and authentication milestones independently.

## Options considered

- Secure sockets as one capability: convenient but conflates transport and trust policy.
- Leave security entirely to applications: flexible but duplicates critical cross-platform behavior.
- Composed secure-channel service: narrow transport contracts with reusable security policy.

## Consequences

- Plain transport remains usable for local/testing or protocols with their own security.
- Profiles can require secure channels without pretending every connection is TLS.
- Cancellation, close, truncation, and early-data semantics need cross-layer evidence.

