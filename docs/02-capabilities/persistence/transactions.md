# Transactions, isolation, and durability

**RM-PERSISTENCE-TXN-0001:** A transaction plan binds read/write objects or dynamic-access policy, isolation/history property, read timestamp/snapshot, durability/replication acknowledgment, read-only/deferrable mode, timeout, retry/idempotency, lock/conflict policy, and external-effect exclusions.

**RM-PERSISTENCE-TXN-0002:** Begun, snapshot acquired, statement accepted/completed, writes buffered/logged, commit requested, logically committed, requested durability satisfied, replica visibility achieved, response observed, and archived are distinct milestones.

**RM-PERSISTENCE-TXN-0003:** Read-uncommitted, read-committed, cursor stability, repeatable-read, snapshot isolation, serializable, strict-serializable/external, and provider-specific levels map to exact allowed/prohibited histories and retry behavior. Equal names do not imply equal provider semantics.

**RM-PERSISTENCE-TXN-0004:** Savepoints create nested rollback markers within one transaction, not nested durability or independent commits. Rollback-to, release, statement failure, transaction-aborted state, locks/resources, and external effects remain explicit.

**RM-PERSISTENCE-TXN-0005:** Commit timeout/disconnect/cancellation can produce unknown outcome. Clients reconcile by transaction/idempotency/domain identity and current authoritative state; they do not automatically rerun a non-idempotent transaction.

**RM-PERSISTENCE-TXN-0006:** Durability claims name log/data/checksum flush, filesystem/storage/controller/device boundary, replicas/quorum, synchronized/async mode, acknowledged failure model, battery/cache assumptions, recovery point, and provider evidence. `committed` alone cannot imply power-loss durability.

**RM-PERSISTENCE-TXN-0007:** Serialization, conflict, deadlock-victim, leader/topology retry, and transient errors are separate. Retrying re-executes the entire logical transaction under a new snapshot/attempt and revalidates current authority and external inputs.

**RM-PERSISTENCE-TXN-0008:** Transaction cancellation/rollback does not reverse messages, file/device/network/user-visible actions, irreversible sequences, or other stores. Transactional outbox/inbox and saga compensation remain explicit compositions.

