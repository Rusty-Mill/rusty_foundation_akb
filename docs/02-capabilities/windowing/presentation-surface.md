# `rm.windowing.presentation-surface`

| Field | Value |
|---|---|
| Status | Draft |
| Contract version | 0.1.0 |

**RM-WINDOWING-SURFACE-0001:** A presentation surface is acquired for one ready window and one committed surface generation. It exposes a portable descriptor sufficient for compatible graphics-provider selection, not an unrestricted native handle.

**RM-WINDOWING-SURFACE-0002:** Scale, pixel extent, color metadata, alpha/composition mode, and generation are immutable for a surface lease. A change publishes a new generation and invalidates or retires the old generation explicitly.

**RM-WINDOWING-SURFACE-0003:** Invalidation is observable before or with the snapshot that makes a generation stale. Presentation against a stale generation fails deterministically and cannot be reported as visible success.

**RM-WINDOWING-SURFACE-0004:** Surface ownership remains with windowing. Graphics owns device/swapchain/render resources and must release generation-bound resources without destroying the window.

**RM-WINDOWING-SURFACE-0005:** Present completion, frame scheduling, tearing, HDR, color conversion, and device recovery are graphics/presentation contracts. This capability reports only window-side readiness, invalidation, and compatibility facts.

**RM-WINDOWING-SURFACE-0006:** Native-handle escape requires a separate unsafe/advanced contract defining borrow duration, thread affinity, invalidation, exclusivity, and lost portability.

**RM-WINDOWING-SURFACE-0007:** Capture protection and protected-content claims are independent negotiated security properties. Absence or best-effort support is never promoted to confidentiality.

