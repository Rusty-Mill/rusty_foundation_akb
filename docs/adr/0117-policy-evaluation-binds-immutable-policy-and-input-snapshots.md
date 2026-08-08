# ADR-0117: Policy evaluation binds immutable policy and input snapshots

## Status

Accepted

## Context

Policies, schemas, entity data, group membership, risk, time, functions, and evaluator versions change independently. Reading them lazily during evaluation can mix generations and produce decisions that cannot be reproduced or explained. Ambient clock, network, filesystem, or remote calls also defeat purity, caching, simulation, and bounded execution.

## Decision

Rusty Mill evaluates each entry point against one immutable context containing exact policy/schema/data/function/evaluator generations plus the validated request and explicit time/nondeterministic observations. External acquisition occurs before evaluation or through constrained recorded adapters. Missing, stale, partial, and failed dependencies remain decision evidence rather than silent defaults.

## Consequences

- Decisions are attributable and safely cacheable only by complete dependencies.
- Partial evaluation produces generation-bound residual policy.
- Distribution activates coherent bundles rather than individual mutable files.
- External data freshness and acquisition failures remain visible.
