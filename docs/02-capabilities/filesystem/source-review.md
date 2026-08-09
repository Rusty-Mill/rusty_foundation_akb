# Filesystem source review

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Expires | On supported OS/kernel/SDK or filesystem-support change, or 2027-02-08, whichever occurs first |
| Reviewer | Filesystem capability owner |
| Open blocking findings | None for planning eligibility; exact supported generations and filesystem matrices remain trial inputs |

| Source | Class and reviewed status | Proposition supported | Impact and limitation |
|---|---|---|---|
| [CreateFileW](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilew), [ReadFile](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-readfile), [WriteFile](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-writefile), and [CancelIoEx](https://learn.microsoft.com/en-us/windows/win32/fileio/cancelioex-func) | Microsoft platform contracts; reviewed 2026-08-08 | explicit access/share/create/reparse policy, overlapped buffer lifetime, partial transfer, requested cancellation with terminal completion | compatible; exact Windows build, filesystem, flags, handle mode, completion mechanism, and synchronous exceptions remain evidence inputs |
| [GetFileInformationByHandleEx](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-getfileinformationbyhandleex) and [BY_HANDLE_FILE_INFORMATION](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/ns-fileapi-by_handle_file_information) | Microsoft platform contracts; reviewed 2026-08-08 | handle-centric metadata and volume-scoped, reusable file identity | compatible; information classes and field support vary by filesystem and Windows generation |
| [ReplaceFileW](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-replacefilew), [FlushFileBuffers](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-flushfilebuffers), and [file caching](https://learn.microsoft.com/en-us/windows/win32/fileio/file-caching) | Microsoft platform contracts/guidance; reviewed 2026-08-08 | same-volume replacement constraints, metadata/error variance, explicit flush and cache boundaries | supports separating namespace atomicity from durability; storage-stack and directory-persistence claims require tested evidence |
| [open/openat](https://man7.org/linux/man-pages/man2/open.2.html), [openat2](https://man7.org/linux/man-pages/man2/openat2.2.html), and [path resolution](https://man7.org/linux/man-pages/man7/path_resolution.7.html) | Linux man-pages project; reviewed 2026-08-08 | directory-relative lookup, descriptor anchoring, extensible `RESOLVE_*` constraints, mount/link/path-walk semantics | compatible; kernel, libc, filesystem, namespace, and fallback R-level must be bound; `openat` alone does not imply `openat2` containment |
| [pread/pwrite](https://man7.org/linux/man-pages/man2/pread.2.html), [statx](https://man7.org/linux/man-pages/man2/statx.2.html), [renameat2](https://man7.org/linux/man-pages/man2/renameat2.2.html), and [fsync](https://man7.org/linux/man-pages/man2/fsync.2.html) | Linux man-pages project; reviewed 2026-08-08 | positioned I/O, explicit metadata availability, same-filesystem rename semantics, separate file and directory persistence | compatible; documented `pwrite`/`O_APPEND`, filesystem flag support, remote behavior, and device guarantees require exact trial capture |
| [Apple rename](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/rename.2.html), [fsync](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/fsync.2.html), and [fcntl/F_FULLFSYNC](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/fcntl.2.html) | Apple archived platform manual pages; reviewed 2026-08-08 | same-filesystem rename, ordinary synchronization, and stronger provider-specific full synchronization | useful but archived; supported macOS/SDK/APFS behavior and current declaration availability must be verified during trial review |

**RM-FILESYSTEM-SOURCE-0001:** Trial evidence MUST bind exact OS/kernel/SDK, native mechanism, filesystem family/version, mount/volume options, storage/device topology, sandbox/namespace, and network boundary.

**RM-FILESYSTEM-SOURCE-0002:** Living and archived sources MUST be revision- or release-bound where possible; an unchanged URL MUST NOT prove unchanged semantics or current platform support.

**RM-FILESYSTEM-SOURCE-0003:** Documented OS contracts, filesystem-specific observations, device behavior, and Rusty Mill guarantees MUST remain separately identified.

**RM-FILESYSTEM-SOURCE-0004:** A source, OS, kernel, SDK, filesystem, or storage-stack change invalidates affected current claims until path, authority, race, I/O, metadata, atomicity, and durability impact is classified.
