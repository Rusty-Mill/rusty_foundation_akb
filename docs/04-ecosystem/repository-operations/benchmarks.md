# Repository benchmarks and operational objectives

**RM-REPOSITORY-BENCH-0001:** Measure candidate validation, artifact upload/deduplication, signing/timestamp/log, metadata generation/commit, release visibility, channel promotion, mirror replication, advisory publication, yank/revocation propagation, and restore separately and end to end.

**RM-REPOSITORY-BENCH-0002:** Workloads cover small crate/spec releases, multi-platform application releases with many evidence attachments, large artifacts, many packages/versions/channels/referrers, concurrent publishers, global mirrors, advisory bursts, and emergency mass-policy updates.

**RM-REPOSITORY-BENCH-0003:** Report latency distributions, bytes/objects, deduplication ratio, throughput, CPU/memory/allocations, signing/provider waits, metadata size/depth, control-plane conflicts/retries, regional visibility/replication lag, error/indeterminate rates, and storage growth.

**RM-REPOSITORY-BENCH-0004:** Availability objectives separately measure fresh metadata, artifact retrieval, publication control plane, advisory/emergency propagation, mirror failover, and operator recovery by region and percentile; planned maintenance and dependency failures remain visible.

**RM-REPOSITORY-BENCH-0005:** Emergency exercises report detection, declaration, credential disable, publication freeze, advisory/yank/revocation/root metadata, consumer-visible propagation, safe replacement, rollout, and full recovery times plus affected downloads during each window.

**RM-REPOSITORY-BENCH-0006:** Restore benchmarks use independently verified backups and include immutable-object integrity, namespace/ownership, monotonic metadata, advisory/audit history, mirror bootstrap, signing-service recovery, and consumer continuity.

Initial service objectives and error budgets remain RFC-owned after representative GitHub, crates.io, artifact-registry, and self-hosted repository baselines exist.

