# Benchmarks

**RM-APP-AUTHZ-BENCH-0001:** Point-check benchmarks report model/language/provider, policy/rule/entity/relation sizes, request mix, cold/warm cache, dependency reads, consistency, local/remote topology, CPU, allocation, memory, requests, throughput, and p50/p95/p99 latency.

**RM-APP-AUTHZ-BENCH-0002:** Relationship benchmarks vary objects/subjects/tuples, branching/depth/cycles/hotspots, rewrites/set operations, consistency tokens, cache/index state, traversal limits, check/expand/effective-access mixes, tail latency, and amplification.

**RM-APP-AUTHZ-BENCH-0003:** Filter/batch benchmarks report candidate and authorized cardinality, selectivity, query complexity, index strategy, pages/facets/counts, point-check equivalence sampling, snapshot mutations, overfetch, round trips, memory, throughput, and leakage assertions.

**RM-APP-AUTHZ-BENCH-0004:** Mutation/revocation benchmarks report grant/deny/relation/role/policy changes, fan-out, distribution and invalidation topology, accepted-to-check and accepted-to-effect convergence, stale permits/denies, cache churn, backlog, retries, and residuals.

**RM-APP-AUTHZ-BENCH-0005:** Administration/simulation benchmarks report policy size/dependencies, validation/compile/test/change-analysis corpus, rollout scope, mixed generations, rollback, effective-access graph size, explanation/proof cost, memory, latency, and reviewer artifact size.

**RM-APP-AUTHZ-BENCH-0006:** End-to-end benchmarks separately report authentication/token parsing, context/entity acquisition, decision, obligations, native/domain enforcement, commit, visibility, and audit overhead under concurrency, faults, privacy redaction, and accessibility instrumentation.
