# Cryptographic platform research

| Platform/provider family | Primary mechanisms | Architectural observations |
|---|---|---|
| Windows | CNG BCrypt algorithm providers, NCrypt key-storage providers, platform/smart-card providers, DPAPI/DPAPI-NG, certificate stores | CNG separates algorithm providers from key-storage providers. Provider and KSP capabilities, key properties, export policy, UI, hardware, and operation support differ; CNG's extensibility means provider provenance and exact algorithm/parameter evidence are mandatory. |
| Linux | Audited userspace cryptographic libraries, kernel keyrings/trusted keys, PKCS #11 and device/HSM providers, kernel interfaces for specialized consumers | Linux has no single universal application crypto/key-store API. Current kernel documentation deprecates AF_ALG for general userspace use and notes optimized userspace crypto is typically faster. Distribution policy, library/provider version, hardware modules, keyring semantics, and certification boundaries vary. |
| macOS | CryptoKit, Security framework `SecKey`/Keychain, Secure Enclave | CryptoKit supplies strongly typed common operations and integrates native key types; Secure Enclave keys keep selected private operations inside a device boundary with limited algorithms and availability/interaction policy. Keychain identity/access group/sync/accessibility and Secure Enclave evidence remain separate. |

## Standards and primary sources

- [NIST key-management publications](https://csrc.nist.gov/Projects/key-management/publications)
- [NIST SP 800-57 Part 1 Rev. 5](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final)
- [NIST SP 800-131A Rev. 2](https://csrc.nist.gov/pubs/sp/800/131/a/r2/final)
- [Microsoft: Cryptography API Next Generation](https://learn.microsoft.com/en-us/windows/win32/seccng/cng-portal)
- [Microsoft: CNG key-storage providers](https://learn.microsoft.com/en-us/windows/win32/seccertenroll/cng-key-storage-providers)
- [Linux kernel: AF_ALG userspace interface and deprecation](https://docs.kernel.org/next/crypto/userspace-if.html)
- [Linux kernel: Key retention service](https://docs.kernel.org/security/keys/core.html)
- [Apple: CryptoKit](https://developer.apple.com/documentation/cryptokit)
- [Apple: Protecting keys with the Secure Enclave](https://developer.apple.com/documentation/security/protecting-keys-with-the-secure-enclave)

## Evidence gaps

- Exact algorithm/parameter/encoding coverage and provider selection on each supported OS/build and architecture.
- Hardware/key-store concurrency, prompting, rate/use limits, lock/session/sleep behavior, backup/sync/migration, destruction, firmware update, and provider loss.
- Certification operating modes/module boundaries, platform policy overrides, entropy dependencies, self-tests, constant-time/leakage evidence, and remote/HSM behavior.
- Post-quantum and hybrid algorithm availability, key/signature/ciphertext sizes, transition/interoperability policy, and denial-of-service bounds.
