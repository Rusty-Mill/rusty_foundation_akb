# Windowing conformance specification

**Status:** Draft

| ID | Requirements | Method |
|---|---|---|
| WINDOW-001 | WINDOW-0001–0003 | Fault every creation stage and issue unsupported/contradictory descriptors; prove no premature resource or presentation |
| WINDOW-002 | WINDOW-0003–0006 | Race requested size/state, user gestures, compositor rejection, close cancellation, and forced destruction; compare requests with committed observations |
| WINDOW-003 | WINDOW-0004, COORD-0004 | Move repeatedly across mixed-scale/rotated displays while resizing; snapshots never combine geometry, scale, display, or generation from different revisions |
| WINDOW-004 | WINDOW-0007–0010, EVENT-0001–0006 | Inject callback recursion, queue pressure, cancellation, context misuse, and destruction at each phase; verify order, coalescing disclosure, and no post-destroy callback |
| WINDOW-005 | WINDOW-0011–0012 | Exercise Unicode titles, truncation, sensitive canaries, synthetic events, capture/transparency/activation policy, and unsupported security features |
| COORD-001 | COORD-0001–0006 | Property-test point/rectangle round trips, negative origins, fractional scales, rotations, edge rounding, stale revisions, and drift-free repeated resize |
| DISPLAY-001 | DISPLAY-0001–0006 | Hot-plug, mirror, remote, virtual, headless, mode/scale/orientation, privacy denial, and enumeration/subscription race vectors |
| SURFACE-001 | SURFACE-0001–0007 | Recreate/invalidate at every frame phase; reject stale generation; verify window survives graphics resource failure and security claims do not strengthen |

## Cross-platform matrix

The same semantic scenarios run on Win32, Wayland, X11 where supported, and AppKit. Provider adapters record native traces alongside canonical snapshots. Platform-specific extensions have separate assertions and cannot satisfy portable requirements by renaming native success.

Accessibility evidence verifies title/role/root-window exposure, focus transitions, keyboard reachability of native chrome, high-contrast/reduced-motion integration, and nonvisual close/fullscreen state announcements. Application content semantics remain outside this slice.

