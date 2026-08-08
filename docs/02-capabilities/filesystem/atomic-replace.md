# `rm.filesystem.atomic-replace` — Atomic namespace replacement

| Field | Value |
|---|---|
| Status | Draft |
| Contract version | 0.1.0 |
| Domain | Filesystem |
| Owner | Unassigned |
| Candidate profiles | CLI, Desktop, Server |

## Purpose

Replace one destination namespace binding with a prepared regular-file resource so concurrent namespace observers see either the prior or replacement binding, never an intentional missing intermediate state.

## Non-goals

- Cross-filesystem atomic move.
- Transactional update of multiple paths.
- Automatic data or directory durability.
- Universal preservation of ACLs, streams, forks, timestamps, identity, or storage attributes.

## Requirements

- **RM-FILESYSTEM-REPLACE-0001:** Source and destination **MUST** be resolved relative to explicit directory authorities.
- **RM-FILESYSTEM-REPLACE-0002:** The provider **MUST** verify that source and destination are eligible for its atomic replacement guarantee, including filesystem/volume constraints.
- **RM-FILESYSTEM-REPLACE-0003:** On success, namespace observers **MUST** see the destination bound to either the old or replacement object, without an operation-created absent interval.
- **RM-FILESYSTEM-REPLACE-0004:** Atomic namespace visibility **MUST NOT** be described as durable persistence.
- **RM-FILESYSTEM-REPLACE-0005:** Metadata preservation policy **MUST** explicitly cover security, ownership, timestamps, streams/forks, attributes, compression, and encryption as preserve, replace, merge, unsupported, or provider-defined.
- **RM-FILESYSTEM-REPLACE-0006:** Identity behavior **MUST** state whether the resulting destination retains source identity, destination identity, or provider-defined identity.
- **RM-FILESYSTEM-REPLACE-0007:** If the native mechanism exposes partial failure states, the error **MUST** report the observable namespace state or that it is indeterminate and requires inspection.
- **RM-FILESYSTEM-REPLACE-0008:** Replacement **MUST NOT** silently fall back to copy-delete while claiming atomicity.
- **RM-FILESYSTEM-REPLACE-0009:** An optional backup binding **MUST** have independently specified overwrite, atomicity, metadata, and cleanup behavior.
- **RM-FILESYSTEM-REPLACE-0010:** Cancellation after the native commit point **MUST NOT** report the operation as canceled if replacement became visible.
- **RM-FILESYSTEM-REPLACE-0011:** Durability composition **MUST** identify required source-data synchronization and containing-directory synchronization steps and their provider guarantees.
- **RM-FILESYSTEM-REPLACE-0012:** Replacement authority **MUST** include destination namespace mutation and all native metadata rights required by the selected policy.

## Terminal outcomes

- Replaced: destination now names the replacement object.
- Not replaced: pre-operation destination binding remains.
- Partial/inspect: provider reports a documented intermediate namespace or metadata state.
- Indeterminate: loss of connection/device/provider state prevents reliable observation; caller must reconcile.

## Platform realization

| Platform | Candidate mechanism | Key variance |
|---|---|---|
| Windows | `ReplaceFileW` or handle-relative native mechanisms | Same volume, metadata/ACL merging, documented partial error states |
| Linux | `renameat`/`renameat2` | Same mounted filesystem, flags/filesystem support, directory durability separate |
| macOS | `rename` and supported platform extensions | Same filesystem, clone/copy-on-write and metadata behavior vary |

## Conformance direction

Test concurrent observers, source/destination open handles, same/different filesystem, metadata policies, backup behavior, injected failures, cancellation around commit, post-crash inspection, and durability sequences on each claimed filesystem.
