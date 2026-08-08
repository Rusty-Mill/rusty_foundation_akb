# Lifecycle, retention, legal hold, and erasure

**RM-OBJECT-LIFECYCLE-0001:** Lifecycle rules bind exact configuration generation, namespace/prefix/tags/age/version state, action, storage class, retention/hold exclusions, minimum-age/time-zone/clock semantics, priority/conflicts, provider evaluation schedule, and authority.

**RM-OBJECT-LIFECYCLE-0002:** Rule configured/enabled, object eligible, action queued/started/completed, replicas/inventory updated, bytes reclaimed, and billing changed are separate. Eligibility time is not deletion or transition proof.

**RM-OBJECT-RETENTION-0001:** Retention binds scope/object version, mode/governance/compliance quality, retain-until time and clock, policy generation, creator, bypass authority, extension/non-shortening rules, storage/provider enforcement evidence, and legal/audit context.

**RM-OBJECT-HOLD-0001:** Legal/event/administrative holds are separately identified version-scoped states with reason/reference, authority, set/release evidence, concurrency preconditions, audit, and privacy. Hold release does not itself delete content.

**RM-OBJECT-RETENTION-0002:** WORM/immutability claims name protected operations/metadata, principals including administrators, provider/account configuration, versioning prerequisites, replication, key deletion, suspension/termination behavior, certification, and conformance evidence.

**RM-OBJECT-ERASURE-0001:** Erasure plans enumerate live/noncurrent/soft-deleted objects, replicas, caches/CDNs, multipart staging, inventory/events/logs, backups/archives, derived content/address graphs, encryption keys, retention/holds, and third-party copies with legal conflicts and residuals.

**RM-OBJECT-ERASURE-0002:** Logical delete, provider purge, replica/cache expiry, lifecycle execution, media reclamation, encryption-key destruction, backup expiry, and verified privacy completion are separate. Inability to erase due to retention/hold is reported, not concealed.

