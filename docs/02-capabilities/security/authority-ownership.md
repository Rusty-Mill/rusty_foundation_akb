# Authority ownership and trial readiness

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Accountable owner | Authority semantics owner, initially exercised by Foundation maintainers |
| Architecture reviewer | Foundation architecture review |
| Security reviewer | Independent qualified authority, access-control, confused-deputy, delegation, and revocation review |
| Platform/privacy reviewer | Foundation Windows, Linux, macOS, disclosure, accessibility, and privacy review |
| Evidence reviewer | Foundation conformance, interoperability, lifecycle, and performance review |

## Ownership duties

The owner maintains typed vocabulary and descriptors, ambient-authority policy, derivation lattice, policy evaluation/result/provenance/freshness/cache, delegation and transfer transaction, expiry/revocation/alias/in-flight semantics, dependency boundaries, source and quality review, conformance, benchmarks, and the unit dossier. Resource-domain owners retain object identity, operations, effects, native enforcement points, and reconciliation. Provider owners retain exact native mechanisms and deployment claims. Restricted execution retains isolation construction and pre-release verification.

## Bounded trial plan

A later disposable trial may create synthetic principals/claims/policies/resources and non-production Windows tokens/security descriptors, Linux credentials/namespaces/descriptors/Unix sockets, and sandboxed macOS test applications/security-scoped resources. It may exercise namespace collisions, missing/stale evidence, four policy outcomes, cache invalidation, check/use races, ambient inheritance, multidimensional attenuation, borrow/duplicate/move/derive-send, authenticated and hostile channels, audience/replay/depth/use bounds, lost acknowledgments, provider/process failure, close/expiry/revocation with aliases/partitions/in-flight operations, redaction canaries, and staged/sustained benchmarks.

The trial uses the [foundation trial template](../../05-governance/implementation-trials/trial-template.md), isolated accounts/VMs/containers/sandboxes and generated resources, no production identities/policies/permissions/credentials/tokens/bookmarks/services, bounded processes/network/concurrency/time, pinned platforms/providers/toolchains, and complete authority inventory. It does not select permanent Rust APIs/crates, policy engines, serialization, providers, default ambient policy, native mechanisms, performance budgets, packaging, or release support.

Stop conditions include authority expansion, namespace confusion, hidden ambient rights, advisory permit treated as enforcement, stale decision reuse, indeterminate fail-open, confused-deputy access, unprotected transfer, replay/audience/depth bypass, ambiguous move ownership, secret/bearer disclosure, untracked alias, fabricated revocation, unrestricted child execution, uncontrolled host mutation, or inability to reconcile every generated authority and effect.

**RM-SECURITY-AUTHORITY-OWNER-0001:** Promotion and trial records MUST name accountable people for every claimed authority/resource kind, policy/evaluator, native provider/mechanism, platform/deployment, transport, enforcement dimension, revocation context, and consumer, including reviewer independence and qualifications.

**RM-SECURITY-AUTHORITY-OWNER-0002:** Trial hypotheses MUST distinguish identity/claim evidence, authority construction/possession, policy evaluation/cache, native enforcement, operation effect, attenuation, delegation transaction, expiry/revocation, audit, and reconciliation.

**RM-SECURITY-AUTHORITY-OWNER-0003:** This bounded plan is evidence only and MUST NOT authorize implementation, production policy/identity/permission/token/sandbox/resource mutation, native/unsafe code, provider dependencies, packaging, or release.

**RM-SECURITY-AUTHORITY-OWNER-0004:** Closeout MUST account for every synthetic identity/claim/policy, authority generation/alias, native token/descriptor/bookmark/handle, process/channel/resource, cache, revocation state, operation effect, audit/trace/report, dependency/cache, and host change; only verified disposable assets may be removed.
