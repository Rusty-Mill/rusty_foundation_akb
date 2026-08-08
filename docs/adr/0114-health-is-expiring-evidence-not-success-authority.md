# ADR-0114: Health is expiring evidence, not success authority

## Status

Accepted

## Context

Readiness flags, active probes, passive error rates, dependency checks, and outlier algorithms observe different boundaries at different times. A ready endpoint can fail the next request; an ejected endpoint may be healthy for another client; a successful probe does not prove authorization, capacity, data consistency, or domain correctness. Treating “healthy” as truth creates unsafe routing and misleading availability claims.

## Decision

Rusty Mill models every health signal as expiring evidence tied to the exact endpoint generation, observer, checked boundary, policy generation, time, and reason. Routing policy determines eligibility from multiple observations and explicit all-unhealthy behavior. Endpoint authentication, request admission, protocol success, and domain effects remain separate milestones.

## Consequences

- Active and passive evidence can disagree without corrupting endpoint identity.
- Outlier ejection is local routing state, not lifecycle authority.
- Health age and boundary appear in diagnostics and conformance.
- Availability claims use observed request outcomes, not probe counts alone.
