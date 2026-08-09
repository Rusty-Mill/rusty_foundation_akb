# Append, corrections, and supersession

**RM-AUDIT-APPEND-0001:** Accepted audit events are immutable. Validation or enrichment after acceptance creates a derived record with provenance, never an invisible in-place edit.

**RM-AUDIT-APPEND-0002:** Corrections, annotations, disputes, classifications, legal determinations, and outcome updates append records referencing the original event and state exact corrected fields/claims, authority, reason, effective time, and supersession scope.

**RM-AUDIT-APPEND-0003:** Duplicate submissions with equal stable event identity and canonical digest are idempotently acknowledged; mismatched payloads are conflicts and security/audit events.

**RM-AUDIT-APPEND-0004:** Segments/manifests bind collection, schema/policy, sequence range/frontier, record count and canonical digests, creation/finalization, compression/encryption, storage object, integrity proof, and known gaps.

**RM-AUDIT-APPEND-0005:** Finalization closes an append segment but does not prove every expected event arrived. Late events enter a linked backfill segment with explicit interval/frontier and proof chain.

**RM-AUDIT-APPEND-0006:** Query projections and indexes are disposable derived state whose rebuild proves event/correction/suppression convergence; index mutation never changes ledger evidence.
