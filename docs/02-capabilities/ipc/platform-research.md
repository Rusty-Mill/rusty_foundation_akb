# Anonymous pipe platform research

**Status:** Research input

| Concern | Windows | Linux | macOS |
|---|---|---|---|
| Creation | `CreatePipe`; anonymous pipes are implemented with a uniquely named pipe | `pipe2` supports atomic close-on-exec/nonblocking flags | `pipe` descriptor pair; flags configured separately where available |
| Blocking | `ReadFile`/`WriteFile`; write can block until the requested data is written | Blocking/nonblocking descriptor semantics and readiness polling | Blocking/nonblocking descriptor semantics and readiness polling |
| Async | Basic anonymous pipes do not support overlapped I/O; provider may construct a suitably configured named-pipe instance | Nonblocking descriptors with epoll/io_uring integration choices | Nonblocking descriptors with kqueue integration |
| Atomicity | No portable equivalence to POSIX `PIPE_BUF` should be inferred | POSIX writes at or below `PIPE_BUF` are non-interleaved under specified conditions | POSIX/BSD pipe rules; provider reports actual scoped guarantee |
| Broken peer | Write failure after readers close; host termination is not inherent API behavior | `EPIPE` plus `SIGPIPE` unless controlled | `EPIPE` plus `SIGPIPE` unless controlled |

## Conclusions

1. Correct byte-stream semantics are portable; buffer size, write atomicity, and async mechanism are quality claims.
2. The provider must suppress/contain native broken-pipe process-termination behavior behind safe Rust semantics.
3. EOF depends on all write references closing, making inheritance and duplicate cleanup part of correctness.
4. Windows may need a named-pipe implementation detail to reach native completion quality while preserving anonymous capability semantics.
5. A pipe has no message framing, seek position, durable storage, or terminal behavior.

## Primary sources

- Microsoft: [`CreatePipe`](https://learn.microsoft.com/en-us/windows/win32/api/namedpipeapi/nf-namedpipeapi-createpipe), [Anonymous Pipe Operations](https://learn.microsoft.com/en-us/windows/win32/ipc/anonymous-pipe-operations), and [Named Pipe Open Modes](https://learn.microsoft.com/en-us/windows/win32/ipc/named-pipe-open-modes)
- Linux man-pages: [`pipe2`](https://man7.org/linux/man-pages/man2/pipe.2.html) and [pipe capacity/atomicity](https://man7.org/linux/man-pages/man7/pipe.7.html)
- The Open Group: [`pipe`](https://pubs.opengroup.org/onlinepubs/9799919799/functions/pipe.html) and [`write`](https://pubs.opengroup.org/onlinepubs/9799919799/functions/write.html)
- Apple: [`pipe`](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/pipe.2.html)

