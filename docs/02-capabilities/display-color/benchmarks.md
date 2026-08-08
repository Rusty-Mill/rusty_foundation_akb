# Display and color-management benchmarks

| Benchmark | Measures | Required parameters |
|---|---|---|
| COLOR-BENCH-001 | Display/surface-description observation latency | display count, protocol/provider, cold/warm, profile access |
| COLOR-BENCH-002 | Transform-plan creation/cache | description/profile complexity, intent, engine, CPU/GPU path |
| COLOR-BENCH-003 | Pixel transform throughput/tail | resolution, format/precision, gamut/tone map, metadata, alpha, hardware path |
| COLOR-BENCH-004 | Presentation renegotiation | display migration, mode/profile/headroom storm, surface/device recreation |
| COLOR-BENCH-005 | Memory/bandwidth/power cost | frame size/rate, intermediate count, precision, direct/composited path |
| COLOR-BENCH-006 | Numerical quality | corpus, reference engine/version, error metric/tolerance, clipping/mapping class |

Record p50/p95/p99/max, CPU/GPU time, allocations/peak memory, upload/readback/copies, bandwidth, cache hit/miss, compilation, frames interrupted/degraded, time to stable generation, power/thermal state, and transform error statistics. Separate content rendering, color conversion, compositor, scan-out, display response, and measurement latency.

Native comparisons use the identical source/destination descriptions, format, intent, precision, compositor path, and algorithm-quality class. Faster untagged, clipped, lower-precision, different-tone-map, or bypass paths are not equivalent baselines. Sustained tests cover change storms and verify bounded caches, retired generations, no profile/resource leaks, stable frame pacing, and declared degradation under memory/power/thermal pressure.
