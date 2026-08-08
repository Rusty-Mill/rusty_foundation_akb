# Conformance

**RM-CACHE-CONFORMANCE-0001:** Common suites test canonical keys, every declared variant/partition, collisions, Unicode/case/query/header normalization, sensitive-key redaction, and schema migration.

**RM-CACHE-CONFORMANCE-0002:** Deterministic clock suites test age/freshness/expiry, validators, heuristic prohibition, skew/jumps/suspend, stale modes, disconnected operation, authorization revocation, and partial responses.

**RM-CACHE-CONFORMANCE-0003:** Concurrency suites test collapse compatibility, mixed cancellation/deadlines, old-fill overwrite prevention, hot keys, admission/eviction pressure, poison recovery, and bounded origin amplification.

**RM-CACHE-CONFORMANCE-0004:** Tier suites inject disk corruption/crash/full storage, serialization changes, distributed partition/failover/ambiguous writes, promotion/demotion, encryption/key rotation, and startup/shutdown recovery.

**RM-CACHE-CONFORMANCE-0005:** Invalidation suites test exact/prefix/tag/dependency/epoch scope, authorization, races with fills and mutations, provider partial failure, delayed nodes, offline clients, reclamation, and nonclaims about already-served copies.

**RM-CACHE-CONFORMANCE-0006:** Edge suites test routing/key policy, viewer/origin identity, compression/transformation/ranges, signed access, origin shield, retry amplification, failover, regional propagation, privacy, and logs.

**RM-CACHE-CONFORMANCE-0007:** Cross-cutting suites test tenant isolation, timing/key probes, decompression/deserialization limits, accessibility, locale variants, telemetry cardinality/redaction, and cleanup.

**RM-CACHE-CONFORMANCE-0008:** Provider reports publish unsupported semantics, emulations, weaker guarantees, configuration prerequisites, measurements, costs, and waivers; aggregate hit ratio cannot substitute for correctness cases.
