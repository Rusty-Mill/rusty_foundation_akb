# ADR-0095: HTTP replay is an explicit domain authority

## Status

Accepted

## Context

Redirects, authentication challenges, connection failures, refused streams, early data rejection, hedging, and retries can cause a client to transmit an operation again. HTTP method idempotency is useful protocol evidence but cannot prove that an application body is rewindable, an operation is harmless, an idempotency key is enforced, or the first attempt had no effect.

## Decision

Every replay creates a new linked attempt and requires explicit policy binding the trigger, method and domain semantics, body replayability, bytes-sent/effect evidence, idempotency or deduplication contract, credential/origin scope, deadline and attempt budget, and duplicate-effect handling. Unknown effect remains unknown. Unsafe automatic replay is prohibited.

## Consequences

- Redirect, authentication, retry, early-data fallback, and hedging share one reviewable replay boundary.
- Streaming bodies are not assumed rewindable.
- Metrics and errors retain complete attempt lineage.
- Callers must supply stronger domain evidence for automatic replay of consequential operations.

