# ADR-0107: Invalidation completion is boundary-scoped evidence

## Status

Accepted

## Context

Local, distributed, edge, browser, offline, third-party, backup, and derived caches do not share one atomic invalidation boundary. Provider purge APIs acknowledge different milestones, and propagation can be delayed or incomplete. Claiming global removal from a control-plane success is unsafe.

## Decision

Rusty Mill models invalidation as generation-scoped distributed control intent with explicit authority, scope, acceptance, application, propagation, observation, partial-failure, and reconciliation milestones. Completion claims name the boundary measured. Immutable versioned identities are preferred for normal replacement; emergency recall composes origin denial, authorization revocation, bounded freshness, purge, and observation.

## Consequences

- Purge acknowledgments never imply recall of already-served or out-of-scope copies.
- Products define propagation objectives and evidence.
- Namespace epochs can reject old entries before physical reclamation.
- Security response uses layered controls rather than relying on purge alone.
