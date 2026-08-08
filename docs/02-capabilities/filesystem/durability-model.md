# Filesystem durability model

| Field | Value |
|---|---|
| Status | Draft cross-capability quality model |
| Scope | File data, file metadata, namespace metadata, and storage acknowledgement |

## Core distinction

Visibility, atomicity, and durability are independent:

- **Visibility:** another observer can see a new value or namespace binding.
- **Atomicity:** observers see one valid state or another without a contract-created intermediate state.
- **Durability:** state survives a declared failure model after successful acknowledgement.

A successful write or atomic rename does not automatically establish durability.

## Failure models

Durability claims identify the failures they cover:

- Process failure while the OS remains running.
- OS crash or forced reboot.
- Device power loss with functioning write-cache flush semantics.
- Filesystem, controller, or media failure.
- Remote-server failure or network partition.
- Correlated site or hardware loss.

The portable foundation addresses only provider-declared local process/OS/device scopes. Replication and site-loss durability belong to storage services above the local filesystem.

## Durability levels

| Level | Name | Required evidence |
|---|---|---|
| D0 | Visible | Operation completed in the provider's live namespace/cache; no crash-survival promise. |
| D1 | Content synchronized | Required file content and retrieval-critical file metadata were submitted to and acknowledged by the provider's stable-storage boundary. |
| D2 | Namespace synchronized | D1 plus containing-directory/namespace mutation was submitted and acknowledged where the provider exposes that guarantee. |
| D3 | Device-stable ordered | D2 plus provider evidence that volatile device caches were flushed and required write ordering is honored. |

Levels are cumulative only when the provider supports every lower guarantee. An unavailable level is reported as unsupported; it is never silently reduced.

## Requirements

- **RM-FILESYSTEM-DURABILITY-0001:** Every synchronization result **MUST** identify the achieved level and failure model.
- **RM-FILESYSTEM-DURABILITY-0002:** A provider **MUST NOT** claim D1 from buffered write completion alone.
- **RM-FILESYSTEM-DURABILITY-0003:** D1 **MUST** include file-size and allocation metadata required to retrieve acknowledged content after the declared failure.
- **RM-FILESYSTEM-DURABILITY-0004:** D2 **MUST** include the namespace container synchronization required for creation, unlink, rename, or replacement persistence.
- **RM-FILESYSTEM-DURABILITY-0005:** D3 **MUST** be based on an OS/device mechanism with documented cache-flush and ordering semantics; elapsed delay is not evidence.
- **RM-FILESYSTEM-DURABILITY-0006:** A synchronization failure **MUST** preserve whether prior writes or namespace changes remain visible and whether persistence is indeterminate.
- **RM-FILESYSTEM-DURABILITY-0007:** Cancellation after synchronization begins **MUST NOT** report confirmed cancellation unless the provider establishes a canceled terminal state; durability may remain indeterminate.
- **RM-FILESYSTEM-DURABILITY-0008:** Remote and network filesystems **MUST** declare the acknowledgement boundary and server/storage assumptions.
- **RM-FILESYSTEM-DURABILITY-0009:** Providers **MUST** distinguish unsupported directory synchronization from successful D2.
- **RM-FILESYSTEM-DURABILITY-0010:** Benchmark results **MUST** identify durability level; D0 throughput cannot be compared as an equivalent baseline to D2/D3.

## Publication composition

A common single-file durable-publication sequence is:

```mermaid
flowchart LR
    Prepare["Create replacement in destination filesystem"] --> Write["Write complete content"]
    Write --> SyncFile["Synchronize replacement to required level"]
    SyncFile --> Replace["Atomic namespace replacement"]
    Replace --> SyncDirectory["Synchronize containing directory"]
    SyncDirectory --> Report["Report achieved durability + evidence"]
```

The exact sequence, metadata policy, backup, recovery markers, and failure reconciliation belong to a future platform service. This diagram is not a universal crash-consistency proof.

## Platform research

- Windows `FlushFileBuffers` flushes buffered file information to the device, while caching/write-through policy and filesystem/device behavior affect the actual boundary. `ReplaceFileW` documents `REPLACEFILE_WRITE_THROUGH` as unsupported, so replacement durability requires separate evidence.
- Linux `fsync` flushes file data and metadata but explicitly does not ensure the containing directory entry reached storage; directory `fsync` is separate.
- macOS documents that ordinary `fsync` may not force a drive's volatile cache to physical media and provides `F_FULLFSYNC` for a stronger request.

Primary references: [Windows FlushFileBuffers](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-flushfilebuffers), [Windows file caching](https://learn.microsoft.com/en-us/windows/win32/fileio/file-caching), [Linux fsync](https://man7.org/linux/man-pages/man2/fsync.2.html), [macOS fsync](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/fsync.2.html), and [macOS fcntl/F_FULLFSYNC](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/fcntl.2.html).
