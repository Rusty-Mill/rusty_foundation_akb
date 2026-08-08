# Time-based media conformance specification

| Area | Required evidence |
|---|---|
| Source/container | seekable/stream/live/growing, extension/MIME/brand conflict, tracks/programs/edits/indexes/attachments/encryption, malformed/truncated/cyclic/overflow structures |
| Timeline | multiple time bases, negative/start offsets, gaps/overlaps/edits, DTS/PTS reorder, missing/duplicate/nonmonotonic/wrap timestamps, unknown/growing duration, discontinuities |
| Codec | profile/config changes, key/dependent frames, reorder/drain/flush/reset, malformed/reference storms, queue bounds, software/hardware/isolation, device/provider loss |
| Raw output | exact video layout/color/HDR/geometry and audio format/layout/trim, memory leases, corruption/concealment, config/discontinuity generations |
| Playback/sync | clock selection/failover, audio/video/text skew, rate/pause/buffer/end/loop, drop/repeat/stretch corrections, device/compositor latency evidence |
| Seek/buffer | fast/exact/tolerant/forward/reverse/live seek, keyframe/preroll/trim, superseded/canceled seeks, old-generation rejection, byte/buffer/decoder readiness ranges |
| Text/accessibility | captions/subtitles/SDH/forced/audio description/chapters, language/bidi/style, hostile payloads, user styling, semantic exposure, accessible controls/transcript |
| Encode/mux | rate-control/GOP, exact timestamps/interleave/fragments/index/finalize, realtime overload, crash recovery, cancellation, deterministic/fidelity claims |
| Security | provider provenance/isolation, metadata/history privacy, external reference denial, protected-path/key nonexposure, screenshot/export restrictions and nonclaims |

Corpora include independently generated container/codec combinations, standards vectors, timestamp/edit/index adversaries, random-access dependency cases, variable frame rate, priming/padding, channel layouts, interlace/HDR/color changes, subtitle formats, live discontinuities, fuzz regressions, and resource bombs rejected within budgets. Multi-provider differential results classify allowed variance rather than selecting majority output as truth.

Reports bind corpus digest/provenance/license, source mode/network/cache, container/tracks/configs, provider/framework/codec/version/build/signature/isolation, hardware/driver/memory path, all time bases/mappings/generations, selected clock/sinks, requested/effective policy and budgets, output digests/numerical oracles, accessibility/protection state, and every timing/fidelity/security/physical-presentation nonclaim.
