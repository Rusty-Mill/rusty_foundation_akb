# Threading conformance specification

| Area | Evidence |
|---|---|
| Lifecycle | creation failure, stack rounding/guard, join/self-join, panic containment, cooperative cancellation, ID reuse |
| Mutex/rwlock | happens-before litmus tests, try/deadline, recursion, poisoning, starvation/fairness claims, upgrade denial |
| Waits | spurious/obsolete wake, notify races, semaphore overflow, event reset, wait-any/all, destruction/cancellation |
| Atomics | supported widths/alignment, order litmus tests, weak CAS, lock-free claims, mixed-size/unaligned rejection |
| Scheduling | priority/QoS mapping, denial/degradation, inversion, processor groups/hotplug/stale topology |
| Realtime | privilege, bounded paths, page faults/allocations/locks, watchdog/fallback, interference |
| TLS | recursive init, destructor variance, foreign/pool threads, process exit and plugin retirement |
| Integration | UI/apartment waits, async worker blocking, shutdown, observability recursion, deadlock detection tooling |

Stress and model-based tests vary CPU count, oversubscription, weak-memory architecture, contention, timeouts, cancellation, suspension, hotplug/affinity, and injected owner failure. Reports bind OS/build, CPU/topology, architecture, scheduler policy, power mode, mitigations, runtime/compiler/provider versions, and all fairness/progress nonclaims.

