# Platform research

| Platform | Primary mechanisms | Architectural observations |
|---|---|---|
| Windows | `SendInput`, pointer/touch injection APIs, session/desktop/integrity boundaries | `SendInput` serially inserts keyboard/mouse events but UIPI limits targets to equal or lower integrity and does not clearly diagnose UIPI blocking. Existing keyboard state can interfere. Touch injection is desktop/session scoped and has strict contact/timestamp state. These are native side-effect boundaries, not delivery or semantic-success proof. |
| Linux desktop | XDG RemoteDesktop portal, ScreenCast portal, PipeWire, libei/libeis | Portal flow jointly presents source/device choice and returns selected device classes plus optional screen streams. Absolute motion is stream-logical-coordinate scoped. libei makes emulated devices distinguishable inside the compositor for access control even though ordinary clients may see normal input. EIS/compositor remains authoritative. |
| macOS | Quartz event posting, Accessibility trust/services, ScreenCaptureKit, session/security policy | Event posting and accessibility-mediated control have privacy permission and secure-input/session constraints. Research must measure effective target scope, provenance visibility, keyboard layout/text behavior, and behavior across lock/login/elevation; permission is not a portable grant or success proof. |

## Primary sources

- [Microsoft: SendInput](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-sendinput)
- [Microsoft: InjectTouchInput](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-injecttouchinput)
- [XDG Desktop Portal: Remote Desktop](https://flatpak.github.io/xdg-desktop-portal/docs/doc-org.freedesktop.portal.RemoteDesktop.html)
- [libei protocol documentation](https://libinput.pages.freedesktop.org/libei/)
- [libei sender API](https://libinput.pages.freedesktop.org/libei/api/group__libei-sender.html)
- [Apple: Quartz Event Services](https://developer.apple.com/documentation/coregraphics/quartz-event-services)

## Evidence gaps

- macOS current permission, secure-input, event-source attribution, session, and sandbox behavior across supported releases.
- Windows UIPI, desktops/sessions, protected UI, touch/pen state, injected-event flags, partial insertion, and local-input arbitration.
- Portal/libei compositor implementations, restore-token policy, keymap/text support, device-region mapping, revoke latency, and X11 fallback.
- Multiple participants/devices, focus races, layout/IME changes, lock/switch/elevation, local emergency stop, accessibility coexistence, and reconnect cleanup on every platform.
