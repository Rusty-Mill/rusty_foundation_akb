# PKI-issuance promotion-unit readiness review

| Field | Value |
|---|---|
| Status | Proposed unit dossier; no maturity change |
| Subject | `rm.promotion.security.pki-issuance` |
| Architecture | Model 1.96.0 |
| Proposed decision | Unit planning evidence is reviewable; the unit and security directory remain Draft |
| Implementation authority | None |

| Gate | State | Evidence | Qualification |
|---|---|---|---|
| Contract semantics | Pass | [foundations](pki-issuance-README.md), enrollment/authority/request/policy/protocol/renewal/CA specifications, [ADR-0090](../../adr/0090-certificate-requests-prove-key-possession-not-issuance-authority.md), [ADR-0091](../../adr/0091-renewal-creates-a-new-credential-generation-with-explicit-continuity.md) | public API, crates, providers, protocols, profiles, CAs, stores, and deployment consumers remain unselected |
| Unit boundary | Pass | [promotion registry](promotion-units.md), [composition](pki-issuance-dependencies.md), [ADR-0163](../../adr/0163-maturity-promotion-units-follow-evidence-boundaries-not-directory-layout.md) | request through CA and lifecycle operations share authority/policy/durability evidence; validation remains separate |
| Dependencies/profiles | Pass | [composition](pki-issuance-dependencies.md), [server profile](../profiles/foundation-server.md), [windowed desktop profile](../profiles/foundation-windowed-desktop.md) | exact edges are classified; no protocol, CA, key provider, proofing, trust, installation, runtime, identity, or authorization edge is universal |
| Platform/source review | Pass | [platform research](pki-issuance-platform-research.md), [source review](pki-issuance-source-review.md) | exact profiles, updates, platforms, providers, CAs, key stores, proofing, and deployment paths remain trial inputs |
| Cross-cutting planning | Pass | [quality review](pki-issuance-cross-cutting-review.md) | no qualified PKI/cryptography, CA-operations, platform, privacy/accessibility, or production lifecycle signoff exists |
| Assertions/cases | Pass | [traceability](pki-issuance-traceability.md), [conformance](pki-issuance-conformance.md) | fixtures/cases are specified but not selected, licensed, pinned, or executed |
| Benchmark scenarios | Pass | [scenario mapping](pki-issuance-traceability.md#benchmark-scenario-mapping), [benchmarks](pki-issuance-benchmarks.md) | no baseline, budget, native-performance, fleet-load, CA-durability, recovery, or availability conclusion exists |
| Ownership/trial bounds | Qualified | [ownership](pki-issuance-ownership.md), [trial governance](../../05-governance/implementation-trials/README.md) | roles exist; named qualified people, independent review, authorization, disposable PKI, artifacts, and closeout do not |

The dossier makes the issuance planning evidence reviewable without authorizing any name, profile, certificate, key, issuer, protocol, account, store, service binding, trust relationship, renewal, or revocation. An issued certificate is not proof of installation, activation, relying-party acceptance, identity, or application authority.

**RM-PKI-ISSUANCE-READINESS-0001:** Dossier presence or planned evidence MUST NOT be represented as issuance authorization, identity proof, key possession, certificate validity/trust, successful installation/activation, relying-party acceptance, native performance, implementation, profile satisfaction, or release evidence.

**RM-PKI-ISSUANCE-READINESS-0002:** A named review MUST bind exact standards/profile/update set, platform/provider/protocol/CA, key protection, proofing/authorization, request and certificate policy, ledger/durability, status/transparency, network/clock/retry, installation/activation consumer, exclusions, findings/waivers, accountable people, and decision date.

**RM-PKI-ISSUANCE-READINESS-0003:** Promotion MUST require executed adversarial authority/POP/request/policy/protocol/install/activation/lifecycle evidence, cross-provider differentials, CA durability and recovery, privacy/accessibility review, staged/sustained benchmarks, and consumer-qualified identity/trust/authorization nonclaims.
