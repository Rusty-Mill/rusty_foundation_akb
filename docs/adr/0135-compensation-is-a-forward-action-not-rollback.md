# ADR-0135: Compensation is a forward action, not rollback

## Status

Accepted

## Context

Long-running workflows cross databases, services, people, physical processes, and external organizations. Their effects do not share one atomic transaction and may be observed, copied, billed, published, or become irreversible. Calling compensating operations rollback falsely implies restoration of the prior world.

## Decision

Rusty Mill models compensation as a newly authorized, idempotent or fenced forward activity bound to an observed prior effect and its current target state. Each compensation defines preconditions, ordering, retry, failure, residual, and evidence. Success proves only the new effect it performs; impossible or partial compensation remains explicit.

## Consequences

- Workflow designers identify irreversible and externally visible effects.
- Compensation ordering follows effect dependencies, not naive reverse syntax.
- Cancellation, termination, compensation, and database rollback remain distinct.
- Operators receive residual states and repair paths instead of false rolled-back status.
