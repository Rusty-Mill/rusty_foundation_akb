# ADR-0111: Exactly-once is scoped to named state and effect boundaries

## Status

Accepted

## Context

Fault-tolerant processors commonly restore checkpoints and replay records. They can ensure that each record affects restored operator state once even though the processing code runs multiple times. External calls, files, messages, databases, and user-visible effects require their own transactions, fencing, or idempotency. An unqualified “exactly once” claim hides duplicates, lost effects, ambiguity, and retention assumptions.

## Decision

Rusty Mill permits exactly-once claims only when they name input identities and replay horizon, operator state/checkpoint boundary, result/effect identities, every participating sink or protected resource, transaction/fencing/idempotency mechanism, failure model, recovery/reconciliation, and exclusions. Re-execution is allowed; duplicate committed effects at the claimed boundary are not.

## Consequences

- Operator-state and end-to-end effect guarantees are reported separately.
- Connectors participate in conformance rather than inheriting engine claims.
- External nontransactional effects require durable idempotency or remain at-least-once.
- Checkpoint completion is not promoted into business outcome proof.
