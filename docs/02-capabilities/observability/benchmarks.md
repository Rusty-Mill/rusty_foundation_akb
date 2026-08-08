# Observability and diagnostics benchmark specification

| Workload | Metrics |
|---|---|
| Disabled event | nanoseconds, branches, allocations, code-size impact |
| Enabled event | producer latency distribution, allocations, encoded bytes |
| Context propagation | derive/inject/extract latency and allocation |
| Metrics | update latency, contention, collection/export cost, cardinality memory |
| Spans | start/event/end latency, sampled versus nonrecording overhead |
| Pipeline saturation | throughput, tail latency, queue bytes, loss/coalescing accounting |
| Export outage | application impact, spool growth, retry CPU/I/O, recovery convergence |
| Flush/shutdown | completion latency and record outcome counts by budget |
| Breadcrumb | write latency and contention under wraparound |
| Crash path | time to external capture completion, artifact size, successful-capture rate |
| Symbolication | artifacts/second, peak memory, resolved-frame ratio |

Benchmarks compare the portable producer path with an idiomatic native baseline under the same enabled/disabled policy and payload. They record hardware, OS/build, compiler/profile, event schema/payload, concurrency, buffer/export configuration, native facility, collector topology, storage, symbols, and statistical variance. Crash benchmarks execute sacrificial subprocesses and exclude launch time from capture latency where reported separately.

