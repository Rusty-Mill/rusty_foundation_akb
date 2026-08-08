# Schema, mappings, and analysis

**RM-SEARCH-SCHEMA-0001:** Field definitions name logical type, cardinality, null/missing/empty distinctions, stored/source/doc-value/indexed forms, normalization, analyzer, positions/offsets/payloads, sort/aggregate eligibility, and limits.

**RM-SEARCH-SCHEMA-0002:** Text analysis is a versioned pipeline of character normalization, tokenization, token filters, dictionaries, stemming/lemmatization, stop words, synonyms, case/diacritics, script/language policy, and emitted position/offset semantics.

**RM-SEARCH-SCHEMA-0003:** Query-time and index-time analysis differences are explicit and conformance-tested; changing either can alter match sets, phrase behavior, highlighting, and ranking.

**RM-SEARCH-SCHEMA-0004:** Numeric, temporal, boolean, keyword, geo, vector, nested/object, relation, and binary metadata types preserve exact unit, precision, coordinate reference, dimensionality, similarity, nesting, and coercion policy.

**RM-SEARCH-SCHEMA-0005:** Dynamic fields/mappings are disabled by default at untrusted boundaries or constrained by allowlists, depth/field/cardinality limits, type-conflict policy, and versioned review.

**RM-SEARCH-SCHEMA-0006:** Synonym, dictionary, morphology, embedding model, quantization, stop-word, and locale resources are immutable generation-addressed inputs with provenance, licensing, rollout, rollback, and evaluation evidence.

**RM-SEARCH-SCHEMA-0007:** Schema compatibility classifies query-compatible additions, reindex-required changes, destructive changes, mixed-generation behavior, and rollback limits.
