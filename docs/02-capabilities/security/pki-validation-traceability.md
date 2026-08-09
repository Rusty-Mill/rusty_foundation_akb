# PKI-validation assertion and benchmark traceability

**Status:** Draft promotion-unit mapping  
**Authority:** [PKI-validation foundations](pki-README.md)  
**Promotion unit:** `rm.promotion.security.pki-validation`

| Assertion | Covered normative source | Requirements | Verification intention |
|---|---|---|---|
| `rm.assertion.security.pki.certificate@1` | `pki-certificates.md` | CERT-0001–0007 | Verify typed bounded parsing, original signed bytes, extension criticality, malformed/ambiguous cases, presentation separation, and side-effect-free inspection. |
| `rm.assertion.security.pki.trust-store@1` | `pki-trust-stores.md` | TRUST-0001–0007 | Verify anchor/intermediate/distrust/store-role separation, provenance/precedence, non-self-signature trust, side-effect-free snapshots, mutation separation, and invalidation. |
| `rm.assertion.security.pki.path-construction@1` | `pki-path-construction.md` | PATH-0001–0007 | Verify untrusted unordered candidates, issuer/signature proof, bounds, alternate/cross-signed/loop cases, provenance, deterministic preference, and distinct no-path/indeterminate outcomes. |
| `rm.assertion.security.pki.path-validation@1` | `pki-path-validation.md` | VALIDATE-0001–0007 | Verify exact path/anchor/purpose/policy, per-role checks, time/algorithm/status policy, evidence-rich result, and identity/authorization nonclaims. |
| `rm.assertion.security.pki.identity@1` | `pki-identity-matching.md` | IDENTITY-0001–0007 | Verify typed consumer-profile identities, exact canonicalization/name sources/wildcards/IDNs, display separation, proof-of-possession nonclaim, and complete pin policy. |
| `rm.assertion.security.pki.status@1` | `pki-revocation.md` | STATUS-0001–0007 | Verify per-certificate status distinctions, source provenance/precedence, responder/freshness/replay, explicit failure policy, bounds, nonclaims, and dependency invalidation. |
| `rm.assertion.security.pki.network-cache@1` | `pki-network-cache.md` | NETWORK-0001–0007 | Verify attenuated retrieval, hostile locator/SSRF/recursion defenses, network-state distinctions, complete cache keys/evidence, concurrency/cancellation, and no hidden blocking I/O. |
| `rm.assertion.security.pki.result@1` | `pki-results-lifecycle.md` | RESULT-0001–0007 | Verify terminal categories, reproducible evidence, scoped overrides/pins, earliest-expiry/dependency invalidation, redaction, and consumer authorization separation. |
| `rm.assertion.security.pki.dependencies@1` | `pki-validation-dependencies.md` | DEPENDENCY-0001–0005 | Verify crypto/time/network/authority/provider/profile/consumer composition without hidden retrieval, trust, identity, or authorization inference. |
| `rm.assertion.security.pki.quality@1` | `pki-validation-cross-cutting-review.md` | QUALITY-0001–0004 | Verify six quality dimensions, evidence methods/nonclaims, specialist obligations, privacy, and lifecycle response. |
| `rm.assertion.security.pki.sources@1` | `pki-validation-source-review.md` | SOURCE-0001–0005 | Bind RFC update sets, identity profiles, platform sources, exact frontier, invalidation, and documented-observed separation. |
| `rm.assertion.security.pki.ownership@1` | `pki-validation-ownership.md` | OWNER-0001–0004 | Verify accountable roles, bounded adversarial trial, trust/network/lifecycle matrix, stop conditions, and closeout. |
| `rm.assertion.security.pki.readiness-boundary@1` | `pki-validation-readiness-review.md`, `pki-validation-traceability.md` | READINESS-0001–0003, TRACE-0001–0003 | Verify unit dossier reviewability without implying trust-store/profile/provider selection, implementation, identity, authorization, or release readiness. |

## Benchmark scenario mapping

| Scenario | Benchmark requirements | Workloads | Comparison contract |
|---|---|---|---|
| `rm.benchmark.security.pki.parse@1` | `RM-PKI-BENCH-0001`, `RM-PKI-BENCH-0005`, `RM-PKI-BENCH-0006` | PKI-BENCH-001 | Same exact bytes/object type, parser/profile, limits, valid/malformed classification, original-byte retention, cold/warm state, and output evidence. |
| `rm.benchmark.security.pki.trust-snapshot@1` | `RM-PKI-BENCH-0002`, `RM-PKI-BENCH-0005`, `RM-PKI-BENCH-0006` | PKI-BENCH-002 | Same provider/store scopes/sources/precedence, item classes/count, privacy filter, generation publication, and hidden/unavailable evidence. |
| `rm.benchmark.security.pki.construct@1` | `RM-PKI-BENCH-0003`, `RM-PKI-BENCH-0005`, `RM-PKI-BENCH-0006` | PKI-BENCH-003 | Same leaf/candidate graph/trust snapshot, construction policy, algorithms, provenance, bounds, path/rejection set, preference, and network/cache inputs. |
| `rm.benchmark.security.pki.validate@1` | `RM-PKI-BENCH-0003`, `RM-PKI-BENCH-0005`, `RM-PKI-BENCH-0006` | PKI-BENCH-004 | Same exact path/anchor/purpose/policy/time/identity/algorithm/status inputs, check set, result category, warnings, unknowns, and nonclaims. |
| `rm.benchmark.security.pki.status-network@1` | `RM-PKI-BENCH-0004`, `RM-PKI-BENCH-0005`, `RM-PKI-BENCH-0006` | PKI-BENCH-005 | Same status objects/freshness, network/proxy/redirect/SSRF policy, cache state, requests/bytes, failure schedule, and hard/soft result. |
| `rm.benchmark.security.pki.cache@1` | `RM-PKI-BENCH-0002`, `RM-PKI-BENCH-0004`, `RM-PKI-BENCH-0005`, `RM-PKI-BENCH-0006` | PKI-BENCH-006 | Same complete cache keys, entries/age/partition, dependency changes, invalidation/revalidation, memory/storage, and convergence result. |
| `rm.benchmark.security.pki.concurrent@1` | `RM-PKI-BENCH-0004`, `RM-PKI-BENCH-0005`, `RM-PKI-BENCH-0006` | PKI-BENCH-007 | Same validation mix, provider/network/cache saturation, deduplication, cancellation, queue/fairness, bounds, and recovery. |
| `rm.benchmark.security.pki.lifecycle@1` | `RM-PKI-BENCH-0002`, `RM-PKI-BENCH-0004`, `RM-PKI-BENCH-0005`, `RM-PKI-BENCH-0006` | PKI-BENCH-008 | Same trust/distrust/pin/policy/status/provider/clock update, expiry storm, dependency graph, revalidation, restart, and cleanup semantics. |

**RM-PKI-TRACE-0001:** Every PKI-validation requirement MUST map to a stable assertion and executable case or review method before unit promotion.

**RM-PKI-TRACE-0002:** Windows, Linux, and macOS evidence MUST preserve assertion identity while reporting exact RFC/profile update set, provider/library/platform generation, trust sources/snapshot, policy/purpose/identity, time/clock, network/status/cache mode, and overrides separately.

**RM-PKI-TRACE-0003:** Parsing, inspection, candidate acquisition, path construction, path selection, validation, identity matching, status retrieval/validation, result publication, authentication proof-of-possession, and authorization MUST remain distinct evidence milestones.
