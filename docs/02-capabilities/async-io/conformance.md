# Asynchronous I/O conformance specification

| Area | Required evidence |
|---|---|
| Lifecycle | immediate/deferred completion equivalence, exactly-once terminalization, drop/detach policy, generation/ABA defense |
| Progress | zero/partial/full, EOF, would-block retry, message boundaries, concurrent operation restrictions |
| Readiness | level/edge/one-shot, drain/rearm, stale/duplicate/coalesced events, error/hangup, multiple consumers |
| Cancellation | before/during/after native issue, normal-completion race, partial progress, unsupported cancel, buffer/control-block lifetime |
| Registration | descriptor/handle reuse, deregistration race, close, duplicate/transfer/inheritance, fork/provider restart |
| Load | queue saturation, bounded memory/threads/batches, hot-resource fairness, reserved recovery capacity |
| Runtime | executor migration/drop, wake coalescing, UI/run-loop affinity, callback reentrancy, no hidden runtime/pumping |
| Shutdown | stop admission, mass cancellation, drain, stuck driver/blocking fallback, late completions, terminal report |
| Observability | causal stages, aggregate loss/saturation, recursion safety, redacted identities, timing boundary accuracy |

Model tests generate submission, readiness, completion, cancellation, timeout, close, deregistration, and shutdown interleavings and assert one terminal outcome plus lifetime invariants. Fault injection includes queue-full, interrupted syscalls, spurious readiness, duplicate/stale completions, driver delay, executor stall, memory pressure, and clock discontinuity.

Reports bind OS/kernel/build, provider mode, supported operation/resource matrix, queue and batch bounds, polling/thread strategy, executor, CPU/power conditions, filesystem/network/device type, and every fallback or cancellation nonclaim.
