# Screen and window capture benchmark specification

| Benchmark | Measures |
|---|---|
| Startup | selector-complete to native acceptance, first valid frame, stable configuration, effective indication |
| Frame latency | provider timestamp boundary to callback, consumer acquisition, conversion, preview/encode handoff |
| Stability | achieved frame-rate distribution, jitter, gaps/duplicates/stale frames, queue occupancy and memory over sustained capture |
| Damage efficiency | unchanged and sparse-change CPU/GPU/copy/bandwidth cost versus full-frame behavior |
| Buffer pressure | held-frame threshold, copy/import cost, starvation onset, bounded degradation and recovery |
| Resize/change | latency, dropped frames, memory peak, and generation correctness across resize/migration/mode/color/source changes |
| Cursor/audio | cursor-to-frame correlation; audio latency, jitter, drift/skew, discontinuity, isolation and feedback behavior |
| Recovery | revocation, source close, lock/switch, sleep/resume, device/provider loss, stop-to-last-frame/buffer-release/indicator-clear |
| Power/thermal | CPU/GPU/media-engine load, memory bandwidth, energy, thermal response under resolution/rate/HDR/source combinations |

Results report p50/p95/p99/max and distributions, achieved fps, dropped/coalesced/duplicate frames by cause, CPU/GPU, allocations/copies/imports, memory and bandwidth peaks, queue/pool occupancy, callback duration, cursor/audio skew, power, and thermal state. Runs disclose machine, GPU/driver, OS/build/compositor/portal, source and changes, selection/authority path, frame/color/cursor/audio configuration, clock boundary, buffer policy, downstream workload, remote/virtual state, and raw measurement method. Human picker and consent time is reported separately as UX evidence, not engine latency.
