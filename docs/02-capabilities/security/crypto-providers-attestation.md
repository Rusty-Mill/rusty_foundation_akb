# Providers, hardware, attestation, and certification

**RM-CRYPTO-PROVIDER-0001:** Provider evidence MUST identify implementation/module, version, origin, load/isolation boundary, operation and key-storage boundary, hardware/firmware/device, configuration/mode, self-test state, and transformations/fallbacks.

**RM-CRYPTO-PROVIDER-0002:** `hardware_backed` MUST describe which key generation/storage/operation occurs inside which hardware boundary, which inputs/outputs leave it, authentication/interaction, migration/backup, firmware trust, and fallback behavior.

**RM-CRYPTO-PROVIDER-0003:** Software, OS, hardware, remote/HSM, and plugin providers MUST satisfy the same semantic contracts but may expose different latency, concurrency, availability, interaction, export, attestation, and certification qualities.

**RM-CRYPTO-PROVIDER-0004:** Provider discovery is side-effect-free and does not load untrusted modules, prompt, create keys, contact remote services, or claim algorithm usability. Selection and activation revalidate provenance and policy.

**RM-CRYPTO-PROVIDER-0005:** Attestation is signed, nonce/freshness-bound evidence about a specific key/provider/device/configuration claim. Verification MUST identify trust anchors, endorsement/certificate path, measurements, policy, replay window, privacy impact, and unsupported claims.

**RM-CRYPTO-PROVIDER-0006:** Attestation does not prove application correctness, exclusive key control, absence of side channels, uncompromised firmware, user identity, authorization, or future state beyond its exact evidence and trust model.

**RM-CRYPTO-PROVIDER-0007:** Certification claims MUST survive only while module/version/configuration/operating mode and approved algorithm/use remain within evaluated boundaries; calling a certified primitive through unevaluated composition does not certify the composition.

**RM-CRYPTO-PROVIDER-0008:** Provider failure, removal, firmware/policy update, self-test failure, remote outage, rate limit, or key invalidation creates observable state and cannot silently migrate a non-exportable key to software.
