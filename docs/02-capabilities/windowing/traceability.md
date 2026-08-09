# Windowing assertion traceability

**Status:** Draft assertion mapping  
**Authority:** [Windowing domain](README.md)

The semantic identities below compose the existing `WINDOW-*`, `COORD-*`, `DISPLAY-*`, and `SURFACE-*` executable cases without replacing their historical identities.

| Assertion | Covered normative source files | Verification intention |
|---|---|---|
| `rm.assertion.windowing.lifecycle@1` | `window.md`, `event-model.md` | Verify staged creation, request versus committed state, close/destroy, callback order/context, reentrancy, queue policy, and terminal event boundaries. |
| `rm.assertion.windowing.coordinates@1` | `coordinate-model.md` | Property-test typed spaces, revisioned transforms, rounding, fractional scale, rotation, negative origins, and drift resistance. |
| `rm.assertion.windowing.displays@1` | `display-topology.md` | Verify revisioned snapshots, identity generations, hot-plug/mirror/remote/headless changes, privacy denial, and subscription reconciliation. |
| `rm.assertion.windowing.presentation-surface@1` | `presentation-surface.md`, `traceability.md` | Verify surface generation/invalidation, geometry/display correlation, stale-resource rejection, security nonclaims, and traceability identity rules. |

**RM-WINDOW-TRACE-0001:** Every windowing requirement MUST map to a stable semantic assertion and an executable case/review method before Experimental promotion.

**RM-WINDOW-TRACE-0002:** Native Win32, Wayland, X11, and AppKit case adapters MUST preserve the same semantic assertion identity while reporting provider-specific setup, observations, limitations, and artifacts.

**RM-WINDOW-TRACE-0003:** Presentation success, committed window state, frame display, input focus, and accessible exposure MUST remain separate oracles.
