# `rm.filesystem.resolve` — Directory-relative resolution

| Field | Value |
|---|---|
| Status | Draft |
| Contract version | 0.1.0 |
| Domain | Filesystem |
| Owner | Unassigned |
| Candidate profiles | CLI, Desktop, Server, Embedded/headless |
| Decision | [ADR-0007](../../adr/0007-directory-relative-resolution-is-the-security-boundary.md) |

## Purpose

Resolve a relative path beneath an explicit directory authority and return a typed filesystem resource while enforcing declared traversal, link, object-type, creation, and access policy.

## Non-goals

- Treating lexical normalization as security validation.
- Guaranteeing containment stronger than the selected provider can prove.
- Resolving arbitrary platform device namespaces through the portable contract.
- Returning a canonical path as the primary result.

## Semantic model

Resolution consumes a directory resource, a relative path value, requested access, expected object kind, creation disposition, link/traversal policy, and quality requirements. It returns an opened resource plus a resolution report, or a typed failure. The returned resource remains valid according to handle lifecycle even if namespace bindings subsequently change.

## Requirements

- **RM-FILESYSTEM-RESOLVE-0001:** Portable resolution **MUST** accept an explicit directory authority; process current directory **MUST NOT** be the implicit security root.
- **RM-FILESYSTEM-RESOLVE-0002:** A provider **MUST** distinguish lexical path rejection from filesystem lookup failure.
- **RM-FILESYSTEM-RESOLVE-0003:** Resolution policy **MUST** state whether symbolic links, junctions, reparse points, aliases, and mount crossings are followed, rejected, or reported as unsupported.
- **RM-FILESYSTEM-RESOLVE-0004:** A containment claim **MUST** describe its strength and **MUST NOT** be based only on pre-resolution string normalization or canonicalization.
- **RM-FILESYSTEM-RESOLVE-0005:** Expected object kind **MUST** be checked against the opened object, not a pre-open metadata query alone.
- **RM-FILESYSTEM-RESOLVE-0006:** Creation policy **MUST** distinguish open-existing, create-new, open-or-create, truncate-existing, and create-or-truncate semantics.
- **RM-FILESYSTEM-RESOLVE-0007:** Requested access and sharing/deletion policy **MUST** be explicit and mapped without silently increasing authority.
- **RM-FILESYSTEM-RESOLVE-0008:** The provider **MUST** report emulated or weakened traversal constraints.
- **RM-FILESYSTEM-RESOLVE-0009:** A resolution failure **MUST NOT** expose uninitialized or partially authorized resource state.
- **RM-FILESYSTEM-RESOLVE-0010:** Successful resolution **MUST** return a resource whose cleanup is deterministic and safe across error and cancellation paths.
- **RM-FILESYSTEM-RESOLVE-0011:** Absolute paths and platform device prefixes **MUST** be rejected by the portable relative-resolution operation unless an explicit extension authorizes them.
- **RM-FILESYSTEM-RESOLVE-0012:** Resolution diagnostics **MUST NOT** disclose path components beyond the caller's diagnostic authority.

## Policy dimensions

- Link/reparse traversal: follow all, reject final, reject any, or provider extension.
- Mount/volume crossing: allow, reject, or unknown.
- Parent traversal: reject lexically and enforce containment during lookup.
- Object kind: regular file, directory, link object, or provider extension.
- Access: read data, write data, append, metadata, namespace mutation, synchronization.
- Sharing: portable cooperative default plus explicit platform extension where meaningful.

## Platform realization

| Platform | Candidate path | Key issue |
|---|---|---|
| Windows | Directory handle plus native relative-object facilities or carefully constrained `CreateFileW` path | Reparse traversal and DOS/device namespace semantics |
| Linux | `openat2` where available; `openat`-based fallback with declared weaker guarantees | Kernel/version support for atomic constraints |
| macOS | `openat`/`fstatat` composition with stepwise traversal as required | No direct equivalent to all Linux `RESOLVE_*` policies |

## Conformance direction

Test link-swap and rename races, parent traversal, absolute/prefix rejection, object-kind substitution, mount crossing, create dispositions, access escalation, cleanup, diagnostic redaction, and declared fallback strength on each filesystem family.
