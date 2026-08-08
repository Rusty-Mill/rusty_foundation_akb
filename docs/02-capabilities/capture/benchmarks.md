# Camera and media-capture benchmark specification

| Benchmark | Measures |
|---|---|
| Startup | authorization-excluded session configure/start to first valid frame and stable effective format |
| Frame delivery | exposure/source boundary to native delivery, provider handoff, consumer observation, and preview presentation |
| Stability | achieved frame-rate distribution, jitter, drops/duplicates/corruption, queue occupancy over sustained capture |
| Buffer pressure | retention/copy/import cost, starvation onset, memory bandwidth, peak retained bytes, recovery |
| Conversion | scaling/color/rotation/deinterlace cost, precision/error, hardware/software path, added latency |
| Controls | request-to-effective-frame latency and settling behavior for focus/exposure/white balance/zoom/rate |
| Reconfiguration | pause/drop/generation cost for format, rate, device, orientation, and consumer changes |
| Recovery | interruption, revocation, device/service loss, sleep/resume, stop and buffer/indicator release |
| Power/thermal | CPU/GPU/media-engine use, energy, thermal throttling, rate/quality degradation |

Results report p50/p95/p99/max, achieved fps, jitter, drops by cause, CPU/GPU, allocations, copies, memory bandwidth/peak, buffer occupancy, callback duration, power, and thermal state. Runs disclose device/driver/firmware, OS/build, provider graph, authority state, requested/effective format/rate/color/orientation, controls, buffer mode/count, transformations, clock/timestamp boundary, preview/consumer workload, power/thermal mode, and raw measurement method. Authorization prompt latency is a UX observation, not engine performance.
