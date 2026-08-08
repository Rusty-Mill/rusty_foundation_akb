# ADR-0100: Exclusive coordination requires resource-enforced fencing

## Status

Accepted

## Context

A lease holder or elected leader can pause, lose connectivity, miss expiry, and later continue executing while a replacement has acquired authority. Heartbeats, client-side TTL checks, cooperative release, and a coordination service's single current owner do not stop the stale process from mutating a database, object store, device, or external system it can still reach.

## Decision

Every coordination generation used for exclusive side effects carries a monotonically ordered fencing token. Each protected resource atomically rejects tokens older than the greatest token it has accepted before applying a mutation. When a resource cannot enforce fencing, Rusty Mill reports only best-effort exclusivity and requires a different safety design for consequential effects.

## Consequences

- Paused and partitioned stale holders cannot overwrite newer work at compliant resources.
- Resource adapters participate in coordination safety instead of trusting clients.
- Multi-resource operations must define fencing composition explicitly.
- Some native/external systems cannot satisfy the strong profile and remain declared gaps.

