# Usage dimensions and immutable meter events

**RM-TENANT-GOV-METER-0001:** A meter definition binds stable meter ID, semantic quantity, UCUM or exact unit, aggregation kind, event schema, subject/resource dimensions, event/effective/ingest time, deduplication, late window, privacy, retention, and version.

**RM-TENANT-GOV-METER-0002:** Dimensions have bounded cardinality, stable identifiers, classification, normalization, allowed values, allocation meaning, and missing/unknown behavior; arbitrary user text is prohibited by default.

**RM-TENANT-GOV-METER-0003:** A usage event is immutable and carries event/idempotency identity, tenant/account/resource, meter generation, quantity and unit, event/effective/observed/ingest time, source, authority/provenance, operation/effect receipt, schema, and integrity.

**RM-TENANT-GOV-METER-0004:** Accepted for ingestion, durably stored, validated, deduplicated, assigned to period, aggregated, rated, exported, invoiced, and paid are separate milestones.

**RM-TENANT-GOV-METER-0005:** Duplicate, reordered, late, future-dated, negative, overflow, unit mismatch, unknown tenant/resource, and implausible events receive deterministic accept/quarantine/reject/adjust behavior.

**RM-TENANT-GOV-METER-0006:** Measuring attempts, accepted work, completed effects, retained state, peak/concurrent state, elapsed time, samples, or unique actors are different meters and cannot be substituted silently.
