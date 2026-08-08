# Power and energy-management benchmark specification

| Benchmark | Measures |
|---|---|
| Observation | snapshot/query latency, notification-to-reconciled-state, native calls, allocations, stale/unknown rate |
| Idle overhead | CPU, wakeups, memory, handles, and energy cost of observer at configurable update rates |
| Adaptation | policy-transition to effective workload change, oscillation, quality floor, work deferred/cancelled |
| Lease | acquire/renew/release latency, expiry accuracy, owner-failure cleanup, effective-state observation |
| Suspend/resume | pre-sleep opportunity, resume notification, full resource/clock reconciliation, first useful work |
| Thermal stability | sustained throughput/latency/quality and power over warmup, steady state, throttling, and recovery |
| Energy budget | measured energy/work and energy/time by workload/quality, with uncertainty and whole-system idle subtraction |

Results report distributions, energy in joules/Wh, average/peak power, work completed, quality, CPU/GPU/device utilization, wakeups, thermal state, frequency/throttling evidence, battery-rate uncertainty, and transition counts. Runs disclose hardware/firmware/battery health, OS/provider, ambient/cooling, power source/profile/saver, display/network/device state, workload duration/data, background/foreground/session, measurement instrument/API/calibration, sample rate, idle baseline, and raw artifacts. Cold burst benchmarks cannot substantiate sustained efficiency.
