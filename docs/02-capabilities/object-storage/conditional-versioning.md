# Conditional operations, versioning, and deletion

**RM-OBJECT-CONDITION-0001:** Every mutation supports an explicit condition profile: create only/no live generation, exact data generation/version, exact metadata generation, validator match/nonmatch, retention/lease token where applicable, or unconditional with separately authorized risk.

**RM-OBJECT-CONDITION-0002:** Preconditions bind provider-authenticated immutable properties and are evaluated atomically with the target mutation. Last-modified time and weak/provider-ambiguous validators cannot protect consequential updates unless the profile proves their semantics.

**RM-OBJECT-CONDITION-0003:** Read-modify-write carries observed data and metadata generations through validation and conditional commit. Conflict returns current safe evidence; it never silently overwrites, merges metadata, or retries with a refreshed generation.

**RM-OBJECT-VERSION-0001:** Versioning policy declares enabled/suspended/disabled behavior, live/noncurrent/null versions, delete markers, overwrite semantics, listing consistency, retention/lifecycle, costs, replication, and restoration. Policy changes create new configuration generations.

**RM-OBJECT-DELETE-0001:** Delete intent distinguishes live-key marker, exact-version permanent deletion, soft delete, undelete/restore, metadata/tag removal, multipart abort, namespace deletion, and cryptographic erasure. Each binds exact generation and retention/legal authority.

**RM-OBJECT-DELETE-0002:** Accepted, marker created, version hidden, bytes logically unreachable, lifecycle queued, replicas/caches/inventories updated, retention expired, physical media reclaimed, key destroyed, and privacy erasure verified are separate milestones.

**RM-OBJECT-DELETE-0003:** Bulk/prefix deletion first resolves an immutable bounded manifest with exact versions and authority; listing changes cannot retarget execution. Partial/unknown results are reconciled per manifest entry.

**RM-OBJECT-VERSION-0002:** Restore/undelete creates or selects an explicitly identified live generation according to provider semantics and revalidates metadata, encryption, retention, schema/content safety, and application authority. It is not history rollback.

