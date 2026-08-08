# Seeking, buffering, and discontinuity

**RM-MEDIA-SEEK-0001:** A seek request MUST state target time/domain, before/after tolerance, direction, exact/keyframe/fast policy, selected-track scope, live-edge relation, deadline/cancellation, and whether playback resumes.

**RM-MEDIA-SEEK-0002:** Resolution reports requested target, attainable demux/decode start, actual first eligible presentation time per track, trim/drop/preroll, index/evidence quality, network/range work, and degraded accuracy.

**RM-MEDIA-SEEK-0003:** Seek creates a discontinuity generation and performs bounded cancel/flush/reset, demux reposition, decoder preroll, sink invalidation, clock rebase, and buffer reconstruction. Old-generation outputs are rejected.

**RM-MEDIA-SEEK-0004:** Seek accepted, source repositioned, decoders primed, first target samples available, sinks presentation-ready, and first target output observed are distinct milestones. Cancellation or superseding seek cannot resurrect an earlier generation.

**RM-MEDIA-BUFFER-0001:** Buffered and seekable ranges are revisioned per source/track and time domain with completeness, gaps, byte residency/cache quality, decoder readiness, expiration, and observation time. Downloaded bytes are not automatically playable media.

**RM-MEDIA-BUFFER-0002:** Buffer policy binds minimum/start/resume/maximum horizons, byte/memory/disk budgets, live latency target, throughput estimate/uncertainty, eviction, backpressure, and rebuffer behavior. It exposes why playback is blocked.

**RM-MEDIA-BUFFER-0003:** End-of-current-data, temporary starvation, live-edge wait, source failure, track gap, decoder wait, sink backpressure, and terminal end-of-stream remain distinguishable.

See [ADR-0071](../../adr/0071-media-seek-is-a-negotiated-discontinuity.md).
