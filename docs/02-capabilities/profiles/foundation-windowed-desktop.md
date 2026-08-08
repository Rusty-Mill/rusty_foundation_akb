# `rm.profile.foundation.windowed-desktop`

| Field | Value |
|---|---|
| Status | Draft |
| Version | 0.1.0 |
| Extends | [`rm.profile.foundation.desktop` 1.0.0](foundation-desktop.md) |
| Purpose | Add native top-level window and graphics-presentation infrastructure without claiming a complete GUI toolkit |

## Required members

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0001:** Requires `rm.windowing.window`, `rm.windowing.display-topology`, and `rm.windowing.presentation-surface` `>=0.1.0,<0.2.0`.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0002:** Requires `rm.graphics.device`, `rm.graphics.resource-memory`, and `rm.graphics.submission` `>=0.1.0,<0.2.0` plus graphics presentation service `>=0.1.0,<0.2.0`.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0003:** Window/graphics resolution is joint: the selected device must prove compatibility with the selected presentation surface, format/color policy, frame-flight bound, loss recovery, and required protection properties.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0004:** Window event delivery and frame acquisition/presentation provide async paths that do not block the UI dispatch context while waiting. Sync calls obey provider affinity and never nest a hidden event loop/runtime.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0005:** The minimum workload requires ordinary composited opaque SDR presentation, explicit scale/color observation, bounded frames in flight, resize/surface recreation, and device-loss reporting. Acceleration is preferred but not silently required; software selection is disclosed.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0006:** Exact placement, HDR, tearing/variable refresh, protected content, graphics compute, external resource sharing, and global coordinates are optional constraints, not implied features.

## Whole-product gaps

This profile does not supply a rendering command model, widget/UI framework, text shaping/fonts, images, input, clipboard/drag-and-drop, accessibility content tree, localization, or application lifecycle/session integration. It cannot claim desktop-application completeness.

## Evidence gates

Profile evidence includes window/device joint resolution, mixed-scale display migration, resize/occlusion/minimize, surface and device loss/recovery, bounded frame pacing, color/alpha correctness, keyboard-only native chrome, protected-path nonclaims, software fallback disclosure, and cleanup across logout/suspend/remote-session transitions.

