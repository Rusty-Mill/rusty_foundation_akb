# ADR-0005: Orderly shutdown is a platform service

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

The runtime/time trial initially modeled orderly shutdown as `rm.runtime.shutdown`, alongside monotonic time, deadline timers, and cancellation. Domain analysis showed that shutdown does not represent one independently provided unit of OS behavior. It coordinates multiple capabilities and adds application policy: admission control, dependency ordering, phase deadlines, failure aggregation, and escalation.

The authoritative architecture model assigns coordination and cross-capability policy to platform services. Leaving shutdown as a capability would blur that boundary, place policy in the capability graph, and encourage backends to implement application lifecycle decisions.

## Decision

Classify orderly shutdown as a platform service. It composes `rm.runtime.cancellation` and `rm.time.deadline-timer`, coordinates registered components, and consumes explicit ordering and escalation policy.

The service is excluded from the capability dependency graph and provider negotiation. Its capability dependencies remain visible in a service-composition view. Workload documentation may recommend the service, but capability profiles do not treat it as a capability member.

## Options considered

### Capability

**Advantages:** Uniform discovery and an apparently simple dependency graph.  
**Disadvantages:** Mixes orchestration with backend mechanism, implies independent provider selection, and embeds lifecycle policy at the wrong layer.

### Platform service

**Advantages:** Matches the pyramid, preserves mechanism/policy separation, supports application-defined ordering, and composes independently testable capabilities.  
**Disadvantages:** Requires a service specification and a verification model in addition to capability conformance.

### Domain framework concern

**Advantages:** Maximum application freedom.  
**Disadvantages:** Duplicates a foundational lifecycle facility across frameworks and makes common shutdown guarantees difficult to establish.

## Consequences

- The shutdown document becomes a service specification.
- Capability profiles contain cancellation and timer requirements, not shutdown itself.
- Conformance distinguishes capability assertions from service-behavior assertions.
- The trial validates the model rule that orchestration should be lifted out of capability cycles.
- A general service identity/versioning scheme remains future work; this decision does not invent one prematurely.

## Verification

- The runtime/time capability graph contains only capabilities.
- The service composition view links orderly shutdown to cancellation and deadline timers.
- Shutdown requirements are verified by the service suite, not claimed by OS backends.
