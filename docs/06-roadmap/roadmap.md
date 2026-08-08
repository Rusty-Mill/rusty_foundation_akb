# Specification-led roadmap

Dates are intentionally absent until scope and capacity are known. Progress is controlled by evidence-based exit criteria.

## Phase 0 — Foundation

- Charter, principles, glossary, architecture pyramid, governance, and repository strategy accepted.
- ADR/RFC processes operational.

## Phase 1 — Domain inventory and meta-model

- Decompose the initial taxonomy into capabilities.
- Define graph schema, capability specification format, and seed profiles.
- Record platform research without designing APIs prematurely.

## Phase 2 — Contracts and verification design

- Specify behavioral contracts for a thin vertical slice across all three platforms.
- Define conformance report and benchmark schemas.
- Establish security, compatibility, and quality review gates.

## Phase 3 — Reference vertical slice

- Through an accepted RFC, select a small capability set with meaningful async, sync, resource, and platform variance.
- Only then create implementation and verification workspaces.
- Prove native mapping, conformance portability, performance methodology, packaging, and update assumptions.

## Phase 4 — Core profiles

- Expand verified capabilities toward CLI, server, desktop, and constrained/headless profiles.
- Stabilize only capabilities supported by evidence on Windows, Linux, and macOS.

## Phase 5 — Ecosystem scale-out

- Add domain frameworks, tooling, distribution channels, and additional repositories only when explicit forcing functions appear.
- Operate compatibility, deprecation, supply-chain, and governance processes continuously.

## Immediate next decisions

1. ~~Review RFC-0001 and exercise its templates.~~ Completed: [RFC-0001](../rfc/0001-capability-specification-system.md) is Accepted after the runtime/time trial.
2. Review the [runtime and time vertical slice](../02-capabilities/runtime-time/README.md), including its four candidate specifications and open questions.
3. ~~Decide whether orderly shutdown is a capability or a platform service.~~ Resolved as a platform service by [ADR-0005](../adr/0005-orderly-shutdown-is-a-platform-service.md).
4. Review the runtime/time [conformance specification](../02-capabilities/runtime-time/conformance.md) and [benchmark specification](../02-capabilities/runtime-time/benchmarks.md).
5. Define prototype experiments for timer scale, timing behavior, cancellation races, and shutdown ordering.
6. Choose a machine-readable graph format only after at least two reviewed capability specifications expose the requirements.

## Active second slice

The [filesystem foundations analysis](../02-capabilities/filesystem/README.md) now tests the model against path representation, directory-relative authority, file resources, metadata variance, atomic replacement, resolution quality, durability, conformance, and benchmarks. Its next gates are permissions/ACL inspection, directory enumeration, link semantics, and adversarial platform evidence.

## Active third slice

The [security and authority foundations analysis](../02-capabilities/security/README.md) separates identity, security context, explicit authority, policy advice, and native enforcement. It establishes attenuation and fail-closed rules and exercises them through `rm.security.random`. Its next gates are restricted-execution boundary analysis, authority delegation lifecycle, and cross-domain security review criteria.
