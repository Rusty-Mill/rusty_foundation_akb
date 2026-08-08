# Encode, mux, and recording boundaries

Encoding/muxing is a rateless or realtime pipeline selected separately from playback. Camera/microphone capture, editing, and artifact durability compose but do not merge with it.

**RM-MEDIA-ENCODE-0001:** An encoder plan binds exact codec/profile/level/tier, raw input generation, rate-control/quality/latency/GOP/reference/scalability vector, pixel/audio/color/layout policy, metadata, hardware/isolation, deterministic claim, and resource budget.

**RM-MEDIA-MUX-0001:** A mux plan binds container/profile/brands, track identities/configurations/time bases, interleave/chunk/index policy, timestamp/edit mapping, metadata/chapters, fragmentation/streamability, encryption signaling under separate authority, destination behavior, and finalization/recovery.

**RM-MEDIA-ENCODE-0002:** Submit, encoded output, drain, flush/reset, and close semantics match codec sessions. Keyframe request is intent and reports the actual produced random-access type/time.

**RM-MEDIA-MUX-0002:** DTS/PTS ordering, negative offsets, priming/padding, gaps, discontinuities, configuration changes, and track end are validated before writing. Timestamp rescaling uses exact checked arithmetic and named rounding.

**RM-MEDIA-MUX-0003:** Header written, media fragment durable, index/final metadata written, mux finalized, file atomically replaced, storage synchronized, and remote accepted are distinct milestones. A canceled/unfinalized artifact is not implicitly valid.

**RM-MEDIA-RECORD-0001:** Realtime recording defines overload/drop policy, timestamp source/correlation, A/V sync, checkpoint/fragment recovery, storage budget, permission/privacy indication, interruption, background/power, and crash salvage. Recording never follows automatically from raw capture.

**RM-MEDIA-ENCODE-0003:** Deterministic and quality claims bind implementation/version, hardware, threads, rate-control state, metadata/timestamps, and analysis passes. Byte identity, decoded equivalence, and perceptual quality remain separate.
