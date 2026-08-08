# Runtime and time benchmark specification

**Status:** Draft  
**Suite version:** 0.1.0

## Measurement principles

- Measure an idiomatic native mechanism, the Rusty Mill path, and an end-to-end workload separately.
- Report distributions, not only averages: minimum, median, p90, p99, p99.9, maximum, sample count, and confidence interval where valid.
- Record hardware, OS build, firmware, virtualization, power plan, CPU topology/frequency policy, load, provider version, compiler, and build profile.
- Warm-up, randomized order, outlier policy, and clock source are part of the result.
- A benchmark never weakens a behavioral requirement. Faster but semantically different mechanisms are not valid baselines.

## Benchmark catalog

| ID | Subject | Primary measures | Scale |
|---|---|---|---|
| BM-TIME-MONO-001 | Active clock read | latency, throughput, cycles/read | single thread; all logical CPUs |
| BM-TIME-MONO-002 | Continuous clock read | latency, throughput, cycles/read | supported providers |
| BM-TIME-MONO-003 | Instant/duration arithmetic | latency, branches, overflow cost | hot loop |
| BM-TIME-DEADLINE-001 | Timer create/arm/disarm | latency, allocations, native calls | cold and reused |
| BM-TIME-DEADLINE-002 | Delivery quality | lateness distribution, early-fire count | 100 µs to 24 h deadlines where practical |
| BM-TIME-DEADLINE-003 | Pending-timer scale | memory/timer, insertion/removal, CPU | 1; 1K; 100K; 1M logical timers |
| BM-TIME-DEADLINE-004 | Expiration burst | completions/s, tail latency, scheduler load | 1K–1M same-window deadlines |
| BM-RUNTIME-CANCEL-001 | Cancellation observation | propagation latency, wakeups, allocations | 1–1M observers |
| BM-RUNTIME-CANCEL-002 | Cancellation hierarchy | propagation latency, stack, CPU | depth/breadth matrix |
| BM-RUNTIME-SHUTDOWN-001 | Service coordination | fixed overhead, per-component cost, report cost | DAG sizes 1–100K |

## Native baselines

Baseline selection follows the platform research and exact contract semantics:

- Windows: appropriate QPC/interrupt-time read and waitable/thread-pool timer path.
- Linux: matching `clock_gettime` domain plus `clock_nanosleep` or `timerfd` integration.
- macOS: matching `clock_gettime_nsec_np` domain plus Dispatch timer integration.

Cancellation and shutdown are primarily userspace semantics. Their baseline is the smallest correct platform/runtime-specific composition that provides the same propagation and terminal-outcome guarantees, not an unsafe thread-termination primitive.

## Workload definitions

### Clock reads

Prevent dead-code elimination, subtract harness overhead, run pinned and unpinned variants, and separate contention from CPU migration. Measure precision reduction policies independently.

### Timer delivery

Measure requested deadline against the same bound monotonic domain. Record lateness and verify no early delivery. Run idle, CPU-saturated, I/O-saturated, and power-saving variants. Tolerance/coalescing is a separate series.

### Timer scale

Use randomized deadlines and cancellation ratios. Report steady-state memory after allocator stabilization, not only logical object size. Include creation bursts, churn, and mass expiration.

### Cancellation

Measure request-to-observer latency separately from operation cleanup. Vary already-canceled registration, hierarchy shape, callback/no-callback mode, and concurrent requesters.

### Shutdown

Use generated acyclic component graphs with configurable work duration, failure rate, and escalation. Separate graph construction from shutdown execution. Validate results against the conformance model while measuring.

## Provisional budgets

Numeric release budgets are deferred until native baselines run on representative hardware. Before measurements exist, the enforceable gates are structural:

- Clock reads and instant arithmetic allocate zero memory.
- One pending logical timer does not require one dedicated thread.
- Cancellation request complexity is not proportional to hierarchy depth on the caller's stack.
- Shutdown coordination is linear in registered components plus dependency edges.
- Rusty Mill results publish absolute cost and overhead relative to the equivalent native guarantee.

After three stable baseline runs per platform, an RFC will establish regression budgets using observed variance rather than aspirational numbers.

## Regression handling

A regression report identifies the first affected commit when bisectable, changed environment, absolute and relative deltas, confidence, affected contract versions, and user impact. A waiver is time-bounded, owned, and linked to the release claim.
