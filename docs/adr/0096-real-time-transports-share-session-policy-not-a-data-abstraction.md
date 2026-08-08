# ADR-0096: Real-time transports share session policy, not a data abstraction

## Status

Accepted

## Context

WebSocket exposes reliable ordered text/binary messages over one full-duplex channel. Server-sent events expose server-to-client UTF-8 events over an HTTP response with reconnection conventions. WebTransport exposes multiple independent reliable byte streams plus unreliable datagrams. A universal message API would buffer arbitrary streams, invent ordering for datagrams, imply client-to-server SSE, or discard WebSocket boundaries.

## Decision

Rusty Mill shares establishment, authority, generation, lifecycle, resource, security, and observability policy across real-time transports. Each protocol retains its native data primitives and delivery/failure scope. Higher-level application protocols may deliberately compose a message abstraction only after specifying framing, bounds, ordering, reliability, replay, and acknowledgment semantics.

## Consequences

- Protocol differences remain visible and testable.
- Applications cannot switch transports under an apparently identical but false contract.
- Shared session policy reduces duplicated security and lifecycle logic.
- Higher-level messaging requires an explicit specification rather than a convenience wrapper.

