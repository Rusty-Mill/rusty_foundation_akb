# ADR-0130: Effective access is a versioned derivation, not stored truth

## Status

Accepted

## Context

Products often store or display a permissions Boolean or flattened list as if it were authoritative. Actual access can depend on current roles, attributes, relationships, ownership, grants, denies, delegation, tenant policy, resource state, environment, native controls, and their respective consistency frontiers. Materialized summaries inevitably lag and may omit contextual or downstream checks.

## Decision

Rusty Mill defines effective access as a qualified derivation over named subject/actor, resource/action scope, context assumptions, policy and data generations, consistency frontier, traversal limits, and native enforcement nonclaims. Cached or materialized access is a versioned projection that must be invalidated and revalidated, not stored authorization truth.

## Consequences

- Reports expose freshness, unknowns, truncation, derivation paths, and enforcement boundaries.
- Access reviews can use the evidence without mistaking it for current universal truth.
- Policy and relationship changes have explicit invalidation dependencies.
- Resource operations still authorize at their effect boundary.
