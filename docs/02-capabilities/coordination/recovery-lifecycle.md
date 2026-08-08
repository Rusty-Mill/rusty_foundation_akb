# Failure, recovery, reconfiguration, and lifecycle

**RM-COORDINATION-RECOVERY-0001:** Startup verifies durable identity/incarnation, cluster/configuration, log/snapshot/checksums, schema, credentials, clocks, fencing/dedup state, and recovery mode before serving. Corruption, rollback, clone, partial write, and foreign-cluster data fail distinctly.

**RM-COORDINATION-RECOVERY-0002:** Restart, reconnect, catch-up, snapshot restore, backup restore, member replacement, quorum recovery, disaster failover, region return, and cluster migration create explicit generations and reconciliation plans; endpoint reuse cannot imply continuity.

**RM-COORDINATION-RECOVERY-0003:** Backup/restore binds a coherent committed revision, membership/configuration, state/log/snapshot/schema, encryption/signature, fencing/dedup/lease policy, external dependencies, retention, verification, restore target identity, and point-in-time loss bounds.

**RM-COORDINATION-RECOVERY-0004:** Rolling upgrade/downgrade and protocol/schema transition declare compatible version matrix, feature gates, quorum order, log/snapshot compatibility, mixed-version safety/liveness, rollback point, irreversible format changes, and conformance evidence.

**RM-COORDINATION-RECOVERY-0005:** Graceful drain stops new proposals/leases/transactions, transfers or fences leadership, drains work under deadline, persists required state, and reports residual uncertainty. Forced stop/crash/power loss remain supported outcomes.

**RM-COORDINATION-RECOVERY-0006:** Disaster procedures distinguish loss of minority, quorum, latest committed data, fencing authority, credentials, clocks, or whole fault domains. Unsafe force operations require explicit data-loss/split-brain acceptance and generate a new coordination domain generation.

**RM-COORDINATION-RECOVERY-0007:** Rejoining a previously partitioned site/node requires authenticated identity, fencing, divergence assessment, authoritative-source selection, wipe/restore/catch-up plan, bounded transfer, validation, and staged promotion; histories are never merged by timestamp guess.

