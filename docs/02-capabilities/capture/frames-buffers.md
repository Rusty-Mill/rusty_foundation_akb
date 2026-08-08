# Capture frame and buffer model

A `CaptureFrame` binds stream/session/device generations, sequence, discontinuity epoch, format, planes, valid regions, capture and delivery timing, exposure interval when known, control-state revision, metadata, corruption/drop indicators, and ownership token.

**RM-CAPTURE-FRAME-0001:** Every frame MUST be self-describing against an immutable format revision and MUST NOT depend on ambient session state for safe plane access.

**RM-CAPTURE-FRAME-0002:** Frame sequence and discontinuity epoch MUST expose dropped, duplicated, corrupt, reordered, rate-changed, and stream-restarted conditions where detectable.

**RM-CAPTURE-FRAME-0003:** Buffers MUST declare memory domain, mapping/access rules, alignment, cache/coherency requirements, lifetime, mutability, and cross-device/process transfer support.

**RM-CAPTURE-FRAME-0004:** Borrowed native buffers MUST be returned by a bounded deadline or copied/imported under explicit policy. Holding a frame MUST NOT silently exhaust the entire capture pipeline.

**RM-CAPTURE-FRAME-0005:** GPU/accelerator-backed frames MUST use separately proven graphics resource sharing and synchronization; a native image handle is not a portable safe pixel slice.

**RM-CAPTURE-FRAME-0006:** Sensitive metadata—including faces/subjects, location, device identifiers, calibration, depth, and vendor payloads—MUST be projected explicitly and independently from pixel delivery.
