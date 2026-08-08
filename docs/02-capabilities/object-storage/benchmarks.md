# Object-storage benchmark specification

**RM-OBJECT-BENCH-0001:** Benchmarks publish hardware, OS/provider/SDK/protocol builds, account/region/topology, security/encryption/versioning/storage class/replication, object/key/metadata distributions, concurrency, limits, network/cache, faults, samples, variance, billing, and raw traces.

**RM-OBJECT-BENCH-0002:** Workloads cover small/large whole and ranged reads/writes, streaming, parallel/resumable/multipart, checksums/digests, metadata/tags, list/pages/versions, conditional conflicts, copy/compose, delete/restore, delegated access, archive retrieval, and content-addressed graph traversal.

**RM-OBJECT-BENCH-0003:** Report operation/first-last-byte/commit/visible/replicated/event latency distributions, goodput, request/part/range counts, retries/throttles, CPU, allocations/copies, memory/disk/network, checksum/hash/encryption cost, cache, storage/request/egress cost, and energy.

**RM-OBJECT-BENCH-0004:** Scale/fairness varies objects/versions/key distribution, prefix hotspots, sizes, multipart part counts, clients/tenants, ranges, list pages, metadata, content graph fanout, replication backlog, lifecycle/inventory, and slow consumers under provider quotas.

**RM-OBJECT-BENCH-0005:** Fault/recovery experiments inject disconnect/timeouts at every transfer/completion response, corruption/truncation, clock/credential/key rotation, region/endpoint loss, replication lag, overwrite/delete races, archive delay, event gaps, restore/migration, and unknown-state reconciliation.

**RM-OBJECT-BENCH-0006:** Retention/lifecycle/GC experiments measure eligibility-to-action lag, version and multipart cleanup, CAS reachability scans, inventory cost/freshness, hold exclusion, erasure convergence, restore success/RTO, and storage amplification without weakening protection.

**RM-OBJECT-BENCH-0007:** Provider and Rusty Mill paths use identical object generations, conditions, checksums/digests, encryption, versioning, consistency, retries, cache, retention, replication, telemetry, and completion boundaries. Weaker integrity or durability cannot count as speed.

