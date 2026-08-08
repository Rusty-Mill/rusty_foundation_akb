# Signed-artifact benchmarks

**RM-SIGNED-BENCH-0001:** Measure parsing, hashing, signature verification, path/status evaluation, timestamp verification, transparency proof verification, provenance/SBOM parsing, and final policy evaluation separately and end to end.

**RM-SIGNED-BENCH-0002:** Scenarios cover small metadata, typical binaries/packages/bundles, large archives/images, many files/signatures/certificates/materials, cold/warm caches, offline/online status and log access, and adversarial limits.

**RM-SIGNED-BENCH-0003:** Report latency distributions, streaming first/result time, bytes hashed, throughput, peak/resident memory, allocations, CPU, network requests/bytes, cache hit provenance, cancellation latency, and cleanup.

**RM-SIGNED-BENCH-0004:** Signing benchmarks separate local software, hardware-backed, remote/HSM, approval, timestamp, transparency, and publication time. They report rate limits and ambiguous/retry outcomes without weakening controls for speed.

**RM-SIGNED-BENCH-0005:** Compare native verification, Rusty Mill adapter, and complete acceptance-policy paths only when guarantees and evidence are equivalent. Platform notarization/reputation network time is reported separately.

**RM-SIGNED-BENCH-0006:** Sustained and concurrent tests demonstrate bounded memory, fair work scheduling, bounded external requests, cache contention behavior, provider recovery, and no unbounded decompression or graph/path growth.

Initial budgets remain RFC-owned after representative Windows, Linux, and macOS baselines exist.

