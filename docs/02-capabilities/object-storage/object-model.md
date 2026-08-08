# Object-storage model and capability boundary

**RM-OBJECT-MODEL-0001:** Storage intent binds provider/service/protocol revision, account/project, endpoint/region, namespace/bucket/container generation, tenant/principal, consistency/versioning, encryption, retention, replication, network/cost, resource limits, and exact authority.

**RM-OBJECT-MODEL-0002:** Account/project, service endpoint, namespace/bucket/container, object key, live object, object version/generation, metadata generation, upload session, part/block/chunk, descriptor, replica, inventory, lifecycle rule, retention policy, and legal hold are distinct typed identities.

**RM-OBJECT-MODEL-0003:** Embedded/local blob stores, remote object services, content-addressed stores, and repository registries expose only proven contracts. Filesystem path semantics, atomic rename, directories, append, random mutation, locks, mmap, and POSIX permissions are not inferred.

**RM-OBJECT-MODEL-0004:** Request accepted, bytes transferred, provider validated, staging persisted, completion committed, requested durability/replication satisfied, visible to read/list, event/inventory observed, retained, archived, and recoverable are separate milestones.

**RM-OBJECT-MODEL-0005:** Authority attenuates list/read/range/write/create-only/replace/metadata/copy/compose/delete/version/admin/lifecycle/retention/restore/replication/inventory operations by namespace, key prefix/exact key, generation, size/type, network, lifetime, and conditions.

**RM-OBJECT-MODEL-0006:** Errors distinguish validation, authentication/authorization, not-found/no-live-version, precondition/conflict, retention/hold, checksum/digest, incomplete upload, timeout/cancellation/unknown commit, unavailable/throttle/quota, storage class/archive, stale replica/list, and provider-unsupported qualities.

**RM-OBJECT-MODEL-0007:** Async-first data operations are bounded streaming state machines. Sync-complete equivalents preserve staging/generation/precondition evidence and never create hidden runtimes, buffers, retries, multipart sessions, or credential refresh workers.

