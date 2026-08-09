# Windowing source review

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Expires | On supported-OS/compositor/protocol/SDK change or 2027-02-08, whichever occurs first |
| Reviewer | Windowing capability owner |
| Open blocking findings | None for planning eligibility; exact supported provider generations remain trial inputs |

| Source | Class and reviewed status | Proposition supported | Impact and limitation |
|---|---|---|---|
| [Win32 window procedures](https://learn.microsoft.com/en-us/windows/win32/winmsg/about-window-procedures), [`WM_DPICHANGED`](https://learn.microsoft.com/en-us/windows/win32/hidpi/wm-dpichanged), and [`GetDpiForWindow`](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getdpiforwindow) | Microsoft platform contracts; reviewed 2026-08-08 | thread-affine/reentrant dispatch, per-window DPI observation, suggested geometry | compatible; DPI awareness mode and Windows build are provider inputs, and suggested geometry remains negotiated |
| [Wayland core](https://gitlab.freedesktop.org/wayland/wayland/-/blob/main/protocol/wayland.xml), [xdg-shell](https://gitlab.freedesktop.org/wayland/wayland-protocols/-/blob/main/stable/xdg-shell/xdg-shell.xml), and [fractional scale](https://gitlab.freedesktop.org/wayland/wayland-protocols/-/blob/main/staging/fractional-scale/fractional-scale-v1.xml) | living freedesktop protocol sources; reviewed 2026-08-08 | compositor-authoritative configure/ack/commit lifecycle, local coordinates, separately versioned fractional scale | compatible; repository `main` is mutable, protocol/global versions and compositor behavior must be captured in trial evidence |
| [Xlib manual](https://xorg.freedesktop.org/archive/current/doc/libX11/libX11/libX11.html) | X.Org living/current documentation; reviewed 2026-08-09 | X11 placement/root-coordinate and event mechanisms | compatible as provider-specific extension evidence; X11 guarantees cannot strengthen portable Wayland-compatible semantics |
| [AppKit backing scale](https://developer.apple.com/documentation/appkit/nswindow/backingscalefactor) and [backing-property changes](https://developer.apple.com/documentation/appkit/nswindowdelegate/1419517-windowdidchangebackingproperties) | Apple SDK/platform contracts; reviewed 2026-08-08 | main-actor window observation, dynamic scale/color changes, backing scale not physical density | compatible; exact SDK/macOS availability and notification ordering require tested-version evidence |

**RM-WINDOWING-SOURCE-0001:** Trial evidence MUST bind exact Windows build/DPI context, Wayland compositor and advertised protocol versions, X server/window manager, and macOS/SDK generation.

**RM-WINDOWING-SOURCE-0002:** Mutable protocol/vendor documentation MUST be snapshotted or revision-bound; an unchanged URL MUST NOT prove unchanged semantics.

**RM-WINDOWING-SOURCE-0003:** Documented contracts, observed compositor/window-manager behavior, and Rusty Mill guarantees MUST remain separately identified.

**RM-WINDOWING-SOURCE-0004:** A source/provider update invalidates affected reviewed-current claims until its lifecycle, scale, coordinate, event, surface, security, and compatibility impact is classified.

