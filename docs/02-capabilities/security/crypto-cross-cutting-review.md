# Cryptography and key-management cross-cutting review

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Review frontier | cryptography/key-management foundations 0.1.0; architecture model 1.94.0 |
| Accountable owner | Cryptography and key-management owner |
| Open blocking findings | None for dossier reviewability; cryptographic/platform specialist review, exact policy/provider choices, executed vectors, leakage analysis, and implementation evidence remain required |

| Dimension | Exact requirements | Planned evidence | Findings, limits, or non-applicability |
|---|---|---|---|
| Security/privacy | POLICY/KEY/DERIVE/AEAD/PUBLIC/TRANSFER/PROVIDER/OP requirements | published and independent vectors, malformed/adversarial corpus, nonce/crash/snapshot matrix, downgrade/fallback mutation, key authority/lifecycle races, exposure canaries, oracle/timing/leakage analysis, attestation/certification review | primitive validity is not protocol safety; constant-time, hardware, non-export, zeroization, approval, and certification are exact scoped claims |
| Performance | CRYPTO-BENCH-0001–0006 | staged cold/warm policy/provider/key/operation/lifecycle runs, size/parameter/concurrency matrices, invalid-input/resource cases, sustained/thermal/fairness tests, equivalent native/provider baselines | semantics, policy, validation, nonces, failure, self-tests, and protection cannot be weakened; no universal budget/native-performance claim exists |
| Accessibility | interaction/remote/hardware operation requirements | keyboard/assistive-technology and spoofing review of provider/product authentication, key identity/purpose/operation/scope, progress/cancel/rate/outage/recovery, headless alternatives | base software primitive may have no UI; inaccessible consent cannot authorize export, fallback, weaker policy, or ambiguous destructive action |
| Internationalization | byte/encoding/policy/error boundaries | locale-independent algorithm/key/provider identities and canonical encodings, bidi/control-safe labels, localized product explanations with stable codes, text-to-byte protocol tests | cryptographic inputs are exact bytes; implicit encoding, Unicode normalization, locale/case conversion, or localized algorithm aliases are prohibited at operation boundaries |
| Observability | OP-0002/0005–0007, PROVIDER-0001/0005–0007 | bounded stage/outcome counters, sanitized causal traces, key/policy/provider generation identifiers, redaction/cardinality/recursion review, material/derived-fingerprint canaries | no private/symmetric material, plaintext, shared secret, derived key, nonce/counter, sensitive metadata, signatures/ciphertexts when sensitive, or secret-derived identifier |
| Operations | policy/provider/key lifecycle and transition requirements | provider update/removal/self-test, hardware/remote loss/rate/session, policy/algorithm migration, rotate/revoke/destroy, backup/restore/snapshot, rollback, crash/restart, compromise/recovery drills | policy/provider/configuration/firmware/certification drift invalidates claims; legacy-read and new-write policy remain separate; destruction residuals are explicit |

**RM-CRYPTO-QUALITY-0001:** Every trial or promotion review MUST bind all six quality dimensions to exact workload/policy, algorithm/parameters/encoding, provider/module/platform/hardware/configuration/mode, key lifecycle, methods, reviewers, findings, and affected claims.

**RM-CRYPTO-QUALITY-0002:** Performance, accessibility, localization, diagnostics, and operations mechanisms MUST NOT change exact bytes, weaken policy/validation, broaden authority/export, introduce fallback, expose material, or collapse ambiguous provider outcomes.

**RM-CRYPTO-QUALITY-0003:** Algorithm availability, provider support, hardware execution, attestation, validated module status, approved operation, constant-time evidence, and application/composition compliance MUST remain separate claims.

**RM-CRYPTO-QUALITY-0004:** Algorithm and provider transition evidence MUST cover new-write/new-sign, legacy-read/verify/decrypt, multi-generation interoperability, downgrade/rollback, data/key migration, dependent adoption, compromise, and retirement without treating agility as a string substitution.
