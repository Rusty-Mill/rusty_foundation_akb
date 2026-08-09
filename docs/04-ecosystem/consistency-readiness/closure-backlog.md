# Consistency and readiness closure backlog

This backlog is bounded to architecture-definition readiness. Provider implementation and release evidence remain deliberately downstream.

| ID | Priority | Finding | Closure evidence | State |
|---|---|---|---|---|
| CR-001 | High | Individual capability requirements do not yet map directly to stable assertion identifiers repository-wide. | The [audit-evidence pilot](../../02-capabilities/audit-evidence/traceability.md) proves the identity and expansion scheme; close after reviewed bidirectional mappings cover every domain. | In progress |
| CR-002 | High | Dependency statements are primarily prose and cannot yet be checked for cycles or profile satisfiability. | Derived typed graph with source links, cycle validation, and exception process. | Open |
| CR-003 | High | Shared entity vocabulary has not received a repository-wide collision and authority review. | Canonical vocabulary index, explicit homonyms/mappings, and reviewed contradiction ledger. | Open |
| CR-004 | Medium | Domain status metadata is not uniformly machine-readable. | Canonical metadata convention and migrated domain README records without changing maturity. | Open |
| CR-005 | Medium | Benchmark scenarios exist but lack stable scenario identifiers and requirement links. | Scenario-ID convention, direct links, environment schema, and representative generated matrix. | Open |
| CR-006 | Medium | Normative external sources have no generated freshness/obsolescence ledger. | Source inventory with authority, version/date, affected documents, review date, and replacement status. | Open |
| CR-007 | Medium | Cross-cutting coverage is described per domain but not summarized in a gap matrix. | Domain-by-quality matrix with exact sources, `unknown` states, and owned gaps. | Open |
| CR-008 | Medium | Draft-to-Experimental evidence has not been assessed domain by domain. | Promotion-gate scorecard with evidence links and explicit non-promotion conclusions. | Open |

The next closure order is CR-001/CR-002/CR-003, because direct traceability, dependencies, and shared semantics can invalidate conclusions drawn by the lower-priority reports.
