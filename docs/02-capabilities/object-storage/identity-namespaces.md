# Namespaces, keys, versions, and identity

**RM-OBJECT-IDENTITY-0001:** An object reference contains provider domain, namespace identity/generation, exact opaque key bytes/text profile, and optional provider version/generation. URI, display path, decoded name, DNS host, filesystem path, and key remain distinct.

**RM-OBJECT-IDENTITY-0002:** Key rules declare encoding/Unicode normalization, case sensitivity, separator nonsemantics, empty/prefix/trailing forms, reserved/control/bidi characters, maximum bytes/components, canonical URI encoding, and spoofing-safe display. No directory hierarchy is inferred from delimiters.

**RM-OBJECT-IDENTITY-0003:** Namespace creation/configuration binds globally/provider-scoped name, region/location, versioning, consistency, encryption, public-access prevention, network policy, retention, replication, logging/inventory, tags, generation precondition, and authority.

**RM-OBJECT-IDENTITY-0004:** Provider object generation/version, metadata generation, ETag/validator, last-modified time, length, storage class, checksum, and content digest are individually typed evidence. None is treated as another unless the provider profile proves equivalence.

**RM-OBJECT-IDENTITY-0005:** A live-key lookup and an exact-version lookup are separate. Delete markers/tombstones, null/default versions, archived/noncurrent versions, soft-deleted objects, restored copies, and absent keys are distinct states.

**RM-OBJECT-IDENTITY-0006:** Identity survives endpoint, replica, region, and access-path changes only through provider-authenticated namespace and exact generation evidence. Copying bytes creates a new provider object identity even when content digest matches.

**RM-OBJECT-IDENTITY-0007:** User-supplied keys are untrusted identifiers and cannot select another tenant, escape a prefix capability, inject headers/logs, alter signing canonicalization, or become local paths without a separate safe mapping.

