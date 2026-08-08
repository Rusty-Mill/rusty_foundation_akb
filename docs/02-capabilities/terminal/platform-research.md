# Terminal platform research

**Status:** Research input

| Concern | Windows | Linux | macOS |
|---|---|---|---|
| Pseudoterminal | ConPTY/`CreatePseudoConsole` with process attribute attachment | PTY master/slave via `posix_openpt`/`openpty`-class facilities, terminal ioctls and termios | `openpty`, `login_tty`, `forkpty`, termios and ioctls |
| Host wire | UTF-8 plain text interleaved with virtual-terminal sequences | Native bytes; terminal line discipline/output processing; encoding is application/locale convention | Native bytes; terminal line discipline/output processing |
| Size | Initial `COORD`, then `ResizePseudoConsole` | Character-cell winsize and change notification conventions | `winsize` during `openpty` and later ioctl behavior |
| Transport async | ConPTY input/output handles are documented as synchronous; separate threads/queues recommended to avoid deadlock | Nonblocking master plus readiness mechanisms | Nonblocking master plus kqueue/readiness mechanisms |
| Process relation | Attached through extended process attribute; console session rules remain | Session leader, controlling terminal, foreground process group/job control | `login_tty` can create session and controlling terminal, then bind stdio |

## Findings

1. ConPTY intentionally exposes UTF-8 plus VT sequences and performs translation for attached console applications.
2. ConPTY communication channels are synchronous and bidirectional activity needs independent progress to avoid deadlock.
3. POSIX PTYs expose terminal subsystem behavior, including canonical/raw modes, echo, control characters, output processing, and job control; there is no universal text encoding guarantee.
4. A character-cell resize is portable at a broad level, but delivery/observation and pixel metadata vary.
5. PTY creation, controlling-terminal setup, process launch, and supervision must be composed without a child execution window.

## Primary sources

- Microsoft: [Pseudoconsoles](https://learn.microsoft.com/en-us/windows/console/pseudoconsoles), [`CreatePseudoConsole`](https://learn.microsoft.com/en-us/windows/console/createpseudoconsole), and [Creating a Pseudoconsole Session](https://learn.microsoft.com/en-us/windows/console/creating-a-pseudoconsole-session)
- The Open Group: [General Terminal Interface](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap11.html) and [`termios.h`](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/termios.h.html)
- Linux man-pages: [PTY overview](https://man7.org/linux/man-pages/man7/pty.7.html), [`posix_openpt`](https://man7.org/linux/man-pages/man3/posix_openpt.3.html), and [`ioctl_tty`](https://man7.org/linux/man-pages/man2/ioctl_tty.2.html)
- Apple: [`openpty`/`login_tty`/`forkpty`](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/openpty.3.html)

