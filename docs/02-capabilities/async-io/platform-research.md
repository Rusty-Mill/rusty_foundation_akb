# Asynchronous I/O platform research

| Platform | Native mechanisms | Architectural consequence |
|---|---|---|
| Windows | Overlapped I/O, I/O completion ports/thread-pool I/O, `CancelIoEx`, waitable/event resources | Completion is native for supported handles; cancellation is a request and operation memory survives until completion; completion dequeue and execution ordering differ |
| Linux | `io_uring` submission/completion queues and cancellation; `epoll` readiness; nonblocking descriptors; bounded blocking fallback for unsupported file operations | Operation support and cancellation vary by kernel/resource/opcode; readiness requires retry/drain/rearm; descriptor reuse needs generation defense |
| macOS | `kqueue`/`kevent` readiness and filters, dispatch sources/I/O, POSIX AIO for limited operations, run-loop integrations | General resource support is primarily readiness/callback based; cancellation and close semantics vary; delivery queues/run loops must not leak into portable semantics |

## Primary sources

- Microsoft, [I/O completion ports](https://learn.microsoft.com/windows/win32/fileio/i-o-completion-ports), [Overlapped I/O](https://learn.microsoft.com/windows/win32/sync/synchronization-and-overlapped-input-and-output), and [`CancelIoEx`](https://learn.microsoft.com/windows/win32/api/ioapiset/nf-ioapiset-cancelioex)
- Linux, [`io_uring_enter(2)`](https://man7.org/linux/man-pages/man2/io_uring_enter.2.html), [`io_uring_setup(2)`](https://man7.org/linux/man-pages/man2/io_uring_setup.2.html), [`epoll(7)`](https://man7.org/linux/man-pages/man7/epoll.7.html), and kernel [io_uring documentation](https://docs.kernel.org/io_uring/index.html)
- Apple, [`kqueue(2)`](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/kqueue.2.html), [Dispatch I/O](https://developer.apple.com/documentation/dispatch/dispatch_io), and [Dispatch sources](https://developer.apple.com/documentation/dispatch/dispatch-source)

## Synthesis

The public contract cannot be “IOCP everywhere,” “io_uring everywhere,” or a portable readiness token. A completion-oriented operation lifecycle preserves exact results and ownership while allowing completion engines, readiness engines, and disclosed blocking adapters. Provider capability matrices are per operation/resource/OS version, not per operating-system name alone.
