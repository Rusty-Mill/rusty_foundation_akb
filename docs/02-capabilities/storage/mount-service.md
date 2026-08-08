# Mount and unmount service

Mounting is a platform service composing a filesystem instance, namespace authority, target location, mount options, authentication/unlock prerequisites, policy, and arbitration. It is not part of passive discovery.

**RM-STORAGE-MOUNT-0001:** A mount request MUST identify source generation, target namespace, target authority/location, requested access/options, interaction policy, and acceptable degradation.

**RM-STORAGE-MOUNT-0002:** The result MUST report the effective mount relationship, namespace revision, effective read/write/security/execution/cache options, provider transformations, and any ignored or degraded request.

**RM-STORAGE-MOUNT-0003:** The service MUST NOT silently unlock encrypted media, execute autorun content, trust filesystem labels, weaken execution/security options, or choose a new target after a conflict.

**RM-STORAGE-MOUNT-0004:** Unmount MUST distinguish ordinary, lazy/detached, forced, recursive/whole-media, and namespace-only semantics. Unsupported force/lazy behavior MUST NOT be emulated by merely forgetting the mount.

**RM-STORAGE-MOUNT-0005:** Busy/veto results SHOULD report bounded structured causes where available without leaking another user's sensitive paths or process details.

**RM-STORAGE-MOUNT-0006:** Mount/unmount completion MUST be followed by snapshot reconciliation; service callback success is not proof that every namespace view or client has converged.

Application sandbox document-picker/security-scoped access is not a general mount capability. It yields filesystem authority through the platform's user-consent path.
