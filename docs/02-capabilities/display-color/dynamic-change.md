# Dynamic change and lifecycle

**RM-COLOR-CHANGE-0001:** Display color events carry display/surface/provider generation, observation revision, known change class, loss/coalescing, and resynchronization need. They are invalidation hints, not a lossless settings journal.

**RM-COLOR-CHANGE-0002:** Consumers re-read coherent topology, display color state, surface preference, and presentation compatibility after display add/remove, mode/HDR/profile/reference-white/headroom change, window migration, compositor restart, remote-session transition, resume, or event gap.

**RM-COLOR-CHANGE-0003:** A new display snapshot never mutates an existing image description or transform plan. Dependent caches and surface sessions bind generations and retire deterministically.

**RM-COLOR-CHANGE-0004:** Transition policy defines whether to hold the last valid frame, temporarily use conservative SDR, re-render immediately, cross-fade only where safe, or suspend presentation. It MUST NOT flash unbounded luminance or reinterpret old pixels.

**RM-COLOR-CHANGE-0005:** Rapid migration/headroom/ambient changes use bounded coalescing and hysteresis while preserving the latest authoritative state. Accessibility and safety changes may bypass aesthetic smoothing.

**RM-COLOR-CHANGE-0006:** Suspend, display loss, or application shutdown provides no cleanup or restoration guarantee. Privileged calibration/configuration services use leases/transactions and crash-safe rollback policies defined by their own contracts.
