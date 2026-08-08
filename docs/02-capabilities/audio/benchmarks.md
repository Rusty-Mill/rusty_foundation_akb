# Audio benchmark specification

Benchmarks report distributions and failure counts, not a single “latency” score.

| Benchmark | Measures |
|---|---|
| Callback service | callback duration p50/p95/p99/p99.9/max versus effective quantum; deadline misses |
| Render stability | underruns, silence insertion, discontinuities, effective queue depth over sustained and burst interference |
| Capture stability | overruns, lost frames, timestamp uncertainty, handoff delay |
| Round trip | measured input-to-output latency and jitter with external loopback; software estimates labeled separately |
| Clock quality | correlation error, drift, age, reset detection, cross-stream synchronization |
| Start/route/recovery | open-to-first-frame, stop/drain, hotplug/default-route migration, permission and service-restart recovery |
| Processing cost | CPU time/frame, memory bandwidth, allocations/page faults, scaling by channels/rate/graph size |
| Power | stable-playback and idle cost under declared buffer/period policy |

Runs disclose warmup, duration, sample count, CPU isolation or contention, frequency/power mode, scheduling/QoS, device/driver/transport, effective format/period/buffer, conversion, and measurement apparatus. Realtime claims require sustained tests under representative UI, storage, network, and graphics interference plus raw artifacts sufficient to reproduce percentile and XRUN results.
