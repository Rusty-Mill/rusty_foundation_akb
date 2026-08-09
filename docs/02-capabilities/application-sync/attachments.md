# Attachments and large objects

**RM-APP-SYNC-ATTACH-0001:** Attachment metadata and bytes have separate stable identities/generations, content digests, media/security classification, ownership, retention, and availability state.

**RM-APP-SYNC-ATTACH-0002:** Transfer supports bounded chunking, resume, integrity verification, deduplication scope, compression/encryption relation, cancellation, storage pressure, and retry without exposing partially verified bytes.

**RM-APP-SYNC-ATTACH-0003:** Reference publication and byte availability are separate milestones. Objects report missing/pending/quarantined/failed attachments and do not claim convergence until the selected availability contract is met.

**RM-APP-SYNC-ATTACH-0004:** Concurrent replacement/delete conflicts apply typed object semantics; content-address equality proves bytes only, not metadata, authorization, provenance, or intended attachment role.

**RM-APP-SYNC-ATTACH-0005:** Selective/on-demand transfer preserves authorization at every fetch, handles revoked access and expired delegation, and does not leak existence through deduplication, size, timing, or error behavior.

**RM-APP-SYNC-ATTACH-0006:** Orphan collection is frontier- and retention-aware and composes legal hold, erasure, pending changes, snapshots, and backup recovery.
