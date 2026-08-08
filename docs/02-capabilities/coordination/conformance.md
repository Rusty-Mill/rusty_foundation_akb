# Coordination conformance specification

**RM-COORDINATION-CONFORMANCE-0001:** Reports bind algorithm/provider/client/server/storage builds, domain/configuration and participant incarnations, topology/fault domains/quorums, consistency/durability/clock assumptions, security, workload, limits, fault schedule, and canonical operation/history traces.

**RM-COORDINATION-CONFORMANCE-0002:** Membership/failure tests cover joint changes, concurrent admins, catch-up/promotion, identity reuse/clones, gossip convergence, watch loss/compaction, asymmetric partition, delay/reorder/duplicate, false suspicion, crash/pause/suspend, and endpoint/credential rotation.

**RM-COORDINATION-CONFORMANCE-0003:** Lease/election/lock tests pause and partition holders across expiry/renew/revoke/transfer, inject clock steps and stalls, race cancel/grant/release, reuse names, resize semaphores, and verify monotonically fenced rejection at every protected resource.

**RM-COORDINATION-CONFORMANCE-0004:** Consensus tests cover election terms, stale leaders, log divergence/conflict, delayed old messages, quorum loss/restore, current-term commit rules, linearizable and stale reads, configuration change, snapshots/compaction, disk faults/corruption, dedup, restart, and unsafe-recovery controls.

**RM-COORDINATION-CONFORMANCE-0005:** History checking verifies each declared linearizable/sequential/serializable/snapshot/causal/session/bounded-stale/convergent model under concurrency, partitions, failover, clocks, caches, retries, and client/session loss, including forbidden anomalies and freshness evidence.

**RM-COORDINATION-CONFORMANCE-0006:** Transaction/workflow tests fault coordinator/participants/stores/brokers at every begin/prepare/decision/apply/ack/compensate boundary, exercise in-doubt/heuristic/deadlock states, definition/schema migration, outbox/inbox, external effects, and manual reconciliation.

**RM-COORDINATION-CONFORMANCE-0007:** Recovery tests cover partial/torn/corrupt/rolled-back logs and snapshots, backups/restores/clones, minority/quorum/site loss, region return, rolling upgrade/downgrade, mixed versions, credential/key rotation, forced bootstrap, audit, and residual-state invariants.

**RM-COORDINATION-CONFORMANCE-0008:** Cross-provider matrices compare canonical histories and evidence across selected self-hosted/managed providers and Windows/Linux/macOS clients under identical fault models; untestable or unsupported guarantees remain gaps rather than inferred conformance.

