# Coordination cross-cutting requirements

**RM-COORDINATION-CROSS-0001:** Membership, voting, lease, election, lock, transaction, snapshot, recovery, and administration authorities are separately attenuated. Mutual TLS, network locality, member identity, leader status, or data possession does not grant administrative or domain authority.

**RM-COORDINATION-CROSS-0002:** Protocol messages, logs/snapshots/backups, membership endpoints, election values, lease/lock names, transaction data, causal contexts, topology, telemetry, and audit are authenticated, encrypted, classified, minimized, redacted, retained, and tenant-partitioned.

**RM-COORDINATION-CROSS-0003:** Security review covers rogue/stale members, split brain, quorum manipulation, replay/downgrade, identity clone, stale leader/lease, fencing bypass, endpoint poisoning, snapshot/log substitution, rollback, resource exhaustion, timing/oracle leakage, unsafe recovery, and operator mistakes.

**RM-COORDINATION-CROSS-0004:** Observability correlates domain/configuration, participant incarnation, term/index/revision, operation/attempt, lease/fence, transaction/workflow, quorum/path, consistency/durability, state transition, and recovery without using identifiers as authority or unbounded dimensions.

**RM-COORDINATION-CROSS-0005:** Metrics separate proposal/commit/apply/read, election and unavailable time, quorum/failure suspicion, replication/catch-up/snapshot, lease renewal/fencing, lock queue/hold, transaction prepare/in-doubt, workflow/reconciliation, resource use, and telemetry loss.

**RM-COORDINATION-CROSS-0006:** Administrative approval and status expose affected domain/resources/fault domains, safety versus availability trade-off, consistency/data-loss/split-brain impact, fencing, point of no return, progress, cancellation limits, recovery, and residual uncertainty accessibly and locally.

**RM-COORDINATION-CROSS-0007:** Protocol identifiers, logical clocks, terms/indexes, timestamps, durations, and schemas are locale-independent. Human times and messages use explicit locale/time-zone context without weakening monotonic deadlines or clock-uncertainty evidence.

