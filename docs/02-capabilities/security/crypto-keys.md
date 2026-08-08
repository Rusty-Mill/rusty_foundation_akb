# Key resources, authority, and lifecycle

A `KeyHandle` is opaque and generation-scoped. Its descriptor contains key class, algorithm/parameter set, public attributes, origin, creation/import evidence, permitted operations/purposes, subject/application/tenant binding, provider/storage/protection boundary, export policy, interaction policy, validity/usage limits, rotation lineage, revocation/destruction state, and attestation/certification evidence.

**RM-CRYPTO-KEY-0001:** Key identity, locator, label, public key, certificate, provider handle, secret/private material, and operation authority MUST remain distinct. Possessing metadata or a public key grants no private-key operation.

**RM-CRYPTO-KEY-0002:** Create, import, open, use-by-operation, derive, agree, wrap, unwrap, attest, export-public, export-private/secret, rotate, revoke, and destroy authorities MUST be separately attenuated by purpose, audience, principal, lifetime, use count, and provider.

**RM-CRYPTO-KEY-0003:** Symmetric and private key material MUST be non-exportable by default. Exportability is fixed or narrowed at creation/import and cannot be silently broadened by provider fallback, backup, sync, migration, or update.

**RM-CRYPTO-KEY-0004:** Key generation MUST bind the selected plan and approved random provider, provider/module generation, parameters, usage/export/protection policy, owner, time, and creation evidence before publication.

**RM-CRYPTO-KEY-0005:** Key states MUST distinguish proposed, generating/importing, active, suspended, expired, usage-exhausted, rotating, retired-for-new-use, revoked, destroy-requested, logically-destroyed, and provider-confirmed destruction.

**RM-CRYPTO-KEY-0006:** Rotation creates a new key generation and lineage. It MUST define writer/read/verify transition, data rewrap or re-encryption, overlap, rollback, old-key retention, compromise response, and cutover evidence.

**RM-CRYPTO-KEY-0007:** Destruction claims MUST distinguish handle invalidation, provider logical deletion, hardware slot/key erasure, replica/backup/sync effects, cached/plaintext copies, and physical erasure nonclaims.

**RM-CRYPTO-KEY-0008:** Concurrent use, prompting, lock/unlock, rate/usage counters, expiration, and external policy changes MUST be atomic or generation-observable; cached authority cannot bypass a changed provider decision.
