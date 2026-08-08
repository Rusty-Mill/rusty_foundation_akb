# Plugin benchmark specification

| Workload | Metrics |
|---|---|
| Catalog | scan/verify/resolve latency, bytes read, CPU, allocations by package count/size |
| Activation | verify-to-ready milestones, native load/process spawn/component instantiate, peak resources |
| Calls | latency/throughput/payload scaling for in-process ABI, IPC, and component boundary |
| Async/stream | scheduling, copies, backpressure, cancellation, fairness |
| Isolation | memory/CPU/handle overhead and broker-call cost |
| Crash/restart | detection, service unavailability, restart/readiness, residual resources |
| Update | stage/verify/migrate/switch/quiesce/rollback latency and peak disk/memory |
| Shutdown | quiesce/drain/terminate latency, outstanding-call outcomes |

Results record hardware, OS/build, package/interface/runtime/compiler/loader versions, isolation mode, signing/trust policy, grants/limits, payload and call concurrency, warm/cold caches, telemetry, mitigation settings, and statistical variance. Performance never substitutes for isolation or compatibility evidence.

