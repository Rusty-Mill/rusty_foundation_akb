# Certificate, trust-store, and PKI-validation benchmark specification

| Benchmark | Measures |
|---|---|
| Parsing | cold/warm certificate/bag parse latency, bytes/second, allocations/peak memory and rejection cost by size/complexity |
| Trust snapshot | cold/warm store enumeration/index/build/update latency, item count, memory, privacy-filter and generation-publication cost |
| Path construction | latency, candidates/signatures/paths explored, memory and bound activation across linear, cross-signed, ambiguous and hostile graphs |
| Validation | per-path and full-result latency by depth, algorithms, extensions, policy/name constraints, purpose and identity matching |
| Revocation/network | stapled/cache/online/offline latency, requests/bytes/redirects, concurrency/deduplication, responder failure and hard/soft policy |
| Cache | result/intermediate/status hit rate and latency, dependency invalidation, memory/storage, store/policy/clock update convergence |
| Concurrency | validations/second, queue/fairness, provider/network saturation, cancellation and resource-bound recovery |
| Lifecycle | trust update to revalidation, anchor/distrust/pin rotation, certificate/status expiry storm, provider restart and shutdown cleanup |

Results report p50/p95/p99/max and distributions for parse/build/validate/status/network stages, paths/candidates/signature operations, requests/bytes, cache hit/miss/age, allocations/memory, CPU, queue occupancy, cancellation and bound/failure counts. Runs disclose machine/OS/build, provider/library/version, trust-store sources/item count/generation, certificate/path corpus, policy/purpose/identity, clock/time, network/proxy/cache/revocation mode, warmup, concurrency, and raw measurement method. A faster incomplete path or disabled status check is not a performance win and must be reported as a different policy.
