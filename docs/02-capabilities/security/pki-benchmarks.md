# Certificate, trust-store, and PKI-validation benchmark specification

| ID | Benchmark | Measures |
|---|---|---|
| PKI-BENCH-001 | Parsing | cold/warm certificate/bag parse latency, bytes/second, allocations/peak memory and rejection cost by size/complexity |
| PKI-BENCH-002 | Trust snapshot | cold/warm store enumeration/index/build/update latency, item count, memory, privacy-filter and generation-publication cost |
| PKI-BENCH-003 | Path construction | latency, candidates/signatures/paths explored, memory and bound activation across linear, cross-signed, ambiguous and hostile graphs |
| PKI-BENCH-004 | Validation | per-path and full-result latency by depth, algorithms, extensions, policy/name constraints, purpose and identity matching |
| PKI-BENCH-005 | Revocation/network | stapled/cache/online/offline latency, requests/bytes/redirects, concurrency/deduplication, responder failure and hard/soft policy |
| PKI-BENCH-006 | Cache | result/intermediate/status hit rate and latency, dependency invalidation, memory/storage, store/policy/clock update convergence |
| PKI-BENCH-007 | Concurrency | validations/second, queue/fairness, provider/network saturation, cancellation and resource-bound recovery |
| PKI-BENCH-008 | Lifecycle | trust update to revalidation, anchor/distrust/pin rotation, certificate/status expiry storm, provider restart and shutdown cleanup |

## Comparison requirements

**RM-PKI-BENCH-0001:** Parse comparisons MUST bind identical exact bytes/object type, parser/profile/update set, structural limits, valid/malformed/ambiguous classification, original signed-byte retention, cold/warm state, and evidence output.

**RM-PKI-BENCH-0002:** Trust-snapshot/cache/lifecycle comparisons MUST bind identical provider/store scopes, sources/precedence, anchors/distrust/constraints/overrides, item classes/counts, privacy policy, generations, entries/age/partition, dependency changes, invalidation/revalidation, and terminal state.

**RM-PKI-BENCH-0003:** Construction/validation comparisons MUST bind identical leaf/candidate graph/provenance, trust snapshot, path/preference policy, purpose/reference identity, time/clock, algorithms/constraints/extensions, status inputs, bounds, expected path/rejection set, result category, warnings, unknowns, and nonclaims.

**RM-PKI-BENCH-0004:** Status/network/concurrency comparisons MUST bind identical signed status/freshness, network/DNS/proxy/redirect/SSRF/privacy policy, cache state, hard/soft failure rules, request/byte/concurrency bounds, fault/cancellation schedule, provider saturation, deduplication, fairness, and recovery.

**RM-PKI-BENCH-0005:** Every run MUST record RFC/profile/update/corpus versions, parser/provider/library artifact, OS/kernel/SDK, trust sources/snapshot/generation, policy/purpose/identity, clock/time, algorithm policy, status/network/cache, pins/overrides, toolchain/build, workload/concurrency, stages, samples/statistics, conformance result, and privacy/identity/authorization nonclaims.

**RM-PKI-BENCH-0006:** A baseline is equivalent only when it preserves parsing, path search/preference, trust/constraint/purpose/identity/algorithm/status policy, network/cache/failure, result evidence, bounds, and invalidation semantics; skipping checks or choosing an incomplete path is not a performance win, and numeric/native-performance claims require reviewed representative runs.

Results report p50/p95/p99/max and distributions for parse/build/validate/status/network stages, paths/candidates/signature operations, requests/bytes, cache hit/miss/age, allocations/memory, CPU, queue occupancy, cancellation and bound/failure counts.
