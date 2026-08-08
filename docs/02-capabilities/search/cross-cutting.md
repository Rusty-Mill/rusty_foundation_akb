# Cross-cutting qualities

**RM-SEARCH-XCUT-0001:** Security defaults deny dynamic privileged features, cross-tenant queries, partial authorization, unrestricted scripts/regex/vector work, raw diagnostics, and unverified snapshot/model/configuration inputs.

**RM-SEARCH-XCUT-0002:** Performance budgets cover ingest-to-visible latency, query planning/rewrite, shard fanout, candidate retrieval/reranking, serialization/network, page/aggregation/highlight work, cache/warmup, merge/recovery, memory/disk/CPU/GPU, energy, and provider cost.

**RM-SEARCH-XCUT-0003:** Accessibility supports keyboard and assistive navigation, result count/partial/stale/loading state, meaningful ordering and filter announcements, non-color-only highlights, reduced motion, readable snippets, and controllable result updates.

**RM-SEARCH-XCUT-0004:** Internationalization binds document/query language detection evidence, analyzers, scripts, segmentation, normalization, collation, morphology, transliteration, synonyms, locale-aware fields, directionality, and cross-language behavior without claiming universal equivalence.

**RM-SEARCH-XCUT-0005:** Observability records domain/index/view/configuration generations, tenant-safe query fingerprint/class, plan/rewrite, partitions, candidate stages, approximation, hit relation, latency/resource/cost, timeouts/partial state, ingestion watermark, and causal context without raw sensitive content.

**RM-SEARCH-XCUT-0006:** Metrics distinguish index acceptance, durability and visibility lag; query success and completeness; latency and relevance; exact and approximate work; and source/index convergence with bounded cardinality.

**RM-SEARCH-XCUT-0007:** Shutdown and upgrades drain or cancel queries/ingest, preserve acknowledged boundaries, expire or transfer view/cursor authority explicitly, finish or recover migrations, and reconcile ambiguous mutations.
