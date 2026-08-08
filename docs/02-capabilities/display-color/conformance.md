# Display and color-management conformance specification

| Area | Required evidence |
|---|---|
| Descriptions | named/parametric/ICC, RGB/YUV/range/chroma, SDR/PQ/HLG/linear, alpha, relative/absolute luminance, malformed/conflicting/unknown metadata |
| Display | SDR/HDR/WCG/precision combinations, potential/current headroom, profile sources, internal/external/virtual/remote/mirrored/spanning displays, descriptor errors |
| Surface | accepted/rejected formats/descriptions/intents, atomic pixel tagging, fallback, display migration, compositor/device/surface restart and generations |
| Transform | primaries/white/transfer/matrix, chromatic adaptation, gamut/tone map, black point, clipping/over-range/non-finite, precision/dither, CPU/GPU parity |
| Lifecycle | mode/profile/reference-white/headroom/ambient changes, event loss/coalescing, resume, old-generation retirement, transition luminance safety |
| Calibration | source layering, double-application prevention, profile validation, measured claim uncertainty, configuration binding, privileged-control separation |
| Security/accessibility | fingerprint minimization, hostile profiles/metadata, resource bounds, user color/contrast filters, semantic alternatives, HDR/flash safety, accessible controls |

Reference vectors include exact tristimulus/transfer pairs, grayscale ramps, primaries/secondaries, near-black and highlight steps, out-of-gamut/over-range/negative/non-finite values, alpha-composited edges, gradients for banding, SDR-in-HDR reference white, static/dynamic metadata, and tagged/untagged ambiguity. Numeric tests validate transforms independently of screenshots; compositor/display tests use capture or measurement only with the boundary and uncertainty stated.

Reports bind OS/compositor/window system, GPU/driver, display/connection/mode, provider/protocol versions, surface/buffer format, source/destination descriptions and digests, transform engine/algorithm, profile/calibration sources, SDR/HDR/reference-white/headroom/brightness/ambient/power state, instrument/procedure where used, and every appearance/calibration/direct-scanout nonclaim.
