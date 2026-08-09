# Security foundation benchmark specification

**Status:** Draft

## Principle

Performance evidence must never weaken source choice, fail-closed behavior, memory initialization, or diagnostic secrecy. Native baseline and Rusty Mill measurements use the same source semantics and build mode.

## Measurements

### Secure-random comparison requirements

- **RM-SECURITY-RANDOM-BENCH-0001:** Fill comparisons **MUST** bind the same approved OS source, provider initialization/readiness state, request sizes/chunking, exact-fill/failure semantics, memory policy, concurrency, and build mode.
- **RM-SECURITY-RANDOM-BENCH-0002:** First-use comparisons **MUST** separate provider construction, source readiness wait, first fill, cancellation, and failure boundaries and **MUST NOT** silently prewarm one candidate.
- **RM-SECURITY-RANDOM-BENCH-0003:** Failure comparisons **MUST** use controlled provider fault injection, confirm no usable partial output or fallback, and retain only sanitized non-output diagnostics.
- **RM-SECURITY-RANDOM-BENCH-0004:** Every run **MUST** record provider/module artifact and configuration, OS/kernel/SDK, hardware/virtualization/clone context, security mode, toolchain/build, request/concurrency matrix, warmup, samples/statistics, and conformance result without random-derived artifacts.
- **RM-SECURITY-RANDOM-BENCH-0005:** Numeric budgets and native-performance claims **MUST** derive from reviewed representative runs; statistical properties, uniqueness, checksums, compressibility, or provider names **MUST NOT** establish security or correctness.

| ID | Measurement | Required reporting |
|---|---|---|
| SEC-BENCH-001 | Warm fill latency at 0, 16, 32, 256, 4 KiB, 64 KiB, and 1 MiB | p50/p95/p99, throughput, CPU time, allocations |
| SEC-BENCH-002 | First-use/provider-initialization latency | Distribution, initialization path, source readiness state |
| SEC-BENCH-003 | Concurrent fill scaling | Threads/tasks, aggregate throughput, tail latency, contention indicators |
| SEC-BENCH-004 | Abstraction overhead against native source | Absolute delta and ratio by size; identical failure checks |
| SEC-BENCH-005 | Failure-path latency | Fault mechanism, diagnostic cost, confirmation of no output disclosure |
| SEC-BENCH-006 | Secret create/retrieve/replace/delete | Provider, item size/class, interaction state, warm/cold latency distributions |
| SEC-BENCH-007 | Secret-store contention and scale | Item count, concurrency, lookup mode, throughput, p95/p99, provider serialization |
| SEC-BENCH-008 | Scoped reveal and opaque-use overhead | Native baseline, exposure mode, copies, allocations, boundary transitions |

## Controls

Record hardware, virtualization, power policy, OS/kernel, security configuration, compiler/toolchain, artifact digest, warmup, sample count, and confidence interval. Never persist output buffers. A checksum or compressibility score of generated material is also prohibited because it unnecessarily derives data from secret-quality output.

Regression budgets remain unset until representative Windows, Linux, and macOS baselines exist. No single cross-platform latency budget is presumed.

Interactive prompt time is reported separately from provider processing and never included in an abstraction-overhead ratio. Benchmarks use generated ephemeral test values, destroy them under the provider's declared semantics, and never record values or secret-derived fingerprints.
