# Document identity and source capture

**RM-SEARCH-INGEST-0001:** Document identity is namespace-, tenant-, entity-, and source-generation-scoped; provider IDs, routing keys, content digests, and business identity remain distinct.

**RM-SEARCH-INGEST-0002:** Every indexed document records source version/watermark, schema and transformation generation, authorization projection, language/locale evidence, content descriptor or provenance, and index attempt lineage.

**RM-SEARCH-INGEST-0003:** Snapshot/bootstrap plus ordered change capture define a gap-free handoff or explicit reconciliation procedure; event receipt alone does not prove index convergence.

**RM-SEARCH-INGEST-0004:** Upsert/delete operations use source version preconditions or monotonic external versions so delayed retries cannot resurrect or overwrite newer state.

**RM-SEARCH-INGEST-0005:** Deletes, tombstones, redactions, tenant moves, authorization changes, and erasure requests carry equal ordering authority to creates/updates and survive retry, rebuild, and failover.

**RM-SEARCH-INGEST-0006:** Bulk ingestion reports per-item outcomes and does not promote batch transport success into item success; ambiguous items reconcile from source truth.

**RM-SEARCH-INGEST-0007:** Ingest pipelines bound input size, fields, nesting, token/vector expansion, external enrichment, decompression, parsing, model calls, time, memory, and output size.

**RM-SEARCH-INGEST-0008:** Poison documents enter quarantined, observable workflows without blocking unrelated progress or silently dropping source changes.
