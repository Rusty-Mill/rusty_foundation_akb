# `rm.input.touch`

| Field | Value |
|---|---|
| Status | Draft |
| Contract version | 0.1.0 |

**RM-INPUT-TOUCH-0001:** A touch contact stream uses opaque contact identities scoped to one device/session epoch and distinguishes down, motion, up, cancel, frame/batch boundary, and shape/pressure/orientation availability.

**RM-INPUT-TOUCH-0002:** Contact positions are window-logical values bound to one transform/focus-routing revision. All contacts in an atomic native frame share a consistent snapshot.

**RM-INPUT-TOUCH-0003:** Motion may coalesce with covered interval and retained final state; down, up, cancel, and frame boundaries are non-coalescible.

**RM-INPUT-TOUCH-0004:** Focus loss, surface destruction, gesture takeover, device removal, and overflow cancel every affected active contact exactly once or reset the epoch explicitly.

**RM-INPUT-TOUCH-0005:** Gesture recognition, palm rejection, handwriting, accessibility dwell actions, and mouse emulation are higher-layer/platform services. Providers disclose native transformations and do not double-deliver one action as independent touch and pointer without causal classification.

**RM-INPUT-TOUCH-0006:** Contact geometry/pressure is normalized only with declared ranges and calibration provenance; unavailable values remain unavailable.

**RM-INPUT-TOUCH-0007:** Touch traces are sensitive behavioral data and are excluded from default logs, recordings, crash artifacts, and conformance evidence payloads.

