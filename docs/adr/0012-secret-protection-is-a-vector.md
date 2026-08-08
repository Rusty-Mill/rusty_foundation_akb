# ADR-0012: Secret protection is a vector, not a level

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

Native secret mechanisms vary independently in persistence, subject binding, interaction, exportability, availability, replication, deletion, hardware use, and assurance. A single “secure storage” boolean or ordered quality level would imply false comparability—for example, hardware-backed non-exportable keys and user-synchronized passwords solve different problems.

## Decision

Secret-store providers publish a scoped protection-claim vector. Profiles constrain each required dimension independently. Unknown never satisfies a requirement, and strength in one dimension cannot compensate for weakness in another. Discovery occurs before plaintext submission where possible. Backup, migration, synchronization, interaction, and export are explicit properties.

The portable model distinguishes a secret-value resource from `rm.security.secret-store`. Secret values control exposure and lifecycle in memory; stores control durable or session-scoped items. Neither implies cryptographic certification, physical erasure, or hardware confinement without exact evidence.

## Options considered

### A single security level

Simple selection, but creates a misleading total order and hides workload-specific requirements.

### Provider-specific labels only

Truthful but prevents portable profiles and systematic negotiation.

### A portable claim vector

More verbose, but preserves independent properties and permits precise matching and evidence.

## Consequences

- Profiles and discovery schemas become multidimensional.
- Providers can expose mechanisms that are strong for one workload and unsuitable for another.
- User interaction and headless availability are first-class selection constraints.
- Documentation and reports must retain deployment/account/configuration scope.

## Verification

Conformance mutates session, lock, prompt, backup/sync, export, sandbox, and account conditions and verifies that observations and selection change without silent fallback.

