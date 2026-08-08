# Platform research

| Concern | Windows | Linux | macOS |
|---|---|---|---|
| Display state | Advanced Color/HDR state and display information; descriptors and active OS policy vary | Wayland output image descriptions where color-management protocol is available; compositor/desktop support varies; X11 legacy differs | `NSScreen` color space and EDR headroom observations; display configuration remains platform-owned |
| Surface/content | DXGI swap-chain format/color-space/metadata and compositor Advanced Color path | Wayland color-management surface image description/rendering intent; Vulkan/EGL paths plus compositor support | Color-space-tagged Core Animation/Metal content and EDR-capable formats |
| Profiles/transforms | Windows Color System/ICC and Advanced Color policy; MHC/ACM behavior version-dependent | ICC/colord and compositor color pipeline vary; Wayland protocol supports ICC or parametric descriptions conditionally | ColorSync profiles/transforms and system-managed display matching |
| HDR adaptation | OS compositor maps SDR/HDR under current Advanced Color/reference-white policy | Protocol carries colorimetry/luminance/target metadata; compositor owns mapping | EDR/ColorSync and platform tone/adaptive gain behavior |

## Portability findings

1. Windows Advanced Color distinguishes display capability, active mode, swap-chain format/color space, and OS color management; flip-model and version-specific constraints remain provider evidence.
2. Wayland's staged color-management protocol uses immutable image descriptions for outputs and surfaces, rendering intents, and change-driven re-query—strong support for the semantic model, but deployment support cannot be assumed.
3. Apple exposes ColorSync profile transforms and display EDR potential/current values; content tagging and system composition remain different from direct control or measured output.
4. X11, remote sessions, virtual displays, screen capture, mirroring, docks/KVMs, and vendor utilities can weaken or replace evidence. Providers must expose gaps instead of defaulting unknown output to sRGB or “HDR off.”

## Primary references

- [Microsoft: Advanced Color for DirectX apps](https://learn.microsoft.com/en-us/windows/win32/direct3darticles/high-dynamic-range)
- [Microsoft: AdvancedColorInfo](https://learn.microsoft.com/en-us/uwp/api/windows.graphics.display.advancedcolorinfo)
- [Wayland color-management protocol](https://wayland.app/protocols/color-management-v1)
- [Apple: ColorSync](https://developer.apple.com/documentation/colorsync)
- [Apple: Determining support for EDR values](https://developer.apple.com/documentation/metal/determining-support-for-edr-values)
