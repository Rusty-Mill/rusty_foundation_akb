# Platform research

| Platform | Candidate mechanisms | Variance |
|---|---|---|
| Windows | threads, critical sections/SRW locks/condition variables, events/semaphores/waits, interlocked ops, processor groups/CPU sets, priority classes | Waits may interact with messages/APCs; affinity spans groups differently by OS version; SRW fairness/upgrade are limited; priority is dynamic. |
| Linux | pthreads, mutex/cond/rwlock/semaphore, futex-backed implementations, scheduler/affinity APIs | Robust/PI/process-shared features depend on attributes/kernel; realtime requires privilege; CPU sets/namespaces/hotplug alter topology. |
| macOS | pthreads, os_unfair_lock/conditions, dispatch/QoS, affinity hints limited, work queues | QoS is preferred over numeric priority; dispatch tasks are not stable native threads; hardened UI/run-loop affinity matters. |

## Primary references

- [Microsoft: Synchronizing execution](https://learn.microsoft.com/windows/win32/procthread/synchronizing-execution-of-multiple-threads)
- [Microsoft: Processor groups](https://learn.microsoft.com/windows/win32/procthread/processor-groups)
- [Linux: pthreads(7)](https://man7.org/linux/man-pages/man7/pthreads.7.html)
- [Linux: sched_setaffinity(2)](https://man7.org/linux/man-pages/man2/sched_setaffinity.2.html)
- [Apple: Tuning performance for Apple silicon](https://developer.apple.com/documentation/apple-silicon/tuning-your-code-s-performance-for-apple-silicon/)
- [Rust atomics](https://doc.rust-lang.org/core/sync/atomic/)

