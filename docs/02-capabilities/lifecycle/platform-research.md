# Platform research

| Platform | Candidate mechanisms | Variance shaping the contract |
|---|---|---|
| Windows | process/window launch, file/URI activation, `WM_QUERYENDSESSION`/`WM_ENDSESSION`, power/session notifications, restart registration | Query and committed end-session stages differ; forced shutdown and time limits exist; GUI, console, and service processes receive different mechanisms. |
| Linux desktop | desktop-entry/D-Bus activation, systemd-logind session/power signals and inhibitor locks where present, compositor/desktop-specific session protocols | No universal desktop lifecycle stack; systemd and portals are not guaranteed; signals/termination may arrive without cooperative UI negotiation. |
| macOS | AppKit application delegate, open-file/URL and reopen handling, workspace sleep/wake/session notifications, sudden/automatic termination, AppKit restoration | Termination replies may be deferred, but force quit/sudden termination bypass cleanup; restoration is product/UI policy and may be discarded. |

## Primary references

- [Microsoft: WM_QUERYENDSESSION](https://learn.microsoft.com/windows/win32/shutdown/wm-queryendsession)
- [Microsoft: WM_ENDSESSION](https://learn.microsoft.com/windows/win32/shutdown/wm-endsession)
- [Microsoft: RegisterApplicationRestart](https://learn.microsoft.com/windows/win32/api/winbase/nf-winbase-registerapplicationrestart)
- [freedesktop.org: systemd-logind D-Bus API](https://www.freedesktop.org/software/systemd/man/latest/org.freedesktop.login1.html)
- [freedesktop.org: Desktop Entry Specification](https://specifications.freedesktop.org/desktop-entry-spec/latest/)
- [Apple: NSApplicationDelegate](https://developer.apple.com/documentation/appkit/nsapplicationdelegate)
- [Apple: Restoring app state with AppKit](https://developer.apple.com/documentation/appkit/restoring-your-app-s-state-with-appkit)

## Conclusions

Portable contracts describe requests, observations, deadlines, and missing-event outcomes. They do not promise a common callback sequence. Adapter evidence must cover normal quit, cancelled quit, logout, shutdown/restart, sleep/wake, session lock/disconnect, force termination, crash, activation while running/not running, and restoration rejection.

