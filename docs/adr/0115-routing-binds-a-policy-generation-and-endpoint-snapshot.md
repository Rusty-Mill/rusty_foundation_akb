# ADR-0115: Routing binds a policy generation and endpoint snapshot

## Status

Accepted

## Context

Discovery systems return candidates with priorities, weights, labels, locality, and readiness. Clients, proxies, meshes, and servers then filter and balance them using independently changing policy, load, affinity, security, and failure evidence. Allowing discovery metadata or a live mutable map to decide implicitly makes attempts unreproducible, enables metadata privilege escalation, and mixes configuration generations.

## Decision

Rusty Mill makes each routing decision evidence over one resolved service identity, immutable endpoint-snapshot revision, immutable route/balancer/security policy generation, request/tenant context, health/admission observations, and attempt budget. Discovery metadata is typed input with provenance and routing authority, not executable policy. Attempts retain the decision lineage even if later generations arrive.

## Consequences

- Route outcomes are explainable and replayable within declared nondeterminism.
- Configuration updates affect new decisions at explicit boundaries.
- Untrusted endpoint labels cannot create privileged routes.
- Retries and failover can select newer snapshots only under explicit policy.
