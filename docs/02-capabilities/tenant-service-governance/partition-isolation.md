# Resource partitioning, placement, and isolation

**RM-TENANT-GOV-ISOLATION-0001:** A placement plan binds tenant/resource class, isolation tier, cell/shard/cluster/region, capacity and affinity constraints, residency, encryption/key policy, fault domain, noisy-neighbor policy, and migration support.

**RM-TENANT-GOV-ISOLATION-0002:** Isolation claims form a vector covering identity namespace, authorization, compute, memory, storage, network, caches, queues, search/index, encryption keys, logs/telemetry, backups, operations, and side channels.

**RM-TENANT-GOV-ISOLATION-0003:** Shared, pooled-with-partition-key, schema/database, process/container, VM, host, account/project, cluster, cell, and dedicated deployment are separate mechanisms; strength in one dimension cannot hide a shared boundary elsewhere.

**RM-TENANT-GOV-ISOLATION-0004:** Every request, job, message, cache key, query, index document, object, trace, meter event, and administrative operation carries authenticated tenant context or fails closed at its boundary.

**RM-TENANT-GOV-ISOLATION-0005:** Capacity placement and commercial plan are independent. An entitled tenant can encounter unavailable capacity, and reserved capacity requires separate evidence.

**RM-TENANT-GOV-ISOLATION-0006:** Cell/shard movement is a fenced workflow with source snapshot, dual-routing/replication policy, validation, cutover generation, stale-writer denial, rollback horizon, and residual cleanup.
