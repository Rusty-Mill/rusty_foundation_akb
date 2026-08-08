# Benchmarks and relevance evaluation

**RM-SEARCH-BENCH-0001:** Benchmarks publish hardware/OS/provider/version/region, topology/shards/replicas, schema/analyzers/models/index algorithms, corpus and query/judgment provenance, tenant/security mix, warmup, cache state, refresh/merge policy, load, repetitions, and uncertainty.

**RM-SEARCH-BENCH-0002:** Ingestion reports documents/bytes/tokens/vectors per second, CPU/memory/disk/network/GPU/cost, source-to-accepted/durable/replicated/visible/converged latency distributions, backfill, update/delete, merge, and pressure/failure behavior.

**RM-SEARCH-BENCH-0003:** Query reports end-to-end and stage latency distributions, throughput, fanout, timeouts/partials, CPU/memory/disk/network/GPU/cost under cold/warm, mixed query, aggregation, highlighting, pagination, hot-term, and adversarial loads.

**RM-SEARCH-BENCH-0004:** Approximate retrieval reports recall@k against exact neighbors, precision@k, candidate/fusion/rerank depth, filter selectivity, index build/size, update visibility, nondeterminism, latency/resource distributions, and tail failures.

**RM-SEARCH-EVAL-0001:** Relevance evaluation binds immutable corpus/query/judgment/policy/model generations, assessors and agreement, sampling, intent/locale/device/accessibility segments, leakage controls, metrics such as precision/recall/MRR/nDCG, confidence intervals, and regression thresholds.

**RM-SEARCH-EVAL-0002:** Offline judgments, interleaving, A/B tests, clicks, dwell, reformulation, abandonment, and task success remain distinct biased evidence; no single engagement metric defines relevance or user benefit.

**RM-SEARCH-EVAL-0003:** Evaluation reports protected-group and language/script coverage, zero-result and harmful-result analysis, position/presentation bias, privacy/legal basis, guardrail metrics, and rollback criteria.

**RM-SEARCH-BENCH-0005:** Migration/recovery trials measure rebuild/catch-up, dual-index overhead, alias switch, snapshot restore, source reconstruction, failover/failback, relevance parity, and RPO/RTO under realistic concurrent query/ingest load.

**RM-SEARCH-BENCH-0006:** Faster, higher-engagement, or higher-recall results that violate authorization, completeness claims, freshness, resource limits, accessibility, privacy, or reproducibility are failures.
