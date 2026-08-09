# IPC byte-pipe source review

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Expires | On supported OS/kernel/SDK or runtime-integration change, or 2027-02-08, whichever occurs first |
| Reviewer | IPC capability owner |
| Open blocking findings | None for planning eligibility; exact supported mechanisms, generations, and Q-levels remain trial inputs |

| Source | Class and reviewed status | Proposition supported | Impact and limitation |
|---|---|---|---|
| [CreatePipe](https://learn.microsoft.com/en-us/windows/win32/api/namedpipeapi/nf-namedpipeapi-createpipe), [anonymous pipe operations](https://learn.microsoft.com/en-us/windows/win32/ipc/anonymous-pipe-operations), and [named-pipe open modes](https://learn.microsoft.com/en-us/windows/win32/ipc/named-pipe-open-modes) | Microsoft platform contracts; reviewed 2026-08-08 | anonymous-pipe creation/inheritance/blocking behavior and the need for a different native realization for overlapped completion | compatible; exact Windows build, flags/security, process binding, named-pipe realization, buffer behavior, and completion mechanism require trial evidence |
| [Linux `pipe2`](https://man7.org/linux/man-pages/man2/pipe.2.html) and [pipe overview](https://man7.org/linux/man-pages/man7/pipe.7.html) | Linux man-pages project; reviewed 2026-08-08 | atomic creation flags, byte-stream/EOF/broken-peer/capacity behavior, `PIPE_BUF`-scoped atomicity, and readiness integration basis | compatible; exact kernel/libc, flags, capacity policy, signal disposition, epoll/io_uring integration, namespaces, and limits must be bound |
| [POSIX `pipe`](https://pubs.opengroup.org/onlinepubs/9799919799/functions/pipe.html) and [`write`](https://pubs.opengroup.org/onlinepubs/9799919799/functions/write.html) | The Open Group Issue 8 contracts; reviewed 2026-08-08 | directional descriptor pair, byte writes, partial/error behavior, and scoped pipe atomicity | compatible semantic floor; implementation limits, signal behavior, nonblocking/readiness extensions, and exact atomicity value remain provider evidence |
| [Apple `pipe`](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/pipe.2.html) | Apple archived platform manual; reviewed 2026-08-08 | macOS descriptor-pair creation and POSIX-style byte-pipe basis | useful but archived; exact macOS/SDK, flags, kqueue integration, capacity/atomicity, signal handling, sandbox, and current availability require trial review |

**RM-IPC-SOURCE-0001:** Trial evidence MUST bind exact OS/kernel/SDK, native creation and I/O mechanism, flags/security, Q-level/integration, capacity/atomicity scope, signal policy, process context, quotas, and provider artifact.

**RM-IPC-SOURCE-0002:** Living and archived sources MUST be release- or revision-bound where possible; an unchanged URL MUST NOT prove unchanged behavior or support.

**RM-IPC-SOURCE-0003:** Documented platform contracts, observed capacity/scheduling, runtime integration, process inheritance behavior, and Rusty Mill guarantees MUST remain separately identified.

**RM-IPC-SOURCE-0004:** A source, OS, kernel, SDK, runtime, native mechanism, signal policy, or process-binding change invalidates affected current claims until impact is classified.
