# Query, ranking, and result contracts

**RM-SEARCH-QUERY-0001:** A query request binds domain/index aliases to resolved generations, point-in-time view or freshness requirement, tenant/principal/security context, typed query tree, ranking policy, projection, aggregation, sort, cursor, limits, deadline, and partial-result policy.

**RM-SEARCH-QUERY-0002:** Query parsing distinguishes syntax errors, unsupported constructs, type conflicts, unmapped fields, unauthorized fields, rejected expense, rewrite expansion, and provider translation loss.

**RM-SEARCH-RANK-0001:** Scores are meaningful only within an exact query, view, provider/index statistics, candidate set, similarity/fusion/reranker policy, and configuration generation.

**RM-SEARCH-RANK-0002:** Scores are not exposed as probabilities, confidence, semantic truth, quality, safety, popularity, or cross-query/provider comparable values unless a separately calibrated and validated contract establishes that meaning.

**RM-SEARCH-RANK-0003:** Ranking provides deterministic total ordering where pagination/replay requires it, including a stable unique tie-breaker; declared nondeterminism is bounded and excluded from stable cursor claims.

**RM-SEARCH-RESULT-0001:** Each hit binds document/source/index generation, tenant/security decision, matched clauses/fields where permitted, score/sort tuple, approximation and transformation evidence, and projected/stored/source field provenance.

**RM-SEARCH-RESULT-0002:** Total-hit results distinguish exact, lower-bound, estimated, unknown, and disabled counting with the threshold and partition coverage.

**RM-SEARCH-RESULT-0003:** Explanations/profiles are privileged diagnostic evidence, bounded and redacted; they are not stable APIs or proof of causal user relevance.

**RM-SEARCH-RESULT-0004:** Search responses do not authorize domain actions; callers revalidate source generation and current authority before consequential use.
