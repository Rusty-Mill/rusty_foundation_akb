# `rm.filesystem.file` — Regular-file resource and I/O

| Field | Value |
|---|---|
| Status | Draft |
| Contract version | 0.1.0 |
| Domain | Filesystem |
| Owner | Unassigned |
| Candidate profiles | CLI, Desktop, Server, Embedded/headless |

## Purpose

Provide owned regular-file resources with explicit access authority, positioned byte I/O, size management, synchronization, cancellation semantics, and both async and sync use paths.

## Scope

Positioned operations are primitive. A mutable shared cursor is a separately synchronized convenience above them. The base capability addresses regular files, not terminals, pipes, sockets, directories, or arbitrary devices.

## Requirements

- **RM-FILESYSTEM-FILE-0001:** A file resource **MUST** expose its granted access and relevant provider constraints without increasing them after open.
- **RM-FILESYSTEM-FILE-0002:** Resource close **MUST** be deterministic when requested and eventual on drop; double close **MUST** be impossible through safe interfaces.
- **RM-FILESYSTEM-FILE-0003:** Positioned reads and writes **MUST NOT** modify a shared file cursor.
- **RM-FILESYSTEM-FILE-0004:** Successful reads and writes **MAY** transfer fewer bytes than requested and **MUST** report exact progress.
- **RM-FILESYSTEM-FILE-0005:** End of file **MUST** be distinct from failure and represented as zero read progress at or beyond the current end.
- **RM-FILESYSTEM-FILE-0006:** Offset and length arithmetic **MUST** detect overflow and provider range limits before unsafe conversion.
- **RM-FILESYSTEM-FILE-0007:** Concurrent positioned operations **MUST** define overlapping-write behavior and **MUST NOT** introduce cursor races.
- **RM-FILESYSTEM-FILE-0008:** Async operations **MUST** retain exclusive access to required buffers and native operation state until terminal completion.
- **RM-FILESYSTEM-FILE-0009:** Cancellation **MUST** follow `rm.runtime.cancellation`; a request **MUST NOT** be reported as confirmed cancellation until the I/O operation reaches a terminal canceled outcome.
- **RM-FILESYSTEM-FILE-0010:** The synchronous path **MUST NOT** create or nest an async runtime.
- **RM-FILESYSTEM-FILE-0011:** Size change **MUST** define zero-fill/hole behavior only to the extent guaranteed by the provider and filesystem.
- **RM-FILESYSTEM-FILE-0012:** Data synchronization **MUST** distinguish requests to flush file content, file metadata, and containing-directory namespace metadata where supported.
- **RM-FILESYSTEM-FILE-0013:** A successful synchronization request **MUST** state its durability scope and **MUST NOT** imply resistance to failures outside that scope.
- **RM-FILESYSTEM-FILE-0014:** Errors **MUST** use portable semantic categories with preserved provider diagnostics; raw OS codes **MUST NOT** be the only public model.

## Error categories

Access denied, resource closed, unsupported operation, invalid range, storage exhausted, quota exceeded, read-only filesystem, interrupted, confirmed canceled, device/media failure, stale/disconnected resource, and other provider failure with diagnostic context.

## Concurrency and atomicity

Disjoint positioned I/O may proceed concurrently. Atomicity of overlapping reads/writes, append operations, sector-sized operations, or multi-buffer operations is not assumed; each provider declares guarantees. Append is not modeled as positioned write because some platforms/filesystems bind it to open state and provide different atomicity.

## Platform realization

| Platform | Candidate mechanisms | Important variance |
|---|---|---|
| Windows | File handle, `ReadFile`/`WriteFile` with explicit offsets and completion | Sharing, delete-pending, buffer lifetime, cancellation completion |
| Linux | Descriptor plus `pread`/`pwrite` or async facilities | `O_APPEND` interaction with `pwrite`, signals, filesystem behavior |
| macOS | Descriptor plus `pread`/`pwrite` or platform async composition | Filesystem caching/durability and cancellation mechanism |

## Conformance direction

Test short I/O, EOF, sparse/extended size behavior, large offsets, close races, buffer ownership, overlapping operations, cancellation races, sync/async parity, storage exhaustion, read-only media, and durability claims on representative local and network filesystems.

Synchronization claims use the [filesystem durability model](durability-model.md).
