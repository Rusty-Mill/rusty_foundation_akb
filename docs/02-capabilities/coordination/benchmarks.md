# Coordination benchmark specification

**RM-COORDINATION-BENCH-0001:** Benchmarks publish hardware, OS/provider/client/server/storage builds, topology/fault domains, membership/quorums, consistency/durability/clocks, security, payload/key distributions, concurrency, limits, impairment, samples, variance, and raw histories.

**RM-COORDINATION-BENCH-0002:** Workloads cover proposals/writes and every read mode, watches, leases/renewals, elections, contended/uncontended locks/semaphores, membership changes, snapshots/compaction/catch-up, transactions/workflows, backups/restores, and mixed key/tenant hot spots.

**RM-COORDINATION-BENCH-0003:** Report operation/commit/apply/visibility latency distributions, throughput/goodput, election/unavailability/recovery time, replication/catch-up/snapshot rates, staleness, lease margin, lock wait/hold, transaction in-doubt, fairness, CPU/memory/disk/network, write amplification, and energy where available.

**RM-COORDINATION-BENCH-0004:** Fault experiments vary crash/restart/pause, asymmetric partition, latency/loss/reorder, disk latency/full/corruption, clock uncertainty/step, member/site loss, leader transfer, quorum change, restore, and upgrade while running history/safety checks; availability never outranks violated safety.

**RM-COORDINATION-BENCH-0005:** Scale experiments vary members/voters/learners, keys/ranges, clients, leases/locks/watches, transactions, snapshots/log size, geographic distance, tenants, and skew while reporting tail amplification, hotspots, fairness, quorum cost, and control-plane saturation.

**RM-COORDINATION-BENCH-0006:** Provider and Rusty Mill paths use identical algorithms/qualities, durability, security, batching, consistency, fencing, recovery, limits, telemetry, and completion boundaries. Lease safety, consistency, or durability omitted for speed is reported as a different workload.

