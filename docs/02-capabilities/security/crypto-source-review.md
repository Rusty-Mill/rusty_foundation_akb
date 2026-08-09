# Cryptography and key-management source review

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Expires | On policy/standards revision, supported OS/kernel/SDK, provider/module/library, hardware/firmware, configuration/operating mode, certification, or algorithm-catalog change, or 2027-02-08, whichever occurs first |
| Reviewer | Cryptography and key-management owner |
| Open blocking findings | None for dossier reviewability; exact algorithms, libraries/providers, supported generations, validated modules, and leakage evidence remain trial inputs |

| Source | Class and reviewed status | Proposition supported | Impact and limitation |
|---|---|---|---|
| NIST [key-management publications](https://csrc.nist.gov/Projects/key-management/publications), [SP 800-57 Part 1 Rev. 5](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final), and [SP 800-131A Rev. 2](https://csrc.nist.gov/pubs/sp/800/131/a/r2/final) | authoritative guidance/final publications; reviewed 2026-08-08 | lifecycle, strength, use, protection, transition, and algorithm/key-length status guidance | policy input, not an API or automatic compliance result; exact purpose/profile/jurisdiction and newer drafts/standards transitions require review |
| NIST [SP 800-131A Rev. 3 Initial Public Draft](https://csrc.nist.gov/pubs/sp/800/131/a/r3/ipd) | draft transition guidance dated 2024-10-21; reviewed 2026-08-08 | proposed retirement and post-quantum-aware transition direction | informative horizon only; MUST NOT replace Rev. 2 final or become a compliance claim until final/selected by explicit policy |
| Microsoft [CNG portal](https://learn.microsoft.com/en-us/windows/win32/seccng/cng-portal), [primitive functions](https://learn.microsoft.com/en-us/windows/win32/seccng/cng-cryptographic-primitive-functions), and [key-storage providers](https://learn.microsoft.com/en-us/windows/win32/seccertenroll/cng-key-storage-providers) | Microsoft platform contracts; reviewed 2026-08-08 | extensible algorithm/key-storage providers, operation surfaces, and provider-specific storage/hardware capabilities | installed/default provider catalogs are mutable; exact Windows build, provider/KSP/module/version, algorithm/property/mode, key boundary, policy, self-tests, and validation status require evidence |
| Linux kernel [AF_ALG userspace interface](https://docs.kernel.org/crypto/userspace-if.html) and [key retention service](https://docs.kernel.org/security/keys/core.html) | Linux kernel contracts; reviewed 2026-08-08 | kernel crypto-user interface status plus key/keyring types, permissions, lifetimes, quotas, and readability variance | current documentation explicitly calls AF_ALG insecure and deprecated and recommends userspace crypto; it is not a general provider candidate. Exact kernel/configuration/key type/namespace/LSM and any specialized consumer remain scoped evidence |
| Apple [CryptoKit](https://developer.apple.com/documentation/cryptokit), [SecureEnclave](https://developer.apple.com/documentation/cryptokit/secureenclave), [Security keys](https://developer.apple.com/documentation/security/keys), and [Secure Enclave key protection](https://developer.apple.com/documentation/security/protecting-keys-with-the-secure-enclave) | Apple platform contracts; reviewed 2026-08-08 | typed algorithms/keys, Security-framework key operations, hardware-bound operation and availability constraints | current CryptoKit catalog includes platform/version-specific post-quantum Secure Enclave types while older Security-framework guidance describes a narrower P-256 surface; exact OS/SDK/hardware/API/type/availability, keychain/access control, fallback, and operation boundary must be tested rather than generalized |

**RM-CRYPTO-SOURCE-0001:** Trial evidence MUST bind exact standards/policy revisions, OS/kernel/SDK, provider/module/library artifact and provenance, algorithm/parameters/encoding, hardware/firmware, configuration/operating mode, key origin/protection/export, self-tests, certification/attestation, toolchain/build, and corpus provenance.

**RM-CRYPTO-SOURCE-0002:** Living sources and provider catalogs MUST be release- or revision-bound where possible; an unchanged URL, algorithm name, API family, OS identity, hardware label, or installed default MUST NOT prove unchanged semantics, availability, provider selection, validation, or leakage properties.

**RM-CRYPTO-SOURCE-0003:** Final standards, drafts, provider/API documentation, observed platform behavior, algorithm/vector evidence, side-channel review, attestation, certification validation, and Rusty Mill guarantees MUST remain separately identified.

**RM-CRYPTO-SOURCE-0004:** Draft guidance MAY inform transition planning but MUST NOT be represented as final normative or certification policy without explicit accepted selection and exact revision/status disclosure.

**RM-CRYPTO-SOURCE-0005:** A standards, algorithm, provider/module/library, platform, hardware/firmware, configuration/mode, compiler, microcode, certification, or policy change invalidates affected claims until resolution, interoperability, security, lifecycle, performance, and migration impact is classified.
