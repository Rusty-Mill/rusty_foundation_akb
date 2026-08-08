# Admission, eviction, and tiers

**RM-CACHE-TIER-0001:** Admission policy is explicit about item size, reuse estimate, cost, sensitivity, origin expense, pollution resistance, quota, and bypass; observing a value does not require storing it.

**RM-CACHE-TIER-0002:** Eviction policy names capacity units, priority, recency/frequency evidence, tenant fairness, pinned/reserved entries, expiration, cleanup, and behavior under pressure.

**RM-CACHE-TIER-0003:** Memory, local-disk, shared-process, distributed, origin-shield, and edge tiers have separate identities, trust, durability, latency, capacity, consistency, encryption, and failure contracts.

**RM-CACHE-TIER-0004:** Promotion/demotion between tiers revalidates identity, partition, policy epoch, integrity, and limits; a lower-tier hit is not automatically admissible to an upper tier.

**RM-CACHE-TIER-0005:** Disk caches use crash-safe publication, bounded startup/index recovery, permission isolation, corruption detection, storage-pressure handling, and secure erasure consistent with data classification.

**RM-CACHE-TIER-0006:** Distributed caches expose sharding/routing generation, failover, replication, hot-key behavior, serialization compatibility, item limits, TTL precision, and ambiguous mutation outcomes.

**RM-CACHE-TIER-0007:** Write-through and write-behind are separately selected persistence workflows; cache acknowledgment never implies authoritative commit unless a product defines that exact boundary.
