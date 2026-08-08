# Volume and mount observation

`rm.storage.volume-observer` publishes immutable snapshots of visible storage entities and their relationships. `rm.storage.mount-observer` publishes mounts within one explicitly selected mount namespace/session scope.

**RM-STORAGE-OBSERVE-0001:** Snapshots MUST record revision, observation bounds, scope/namespace generation, completeness, entities, relationships, properties, and redactions.

**RM-STORAGE-OBSERVE-0002:** Present, recognized, unlock-required, mountable, mounted, read-only, degraded, faulted, ejecting, disconnected, and unknown states MUST remain distinct where supported.

**RM-STORAGE-OBSERVE-0003:** Enumeration MUST NOT mount, unlock, repair, probe by executing filesystem code outside platform policy, spin up media solely for optional metadata, or request privileges/consent.

**RM-STORAGE-OBSERVE-0004:** Notifications are invalidation hints. Add/remove/change/mount/unmount events MUST trigger bounded reconciliation and publish diffs between coherent snapshot revisions.

**RM-STORAGE-OBSERVE-0005:** Namespace changes, overflow, service restart, suspend/resume, and surprise removal MUST force full reconciliation when incremental completeness is not proven.

General device correlation uses the [device discovery](../devices/README.md) handoff only when proven. A filesystem supplied by network, disk image, synthetic provider, or userspace service may have no physical-device mapping.
