# Conformance

**RM-APP-SYNC-CONFORMANCE-0001:** Deterministic history suites enumerate replica/incarnation creation, offline edits, causal/concurrent changes, duplicates/reorder/loss, partition/heal, retries, crashes at every durability boundary, and final visible plus hidden metadata state.

**RM-APP-SYNC-CONFORMANCE-0002:** Identity suites cover reinstall, clone, restore, clock rollback, actor reuse, account/device transfer, key rotation, lost/retired return, object delete/recreate, and cross-tenant collisions.

**RM-APP-SYNC-CONFORMANCE-0003:** Merge suites cover every typed policy, three or more writers, delete-update, list/map/set/register operations, relation/invariant conflicts, malformed causal context, resolver crash/retry, unresolved state, and differential permutation tests.

**RM-APP-SYNC-CONFORMANCE-0004:** Selection suites cover expansion/contraction, missing dependencies, authorization/revocation changes, pagination mutation, partial snapshots, invalid checkpoints, full resnapshot, storage pressure, and metered/offline scheduling.

**RM-APP-SYNC-CONFORMANCE-0005:** Lifecycle suites cover schema/merge-policy migration with queued old changes, tombstone/frontier compaction, late replicas, backup/restore, downgrade, attachment partial transfer, erasure/hold, provider migration, and disaster recovery.

**RM-APP-SYNC-CONFORMANCE-0006:** Security suites cover cross-tenant substitution, forged replica/context/checkpoint, replay, downgrade, unauthorized filters/attachments/conflicts, metadata inference, decompression/parser bombs, and diagnostic leakage.

**RM-APP-SYNC-CONFORMANCE-0007:** Evidence records seeds, history/fault schedule, dataset/replica/schema/policy/provider/tool generations, selections/frontiers, clocks/network/storage limits, outputs, residual conflicts, convergence assertion, and artifact digests.
