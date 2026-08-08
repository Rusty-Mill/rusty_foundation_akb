# Visibility, consistency, and lifecycle

**RM-SEARCH-VISIBILITY-0001:** Mutation outcomes separately report provider acceptance, primary application, durability boundary, replica acknowledgment, refresh/search visibility, and source convergence.

**RM-SEARCH-VISIBILITY-0002:** A search-visible view is an immutable logical generation over exact shard/segment generations, schema/analyzer/ranking configuration, security policy, and freshness watermark.

**RM-SEARCH-VISIBILITY-0003:** Read-your-write, monotonic-read, session, bounded-staleness, and point-in-time claims name exact clients, mutations, indexes/replicas, routing, time/watermark, failure assumptions, and tested histories.

**RM-SEARCH-VISIBILITY-0004:** Refresh makes an index generation eligible for search but does not imply source commit, durable flush, complete replication, backup, or downstream observation.

**RM-SEARCH-VISIBILITY-0005:** Flush/commit, refresh, segment merge, cache invalidation, replica recovery, snapshot, and lifecycle retention are distinct operations with observable resource and availability effects.

**RM-SEARCH-VISIBILITY-0006:** Point-in-time views have bounded lifetime, resource budgets, renewal/expiry behavior, authorization revalidation policy, and explicit behavior when shards relocate or fail.

**RM-SEARCH-VISIBILITY-0007:** Partial search is opt-in by workload or explicitly surfaced; failed/timed-out partitions cannot be represented as a complete empty or low-result response.
