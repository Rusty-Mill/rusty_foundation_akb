# Cryptography and key-management ownership and trial readiness

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Accountable owner | Cryptography and key-management owner, initially exercised by Foundation maintainers |
| Architecture reviewer | Foundation architecture review |
| Cryptography reviewer | Independent qualified cryptography review for policy, algorithms/compositions, nonce/domain separation, keys, encodings, oracles, leakage, and transitions |
| Platform/provider reviewer | Foundation provider review for module/artifact/hardware/firmware/configuration, lifecycle, attestation, certification, and fallback claims |
| Evidence reviewer | Foundation conformance, interoperability, lifecycle, and performance review |
| Compatibility authority | Foundation architecture review until a dedicated compatibility council exists |

## Ownership duties

The owner maintains workload/policy resolution, algorithms/parameters/encodings, key authority/lifecycle, hash/MAC/KDF/password derivation, AEAD, signatures/verification/agreement/KEM, import/export/wrapping, providers/hardware/remote operation, attestation/certification, buffers/concurrency/async/failure, dependencies/profiles, source/quality review, conformance, benchmarks, and dossier boundaries. Provider owners maintain distinct module/artifact/platform/hardware/firmware/configuration/mode frontiers. Consumer owners retain protocols, formats, trust/identity, nonce allocation topology, key adoption/rotation, replay/freshness, and application acceptance.

## Bounded trial plan

A later disposable trial may implement only enough isolated adapters to execute reviewed published and independently generated vectors plus malformed/adversarial cases for a small policy-selected suite on one exact software/native provider per platform. It may exercise policy/provider mismatch and fallback denial, ephemeral/persisted key lifecycle, non-export enforcement, nonce concurrency/crash/snapshot strategy, streaming/buffer aliasing, invalid tags/signatures/keys/encodings, prompt/headless/cancel/remote or hardware failure where selected, rotation/migration, self-test/provider loss, and staged/sustained benchmarks.

The trial uses the [foundation trial template](../../05-governance/implementation-trials/trial-template.md), generated non-production keys/data, disposable stores/accounts/modules/sessions/devices or emulators, isolated native/unsafe code, bounded algorithms/parameters/input/concurrency/time, pinned corpora/toolchains/providers, and no production credentials, certificates, artifacts, protocols, or data. It does not select a permanent Rust API, crates/workspaces, default algorithms/providers, protocol suites, remote/HSM vendors, certification claims, numeric budgets, or release support.

Stop conditions include policy/provider substitution, legacy mode used for new protection, nonce collision/owner ambiguity, unauthenticated plaintext release, malformed-input acceptance, key/authority/export broadening, material/derived-artifact leakage, false constant-time/hardware/certification claim, silent software fallback, fabricated cancellation/destruction, unsafe destructive lifecycle tests, unbounded resource/DoS behavior, provenance loss, corpus/license concern, or material drift.

**RM-CRYPTO-OWNER-0001:** Promotion and trial records MUST name accountable people for the unit and every claimed policy/algorithm/provider/module/platform/hardware/configuration/certification context, exact generations/revisions, reviewer independence/qualifications, and unresolved limitations.

**RM-CRYPTO-OWNER-0002:** Trial hypotheses MUST distinguish policy resolution, provider discovery/activation/self-test, key creation/import/open/publication, operation acceptance/progress/result, output authentication/publication, cancellation/unknown outcome, rotation/revocation/destruction, backup/replica residuals, attestation, and certification.

**RM-CRYPTO-OWNER-0003:** This bounded plan is evidence only and MUST NOT authorize production cryptography, native/unsafe code, algorithm/provider/library dependencies, hardware/remote services, keys/credentials, host security configuration, certification language, packaging, or release.

**RM-CRYPTO-OWNER-0004:** Closeout MUST account for every generated key/material, public/ciphertext/signature artifact, nonce/counter state, provider/module/session/store/device fixture, backup/replica, temporary buffer, log/trace/report, dependency/cache, and host change; remove only verified disposable assets and retain sanitized reproducible evidence/nonclaims.
