# Threading benchmark specification

| Workload | Metrics |
|---|---|
| Thread lifecycle | create/start/join latency, stack address/commit/RSS, throughput |
| Mutex/rwlock | uncontended/contended latency, throughput, tail wait, fairness/starvation, cache traffic |
| Condition/event/semaphore | wake latency, handoff, herd size, spurious/obsolete rate, CPU |
| Atomics | per-operation latency/throughput by ordering and contention, lock-free status |
| Affinity/QoS | migration, latency variance, throughput, energy, topology locality |
| Realtime | deadline miss distribution, worst observed latency, inversion duration, interference |
| TLS | first/subsequent access, key creation, destructor overhead |

Record hardware/topology/NUMA/SMT, OS/build, architecture, power/thermal state, scheduler/affinity/QoS, compiler/runtime/provider, primitive attributes, thread count, critical-section/work ratio, memory placement, warmup, and distributions. Microbenchmarks do not establish application-level scalability or hard realtime guarantees.

