# Process platform research

**Status:** Research input

| Concern | Windows | Linux | macOS |
|---|---|---|---|
| Direct launch | `CreateProcessW` and extended startup attributes | `posix_spawn` or controlled `fork`/`execve`; implementation-dependent primitives | `posix_spawn`; platform launch constraints may apply |
| Arguments | One UTF-16 command-line string parsed by target convention | Native byte-string `argv` | Native `argv` with platform conventions |
| Environment | UTF-16 environment block; name rules and sorting details | Native `envp` byte strings | Native `envp`; app/service policy may constrain launch |
| Inheritance | Explicit `PROC_THREAD_ATTRIBUTE_HANDLE_LIST`; standard handles require care | File actions, close-on-exec, close-range strategies | `posix_spawn` file actions and close-on-exec behavior |
| Child identity/wait | Process handle plus ID; waitable handle and exit code | PID plus wait APIs; Linux pidfd improves reuse/race handling | PID plus wait APIs; lifecycle/service facilities vary |

## Findings

1. Windows direct launch accepts a command line, not an OS-created `argv`; target parser conventions determine round-trip behavior.
2. Passing a null Windows application name can create ambiguous executable parsing/search behavior. The portable base requires explicit executable identity.
3. Broad inherited-handle flags can leak concurrent resources; modern Windows supports an explicit handle list.
4. POSIX `posix_spawn` may report some post-return pre-exec failures through child exit status 127, which is not universally distinguishable from application exit.
5. PID reuse makes numeric IDs insufficient as owned authority. Linux pidfds and Windows process handles offer stronger object binding; macOS/POSIX providers require scoped lifecycle controls and disclosure.
6. Long-lived background services and desktop activation have platform policy and lifecycle beyond direct child launch.

## Primary sources

- Microsoft: [Create processes](https://learn.microsoft.com/en-us/windows/win32/procthread/creating-processes), [`CreateProcessW`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw), and [Process Thread Attribute List](https://learn.microsoft.com/en-us/windows/win32/procthread/attribute-list)
- The Open Group: [`posix_spawn`](https://pubs.opengroup.org/onlinepubs/9799919799/functions/posix_spawn.html), [`exec`](https://pubs.opengroup.org/onlinepubs/9799919799/functions/exec.html), and [`wait`](https://pubs.opengroup.org/onlinepubs/9799919799/functions/wait.html)
- Linux man-pages: [`pidfd_open`](https://man7.org/linux/man-pages/man2/pidfd_open.2.html), [`waitid`](https://man7.org/linux/man-pages/man2/waitpid.2.html), and [`close_range`](https://man7.org/linux/man-pages/man2/close_range.2.html)
- Apple: [`posix_spawn`](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/posix_spawn.2.html), [launch environment constraints](https://developer.apple.com/documentation/security/defining-launch-environment-and-library-constraints), and [background process guidance](https://developer.apple.com/documentation/appkit/managing-ongoing-background-processes-in-your-mac)

