# Storage entity and identity model

| Entity | Meaning |
|---|---|
| Device | Platform hardware/virtual device generation |
| Media | Inserted, attached, or virtual storage medium generation |
| Region | Partition, logical volume, container, or addressable slice |
| Filesystem instance | Recognized filesystem state on a region or virtual source |
| Mount | Relationship between a filesystem view and one namespace location |
| Path | Name resolved relative to filesystem directory authority |

**RM-STORAGE-IDENTITY-0001:** Every reference MUST state its entity kind, provider, observation scope, and generation; references of different kinds MUST NOT compare as the same identity.

**RM-STORAGE-IDENTITY-0002:** Removal/reinsertion, media change, remapping, filesystem recreation, mount replacement, namespace change, or material uncertainty MUST invalidate or advance the affected generation.

**RM-STORAGE-IDENTITY-0003:** Labels, filesystem UUIDs, partition GUIDs, drive letters, mount paths, device nodes, serial numbers, capacities, and content fingerprints MUST NOT individually be treated as universal identity.

**RM-STORAGE-IDENTITY-0004:** Persistent matching MUST report the evidence vector, scope, confidence, duplicates, and ambiguity. Destructive or sensitive operations require current-generation revalidation and confirmation policy.

**RM-STORAGE-IDENTITY-0005:** A mount reference MUST bind both the namespace generation and filesystem-view generation; a path string is neither mount identity nor authority.

See [ADR-0054](../../adr/0054-a-mount-is-a-namespace-relationship-not-volume-identity.md).
