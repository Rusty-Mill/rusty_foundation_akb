# Persistence model and capabilities

**RM-PERSISTENCE-MODEL-0001:** A database intent binds product/provider/engine and protocol revisions, logical database/namespace, tenant and principal, data/schema generations, consistency/isolation/durability, encryption, topology, resource limits, migration/recovery policy, and exact authority.

**RM-PERSISTENCE-MODEL-0002:** Database, cluster, instance/process, storage generation, catalog/schema, namespace, table/collection, record/document/row, key, index, constraint, transaction, session, statement, cursor, replica, log/stream, backup, and restore are distinct typed identities.

**RM-PERSISTENCE-MODEL-0003:** Embedded/in-process, local service, remote service, distributed SQL, key-value, document, and other selected models expose only proven capabilities. Provider selection follows workload contracts and cannot silently emulate missing transactions, constraints, isolation, or durability client-side.

**RM-PERSISTENCE-MODEL-0004:** Open, authenticated, session-ready, statement prepared, execution started, rows/records produced, mutation accepted, transaction committed, durable, replicated, visible, archived, change-published, and externally reconciled are distinct milestones.

**RM-PERSISTENCE-MODEL-0005:** Authority attenuates connect/read/query/write/schema/admin/backup/restore/replication/key-management operations by database, namespace, object, row/tenant policy, operation, and lifetime. Connection strings, paths, object names, or transaction tokens grant no authority.

**RM-PERSISTENCE-MODEL-0006:** Errors distinguish validation/schema, authentication/authorization, unavailable, overload/quota, timeout/cancellation, conflict/serialization/deadlock, constraint, data corruption, storage full/read-only, transaction uncertain, stale replica/schema, migration/recovery, and unsupported-quality outcomes.

**RM-PERSISTENCE-MODEL-0007:** Async-first query/mutation/stream/transaction operations are bounded and cancellation-safe. Sync-complete equivalents preserve session/transaction semantics and never start a hidden runtime, transaction, retry loop, or pool.

