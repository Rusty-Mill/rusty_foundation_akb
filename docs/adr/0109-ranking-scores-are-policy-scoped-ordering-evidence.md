# ADR-0109: Ranking scores are policy-scoped ordering evidence

## Status

Accepted

## Context

Lexical scores depend on corpus statistics and similarity formulas; vector scores depend on embedding spaces, metrics, quantization, and approximate candidate sets; hybrid and learned ranking transform or fuse them again. Raw values can change with refresh, shard statistics, provider versions, query rewrites, models, and candidates. Presenting them as portable confidence or comparing them across queries/providers is misleading.

## Decision

Rusty Mill scopes every score to the exact query, search view, candidate set, provider/statistics boundary, and versioned ranking/model policy. Scores provide ordering evidence only. Probability, confidence, calibration, cross-query comparison, or semantic-quality meaning requires a separate validated contract. Stable traversal adds deterministic tie breakers independent of equal scores.

## Consequences

- Result contracts expose ranking provenance and approximation.
- Hybrid fusion and reranking are explicit versioned stages.
- Provider score differences are expected rather than normalized deceptively.
- Product relevance requires corpus- and task-specific evaluation.
