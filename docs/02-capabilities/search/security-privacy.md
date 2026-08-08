# Security, privacy, and multi-tenancy

**RM-SEARCH-SECURITY-0001:** Authorization is enforced before or within candidate retrieval using index/document/field/query/aggregation controls that cannot leak forbidden existence, counts, terms, scores, timing, highlights, suggestions, or cache state.

**RM-SEARCH-SECURITY-0002:** Tenant isolation binds document routing/index topology, aliases, caches, point-in-time views, models, logs, snapshots, quotas, and administrative operations; application-supplied filters alone are insufficient isolation for high-risk data.

**RM-SEARCH-SECURITY-0003:** Query DSL, analyzers, scripts, ingest processors, plugins, models, templates, synonyms, and snapshot inputs are untrusted or privileged according to explicit policy and constrained against injection, denial of service, and ambient access.

**RM-SEARCH-PRIVACY-0001:** Source text, tokens, term statistics, embeddings, queries, clicks/judgments, results, highlights, logs, traces, caches, and backups are classified, minimized, encrypted, retained, exported, and erased under governance.

**RM-SEARCH-PRIVACY-0002:** Erasure and access revocation propagate through source, capture backlog, active indexes, replicas, aliases, caches, snapshots, evaluation corpora, and derived models according to an evidence-bearing workflow with declared immutable/legal exceptions.

**RM-SEARCH-PRIVACY-0003:** Query and click analytics require purpose, consent/legal basis, aggregation thresholds, retention, anti-reidentification, administrator access, user controls, and exclusion from ranking/model training unless separately authorized.

**RM-SEARCH-SECURITY-0004:** Rate/admission policy bounds per-principal/tenant query concurrency, clauses, expansions, result depth, aggregations, vector work, scripts, ingest, refresh, snapshots, and administrative operations.

**RM-SEARCH-SECURITY-0005:** Search results are untrusted content for rendering and downstream retrieval-augmented systems; escaping, provenance, instruction/content separation, safety policy, and source revalidation occur at those boundaries.
