# ADR-0098: A remote call is an asynchronous interaction, not a local procedure

## Status

Accepted

## Context

RPC syntax often resembles a local function, but resolution, serialization, queues, networks, proxies, remote admission, independent clocks, cancellation races, partial messages, retries, failover, and divergent client/server observations introduce distributed partial failure. Hiding those boundaries encourages missing deadlines, unsafe retry, implicit ambient context, and false assumptions about atomicity or cancellation.

## Decision

Rusty Mill models RPC as an explicit asynchronous interaction with typed request/response/error schemas, immutable call and attempt identities, original service and authority, overall deadline budget, bounded metadata/content, staged progress, cooperative cancellation, retry/idempotency policy, and boundary-scoped results. Sync-complete APIs preserve the same evidence and cannot make the interaction semantically local.

## Consequences

- Callers must handle timeout, cancellation, partial progress, and unknown effect.
- Streaming and unary interactions share lifecycle concepts without pretending to be ordinary iterators/functions.
- Context propagation becomes explicit and reviewable.
- Generated clients can be ergonomic but cannot erase distributed semantics.

