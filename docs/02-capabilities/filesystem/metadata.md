# `rm.filesystem.metadata` — Filesystem metadata snapshot

| Field | Value |
|---|---|
| Status | Draft |
| Contract version | 0.1.0 |
| Domain | Filesystem |
| Owner | Unassigned |
| Candidate profiles | CLI, Desktop, Server, Embedded/headless |

## Purpose

Return a typed, point-in-time description of a resolved filesystem resource with explicit field availability, timestamp precision, identity scope, and link-subject semantics.

## Requirements

- **RM-FILESYSTEM-METADATA-0001:** Metadata query **MUST** state whether it describes the opened object, a directory entry, or an unresolved link object.
- **RM-FILESYSTEM-METADATA-0002:** Each optional field **MUST** distinguish present, unavailable, unsupported, and unknown/error states where the distinction is observable.
- **RM-FILESYSTEM-METADATA-0003:** Providers **MUST NOT** fabricate zero, epoch, or empty values for unsupported fields.
- **RM-FILESYSTEM-METADATA-0004:** Object kind **MUST** distinguish regular file, directory, symbolic-link/reparse object, and other provider-defined kinds without misclassifying unknown kinds.
- **RM-FILESYSTEM-METADATA-0005:** Size **MUST** distinguish logical byte length from allocated storage when both are exposed.
- **RM-FILESYSTEM-METADATA-0006:** Timestamps **MUST** identify semantic kind and reported precision; creation/birth time **MUST NOT** be inferred from change time.
- **RM-FILESYSTEM-METADATA-0007:** A stable identity claim **MUST** include its scope and lifetime limitations and **MUST NOT** promise global or permanent uniqueness.
- **RM-FILESYSTEM-METADATA-0008:** Metadata snapshots **MUST** be immutable values and **MUST NOT** imply that the resource remains unchanged afterward.
- **RM-FILESYSTEM-METADATA-0009:** Path-based convenience queries **MUST** disclose their race and link-following semantics; handle-based queries are the normative stable path.
- **RM-FILESYSTEM-METADATA-0010:** Permission/security summaries **MUST NOT** collapse ACL, inheritance, and platform policy into misleading POSIX-style bits.
- **RM-FILESYSTEM-METADATA-0011:** Unknown native attributes **MUST** be preserved through an extension mechanism or reported as unmodeled; they **MUST NOT** change base semantics silently.

## Base fields

Object kind, logical size, allocated size, modification time, access time, metadata-change time, creation/birth time, link count, scoped object identity, read-only indicator, and coarse execution/hidden/archive-like attributes only where their semantics are honestly representable.

Security descriptors, POSIX mode/owner, ACLs, extended attributes, alternate streams, forks, compression, encryption, sparse state, and filesystem-specific flags are extensions or later capabilities.

## Identity model

Identity is a tuple whose provider-defined scope can include filesystem/volume identity, object identifier, and generation where available. Equality means evidence that two handles referred to the same live object within the provider's stated scope at observation time. IDs may be reused after deletion and may change on some filesystems or replacement operations.

## Conformance direction

Test missing fields, timestamp precision, link follow/no-follow, handle versus path races, identity comparison and reuse caveats, concurrent mutation, large sizes, uncommon object kinds, and multiple filesystem formats per platform.
