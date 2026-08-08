# Lexical and structured retrieval

**RM-SEARCH-LEXICAL-0001:** Typed lexical queries distinguish exact term, analyzed match, boolean, phrase/proximity, prefix, wildcard/regular expression, fuzzy, range, existence, nested/relation, and provider extension semantics.

**RM-SEARCH-LEXICAL-0002:** Expensive multi-term expansion, fuzzy distance, automata, clauses, nesting, joins, scripts, regexes, and leading wildcards require explicit bounded policy and admission.

**RM-SEARCH-LEXICAL-0003:** Boolean occurrence, minimum-match, phrase slop, field boosts, term statistics scope, similarity formula, coordination, tie breaking, and missing-field behavior belong to the versioned ranking contract.

**RM-SEARCH-LEXICAL-0004:** Filters are non-scoring predicates with explicit cacheability and authorization composition; post-filtering and pre-filtering expose different hit/aggregation semantics.

**RM-SEARCH-LEXICAL-0005:** Sorts define direction, type/coercion, missing values, multi-value reduction, locale/collation, geo distance, nested scope, stability, and a unique deterministic tie-breaker.

**RM-SEARCH-LEXICAL-0006:** Scripted/computed queries execute in constrained environments with typed inputs, resource limits, determinism/cache policy, no ambient authority, and audited provider escape hatches.

**RM-SEARCH-LEXICAL-0007:** Exact retrieval/completeness claims name query class, indexed fields, source watermark, partition success, total-hit tracking, and limits; top-k ranking alone is not exhaustive retrieval.
