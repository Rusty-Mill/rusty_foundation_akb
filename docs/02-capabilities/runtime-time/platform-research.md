# Runtime and time platform research

**Status:** Draft research; descriptive, not normative  
**Reviewed:** 2026-08-08

## Cross-platform findings

All three target platforms expose a useful distinction between a monotonic clock that excludes system suspend and one that includes it. They also expose timer mechanisms with different integration, resolution, coalescing, and wake behavior. Rusty Mill should specify clock domains and timer behavior independently of any one mechanism.

Cancellation mechanisms are operation-specific and race with completion. The portable model must therefore distinguish requesting cancellation, observing cancellation, operation completion, and confirmed cancellation.

## Windows

| Concern | Candidate mechanism | Architectural implication |
|---|---|---|
| High-resolution active monotonic time | `QueryPerformanceCounter` | Suitable for interval measurement; values use a boot-stable frequency and arbitrary origin. |
| Active time excluding sleep | `QueryUnbiasedInterruptTimePrecise` | Explicitly excludes sleep/hibernation but has a higher call cost than its non-precise variant. |
| Elapsed time including sleep | `GetTickCount64`/interrupt-time family | Separate semantic clock domain; resolution and precision differ from QPC. |
| Deadline notification | Waitable timers or thread-pool timers | Waitable timers integrate with Windows waits; APC delivery is a poor general runtime primitive. |
| Coalescing | `SetWaitableTimerEx` tolerable delay | Maps to a timer tolerance policy, not a change in requested deadline. |
| Suspend behavior | Relative waitable timers exclude low-power time on Windows 8+ | Backend choice must match the requested clock domain. |
| I/O cancellation | `CancelIoEx` | Requests cancellation but may race with normal completion and does not wait for completion. |

Microsoft documents `QueryPerformanceCounter` as a high-resolution timestamp for interval measurements. `QueryUnbiasedInterruptTimePrecise` excludes sleep and hibernation. `SetWaitableTimerEx` supports relative/absolute due times and tolerable delay, with changed low-power behavior beginning in Windows 8. `CancelIoEx` marks operations for cancellation, but completion may still be normal, canceled, or failed. See [primary sources](#primary-sources).

## Linux

| Concern | Candidate mechanism | Architectural implication |
|---|---|---|
| Active monotonic time | `clock_gettime(CLOCK_MONOTONIC)` | Non-settable clock that excludes suspend. |
| Suspend-inclusive monotonic time | `clock_gettime(CLOCK_BOOTTIME)` | Linux-specific clock that includes suspend. |
| Synchronous deadline wait | `clock_nanosleep(..., TIMER_ABSTIME, ...)` | Absolute deadlines avoid drift; signals can interrupt the wait. |
| Async/event-loop timer | `timerfd_create`/`timerfd_settime` | File-descriptor notification composes with `poll`/`epoll`; should remain backend detail. |
| Coalescing | Per-thread timer slack | Power policy can allow delayed wakeup without changing logical clock semantics. |
| Cancellation | Mechanism-specific: descriptor closure, signals, or async-I/O facilities | No single primitive provides a universal operation-cancellation contract. |

`CLOCK_MONOTONIC` and `CLOCK_BOOTTIME` encode the active-versus-suspend-inclusive split. `clock_nanosleep` supports absolute deadlines and documents rounding and scheduling delays; `timerfd` exposes expirations through file descriptors suitable for an event loop.

## macOS

| Concern | Candidate mechanism | Architectural implication |
|---|---|---|
| Active monotonic time | `clock_gettime_nsec_np(CLOCK_UPTIME_RAW)` / `mach_absolute_time` | Excludes time asleep; nanosecond API avoids exposing Mach timebase conversion. |
| Suspend-inclusive monotonic time | `clock_gettime_nsec_np(CLOCK_MONOTONIC_RAW)` / `mach_continuous_time` | Includes sleep and remains separate from calendar time. |
| Deadline notification | Dispatch source timers | Supports monotonic deadlines, repeating intervals, and leeway. |
| Cancellation | Dispatch work-item cancellation and operation-specific mechanisms | Dispatch cancellation does not stop work that has already begun. |

Apple recommends nanosecond `clock_gettime_nsec_np` equivalents over raw Mach tick APIs. Dispatch timers expose deadline and leeway. Dispatch work-item cancellation prevents future execution but does not affect work already running, reinforcing the cooperative portable model.

## Research caveats

- Candidate mechanisms are not implementation decisions.
- Minimum supported OS versions remain undecided.
- Precision, resolution, accuracy, and scheduling latency are different quantities and must be measured separately.
- Virtualization, CPU power management, system suspend, and timer-policy changes require test coverage.
- Wake-from-suspend requires platform-specific authority and user-impact analysis.

## Primary sources

### Microsoft

- [QueryPerformanceCounter](https://learn.microsoft.com/en-us/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter)
- [QueryUnbiasedInterruptTimePrecise](https://learn.microsoft.com/en-us/windows/win32/api/realtimeapiset/nf-realtimeapiset-queryunbiasedinterrupttimeprecise)
- [Windows Time](https://learn.microsoft.com/en-us/windows/win32/sysinfo/windows-time)
- [SetWaitableTimerEx](https://learn.microsoft.com/en-us/windows/win32/api/synchapi/nf-synchapi-setwaitabletimerex)
- [CancelIoEx](https://learn.microsoft.com/en-us/windows/win32/fileio/cancelioex-func)
- [Canceling pending I/O](https://learn.microsoft.com/en-us/windows/win32/fileio/canceling-pending-i-o-operations)

### Linux man-pages project

- [clock_gettime](https://man7.org/linux/man-pages/man3/clock_gettime.3.html)
- [clock_nanosleep](https://www.man7.org/linux/man-pages/man2/clock_nanosleep.2.html)
- [timerfd_create and timerfd_settime](https://man7.org/linux/man-pages/man2/timerfd_create.2.html)
- [time overview and timer slack](https://man7.org/linux/man-pages/man7/time.7.html)

### Apple

- [mach_absolute_time](https://developer.apple.com/documentation/driverkit/mach_absolute_time)
- [mach_continuous_time](https://developer.apple.com/documentation/kernel/1646199-mach_continuous_time)
- [DispatchSourceTimer](https://developer.apple.com/documentation/dispatch/dispatchsourcetimer)
- [DispatchWorkItem cancellation](https://developer.apple.com/documentation/dispatch/dispatchworkitem/cancel%28%29)
