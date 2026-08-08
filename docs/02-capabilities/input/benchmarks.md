# Input benchmark specification

**Status:** Draft

| ID | Workload | Measures |
|---|---|---|
| INPUT-BENCH-001 | Hardware/native observation to portable delivery | p50/p95/p99/max latency, jitter, queue depth, allocations |
| INPUT-BENCH-002 | 125–8000 Hz pointer motion with batching/coalescing | CPU, wakeups, throughput, coverage, transition latency |
| INPUT-BENCH-003 | Keyboard press/release/repeat burst | tail latency, ordering, layout lookup cost, allocations |
| INPUT-BENCH-004 | IME preedit/update/commit and candidate geometry | callback/stream latency, revision retries, UI response |
| INPUT-BENCH-005 | Multi-touch contact frames | throughput, atomic-frame latency, cancellation cost |
| INPUT-BENCH-006 | Focus/capture/window-transform churn | routing convergence, stale-event rejection, reset recovery |
| INPUT-BENCH-007 | Terminal key/text/pointer encoding | input-to-submit latency, mode/geometry reconciliation, backpressure |

Results record input hardware/rate, connection, OS/session/remote mode, layout and IME, accessibility filters, display refresh/scale, power state, provider version, queue/coalescing policy, timestamp source/calibration, workload, samples, and native baseline with equivalent semantics. End-to-end latency reports each available milestone separately and never subtracts unrelated clock domains without calibration evidence.

