# `rm.input.pointer`

| Field | Value |
|---|---|
| Status | Draft |
| Contract version | 0.1.0 |

**RM-INPUT-POINTER-0001:** Pointer events distinguish enter, leave, absolute motion, relative motion, button transition, axis/scroll, axis stop, and cancellation/reset. Each carries sequence, timestamp, device/provenance, modifier/button snapshot, focus/capture revision, and applicable window transform revision.

**RM-INPUT-POINTER-0002:** Absolute coordinates are typed window-logical positions tied to a committed window transform revision. Relative motion is a distinct unaccelerated/accelerated quality claim and is never derived by subtracting warped absolute positions silently.

**RM-INPUT-POINTER-0003:** Axis data preserves axis identity, continuous delta, discrete steps, source (wheel/finger/continuous/unknown), direction/inversion information, phase/stop, and precision availability. Providers do not invent pixels per wheel notch.

**RM-INPUT-POINTER-0004:** Motion and compatible axis updates may coalesce only when the event reports covered sequence/time interval and final state. Enter/leave, buttons, axis-stop, capture change, and reset are non-coalescible.

**RM-INPUT-POINTER-0005:** Capture/confinement/lock are asynchronous policy requests. Effective state is observed separately and automatically terminates on focus loss, destruction, authority loss, or compositor cancellation.

**RM-INPUT-POINTER-0006:** Cursor image/visibility/shape is a window/UI presentation concern coordinated with pointer focus; it is not part of device observation fidelity.

**RM-INPUT-POINTER-0007:** High-frequency delivery applies bounded batching/backpressure without blocking native dispatch. Overflow terminates the state epoch or reports exact loss; button transitions never vanish silently.

**RM-INPUT-POINTER-0008:** Pointer location, device identity, pressure/tilt extensions, and raw motion may be fingerprinting-sensitive. Access and telemetry follow least-detail policy.

