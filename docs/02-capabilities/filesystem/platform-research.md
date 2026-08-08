# Filesystem foundations platform research

| Field | Value |
|---|---|
| Status | Draft research; descriptive, not normative |
| Reviewed | 2026-08-08 |

## Cross-platform findings

The common foundation should be handle-centric and directory-relative. Paths remain necessary for namespace lookup, but security and race resistance improve when later operations refer to already-open directories and files. Native filesystems differ in name encoding, sharing, deletion, metadata, link traversal, asynchronous I/O, identity stability, and durability.

## Windows

| Concern | Candidate mechanism | Architectural implication |
|---|---|---|
| Open/resolution | `CreateFileW` with access, sharing, creation, attributes, and reparse options | Open policy must model sharing and link/reparse behavior explicitly. |
| Resource identity | File handles plus `FILE_ID_INFO` and volume identity | IDs are scoped and may be reused; handle identity is primary while open. |
| Metadata | `GetFileInformationByHandleEx` | Fields and precision depend on filesystem; query by handle avoids a second path race. |
| Sync/async I/O | `ReadFile`/`WriteFile`, positioned `OVERLAPPED`, completion mechanisms | Buffer lifetime extends through terminal completion; partial I/O remains possible. |
| Cancellation | `CancelIoEx` | Cancellation is requested, not confirmed until completion is observed. |
| Replacement | `ReplaceFileW` | Same-volume requirement; metadata/ACL/stream merging and partial failure states require explicit policy. |
| Namespace semantics | Share modes, delete-pending state, reparse points, drive/UNC/device prefixes | POSIX unlink/rename assumptions are not portable. |

## Linux

| Concern | Candidate mechanism | Architectural implication |
|---|---|---|
| Directory-relative open | `openat` | Avoids process-current-directory races and anchors lookup to a directory descriptor. |
| Constrained resolution | `openat2` with `RESOLVE_*` | Strong containment is native on newer kernels; fallback strength must be declared. |
| Positioned I/O | `pread`/`pwrite` | Independent offsets avoid shared-cursor races; successful partial transfer is normal. |
| Metadata | `statx`/`fstatat`/`fstat` | Field availability masks and timestamps support explicit metadata presence. |
| Replacement | `renameat`/`renameat2` | Existing destination replacement is namespace-atomic on the same mounted filesystem, subject to filesystem support and flags. |
| Watching | inotify/fanotify | Event loss and watch invalidation require rescan semantics; deferred from this slice. |

Linux documents `openat` directory descriptors as a defense against path-prefix races. `openat2` adds extensible resolution constraints. `pread` and `pwrite` preserve the descriptor's shared file offset, although Linux `pwrite` with `O_APPEND` has a documented semantic caveat.

## macOS

| Concern | Candidate mechanism | Architectural implication |
|---|---|---|
| Directory-relative operations | POSIX `openat`/`fstatat` family | Supports handle-relative structure, though Linux-specific `openat2` constraints are unavailable. |
| Positioned I/O | `pread`/`pwrite` | Same portable partial-progress model as POSIX, with platform/filesystem-specific errors. |
| Metadata | `fstat`/`fstatat`, attribute APIs where advanced fields are required | Basic metadata is common; Finder metadata, forks, ACLs, and extended attributes are extensions. |
| Replacement | `rename` and platform extensions such as swap/exclusive variants | Same-filesystem namespace semantics must be separated from durability. |
| Watching | FSEvents or vnode dispatch sources | FSEvents can be coarse, persistent, and lossy with explicit rescan flags; deferred from this slice. |

Apple's FSEvents documentation explicitly exposes dropped-event and must-rescan states, supporting a future watch contract that treats events as invalidation hints rather than a perfect journal by default.

## Primary sources

### Microsoft

- [CreateFileW](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilew)
- [GetFileInformationByHandleEx](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-getfileinformationbyhandleex)
- [BY_HANDLE_FILE_INFORMATION and identity caveats](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/ns-fileapi-by_handle_file_information)
- [ReadFile](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-readfile)
- [WriteFile](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-writefile)
- [ReplaceFileW](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-replacefilew)
- [CancelIoEx](https://learn.microsoft.com/en-us/windows/win32/fileio/cancelioex-func)
- [FlushFileBuffers](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-flushfilebuffers)
- [File caching](https://learn.microsoft.com/en-us/windows/win32/fileio/file-caching)

### Linux man-pages project

- [open and openat](https://man7.org/linux/man-pages/man2/open.2.html)
- [openat2](https://www.man7.org/linux/man-pages/man2/openat2.2.html)
- [pread and pwrite](https://www.man7.org/linux/man-pages/man2/pwrite.2.html)
- [statx](https://man7.org/linux/man-pages/man2/statx.2.html)
- [rename, renameat, and renameat2](https://man7.org/linux/man-pages/man2/renameat2.2.html)
- [inotify](https://man7.org/linux/man-pages/man7/inotify.7.html)
- [fsync](https://man7.org/linux/man-pages/man2/fsync.2.html)

### Apple

- [rename manual page](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/rename.2.html)
- [File System Events](https://developer.apple.com/documentation/coreservices/file_system_events)
- [FSEventStream event flags](https://developer.apple.com/documentation/coreservices/file_system_events/1455361-fseventstreameventflags)
- [fsync](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/fsync.2.html)
- [fcntl and F_FULLFSYNC](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/fcntl.2.html)
