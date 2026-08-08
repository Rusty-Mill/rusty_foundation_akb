# Catalogs, sources, and formats

**RM-ANALYTICS-CATALOG-0001:** Catalog resolution binds namespace/object identity, schema/partitioning/sort generations, snapshot/version, location/provider, statistics freshness, security policy, retention, and format options into an immutable query input.

**RM-ANALYTICS-CATALOG-0002:** Table/stream/view/function aliases resolve once per plan or under an explicit dynamic-resolution policy; silent mid-query alias movement cannot mix incompatible generations.

**RM-ANALYTICS-SOURCE-0001:** Sources expose bounded/unbounded nature, split/partition discovery, snapshot/frontier, ordering, replayability, offset/version identity, change semantics, late discovery, deletion/tombstone behavior, authentication, locality, limits, and failure modes.

**RM-ANALYTICS-SOURCE-0002:** File/object datasets use immutable manifests or equivalent snapshot evidence; directory/listing observation alone is not a coherent dataset when concurrent publication, eventual visibility, or replacement is possible.

**RM-ANALYTICS-FORMAT-0001:** Format contracts bind exact version, schema projection, physical/logical type mapping, compression/encoding, statistics/indexes, checksums, encryption, metadata, row-group/page/batch boundaries, corruption handling, and conversion loss.

**RM-ANALYTICS-FORMAT-0002:** Partition and predicate/projection/limit/aggregation pushdown are semantics-preserving optimizations with provider evidence; unsupported or approximate pushdown is rejected or surfaced rather than silently altering results.

**RM-ANALYTICS-SOURCE-0003:** Change streams distinguish inserts, before/after updates, deletes, snapshots, transaction/order boundaries, schema changes, duplicates, gaps, heartbeats, and source positions.

**RM-ANALYTICS-CATALOG-0003:** Statistics are qualified estimates with collection time/snapshot, sample, null/distinct/min/max/histogram correlation limits, privacy policy, and optimizer fallback; they are not source constraints.
