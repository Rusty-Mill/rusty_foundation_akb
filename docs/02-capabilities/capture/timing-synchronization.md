# Capture timing and synchronization

Frame timestamps may refer to start of exposure, end of frame, device/driver dequeue, transformed presentation time, or software observation. The timestamp value is meaningless without source boundary and clock domain.

**RM-CAPTURE-TIME-0001:** Each frame MUST report timestamp, clock identity/generation, timestamp source boundary, uncertainty/quality, and whether it was copied, inferred, transformed, or directly observed.

**RM-CAPTURE-TIME-0002:** Capture clocks MUST correlate to the portable monotonic clock through explicit snapshots carrying uncertainty, age, drift, and discontinuity.

**RM-CAPTURE-TIME-0003:** Frame rate is observed delivery/capture behavior, not merely a nominal format value. Variable rate, stalls, duplicates, drops, and rate transitions MUST remain visible.

**RM-CAPTURE-TIME-0004:** Session restart, device switch, clock reset, sleep/resume, route change, and format reconfiguration MUST advance a timing epoch unless continuity is measured and proven.

**RM-CAPTURE-TIME-0005:** Multi-camera, audio/video, depth/video, and external-sensor synchronization MUST state clock sources, alignment method, maximum skew/uncertainty, buffering, and failure behavior. Common session membership alone is not a synchronization guarantee.

Latency metrics identify exposure/source boundary, driver/native delivery, provider delivery, consumer observation, preview presentation, encode, and storage milestones separately.
