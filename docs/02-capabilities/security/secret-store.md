# `rm.security.secret-store` — Protected secret storage

| Field | Value |
|---|---|
| Status | Draft |
| Contract version | 0.1.0 |
| Domain | Security |
| Owner | Unassigned |
| Candidate profiles | CLI, Desktop, Server; constrained/headless when an eligible provider exists |

## Purpose

Create, retrieve, replace, inspect, and delete named secret items through a provider whose persistence, protection boundary, subject binding, interaction, export, availability, replication, deletion, and assurance claims satisfy explicit policy.

The capability does not invent an encryption scheme, store secrets in arbitrary configuration files, synchronize secrets, implement remote vault protocols, or promise deletion from backups and physical media.

## Data model

An item has an opaque provider-scoped identifier, secret class, protected value or opaque-use reference, non-secret and sensitive metadata partitions, version/generation, creation/update observations, access policy, and protection-claim vector. Lookup attributes are not assumed confidential or unique.

## Requirements

- **RM-SECURITY-SECRET-0001:** Provider selection **MUST** match every required protection dimension before accepting secret plaintext.
- **RM-SECURITY-SECRET-0002:** Unknown or dynamically unavailable protection **MUST NOT** satisfy a required claim.
- **RM-SECURITY-SECRET-0003:** Create **MUST** state collision behavior and **MUST NOT** overwrite an existing item unless replace authority and an explicit replace operation are used.
- **RM-SECURITY-SECRET-0004:** Item identifiers and lookup attributes **MUST** be provider-scoped and **MUST NOT** be treated as authority.
- **RM-SECURITY-SECRET-0005:** Retrieval **MUST** return a secret-value resource; plaintext export requires separately declared export authority and provider support.
- **RM-SECURITY-SECRET-0006:** Interactive authentication or consent **MUST** be declared during discovery and operation; synchronous UI-thread blocking **MUST NOT** be the only path for a provider that may prompt or wait.
- **RM-SECURITY-SECRET-0007:** Cancellation during a prompt or provider operation **MUST** distinguish confirmed cancellation, normal completion, and indeterminate outcome.
- **RM-SECURITY-SECRET-0008:** Replace **MUST** define generation preconditions and conflict outcomes; blind read-then-write **MUST NOT** claim atomic compare-and-replace.
- **RM-SECURITY-SECRET-0009:** Delete **MUST** describe logical visibility, provider garbage collection, backup/replica effects, and whether cryptographic erasure is evidenced.
- **RM-SECURITY-SECRET-0010:** Enumeration and metadata access **MUST** require explicit authority and honor sensitive-metadata disclosure policy.
- **RM-SECURITY-SECRET-0011:** Errors, audit events, traces, metrics, panic paths, and conformance artifacts **MUST NOT** contain secret values or secret-derived fingerprints.
- **RM-SECURITY-SECRET-0012:** A provider **MUST** disclose effects of logout, lock, account change, password reset, machine migration, backup/restore, synchronization, sandboxing, and headless execution where applicable.
- **RM-SECURITY-SECRET-0013:** The sync path **MUST** be complete for providers whose selected operation cannot prompt or materially wait; other providers **MUST** expose an async path and reject unsafe UI-thread use according to policy.
- **RM-SECURITY-SECRET-0014:** Native errors **MUST** map to portable categories while preserving sanitized provider diagnostics.
- **RM-SECURITY-SECRET-0015:** A compliance, hardware-backed, non-exportable, or deletion claim **MUST** identify the exact item class, operation, boundary, configuration, and evidence.

## Error categories

Not found, already exists, access denied, interaction required, interaction prohibited, locked/unavailable session, policy mismatch, unsupported protection, conflict/stale generation, confirmed canceled, indeterminate outcome, quota/storage exhausted, provider unavailable, corrupted item, migration/recovery required, and other provider failure with sanitized context.

## Concurrency and atomicity

Independent items may proceed concurrently subject to provider limits. Operations on one item use provider generations where available. If a provider cannot offer atomic conditional replace, that feature is unavailable rather than emulated with a race. Enumeration is a snapshot or stream with explicit consistency; it does not lock the store.

## Platform realization

| Platform | Candidate mechanisms | Important variance |
|---|---|---|
| Windows | Credential Manager; DPAPI-protected blobs under an application-owned store | Credential type/size/persistence, user vs machine binding, profile availability, application-owned metadata and rollback |
| Linux | Freedesktop Secret Service when present; kernel keyrings for appropriate ephemeral/kernel-consumed cases; explicit remote/provider extensions | Desktop service and prompt availability are not universal; keyring types differ in readability and lifetime |
| macOS | Keychain Services item APIs and access-control policy | Calls may block or prompt; keychain/access-group, synchronizable, backup, and device state matter |

No provider is selected solely from OS identity. Server/headless profiles may require a configured non-interactive provider and must not silently fall back to plaintext files or an unavailable desktop service.

