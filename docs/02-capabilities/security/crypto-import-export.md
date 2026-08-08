# Import, export, wrapping, and serialization

**RM-CRYPTO-TRANSFER-0001:** Public, private, symmetric, wrapped, provider-reference, certificate, and attestation objects MUST use distinct typed formats with exact version, algorithm/parameters, encoding, and bounded parser limits.

**RM-CRYPTO-TRANSFER-0002:** Import MUST validate complete structure, canonicality where required, algorithm/parameter consistency, public/private coherence, key strength, usage/export/protection policy, ownership, duplicate identity, and provider compatibility before atomic publication.

**RM-CRYPTO-TRANSFER-0003:** Importing secret/private material MUST use a secret-value resource, bounded parser/isolation policy, explicit copy/exposure map, and cleanup evidence. Generic byte buffers and logging/debug formatting are forbidden.

**RM-CRYPTO-TRANSFER-0004:** Public export and private/secret export are separate authorities. Export MUST report plaintext, encrypted, wrapped, reference-only, hardware-migration, or unsupported form and MUST NOT weaken source protection silently.

**RM-CRYPTO-TRANSFER-0005:** Key wrapping MUST bind wrapping and wrapped key generations, exact authenticated wrapping scheme, metadata/context, allowed destination/provider/tenant, replay/rollback policy, and resulting usage/export restrictions.

**RM-CRYPTO-TRANSFER-0006:** Provider references and handles are opaque, provider/version/scope bound, non-portable, non-authoritative after close/restart unless explicitly persisted, and never serialized as bearer credentials by default.

**RM-CRYPTO-TRANSFER-0007:** Backup, escrow, replication, synchronization, recovery, cross-device migration, and threshold custody are separately selected services with principal quorum, audit, revocation, rollback, and compromise policy.
