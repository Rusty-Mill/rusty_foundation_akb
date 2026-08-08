# Backup, restore, and point-in-time recovery

**RM-PERSISTENCE-BACKUP-0001:** A backup plan binds database/storage/schema/timeline generations, backup kind/base/dependencies, consistency point, included/excluded objects/logs/keys/configuration, encryption/signing, destination authority, retention/legal hold, resource policy, and restore objective.

**RM-PERSISTENCE-BACKUP-0002:** Started, snapshot established, data/log copied, manifest finalized, encrypted/signed, uploaded, replicated, cataloged, verified, retained, and expired/deleted are separate milestones. Copy completion is not recoverability.

**RM-PERSISTENCE-BACKUP-0003:** A manifest records exact provider/build/format, database/timeline/system identity, schema/catalog, object/chunk digests/lengths, base/incremental/log dependencies and ranges, consistency/LSN/version/time, keys, compression, creation evidence, and restore compatibility.

**RM-PERSISTENCE-BACKUP-0004:** Backup validation includes authenticated manifest and byte integrity, dependency closure, decrypt/decompress/read, isolated restore, provider recovery, schema/object/data invariants, application semantic probes, and measured recovery point/time. Sampling scope is disclosed.

**RM-PERSISTENCE-PITR-0001:** Point-in-time recovery binds one base and complete ordered log/archive chain, target by exact log/version/transaction or clock-qualified time, timeline/fork policy, excluded intervals, recovery mode, and expected data-loss boundary. Wall-clock targets include uncertainty.

**RM-PERSISTENCE-RESTORE-0001:** Restore is an immutable plan to a new database/storage/timeline generation with target isolation, overwrite prohibition by default, key/configuration mapping, topology, capacity, log application, validation, credential/endpoint cutover, fencing, rollback, and audit.

**RM-PERSISTENCE-RESTORE-0002:** Restored data cannot rejoin production until identity-clone/split-brain risks are fenced, secrets/tokens/leases/outbox jobs are reconciled, external systems are assessed, integrity/semantic checks pass, and application compatibility/readiness is proven.

**RM-PERSISTENCE-BACKUP-0005:** RPO, RTO, backup frequency, archive lag, retention, restore throughput, verification frequency, regional independence, immutability, deletion, and cost are measured objectives/evidence, never inferred from configured schedules.

