# `rm.filesystem.directory` — Directory resource

| Field | Value |
|---|---|
| Status | Draft |
| Contract version | 0.1.0 |
| Domain | Filesystem |
| Owner | Unassigned |
| Candidate profiles | CLI, Desktop, Server, Embedded/headless |

## Purpose

Represent an opened directory as an authority-bearing resource that anchors relative resolution, namespace mutation, enumeration, metadata, and directory synchronization without relying on process current directory.

## Requirements

- **RM-FILESYSTEM-DIRECTORY-0001:** A directory resource **MUST** identify its granted lookup, enumeration, mutation, metadata, and synchronization authority.
- **RM-FILESYSTEM-DIRECTORY-0002:** Relative operations **MUST** remain anchored to the opened directory object even if its external path is renamed.
- **RM-FILESYSTEM-DIRECTORY-0003:** Resource close **MUST** be deterministic when requested and eventual on drop; safe interfaces **MUST** prevent double close.
- **RM-FILESYSTEM-DIRECTORY-0004:** Enumeration, when requested, **MUST** preserve native names losslessly and **MUST** define ordering as unspecified unless a stronger quality is selected.
- **RM-FILESYSTEM-DIRECTORY-0005:** Enumeration **MUST** define behavior under concurrent namespace mutation and **MUST NOT** imply a consistent snapshot unless proven.
- **RM-FILESYSTEM-DIRECTORY-0006:** Namespace mutation operations **MUST** require explicit mutation authority and typed creation/removal semantics.
- **RM-FILESYSTEM-DIRECTORY-0007:** Directory synchronization **MUST** report its supported durability scope and **MUST NOT** be simulated as successful when the provider cannot flush namespace metadata.
- **RM-FILESYSTEM-DIRECTORY-0008:** Object identity **MUST** follow the scoped, reusable identity model in `rm.filesystem.metadata`.
- **RM-FILESYSTEM-DIRECTORY-0009:** A directory resource **MUST NOT** grant absolute/device namespace access merely because it can anchor relative operations.
- **RM-FILESYSTEM-DIRECTORY-0010:** Diagnostics and enumeration **MUST** apply the caller's path-disclosure policy.

## Dependencies

None. Resolution consumes a directory resource; it does not create the directory capability's semantics.

## Platform realization

| Platform | Candidate mechanism | Key variance |
|---|---|---|
| Windows | Directory handle with appropriate native access/share flags | Relative native operations, deletion sharing, reparse behavior, directory flush support |
| Linux | Directory file descriptor (`O_DIRECTORY`/`O_PATH` as appropriate) | Read versus path-only authority, directory `fsync` support |
| macOS | Directory descriptor | Enumeration mutation behavior and filesystem-specific sync guarantees |

## Conformance direction

Test rename stability, authority separation, close races, concurrent enumeration mutation, lossless names, namespace mutation, identity, diagnostic redaction, and directory synchronization claims.
