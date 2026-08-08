# Incremental materialization and serving

**RM-ANALYTICS-MAT-0001:** A materialization binds logical query, source/catalog frontiers, schema/function/time/ranking generations, update mode, key/partitioning, refresh trigger, consistency, retention, and serving authority.

**RM-ANALYTICS-MAT-0002:** Append, complete replacement, keyed upsert, change/retraction, snapshot, and differential outputs are distinct protocols with exact identity, ordering, duplicate, and consumer reconciliation semantics.

**RM-ANALYTICS-MAT-0003:** Incremental maintenance declares supported operators and source changes, state lineage, correctness equivalence, fallback rebuild, late/corrected data, schema changes, and recovery behavior.

**RM-ANALYTICS-MAT-0004:** Result publication uses immutable generations or conditional atomic pointer/manifest change so readers observe a coherent set rather than partially written partitions.

**RM-ANALYTICS-MAT-0005:** Materialization freshness distinguishes source-event, capture, processing, checkpoint, sink commit, catalog publication, replica/cache, and caller-observation lag.

**RM-ANALYTICS-MAT-0006:** Serving queries bind an exact materialization generation or declared staleness policy and expose incomplete/partial/rebuilding/degraded state.

**RM-ANALYTICS-MAT-0007:** Backfill and live processing use a gap-free frontier handoff, consistent deduplication/result identity, resource isolation, validation, and controlled promotion.
