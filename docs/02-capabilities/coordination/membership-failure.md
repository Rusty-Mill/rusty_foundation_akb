# Membership and failure evidence

**RM-COORDINATION-MEMBERSHIP-0001:** Membership snapshots identify configuration revision, participant identities/roles/endpoints/credentials/fault domains, voter/quorum rules, joint-transition state, source, commit evidence, and freshness. Observed endpoints or heartbeats cannot amend membership.

**RM-COORDINATION-MEMBERSHIP-0002:** Join, promote/demote, replace, remove, and fault-domain change are authority-bearing configuration operations with immutable plans, catch-up preconditions, quorum safety, joint/overlap transition, rollback limitations, audit, and final commit evidence.

**RM-COORDINATION-MEMBERSHIP-0003:** Reusing a participant identity after data loss, reinstall, restore, clone, or credential rotation is prohibited unless a recovery protocol proves continuity. New storage or process state receives a new incarnation even at the same host/address.

**RM-COORDINATION-FAILURE-0001:** Failure detectors emit alive/suspected/unreachable/left/removed/recovering/unknown observations with subject generation, source, monotonic time, evidence window, threshold, path and clock quality, and false-positive/negative characteristics.

**RM-COORDINATION-FAILURE-0002:** Timeout, refused connection, missing heartbeat, process exit observation, host health, quorum loss, and administrative removal are different. None alone proves that a participant cannot execute against another network path or external resource.

**RM-COORDINATION-FAILURE-0003:** Gossip and eventually convergent membership expose local view revision, dissemination/merge rules, tombstone/identity reuse policy, anti-entropy, partition behavior, convergence evidence, and explicit nonclaims about linearizable membership or exclusive authority.

**RM-COORDINATION-FAILURE-0004:** Watches are invalidation streams over revisioned snapshots. Compaction, overflow, disconnect, reordering, duplicate, reset, and resubscription require bounded snapshot reconciliation; event receipt is not current-state proof.

