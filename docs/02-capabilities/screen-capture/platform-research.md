# Platform research

Research records native mechanisms; it does not make them the portable contract.

| Platform | Primary mechanisms | Architectural observations |
|---|---|---|
| Windows | `Windows.Graphics.Capture`, `GraphicsCapturePicker`, `GraphicsCaptureItem`, `GraphicsCaptureSession`, `Direct3D11CaptureFramePool` | Secure system picker selects a window/display; the system draws an active-capture border; frame pools are recreated for resize/device change and discard prior frames. Programmatic item creation and cursor/border options require separate version/capability review. |
| Linux desktop | XDG Desktop Portal ScreenCast + PipeWire | Portal session separates source selection, start, and restricted PipeWire access. Monitor/window/virtual sources and hidden/embedded/metadata cursor modes are advertised. Node IDs may be reused; newer portal versions expose non-reused PipeWire serials and session-local source IDs. Compositor/portal variance is contractual evidence. |
| macOS | ScreenCaptureKit `SCContentSharingPicker`, `SCContentFilter`, `SCStream`, `SCStreamConfiguration`, screenshot manager | System picker supports windows, applications, and displays and can update active selection. Configuration covers pixel format, output dimensions, queue depth, cursor, system/app audio, microphone, and HDR modes; each feature remains independently negotiated. |

## Primary sources

- [Microsoft: Screen capture](https://learn.microsoft.com/en-us/windows/uwp/audio-video-camera/screen-capture)
- [Microsoft: Windows.Graphics.Capture](https://learn.microsoft.com/en-us/uwp/api/windows.graphics.capture)
- [XDG Desktop Portal: ScreenCast](https://flatpak.github.io/xdg-desktop-portal/docs/doc-org.freedesktop.portal.ScreenCast.html)
- [XDG Desktop Portal: PipeWire access](https://flatpak.github.io/xdg-desktop-portal/docs/pipewire.html)
- [Apple: SCContentSharingPicker](https://developer.apple.com/documentation/screencapturekit/sccontentsharingpicker)
- [Apple: Capturing screen content in macOS](https://developer.apple.com/documentation/screencapturekit/capturing-screen-content-in-macos)

## Evidence gaps

- Exact window occlusion, minimized/offscreen, child/popup, decoration, and alpha behavior by OS/build/compositor.
- Protected media, secure UI, capture-exclusion, overlay-plane, HDR, color, and remote/virtual-display behavior.
- Cursor metadata timing and shape lifetime; application/system audio isolation and clock correlation.
- Portal implementation, Wayland compositor, X11 fallback, sandbox, remote-session, and multi-seat variance.
- Revocation latency, indicator behavior, restored selection semantics, source identity reuse, and session teardown.
