# `rm.security.attenuate` — Authority attenuation

| Field | Value |
|---|---|
| Status | Draft |
| Contract version | 0.1.0 |
| Domain | Security |
| Owner | Unassigned |
| Candidate profiles | CLI, Desktop, Server, Embedded/headless |

## Purpose

Derive a child authority whose usable rights are provably contained by a parent authority. This provides a common semantic operation for least-authority composition without pretending every platform can revoke, serialize, or independently enforce every constraint.

## Non-goals

Elevation, authentication, unrestricted native-handle duplication, cross-machine delegation, durable authority serialization, revocation of all aliases, and creation of a process sandbox are outside this capability.

## Requirements

- **RM-SECURITY-ATTENUATE-0001:** Every derived authority **MUST** be a subset of its parent across operation, resource, lifetime, audience, and further-delegation dimensions.
- **RM-SECURITY-ATTENUATE-0002:** An unrepresentable or incomparable restriction **MUST** fail; it **MUST NOT** be silently dropped.
- **RM-SECURITY-ATTENUATE-0003:** Derivation **MUST NOT** add rights from ambient process credentials or an unrelated authority.
- **RM-SECURITY-ATTENUATE-0004:** The result **MUST** preserve an auditable, non-secret provenance chain to its parent and attenuation request.
- **RM-SECURITY-ATTENUATE-0005:** A caller **MUST** be able to inspect the effective portable constraint summary without receiving native credentials or secret material.
- **RM-SECURITY-ATTENUATE-0006:** Closing a child **MUST NOT** close its parent; closing a parent **MUST** have explicitly declared effects on existing children.
- **RM-SECURITY-ATTENUATE-0007:** Duplication and transfer **MUST** preserve or further narrow the effective constraints and delegation depth.
- **RM-SECURITY-ATTENUATE-0008:** Revocation support **MUST** declare scope, latency, already-started-operation behavior, and native aliases outside provider control.
- **RM-SECURITY-ATTENUATE-0009:** Failed derivation **MUST** leave the parent usable and unchanged.
- **RM-SECURITY-ATTENUATE-0010:** Errors and audit events **MUST NOT** expose native credentials, secret policy inputs, or authority material.

## Enforcement levels

| Level | Meaning |
|---|---|
| A0 — Logical | Rusty Mill APIs enforce narrowing, but native aliases or bypass paths may retain broader access |
| A1 — Native object | The derived native object enforces the declared operation/resource subset |
| A2 — Isolated context | A separate execution context enforces the subset and excludes known ambient inheritance |
| A3 — Defense in depth | Independent native controls enforce intersecting constraints with adversarial evidence |

Levels are scoped claims, not a total ordering of platform security. A provider states which dimensions each native control covers and all known bypass assumptions.

## Concurrency and failure

Concurrent derivations from the same parent do not mutate one another. Revocation and close may race with derivation; exactly one documented terminal result occurs, and a returned child satisfies its declared validity semantics. There is no implicit retry after policy or native denial.

## Platform realization direction

Windows restricted tokens and scoped handles, Linux credential/capability changes and descriptor passing, and macOS sandbox-scoped resources are candidate ingredients. A provider may truthfully offer only A0 or A1 for a given authority kind. Constructing a sandboxed child belongs to the [restricted execution service](restricted-execution.md).

