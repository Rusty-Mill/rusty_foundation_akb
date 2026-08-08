# ADR-0008: Atomic namespace replacement is a capability

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

Atomic replacement consumes directory authority and a prepared file, and often participates in a larger durable-publication workflow. This raised the same classification question as orderly shutdown. Unlike shutdown, however, atomic replacement describes one cohesive namespace transition with a native commit point, independently selectable semantics, and backend-specific conformance.

Data synchronization, metadata policy, backup policy, and directory durability can be composed around the transition. They do not change the fact that the atomic old-or-new namespace binding is a distinct mechanism.

## Decision

Keep `rm.filesystem.atomic-replace` as a capability. Its minimum contract covers one same-filesystem atomic namespace transition, explicit metadata/identity policy, and truthful terminal outcomes. It does not promise persistence after crash or power loss.

A future durable-publication platform service may compose file synchronization, atomic replacement, directory synchronization, recovery records, and application policy. That service cannot redefine the capability's atomicity.

## Options considered

### Platform service only

Combines all publication policy, but obscures the independently native and testable namespace primitive.

### Capability including durability

Provides one convenient operation, but falsely couples namespace visibility to storage-stack guarantees that vary independently.

### Atomic capability plus optional publication service

Preserves the native mechanism and makes stronger durability an explicit composition.

## Consequences

- Replacement stays in the capability graph.
- Namespace atomicity and durability are versioned and tested separately.
- Applications can request replacement without paying for stronger persistence.
- Durable publication can later define recovery and multi-step policy at the service layer.

## Verification

Conformance proves old-or-new visibility and absence of copy-delete fallback. Separate durability evidence proves each requested synchronization boundary.
