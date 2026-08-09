# Async I/O source review

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Expires | On supported OS/kernel/SDK, native-engine, or runtime-integration change, or 2027-02-08, whichever occurs first |
| Reviewer | Async I/O integration owner |
| Open blocking findings | None for planning eligibility; exact operation/resource/mechanism/version matrices remain trial inputs |

| Source | Class and reviewed status | Proposition supported | Impact and limitation |
|---|---|---|---|
| [I/O completion ports](https://learn.microsoft.com/en-us/windows/win32/fileio/i-o-completion-ports), [overlapped I/O](https://learn.microsoft.com/en-us/windows/win32/sync/synchronization-and-overlapped-input-and-output), and [CancelIoEx](https://learn.microsoft.com/en-us/windows/win32/api/ioapiset/nf-ioapiset-cancelioex) | Microsoft platform contracts; reviewed 2026-08-08 | completion dequeue/concurrency model, retained OVERLAPPED/buffer state, and cancellation as a request resolved by terminal completion | compatible; exact Windows build, handle type/mode, operation, completion association, thread/apartment, and shutdown behavior require evidence |
| [`io_uring_setup`](https://man7.org/linux/man-pages/man2/io_uring_setup.2.html), [`io_uring_enter`](https://man7.org/linux/man-pages/man2/io_uring_enter.2.html), and [`io_uring` overview](https://man7.org/linux/man-pages/man7/io_uring.7.html) | Linux man-pages plus kernel documentation; reviewed 2026-08-09 | bounded submission/completion rings, operation-specific support, completion records, feature negotiation, and kernel-version-sensitive semantics | compatible; exact kernel/liburing/provider artifact, opcode/resource/flag matrix, cancellation, memory ordering, registration, restrictions, and fallback must be bound |
| [`epoll`](https://man7.org/linux/man-pages/man7/epoll.7.html) | Linux man-pages project; reviewed 2026-08-08 | level/edge/one-shot readiness, drain/rearm obligations, concurrent wait behavior, and descriptor-registration issues | supports readiness-as-hint translation; exact kernel, descriptor type, nonblocking mode, close/reuse, fairness, and wake strategy require trials |
| [Apple `kqueue`](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/kqueue.2.html), [Dispatch I/O](https://developer.apple.com/documentation/dispatch/dispatchio), and [Dispatch sources](https://developer.apple.com/documentation/dispatch/dispatch-source) | Apple archived manual plus living SDK contracts; reviewed 2026-08-09 | readiness/filter and callback/queue delivery strategies with resource-specific cancellation/close behavior | useful but mixed archival status; exact macOS/SDK, resource/filter, dispatch queue, run-loop/app lifecycle, sandbox, and current availability require trial review |

**RM-ASYNC-SOURCE-0001:** Trial evidence MUST bind exact OS/kernel/SDK, provider/runtime artifacts, operation/resource/mechanism/flags, queue/ring/poll settings, cancellation, registration, affinity/fork, limits, shutdown, and consuming-domain contract.

**RM-ASYNC-SOURCE-0002:** Living and archived sources MUST be release- or revision-bound where possible; an unchanged URL or mechanism name MUST NOT prove unchanged semantics or support.

**RM-ASYNC-SOURCE-0003:** Documented native contracts, observed driver/filesystem/network behavior, runtime/executor behavior, consuming-domain semantics, and Rusty Mill guarantees MUST remain separately identified.

**RM-ASYNC-SOURCE-0004:** A source, OS, kernel, SDK, provider, runtime, driver, resource, or operation change invalidates affected current claims until lifecycle, cancellation, registration, load, shutdown, and compatibility impact is classified.
