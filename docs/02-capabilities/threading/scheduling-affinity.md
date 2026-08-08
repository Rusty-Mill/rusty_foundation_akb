# Scheduling, affinity, and realtime

**RM-THREAD-SCHED-0001:** Work intent distinguishes latency-sensitive interactive, user-initiated, utility, background, throughput, and specialized realtime classes. Providers map intent with exact quality rather than equating native numeric priorities.

**RM-THREAD-SCHED-0002:** Requested and effective priority/QoS/scheduling policy are distinct. Success does not guarantee immediate execution, deadline completion, CPU share, or exclusion of lower-priority work.

**RM-THREAD-SCHED-0003:** Affinity uses a topology snapshot and stable-in-that-snapshot processor set identity. Hotplug, processor groups, heterogeneous cores, containers, and policy can invalidate it.

**RM-THREAD-SCHED-0004:** Hard affinity, soft/ideal placement, NUMA locality, core-performance class, and cache relationship are separate optional constraints. Empty/stale/denied sets fail or degrade explicitly.

**RM-THREAD-SCHED-0005:** Realtime scheduling requires explicit privilege/authority, bounded nonblocking code, prefaulted/locked resources where evidenced, priority-inversion policy, watchdog/fallback, and starvation review.

**RM-THREAD-SCHED-0006:** Libraries do not raise process/thread scheduling globally. Policy belongs to the application/service that owns the execution context.

