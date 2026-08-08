# Conformance

**RM-SEARCH-CONFORMANCE-0001:** Ingestion suites test create/update/delete/tombstone ordering, duplicate/delayed changes, snapshot-to-stream handoff, bulk partial/ambiguous outcomes, poison quarantine, authorization changes, and source convergence.

**RM-SEARCH-CONFORMANCE-0002:** Schema suites use golden token/position/offset/vector/spatial corpora across languages/scripts, normalization, synonyms, morphology, malformed input, type limits, dynamic fields, and mixed generations.

**RM-SEARCH-CONFORMANCE-0003:** Visibility suites distinguish acceptance/durability/replication/refresh/source convergence and check read-your-write, monotonic, bounded-stale, point-in-time, partial-shard, partition, relocation, restart, and clock histories.

**RM-SEARCH-CONFORMANCE-0004:** Query suites cover every typed lexical/structured operator, rewrite/expense limits, filters, nested fields, sorts/tie breakers, exact totals, projections, scripts, malformed/unauthorized fields, and provider translation loss.

**RM-SEARCH-CONFORMANCE-0005:** Vector/spatial/hybrid suites cover dimensions/NaN/norm/model generations, exact reference neighbors, ANN recall distributions, filters and adversarial geometry, fusion/reranking attribution, nondeterminism, timeout/fallback, and resource bounds.

**RM-SEARCH-CONFORMANCE-0006:** Traversal suites mutate between pages and verify point-in-time cursor completeness/order, expiry/tamper/principal binding, aggregation exactness/error/partial state, and safe accessible highlighting.

**RM-SEARCH-CONFORMANCE-0007:** Security/privacy suites probe cross-tenant existence/count/score/timing/cache leakage, DSL/script/model/snapshot abuse, redaction/erasure through replicas/snapshots/evaluation sets, quotas, and result-content safety.

**RM-SEARCH-CONFORMANCE-0008:** Migration/recovery suites perform shadow evaluation, alias switch/rollback, mixed clients, cursor retirement, corrupt replica/snapshot, region failover/failback, full source rebuild, and relevance/security parity checks.

**RM-SEARCH-CONFORMANCE-0009:** Provider reports publish unsupported semantics, emulations, weaker guarantees, configuration prerequisites, version differentials, resource/cost measurements, and waivers.
