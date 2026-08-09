# ADR-0126: Directory membership is evidence, not effective authority

## Status

Accepted

## Context

Directories expose users, groups, nested membership, dynamic groups, role-like objects, and attributes that products commonly treat as authorization. Those observations may be stale, partial, issuer-scoped, ambiguous across tenants, or differently interpreted by providers. Even an accurate membership says nothing by itself about the current entitlement mapping, policy, session, or resource-local enforcement.

## Decision

Rusty Mill models directory facts and group membership as versioned provenance-bearing evidence. Entitlement assignment, policy evaluation, credential/session state, and native resource authorization remain separate stages. Every effective-access claim names the relevant generations, freshness, unknowns, and enforcement boundary.

## Consequences

- Group and attribute changes explicitly invalidate dependent decisions.
- Adapters cannot turn provider roles into portable authority silently.
- Products retain flexible RBAC, ABAC, relationship, and resource-local authorization designs.
- Effective-access reports remain qualified evidence rather than universal truth.
