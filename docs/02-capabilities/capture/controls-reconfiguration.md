# Capture controls and reconfiguration

Controls are typed descriptors and negotiated state: identifier, value kind, unit, discrete/menu/range constraints, automatic/manual modes, dependencies, conflicts, default/current/effective values, revision, write authority, application latency, and source of change.

**RM-CAPTURE-CONTROL-0001:** Exposure, focus, gain/ISO, white balance, zoom, frame duration/rate, torch/flash, stabilization, HDR, privacy, and vendor controls MUST NOT be assumed present or numerically equivalent across devices.

**RM-CAPTURE-CONTROL-0002:** Requested, accepted, effective, clamped, overridden, pending, and failed control states MUST remain distinguishable.

**RM-CAPTURE-CONTROL-0003:** Multi-control updates MUST declare atomicity. A provider that cannot apply a coherent transaction MUST report application order and intermediate-state visibility.

**RM-CAPTURE-CONTROL-0004:** Automatic controls MUST publish mode and effective observations where available; setting a value while auto mode remains active MUST NOT imply persistence.

**RM-CAPTURE-CONTROL-0005:** Reconfiguration MUST identify whether it is seamless, frame-boundary, dropping, pausing, or generation-replacing and MUST emit the first frame/control revision governed by the new state.

**RM-CAPTURE-CONTROL-0006:** Torch/flash, indicator-affecting, motorized, infrared, and potentially safety-sensitive controls require separate authority and product disclosure.
