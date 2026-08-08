# Pagination, facets, and highlighting

**RM-SEARCH-PAGE-0001:** Stable multi-page traversal binds a point-in-time view, immutable query/ranking/sort policy, page size, and opaque authenticated cursor containing the last complete deterministic sort tuple.

**RM-SEARCH-PAGE-0002:** Offset pagination is bounded and explicitly permits drift/duplicates/omissions under mutation unless paired with a stable view; deep offsets cannot consume unbounded coordinator memory/CPU.

**RM-SEARCH-PAGE-0003:** Cursors are bearer-like continuation authority scoped to principal/tenant/query/view, expiry, direction, and page limits; they reveal no sensitive key, score, shard, or query data without protection.

**RM-SEARCH-PAGE-0004:** Aggregations/facets declare domain/filter scope, exact versus approximate counts, sampling/error bounds, missing/other buckets, ordering, cardinality precision, time zone/calendar, and partition coverage.

**RM-SEARCH-PAGE-0005:** Aggregations over partial search cannot appear complete; per-bucket approximation and failed partitions remain visible.

**RM-SEARCH-HIGHLIGHT-0001:** Highlighting binds analyzer, source/stored/term-vector provenance, matched query clauses, fragment policy, locale, encoding, offsets, truncation, and HTML/text output escaping.

**RM-SEARCH-HIGHLIGHT-0002:** Highlight fragments are untrusted derived presentation, may be incomplete or semantically misleading, never grant authority, and preserve accessibility through readable non-markup content and language/direction metadata.

**RM-SEARCH-PAGE-0006:** Suggestions, autocomplete, spelling, and related-query features are separately identified result types with privacy, popularity-bias, freshness, abuse, and evaluation policy.
