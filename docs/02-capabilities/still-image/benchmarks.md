# Still-image and image-codec benchmarks

| Benchmark | Measures | Required parameters |
|---|---|---|
| IMAGE-BENCH-001 | Probe/inspection latency and bytes touched | format, size, seekability, metadata/items, cold/warm provider |
| IMAGE-BENCH-002 | Full decode throughput/tail | codec/profile, dimensions, entropy/content class, output layout/color, CPU/hardware |
| IMAGE-BENCH-003 | First useful/final progressive output | delivery chunks/rate, levels/passes, revision policy, decoder |
| IMAGE-BENCH-004 | Region/thumbnail/scale decode | requested/effective region/level, native/full path, source tiling, cache |
| IMAGE-BENCH-005 | Animation steady playback | canvas/frame/dependency/timing, decode-ahead, disposal, drops, memory |
| IMAGE-BENCH-006 | Encode size/quality/speed | codec control vector, corpus class, quality metric/version, deterministic mode |
| IMAGE-BENCH-007 | Transform/transcode | orientation/crop/scale/color/alpha/metadata path, lossless/compressed/full decode |

Measure p50/p95/p99/max, first descriptor/preview/final latency, megapixels and input/output bytes per second, CPU/GPU time, allocations/peak committed/resident/GPU memory, copies/bandwidth, queue depth, cache behavior, power/thermal state, output size, and applicable numerical/perceptual quality metrics. Failures and budget rejections are measured separately from successful throughput.

Pin corpus digest, provider/codec/version, build flags, threading/SIMD/hardware, requested/effective output, color transform, metadata policy, isolation/IPC, cache/input state, OS/driver/hardware, and power/thermal conditions. A native baseline is equivalent only with the same validation, limits, output semantics, transforms, metadata, and isolation. Sustained tests prove bounded memory/resources under mixed thumbnails, large files, hostile rejection, cancellation storms, and provider crashes.
