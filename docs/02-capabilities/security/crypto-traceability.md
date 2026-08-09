# Cryptography and key-management assertion and benchmark traceability

**Status:** Draft promotion-unit mapping  
**Authority:** [Cryptographic foundations](crypto-README.md)  
**Promotion unit:** `rm.promotion.security.cryptography`

| Assertion | Covered normative source | Requirements | Verification intention |
|---|---|---|---|
| `rm.assertion.security.crypto.policy@1` | `crypto-policy.md` | POLICY-0001–0007 | Verify stable identities, exact parameters/purposes, versioned generation-versus-legacy policy, no substitution, transition/downgrade resistance, scoped compliance, and re-evaluation. |
| `rm.assertion.security.crypto.keys@1` | `crypto-keys.md` | KEY-0001–0008 | Verify key/metadata/authority separation, per-operation attenuation, default non-export, generation evidence, lifecycle/rotation/destruction states, and observable races. |
| `rm.assertion.security.crypto.derive@1` | `crypto-hash-mac-kdf.md` | DERIVE-0001–0007 | Verify exact hash/MAC/KDF/password semantics, comparison, domain separation, typed salt/nonce/context roles, bounds, streaming, and terminal behavior. |
| `rm.assertion.security.crypto.aead@1` | `crypto-aead.md` | AEAD-0001–0007 | Verify authenticated-only base contract, nonce ownership across lifecycle, format/AAD/framing, no unauthenticated plaintext, oracle control, aliasing, and limits/rekey. |
| `rm.assertion.security.crypto.public-key@1` | `crypto-public-key.md` | PUBLIC-0001–0007 | Verify signature/verification scope and nonclaims, strict inputs, agreement/KDF, hybrid composition, KEM/encryption rejection, and protocol/PKI separation. |
| `rm.assertion.security.crypto.transfer@1` | `crypto-import-export.md` | TRANSFER-0001–0007 | Verify typed bounded formats, atomic validation/publication, secret exposure, distinct export authority, authenticated wrapping, opaque references, and separately governed custody/recovery. |
| `rm.assertion.security.crypto.provider@1` | `crypto-providers-attestation.md` | PROVIDER-0001–0008 | Verify provider provenance/boundaries, exact hardware claims, side-effect-free discovery, activation, attestation scope/nonclaims, certification boundary, and no weakening on failure. |
| `rm.assertion.security.crypto.operation@1` | `crypto-operations.md` | OP-0001–0008 | Verify exact bytes/buffers, ownership/copies, concurrency/affinity, async milestones/cancellation, error-oracle policy, exposure map, scoped side-channel evidence, and sync completeness. |
| `rm.assertion.security.crypto.dependencies@1` | `crypto-dependencies.md` | DEPENDENCY-0001–0005 | Verify random, authority, secret-value/store, provider, profile, protocol/PKI, and lifecycle composition without inferred universal edges. |
| `rm.assertion.security.crypto.quality@1` | `crypto-cross-cutting-review.md` | QUALITY-0001–0004 | Verify six quality dimensions, exact methods/nonclaims, specialist obligations, and transition operations. |
| `rm.assertion.security.crypto.sources@1` | `crypto-source-review.md` | SOURCE-0001–0005 | Bind standards/provider sources, exact revision/platform frontier, invalidation, documented-observed separation, and mutable catalog treatment. |
| `rm.assertion.security.crypto.ownership@1` | `crypto-ownership.md` | OWNER-0001–0004 | Verify accountable roles, bounded multi-provider trial, algorithm/key/lifecycle matrix, stop conditions, and closeout. |
| `rm.assertion.security.crypto.readiness-boundary@1` | `crypto-readiness-review.md`, `crypto-traceability.md` | READINESS-0001–0003, TRACE-0001–0003 | Verify unit dossier reviewability without implying algorithm/provider approval, certification, implementation, or release readiness. |

## Benchmark scenario mapping

| Scenario | Benchmark requirements | Workloads | Comparison contract |
|---|---|---|---|
| `rm.benchmark.security.crypto.resolve@1` | `RM-CRYPTO-BENCH-0001`, `RM-CRYPTO-BENCH-0005`, `RM-CRYPTO-BENCH-0006` | CRYPTO-BENCH-001 | Same workload/policy generation, provider inventory/provenance, plan result, cold/warm state, activation boundary, and failure oracle. |
| `rm.benchmark.security.crypto.key-lifecycle@1` | `RM-CRYPTO-BENCH-0002`, `RM-CRYPTO-BENCH-0005`, `RM-CRYPTO-BENCH-0006` | CRYPTO-BENCH-002, 008 | Same key plan/origin/protection/export/interaction, lifecycle milestones, rotation/migration inputs, failure/reconciliation, and evidence. |
| `rm.benchmark.security.crypto.symmetric@1` | `RM-CRYPTO-BENCH-0003`, `RM-CRYPTO-BENCH-0005`, `RM-CRYPTO-BENCH-0006` | CRYPTO-BENCH-003–005 | Same exact hash/MAC/KDF/AEAD semantics, sizes/segmentation, nonce/context/AAD, invalid cases, buffers, batching/concurrency, and provider path. |
| `rm.benchmark.security.crypto.public-key@1` | `RM-CRYPTO-BENCH-0003`, `RM-CRYPTO-BENCH-0005`, `RM-CRYPTO-BENCH-0006` | CRYPTO-BENCH-006 | Same algorithm/parameters/encoding/context, key generation/protection, valid/invalid inputs, KDF/composition, concurrency, and provider path. |
| `rm.benchmark.security.crypto.provider@1` | `RM-CRYPTO-BENCH-0004`, `RM-CRYPTO-BENCH-0005`, `RM-CRYPTO-BENCH-0006` | CRYPTO-BENCH-007, 009 | Same software/OS/hardware/remote semantics, prompt/session/rate/failure state, sustained duration/load, fallback denial, and quality disclosures. |

**RM-CRYPTO-TRACE-0001:** Every cryptography/key-management requirement MUST map to a stable assertion and executable case or review method before unit promotion.

**RM-CRYPTO-TRACE-0002:** Windows, Linux, and macOS evidence MUST preserve assertion identity while reporting exact policy, algorithm/parameters/encoding, provider/module/artifact, platform/hardware/firmware/configuration, key origin/protection/export, and operating mode separately.

**RM-CRYPTO-TRACE-0003:** Policy resolution, provider discovery, activation/self-test, key creation/import/open, operation acceptance/progress/result, public publication, rotation/revocation/destruction, replica/backup effects, and certification/attestation claims MUST remain distinct evidence milestones.
