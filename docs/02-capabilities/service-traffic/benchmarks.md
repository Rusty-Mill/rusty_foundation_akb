# Benchmarks

**RM-TRAFFIC-BENCH-0001:** Benchmarks publish hardware/OS/provider/version/regions, service/endpoint/topology/fault domains, protocols/connections, discovery/control source, route/balancer/health/retry/admission policy, load/cost distributions, security, warmup, repetitions, and uncertainty.

**RM-TRAFFIC-BENCH-0002:** Steady-state trials measure discovery/route/pick overhead, connection/auth/reuse, request/stream latency and throughput, fairness/skew, queues, CPU/memory/network, cross-zone/region, energy, and cost across endpoint and concurrency scales.

**RM-TRAFFIC-BENCH-0003:** Churn trials add/remove/restart/reweight/drain endpoints, update subsets/routes/security, change networks, and scale rapidly while reporting propagation, stale attempts, reconnects, remapping, errors, and convergence.

**RM-TRAFFIC-BENCH-0004:** Overload trials vary slow/error/large/multiplexed requests, hot affinity keys, partial capacity, probes, retries/hedges, queues/circuits/outliers, and report offered/admitted/shed/amplified work plus useful throughput and tail latency.

**RM-TRAFFIC-BENCH-0005:** Failure trials interrupt DNS/registry/control/client/proxy/endpoint/network/zone/region/security at each milestone and measure detection, decision, propagation, reroute, recovery/failback, availability, effect duplicates/ambiguity, and resource surge.

**RM-TRAFFIC-BENCH-0006:** Progressive-delivery trials measure allocation accuracy over time/request/session units, cold starts, health guardrails, shadow overhead, rollback propagation, mixed generations, and statistically justified conclusions.

**RM-TRAFFIC-BENCH-0007:** Faster results that weaken original authority, tenant isolation, health/partial evidence, attempt/effect budgets, fairness, propagation truth, accessibility, or cleanup are failures.
