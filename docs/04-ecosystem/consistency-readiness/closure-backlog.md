# Consistency and readiness closure backlog

This backlog is bounded to architecture-definition readiness. Provider implementation and release evidence remain deliberately downstream.

| ID | Priority | Finding | Closure evidence | State |
|---|---|---|---|---|
| CR-001 | High | Individual capability requirements do not yet map directly to stable assertion identifiers repository-wide. | Mappings now cover audit evidence, runtime/time, windowing, messaging/RPC, and application synchronization; close after reviewed bidirectional mappings cover every domain. | In progress |
| CR-002 | High | Dependency statements are primarily prose and cannot yet be checked repository-wide for cycles or profile satisfiability. | The [partial source-linked graph](dependency-graph.md) and validator establish the rules; close after stable nodes/edges and profile resolution cover every promoted capability. | In progress |
| CR-003 | High | Shared entity vocabulary has not received a repository-wide collision and authority review. | The [canonical vocabulary](vocabulary.md) and [contradiction ledger](contradiction-ledger.md) establish roles and findings; close after every domain is reviewed against them. | In progress |
| CR-004 | Medium | Domain status metadata was not uniformly machine-readable. | All 62 domain README records now use the canonical table-form status field without changing maturity. | Closed |
| CR-005 | Medium | Benchmark scenarios lack stable semantic identities and requirement links repository-wide. | Messaging/RPC, application synchronization, and audit evidence now have exact maps under the [benchmark traceability model](benchmark-traceability.md); migrate remaining domains and legacy suite IDs. | In progress |
| CR-006 | Medium | Most normative external sources lack freshness/obsolescence review records. | The generated inventory and [source freshness model](source-freshness.md) establish 620+ source records and a reviewed core frontier; close after risk-prioritized sources have authority/version/impact/expiry evidence. | In progress |
| CR-007 | Medium | Cross-cutting coverage is described per domain but not fully reviewed in a gap matrix. | The generated [domain-by-quality matrix](quality-matrix.md) distinguishes dedicated from embedded-unreviewed analysis and preserves unknowns; close after exact-source reviews. | In progress |
| CR-008 | Medium | Draft-to-Experimental evidence has not been assessed domain by domain. | Promotion-gate scorecard with evidence links and explicit non-promotion conclusions. | Open |

The next closure order is CR-001/CR-002/CR-003, because direct traceability, dependencies, and shared semantics can invalidate conclusions drawn by the lower-priority reports.
