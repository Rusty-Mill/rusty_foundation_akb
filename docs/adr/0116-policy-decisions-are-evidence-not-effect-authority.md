# ADR-0116: Policy decisions are evidence, not effect authority

## Status

Accepted

## Context

Policy engines evaluate attributes and rules into permits, denies, typed results, obligations, or advice. Between evaluation and action, principals, resources, policy, data, and authority can change. Obligations can fail or cause independent effects. Treating a permit as a credential or assuming returned obligations executed creates time-of-check/time-of-use, replay, and partial-effect failures.

## Decision

Rusty Mill models a policy decision as immutable evidence scoped to exact policy, schema, input, data, function, evaluator, and time generations. It is delivered to an independent enforcement boundary that checks applicability and current authority. Obligations are typed authorized plans whose execution, atomicity, idempotency, failure, and reconciliation are separately evidenced.

## Consequences

- Decisions cannot be replayed as ambient capability tokens.
- Enforcement and domain effects have explicit milestones.
- Unsupported critical obligations fail safely.
- Audit can correlate decision, enforcement, obligation, and effect without conflating them.
