# Windowing platform research

**Status:** Research evidence; normative conclusions live in the contracts and ADRs.

## Windows

Win32 creates top-level windows around a thread-affine window procedure and message dispatch. Procedures may be called recursively, so native delivery cannot be exposed as a portable assumption. Per-monitor DPI changes arrive through `WM_DPICHANGED` with a suggested rectangle; current window DPI follows the most recently delivered change. This supports a revisioned committed snapshot rather than independent size and DPI properties.

Primary sources: [Window procedures](https://learn.microsoft.com/en-us/windows/win32/winmsg/about-window-procedures), [`WM_DPICHANGED`](https://learn.microsoft.com/en-us/windows/win32/hidpi/wm-dpichanged), [`GetDpiForWindow`](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getdpiforwindow).

## Linux: Wayland and X11

Wayland gives the compositor authority over top-level configuration. An `xdg_surface.configure` serial must be acknowledged before committing a buffer for that configuration; initial content cannot be attached before initial configuration. Coordinates are surface-local and the core model does not promise the global desktop coordinates familiar from X11. Fractional scaling is a separate protocol and buffer/presentation state remains negotiated.

X11 permits stronger client placement assumptions and exposes root-window coordinates, but those are provider-specific quality/extension claims. The portable contract adopts Wayland's stricter truthful semantics; an X11 provider may advertise additional placement and observation support.

Primary sources: [Wayland core protocol](https://gitlab.freedesktop.org/wayland/wayland/-/blob/main/protocol/wayland.xml), [xdg-shell protocol](https://gitlab.freedesktop.org/wayland/wayland-protocols/-/blob/main/stable/xdg-shell/xdg-shell.xml), [fractional scale protocol](https://gitlab.freedesktop.org/wayland/wayland-protocols/-/blob/main/staging/fractional-scale/fractional-scale-v1.xml), [Xlib manual](https://xorg.freedesktop.org/archive/current/doc/libX11/libX11/libX11.html).

## macOS

AppKit window state and delegate notifications are main-actor/UI-context facilities. A window's backing scale is a rendering scale, not physical DPI. Backing properties may change with scale or color space and applications are expected to invalidate resolution/color-dependent caches. This supports atomic scale/color/surface-generation snapshots.

Primary sources: [`NSWindow.backingScaleFactor`](https://developer.apple.com/documentation/appkit/nswindow/backingscalefactor), [`windowDidChangeBackingProperties`](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowdidchangebackingproperties(_:)), [`didChangeBackingPropertiesNotification`](https://developer.apple.com/documentation/appkit/nswindow/didchangebackingpropertiesnotification).

## Derived portability conclusions

| Concern | Portable conclusion |
|---|---|
| Resize/placement | Request plus later observation; exact placement optional |
| Thread model | Provider-declared affinity behind a non-reentrant portable stream |
| Scale | Per-window, revisioned, and not physical DPI |
| Coordinates | Typed local spaces; global placement optional |
| Surface | Configuration/generation scoped |
| Close | Policy-bearing request distinct from destruction |

