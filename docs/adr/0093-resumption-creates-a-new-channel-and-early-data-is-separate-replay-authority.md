# ADR-0093: Resumption creates a new channel and early data is separate replay authority

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Session tickets can carry prior authentication state, but trust, revocation, credentials, ALPN, topology, and policy change. TLS/QUIC early data can be replayed, rejected, or processed before full handshake and client authentication. Treating resumption as the old channel or early writes as ordinary data hides these differences.

## Decision

Resumption always establishes a new channel generation and revalidates all material current policy, identity, trust, credential, ALPN, provider, and scope inputs before readiness. Tickets are protected scoped secret credentials, not cached trust. Early data is disabled by default and uses a separate typed replay authority binding an explicitly replay-safe/idempotent operation, anti-replay and deduplication policy, maximum bytes, identity/authorization context, and application-controlled fallback. Rejection never automatically resends it.

## Consequences

- Ticket caches have secret lifecycle, tenancy, rotation, and invalidation rules.
- Full-handshake fallback cannot weaken policy.
- Applications see accepted, rejected, replayed, partial, and indeterminate early outcomes.
- Benchmarks report replay defenses and fallback cost alongside latency gains.

