# Authority promotion-unit readiness review

| Field | Value |
|---|---|
| Status | Proposed unit dossier; no maturity change |
| Subject | `rm.promotion.security.authority` |
| Architecture | Model 1.97.0 |
| Proposed decision | Unit planning evidence is reviewable; the unit and security directory remain Draft |
| Implementation authority | None |

| Gate | State | Evidence | Qualification |
|---|---|---|---|
| Contract semantics | Pass | [authority](authority-model.md), [policy](policy-model.md), [delegation](delegation-model.md), [attenuation](attenuation.md), [ADR-0009](../../adr/0009-identity-is-not-authority.md), [ADR-0010](../../adr/0010-native-operation-is-the-authorization-point.md), [ADR-0162](../../adr/0162-attenuation-enforcement-is-a-scoped-claim-vector-not-a-security-score.md) | public API, authority kinds, policy engine, serialization, providers, mechanisms, and consumers remain unselected |
| Unit boundary | Pass | [promotion registry](promotion-units.md), [composition](authority-dependencies.md), [ADR-0163](../../adr/0163-maturity-promotion-units-follow-evidence-boundaries-not-directory-layout.md) | vocabulary, policy, attenuation, delegation, provenance, enforcement, and revocation share semantic evidence; restricted execution and resource domains retain their boundaries |
| Dependencies/profiles | Pass | [composition](authority-dependencies.md), [server profile](../profiles/foundation-server.md), [windowed desktop profile](../profiles/foundation-windowed-desktop.md) | no identity, policy, provider, runtime, transport, sandbox, resource, ambient-authority, or revocation relationship is universal |
| Platform/source review | Pass | [platform research](platform-research.md), [source review](authority-source-review.md) | exact OS/provider/mechanism/deployment/authority/resource/policy/transport matrices remain trial inputs |
| Cross-cutting planning | Pass | [quality review](authority-cross-cutting-review.md) | no qualified security, platform, privacy/accessibility, operational, or production lifecycle signoff exists |
| Assertions/cases | Pass | [traceability](authority-traceability.md), [conformance](conformance.md) | fixtures/cases are specified but not selected, pinned, or executed |
| Benchmark scenarios | Pass | [scenario mapping](authority-traceability.md#benchmark-scenario-mapping), [benchmarks](benchmarks.md) | no baseline, budget, native-performance, propagation, availability, or security conclusion exists |
| Ownership/trial bounds | Qualified | [ownership](authority-ownership.md), [trial governance](../../05-governance/implementation-trials/README.md) | roles exist; named qualified people, independent review, authorization, disposable environments, artifacts, and closeout do not |

The dossier makes authority planning evidence reviewable without granting any subject, process, component, provider, or operator permission. It does not establish that two platform mechanisms are equivalent, that a policy permit predicts future access, that an A-level is a security score, or that close/expiry/revocation eliminates aliases or committed effects.

**RM-SECURITY-AUTHORITY-READINESS-0001:** Dossier presence or planned evidence MUST NOT be represented as identity proof, authority, permission, native enforcement equivalence, sandbox strength, complete revocation, native performance, implementation, profile satisfaction, or release evidence.

**RM-SECURITY-AUTHORITY-READINESS-0002:** A named review MUST bind exact authority/resource kinds, contract and policy/evaluator versions, subject/resource/environment evidence and generations, platform/provider/native mechanisms, deployment/sandbox, ambient inputs, transfer/channel topology, enforcement claim vectors, aliases/inheritance/bypasses, clocks, invalidation/revocation, consumers, exclusions, findings/waivers, accountable people, and decision date.

**RM-SECURITY-AUTHORITY-READINESS-0003:** Promotion MUST require executed adversarial type/namespace, policy/freshness/cache/race, attenuation, delegation/transfer/failure, ambient inheritance, enforcement/bypass, disclosure, expiry/revocation/partition, reconciliation, cross-provider differential, cross-cutting, and staged/sustained benchmark evidence.
