# Platform research

| Platform | Primary mechanisms | Architectural observations |
|---|---|---|
| Windows | Service Control Manager, trigger-start services, Task Scheduler, brokered application background tasks | SCM maintains a security-controlled installed-service database and controls service lifecycle. Trigger-start services, always-on services, scheduled/event tasks, maintenance jobs, and quota-managed app tasks are different mechanisms. Task Scheduler monitors time/system/idle/boot/logon/session criteria; trigger satisfaction is not job completion. |
| Linux | systemd system/user managers, service/socket/path/timer units, transient units, inhibitors/resource control | Service and activation units separate definition from activation source; socket activation can make an endpoint available before the worker. Timers use monotonic or calendar expressions and may coalesce, persist missed activation, add randomized delay, or depend on wake policy. Manager/slice/cgroup evidence defines scope and resource behavior. |
| macOS | `launchd` daemons/agents, XPC services, `SMAppService`, login items, brokered background tasks | Launch daemons run in system context; agents are user/session scoped; XPC and launch-on-demand avoid permanently resident helpers. Modern service management exposes user authorization state. Brokered background tasks are scheduler-controlled and quota/expiration constrained rather than exact timers. |

## Primary sources

- [Microsoft: About Services](https://learn.microsoft.com/en-us/windows/win32/services/about-services)
- [Microsoft: Service Trigger Events](https://learn.microsoft.com/en-us/windows/win32/services/service-trigger-events)
- [Microsoft: Task Scheduler for developers](https://learn.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page)
- [systemd.service](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html)
- [systemd.timer](https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html)
- [Apple: Creating Launch Daemons and Agents](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html)
- [Apple: Managing ongoing background processes](https://developer.apple.com/documentation/appkit/managing-ongoing-background-processes-in-your-mac)
- [Apple: BGTaskScheduler](https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler)

## Evidence gaps

- Exact install/update/remove transactions, ACLs, principal selection, trigger payloads, readiness, restart throttling, and failure action behavior by supported OS/build.
- systemd system versus user managers, timer persistence/time change/wake behavior, socket/path/device activation, cgroup accounting, sandboxing, and distribution policy variance.
- macOS current `SMAppService`, launchd/XPC, login item, user disclosure, sandbox/entitlement, managed-device, and background-task quota/expiration behavior.
- Sleep/downtime/clock/time-zone changes, missed schedules, duplicate triggers, overlap, update coexistence, checkpoint compatibility, service-manager restart, and abrupt termination on all platforms.
