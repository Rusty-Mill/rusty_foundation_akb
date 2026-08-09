# PKI-validation promotion-unit readiness review

| Field | Value |
|---|---|
| Status | Proposed unit dossier; no maturity change |
| Subject | `rm.promotion.security.pki-validation` |
| Architecture | Model 1.95.0 |
| Proposed decision | Unit planning evidence is reviewable; the unit and security directory remain Draft |
| Implementation authority | None |

| Gate | State | Evidence | Qualification |
|---|---|---|---|
| Contract semantics | Pass | [foundations](pki-README.md), parsing/trust/path/validation/identity/status/network/result specifications, [ADR-0082](../../adr/0082-presented-certificates-are-candidates-not-a-chain.md), [ADR-0083](../../adr/0083-trust-results-are-context-bound-evidence-not-identity-or-authority.md) | public API, parsers, profiles, trust sources, providers/libraries, and product consumer policy remain unselected |
| Unit boundary | Pass | [promotion registry](promotion-units.md), [composition](pki-validation-dependencies.md), [ADR-0163](../../adr/0163-maturity-promotion-units-follow-evidence-boundaries-not-directory-layout.md) | parsing through result lifecycle share compatibility/trust/provider/release evidence; issuance/CA operations remain a separate unit |
| Dependencies/profiles | Pass | [composition](pki-validation-dependencies.md), [server profile](../profiles/foundation-server.md), [windowed desktop profile](../profiles/foundation-windowed-desktop.md) | exact relationships are classified; no universal validator/provider/network/runtime/identity/authorization edge is invented |
| Platform/source review | Pass | [platform research](pki-platform-research.md), [source review](pki-validation-source-review.md) | exact RFC update sets, consumer profiles, providers/libraries, trust stores/programs, platform generations, and network/status matrices are trial inputs |
| Cross-cutting planning | Pass | [quality review](pki-validation-cross-cutting-review.md) | no qualified PKI/cryptography review, implementation/provider result, privacy/accessibility signoff, or production lifecycle evidence exists |
| Assertions/cases | Pass | [traceability](pki-validation-traceability.md), [conformance](pki-conformance.md) | corpora/cases are specified but not selected, licensed, pinned, or executed |
| Benchmark scenarios | Pass | [scenario mapping](pki-validation-traceability.md#benchmark-scenario-mapping), [benchmarks](pki-benchmarks.md) | no baseline run, budget, native-performance, trust-policy, privacy, or availability conclusion exists |
| Ownership/trial bounds | Qualified | [ownership](pki-validation-ownership.md), [trial governance](../../05-governance/implementation-trials/README.md) | roles exist; named qualified people, independent review, authorization, disposable PKI/network environments, artifacts, and closeout do not |

The dossier establishes that validation evidence is reviewable without making any certificate, path, anchor, identity, status service, provider, store, or exception trusted. `trusted=true` remains only a lossy projection over context-bound evidence and cannot authorize a channel, account, artifact, installation, execution, or domain action.

**RM-PKI-READINESS-0001:** Dossier presence or planned evidence MUST NOT be represented as certificate trust, identity, private-key possession, authorization, current status, provider equivalence, native performance, implementation, profile satisfaction, or release evidence.

**RM-PKI-READINESS-0002:** A named review MUST bind exact standards/profile/update set, parser/provider/library/platform, trust sources/snapshot/precedence, policy/purpose/reference identity, time/clock, algorithms, status/network/cache, pins/overrides, exclusions, findings/waivers, qualified accountable people, and decision date.

**RM-PKI-READINESS-0003:** Unit promotion MUST require executed adversarial parsing/path/constraint/identity/status/network/cache/lifecycle evidence, cross-provider differentials, privacy/accessibility review, staged/sustained benchmarks, and consumer-qualified identity/authorization nonclaims.
