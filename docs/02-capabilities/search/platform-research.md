# Platform and provider research

## Embedded and database providers

- [SQLite FTS5](https://sqlite.org/fts5.html) exposes virtual-table full-text indexing, tokenizers, prefix indexes, BM25 ranking, highlighting/snippets, external-content modes, and consistency obligations between source tables and derived indexes.
- [PostgreSQL full-text search](https://www.postgresql.org/docs/current/textsearch.html) exposes parser/dictionary configurations, `tsvector`/`tsquery`, ranking, highlighting, and GIN/GiST indexes within database transaction semantics.
- Native Windows, Linux, and macOS indexing/search services may provide product/user search integrations, but do not define one portable application-owned schema, ranking, privacy, or visibility contract.

## Distributed providers

- [Elasticsearch near-real-time search](https://www.elastic.co/docs/manage-data/data-store/near-real-time-search) separates refresh/search visibility from durable commit; [point-in-time search and `search_after`](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-search.html) provide stable-view pagination primitives.
- [OpenSearch refresh](https://docs.opensearch.org/latest/api-reference/index-apis/refresh/) separates document acceptance from searchable segments; its lexical, vector, hybrid, security, replication, snapshot, and lifecycle features have provider- and version-specific behavior.

## Portability conclusions

**RM-SEARCH-RESEARCH-0001:** Portable contracts preserve source/index/view generations, semantic query intent, visibility, approximation, security, and result evidence rather than promising identical DSLs, token streams, scores, plans, or timing.

**RM-SEARCH-RESEARCH-0002:** Providers disclose analyzer/tokenizer behavior, mapping limits, refresh/commit/replication, point-in-time lifetime, total-hit and partial semantics, ranking/statistics scope, ANN algorithms, filter order, aggregations, cursor behavior, snapshots, and resource/cost limits.

**RM-SEARCH-RESEARCH-0003:** Provider extensions remain typed escape hatches with capability discovery, configuration generation, security review, conformance exclusions, and migration consequences.
