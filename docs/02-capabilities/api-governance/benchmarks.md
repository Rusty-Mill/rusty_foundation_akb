# Benchmarks

**RM-API-GOV-BENCH-0001:** Measure parse/validate/serialize and generated-adapter overhead by payload shape, size, field count, nesting, unknown fields, encoding, allocation, copies, and concurrency.

**RM-API-GOV-BENCH-0002:** Measure unary and streaming end-to-end latency/throughput, first/last item, backpressure, cancellation, retries, compression, connection reuse, and tail behavior separately by binding.

**RM-API-GOV-BENCH-0003:** Measure registry resolution, lint, compatibility analysis, generation, documentation, and conformance time against contract graph size and cache state.

**RM-API-GOV-BENCH-0004:** Measure pagination stability, filter/query cost, idempotency-store contention, quota enforcement, webhook redelivery, long-running watch/poll load, and telemetry overhead.

**RM-API-GOV-BENCH-0005:** Report warmup, distributions, confidence, CPU/memory/network, artifact size, dependency/tool versions, representative workloads, faults, and correctness assertions. Comparisons never trade away semantic equivalence silently.
