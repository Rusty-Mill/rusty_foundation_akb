# Time-based media benchmarks

| Benchmark | Measures | Required parameters |
|---|---|---|
| MEDIA-BENCH-001 | Probe/track/index latency and bytes touched | container, tracks, size, source seek/network/cache, cold/warm |
| MEDIA-BENCH-002 | Decode throughput/tail and queueing | codec/profile, resolution/rate/layout, output memory/color/audio, hardware/software |
| MEDIA-BENCH-003 | Playback startup/rebuffer/live latency | source/network, buffer policy, tracks, decoders, sinks, clock |
| MEDIA-BENCH-004 | Seek accepted-to-ready/observed | target/tolerance/distance, index/keyframe/GOP, source cache/range, track count |
| MEDIA-BENCH-005 | A/V/text synchronization stability | duration, clocks/sinks, drift injection, rate, correction policy, load |
| MEDIA-BENCH-006 | Encode/mux throughput/latency/quality | codec controls, realtime/rateless, tracks/interleave/fragmentation, hardware |
| MEDIA-BENCH-007 | Resource and recovery stability | long playback, track/rate/seek storms, device/provider loss, suspend, cancellation |

Measure p50/p95/p99/max, first descriptor/frame/audio/ready/presented milestones, throughput, queue/reorder/buffer occupancy, CPU/GPU, allocations and peak CPU/GPU/disk memory, copies/bandwidth, clock skew/drift/correction, dropped/repeated/concealed samples, underruns, power/thermal state, network throughput/range requests, output size, and applicable numerical/perceptual quality.

Pin corpus/source digest, container/tracks/configs, provider/framework/codec/build, threading/SIMD/hardware/isolation, time mappings, clock/sinks, buffer/seek/sync/drop policy, output/color/audio transforms, OS/driver/hardware/network/cache, and power/thermal state. Native baselines must use equivalent validation, limits, output, synchronization, isolation, and protection. Sustained tests prove bounded resources and recovery without stale-generation presentation or sensitive-data leakage.
