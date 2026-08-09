# Secret-protection source review

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Expires | On supported OS/kernel/SDK, provider/service/store/item class, account/session, sandbox, backup/sync, or protection-policy change, or 2027-02-08, whichever occurs first |
| Reviewer | Secret-protection owner |
| Open blocking findings | None for dossier reviewability; exact generations, configurations, state matrices, and destructive-lifecycle probes remain trial inputs |

| Source | Class and reviewed status | Proposition supported | Impact and limitation |
|---|---|---|---|
| Microsoft [`CredWrite`](https://learn.microsoft.com/en-us/windows/win32/api/wincred/nf-wincred-credwritew), [`CredRead`](https://learn.microsoft.com/en-us/windows/win32/api/wincred/nf-wincred-credreadw), [`CredDelete`](https://learn.microsoft.com/en-us/windows/win32/api/wincred/nf-wincred-creddeletew), [`CryptProtectData`](https://learn.microsoft.com/en-us/windows/win32/api/dpapi/nf-dpapi-cryptprotectdata), and [`CryptUnprotectData`](https://learn.microsoft.com/en-us/windows/win32/api/dpapi/nf-dpapi-cryptunprotectdata) | Microsoft platform contracts; reviewed 2026-08-08 | managed credential records versus application-owned protected blobs, type/size/persistence and user/machine protection behavior | compatible provider shapes, not interchangeable semantics; DPAPI's PromptStruct flow is documented as deprecated with removal in February 2027, so new work cannot depend on it; exact Windows build/profile/service identity, flags, entropy, file/store metadata, generations, backup/restore, prompting, and deletion residuals require evidence |
| Freedesktop.org [Secret Service API](https://specifications.freedesktop.org/secret-service/latest/) | cross-desktop protocol specification, 0.2 Draft published 2026-04-08; reviewed 2026-08-08 | collections/items/sessions, locking, prompts, attributes, secret transfer, create/replace/delete behavior | the `latest` URL is mutable and the protocol is Draft; an installed implementation and interactive session are not universal; trials bind an archived/revisioned copy plus exact service/version/session algorithm, collection state, prompt broker, sandbox/bus policy, persistence, backup, and deletion behavior |
| Linux kernel [Key Retention Service](https://docs.kernel.org/security/keys/core.html) and [Trusted and Encrypted Keys](https://docs.kernel.org/security/keys/trusted-encrypted.html) | Linux kernel contracts; reviewed 2026-08-08 | key/keyring identity, permissions, quotas, lifetimes, userspace readability variance, and hardware/trust-source-related types | distinct ephemeral/kernel-consumed provider classes; exact kernel/configuration/key type/keyring/identity/namespace/LSM/expiry/revocation/readability and persistence require evidence |
| Apple [Keychain Services](https://developer.apple.com/documentation/security/keychain-services), [`SecItemAdd`](https://developer.apple.com/documentation/security/secitemadd(_:_:)), [`SecItemCopyMatching`](https://developer.apple.com/documentation/security/secitemcopymatching(_:_:)), [`SecItemUpdate`](https://developer.apple.com/documentation/security/secitemupdate(_:_:)), and [`SecItemDelete`](https://developer.apple.com/documentation/security/secitemdelete(_:_:)) | Apple platform contracts; reviewed 2026-08-08 | item classes/attributes, synchronous calls, query/match/update/delete operations, access and interaction behavior | exact macOS/SDK, keychain/access group, application identity, sandbox, accessibility/access-control, prompt/session, synchronizable/backup state, and deletion residuals require evidence |

**RM-SECURITY-SECRET-SOURCE-0001:** Trial evidence MUST bind exact OS/kernel/SDK, provider/service/store/item class and artifact, configuration, identity/account/session/sandbox, interaction, protection vector, replication/backup, lifecycle, and artifact provenance.

**RM-SECURITY-SECRET-SOURCE-0002:** Living sources MUST be release- or revision-bound where possible; a familiar store/API/mechanism name or unchanged URL MUST NOT prove unchanged item limits, prompting, protection, synchronization, migration, or deletion behavior.

**RM-SECURITY-SECRET-SOURCE-0003:** Documented API/protocol contracts, observed provider/platform behavior, protection-mechanism evidence, assurance/certification evidence, and Rusty Mill guarantees MUST remain separately identified.

**RM-SECURITY-SECRET-SOURCE-0004:** A provider, service, platform, store/item class, account/session, sandbox, policy, backup/sync, migration, or lifecycle change invalidates affected evidence until selection, interaction, exposure, generations, availability, replication, deletion, and recovery impact is classified.
