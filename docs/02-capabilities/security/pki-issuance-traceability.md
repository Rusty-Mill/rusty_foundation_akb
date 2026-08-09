# PKI-issuance assertion and benchmark traceability

**Status:** Draft promotion-unit mapping  
**Authority:** [PKI-issuance foundations](pki-issuance-README.md)  
**Promotion unit:** `rm.promotion.security.pki-issuance`

| Assertion | Covered normative source | Requirements | Verification intention |
|---|---|---|---|
| `rm.assertion.security.pki-issuance.enrollment@1` | `pki-issuance-enrollment.md` | ENROLLMENT-0001–0008 | Verify typed intent/operation, immutable lifecycle milestones/transaction binding, acceptance-versus-effect separation, cancellation/indeterminate reconciliation, retry/idempotency, and evidence-rich results. |
| `rm.assertion.security.pki-issuance.authority@1` | `pki-issuance-authority.md` | AUTHORITY-0001–0008 | Verify authentication versus authorization, typed proofing/control evidence, template nonauthority, agent delegation, workload lifecycle, approval binding, and issuance/trust nonclaims. |
| `rm.assertion.security.pki-issuance.request@1` | `pki-issuance-requests.md` | REQUEST-0001–0008 | Verify bounded request parsing, context-bound POP, opaque key generation, scoped attestation, requested-versus-issued separation, and disabled-by-default server key/escrow workflows. |
| `rm.assertion.security.pki-issuance.policy@1` | `pki-issuance-policy.md` | POLICY-0001–0009 | Verify immutable profile construction, no blind CSR copy, role separation, time/serial durability, pre-sign revalidation, auditable signing, post-issuance quarantine, and CT/precertificate boundaries. |
| `rm.assertion.security.pki-issuance.protocol@1` | `pki-issuance-protocols.md` | PROTOCOL-0001–0006, DELIVERY-0001–0003 | Verify exact protocol resources, authentication/bootstrap/POP variance, redirect/RA/SSRF controls, response binding, delivery/install/key association/activation separation, and offline custody. |
| `rm.assertion.security.pki-issuance.renewal@1` | `pki-issuance-renewal.md` | RENEWAL-0001–0009 | Verify renewal windows/ARI nonauthority, new generations, explicit continuity/recovery, activation/health/retirement milestones, fleet spreading, and separate revocation authority. |
| `rm.assertion.security.pki-issuance.ca@1` | `pki-issuance-ca-operations.md` | CA-0001–0010 | Verify CA identity/roles/ceremonies, durable ledger/serials, release controls, hierarchy migration, clone-safe recovery, compromise response, termination, and scoped audit/certification. |
| `rm.assertion.security.pki-issuance.cross-cutting@1` | `pki-issuance-security-accessibility.md`, `pki-issuance-cross-cutting-review.md` | CROSS-0001–0008, QUALITY-0001–0004 | Verify hostile-input/network defenses, secret/privacy controls, accessible interaction/operations, correlation/redaction, and six-dimension evidence. |
| `rm.assertion.security.pki-issuance.conformance@1` | `pki-issuance-conformance.md` | CONFORMANCE-0001–0009 | Verify request/authority/POP/issuer/protocol/delivery/renewal/CA/cross-platform planned case coverage and exact evidence frontier. |
| `rm.assertion.security.pki-issuance.dependencies@1` | `pki-issuance-dependencies.md` | DEPENDENCY-0001–0005 | Verify authority/crypto/random/PKI-validation/network/store/service/time/profile composition without inferred issuance, trust, activation, or authorization. |
| `rm.assertion.security.pki-issuance.sources@1` | `pki-issuance-source-review.md` | SOURCE-0001–0005 | Bind protocol/platform sources, RFC update/profile frontier, invalidation, documented-observed separation, and provider-policy scope. |
| `rm.assertion.security.pki-issuance.ownership@1` | `pki-issuance-ownership.md` | OWNER-0001–0004 | Verify accountable roles, bounded private-PKI trial, high-risk CA restrictions, stop conditions, reconciliation, and closeout. |
| `rm.assertion.security.pki-issuance.readiness-boundary@1` | `pki-issuance-readiness-review.md`, `pki-issuance-traceability.md` | READINESS-0001–0003, TRACE-0001–0003 | Verify unit dossier reviewability without implying issuance authority, CA approval, implementation, certification, or release readiness. |

## Benchmark scenario mapping

| Scenario | Benchmark requirements | Workloads | Comparison contract |
|---|---|---|---|
| `rm.benchmark.security.pki-issuance.transaction@1` | `RM-PKI-ISSUANCE-BENCH-0001`, `RM-PKI-ISSUANCE-BENCH-0003`, `RM-PKI-ISSUANCE-BENCH-0006` | PKI-ISSUANCE-BENCH-001 | Same intent, proofing/authority/POP, key plan, profile/policy, protocol, CA/signing/status/CT, delivery/install/activation stages, faults, and evidence. |
| `rm.benchmark.security.pki-issuance.matrix@1` | `RM-PKI-ISSUANCE-BENCH-0002`, `RM-PKI-ISSUANCE-BENCH-0003`, `RM-PKI-ISSUANCE-BENCH-0006` | PKI-ISSUANCE-BENCH-002 | Same interactive/unattended/device/fleet/signing workload, identifiers, key provider/protection, approval, issuer/profile, lifecycle, and platform context. |
| `rm.benchmark.security.pki-issuance.fleet@1` | `RM-PKI-ISSUANCE-BENCH-0003`, `RM-PKI-ISSUANCE-BENCH-0004`, `RM-PKI-ISSUANCE-BENCH-0006` | PKI-ISSUANCE-BENCH-003 | Same population/denominator, ARI/fallback windows, cohorts, retry/outage/emergency schedule, CA/HSM/DNS/network/service capacities, activation/retirement, and missing-device accounting. |
| `rm.benchmark.security.pki-issuance.ca-durability@1` | `RM-PKI-ISSUANCE-BENCH-0003`, `RM-PKI-ISSUANCE-BENCH-0005`, `RM-PKI-ISSUANCE-BENCH-0006` | PKI-ISSUANCE-BENCH-004 | Same ledger/serial/key/hierarchy state, commit/fault/failover/backup/restore schedule, active-clone/rollback oracle, issuance halt, audit, and recovery result. |

**RM-PKI-ISSUANCE-TRACE-0001:** Every PKI-issuance requirement MUST map to a stable assertion and executable case or review method before unit promotion.

**RM-PKI-ISSUANCE-TRACE-0002:** Windows, Linux/portable, and Apple-managed evidence MUST preserve assertion identity while reporting exact protocol/profile/provider/platform, authority/proofing, key protection, issuer/policy, trust/network/time, store/service, and lifecycle scope separately.

**RM-PKI-ISSUANCE-TRACE-0003:** Intent, key generation, POP, authentication/proofing/authorization/approval, submission/pending/challenge, issuance/ledger commit, delivery, installation, association, activation/health, renewal/replacement, old-credential denial, revocation/status publication, and relying-party acceptance MUST remain distinct evidence milestones.
