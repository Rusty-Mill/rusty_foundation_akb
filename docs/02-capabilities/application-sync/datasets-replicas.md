# Datasets, replicas, objects, and topology

**RM-APP-SYNC-REPLICA-0001:** Dataset identity binds namespace, tenant/account, schema lineage, authority model, partitioning, residency, retention, and object-identity rules.

**RM-APP-SYNC-REPLICA-0002:** Replica identity includes immutable replica ID, incarnation, owner/workload/device, trust and key generation, storage generation, capabilities, creation/retirement state, and last authenticated evidence.

**RM-APP-SYNC-REPLICA-0003:** Restored, cloned, reinstalled, transferred, or rolled-back storage cannot silently reuse a replica incarnation or causal actor identity.

**RM-APP-SYNC-REPLICA-0004:** Topology declares authoritative, primary/secondary, peer, hub-spoke, relay, and read-only roles; permitted directions; fan-out; loop prevention; failover; and whether multiple writers exist.

**RM-APP-SYNC-REPLICA-0005:** Replica membership is expiring evidence, not permanent authority. Admission, key rotation, suspension, device loss, account sign-out, transfer, and retirement are versioned transitions.

**RM-APP-SYNC-REPLICA-0006:** Cross-dataset references define identity mapping, synchronization ordering, dangling-reference behavior, integrity repair, and whether atomic multi-object changes are supported.
