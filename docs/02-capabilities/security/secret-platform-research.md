# Secret storage platform research

**Status:** Research input; mechanism names do not define portable semantics

## Windows

Credential Manager provides managed credential records through `CredWrite` and `CredRead`; Microsoft guidance recommends it for passwords. DPAPI `CryptProtectData` protects an application-owned blob, normally binding decryption to the same user logon credentials and computer, with documented variations. These are distinct provider shapes: DPAPI does not supply naming, concurrency, rollback protection, storage durability, or lifecycle policy for the surrounding file/database.

Primary sources:

- Microsoft: [Handling Passwords](https://learn.microsoft.com/en-us/windows/win32/secbp/handling-passwords)
- Microsoft: [`CredWrite`](https://learn.microsoft.com/en-us/windows/win32/api/wincred/nf-wincred-credwritew) and [`CredRead`](https://learn.microsoft.com/en-us/windows/win32/api/wincred/nf-wincred-credreadw)
- Microsoft: [`CryptProtectData`](https://learn.microsoft.com/en-us/windows/win32/api/dpapi/nf-dpapi-cryptprotectdata) and [`CryptUnprotectData`](https://learn.microsoft.com/en-us/windows/win32/api/dpapi/nf-dpapi-cryptunprotectdata)

## Linux

Linux does not guarantee a desktop secret service. The Freedesktop Secret Service specification defines D-Bus collections, items, sessions, locking, prompts, and secret transfer when an implementation is installed. The kernel key retention service provides typed keys/keyrings with permissions, expiry, quotas, and different inheritance; some key types permit userspace payload reads, while `logon` keys are intended for kernel use without userspace reads. Trusted/encrypted key types introduce further trust-source and hardware-specific properties.

Primary sources:

- Freedesktop.org: [Secret Service API](https://specifications.freedesktop.org/secret-service/latest/)
- Linux kernel: [Kernel Key Retention Service](https://docs.kernel.org/security/keys/core.html)
- Linux kernel: [Trusted and Encrypted Keys](https://docs.kernel.org/security/keys/trusted-encrypted.html)

## macOS

Keychain Services stores password, certificate, key, and identity items with item-specific attributes and access policy. `SecItemAdd` is synchronous and may block; operations involving access control can require user interaction. Application identity, access groups, sandboxing, synchronizable attributes, device/keychain state, and chosen accessibility class affect behavior.

Primary sources:

- Apple: [Keychain Services](https://developer.apple.com/documentation/security/keychain-services)
- Apple: [`SecItemAdd`](https://developer.apple.com/documentation/security/secitemadd(_:_:))
- Apple: [`SecItemCopyMatching`](https://developer.apple.com/documentation/security/secitemcopymatching(_:_:))
- Apple: [Restricting keychain item accessibility](https://developer.apple.com/documentation/security/restricting-keychain-item-accessibility)

## Cross-platform conclusions

1. Persistence, interaction, exportability, replication, and protection boundary are independent.
2. A headless-safe provider cannot be inferred from platform name.
3. “Encrypted at rest” does not define who can decrypt, when plaintext exists, how metadata is protected, or whether backup/sync copies exist.
4. Store lookup names and attributes may leak sensitive context even if values are encrypted.
5. OS APIs may synchronously block or prompt, so interaction capability and execution context are contract properties.
6. Protected blobs and managed item stores have different atomicity and storage responsibilities and must not share an undifferentiated claim.

