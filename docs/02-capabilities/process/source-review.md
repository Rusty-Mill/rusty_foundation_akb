# Process source review

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Expires | On supported OS/kernel/SDK/runtime convention change or 2027-02-08, whichever occurs first |
| Reviewer | Process capability owner |
| Open blocking findings | None for planning eligibility; exact supported provider generations and deployment contexts remain trial inputs |

| Source | Class and reviewed status | Proposition supported | Impact and limitation |
|---|---|---|---|
| [CreateProcessW](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw), [creating processes](https://learn.microsoft.com/en-us/windows/win32/procthread/creating-processes), and [attribute lists](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-initializeprocthreadattributelist) (via [`UpdateProcThreadAttribute`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-updateprocthreadattribute)) | Microsoft platform contracts; reviewed 2026-08-09 | explicit application/command-line/environment/current-directory inputs, inherited handle controls, startup attributes, process/thread handles | compatible; exact Windows build, target parser, flags, token/session, handle mode, and creation mitigation context remain evidence inputs |
| [Job Objects](https://learn.microsoft.com/en-us/windows/win32/procthread/job-objects), [TerminateProcess](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-terminateprocess), and [GenerateConsoleCtrlEvent](https://learn.microsoft.com/en-us/windows/console/generateconsolectrlevent) | Microsoft platform contracts; reviewed 2026-08-08 | managed-set semantics, forced single-process control, and console/group preconditions | supports separate control/P-level claims; nesting, breakaway, parent job, console attachment, privilege, and completion evidence require exact trials |
| [POSIX `posix_spawn`](https://pubs.opengroup.org/onlinepubs/9799919799/functions/posix_spawn.html), [`exec`](https://pubs.opengroup.org/onlinepubs/9799919799/functions/exec.html), and [`wait`](https://pubs.opengroup.org/onlinepubs/9799919799/functions/wait.html) | The Open Group Issue 8 contracts; reviewed 2026-08-08 | structured argv/envp, spawn attributes/file actions, execution replacement, wait/status and implementation-dependent failure reporting | compatible; target implementation, extensions, exit-127 ambiguity, thread interactions, and native-string constraints remain provider evidence |
| [pidfd_open](https://man7.org/linux/man-pages/man2/pidfd_open.2.html), [pidfd_send_signal](https://man7.org/linux/man-pages/man2/pidfd_send_signal.2.html), [waitid](https://man7.org/linux/man-pages/man2/waitid.2.html), and [close_range](https://man7.org/linux/man-pages/man2/close_range.2.html) | Linux man-pages project; reviewed 2026-08-08 | race-resistant process references/control/wait and bounded descriptor inheritance cleanup | compatible; kernel/libc versions, pidfd creation path, namespace/permission context, flags, and fallback strength must be captured |
| [Apple `posix_spawn`](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/posix_spawn.2.html), [launch constraints](https://developer.apple.com/documentation/security/defining-launch-environment-and-library-constraints), and [background-process guidance](https://developer.apple.com/documentation/appkit/managing-ongoing-background-processes-in-your-mac) | Apple archived manual plus living platform guidance; reviewed 2026-08-08 | macOS spawn mapping and deployment/security/lifecycle constraints beyond raw child creation | useful but mixed archival status; exact macOS/SDK, sandbox, app/service context, entitlements, and current API availability require trial review |

**RM-PROCESS-SOURCE-0001:** Trial evidence MUST bind exact OS/kernel/SDK, launch/control/wait primitive, parser convention, identity mechanism, containment facility, filesystem, sandbox/service/session, privilege, and security-tool context.

**RM-PROCESS-SOURCE-0002:** Living and archived sources MUST be release- or revision-bound where possible; an unchanged URL MUST NOT prove unchanged behavior or current support.

**RM-PROCESS-SOURCE-0003:** Documented platform contracts, observed provider behavior, target-program parsing, service-manager policy, and Rusty Mill guarantees MUST remain separately identified.

**RM-PROCESS-SOURCE-0004:** A source, OS, kernel, SDK, libc/runtime, target parser, sandbox, service-manager, or containment change invalidates affected claims until its impact is classified.
