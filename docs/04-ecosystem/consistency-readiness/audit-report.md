# Architecture consistency and readiness audit report

**Status:** Generated evidence  
**Authority:** [Consistency and readiness model](README.md)  
**Generator:** `tools/akb_audit.py`  
**Index:** [Machine-readable inventory](index.json)

This report is deterministic and contains no claim that file presence proves semantic coverage.

## Inventory

| Measure | Result |
|---|---:|
| Markdown documents | 1,119 |
| Resolved internal links | 2,064 |
| Unique normative requirements | 5,193 |
| Capability domains | 62 |
| Indexed ADRs | 159 |
| External source URLs inventoried | 630 |
| External URLs with schema-valid domain review | 21 |
| Structural errors | 0 |
| Structural warnings | 0 |

## Artifact coverage

| Evidence | Domains | Coverage |
|---|---:|---:|
| Conformance specification present | 62 / 62 | 100.0% |
| Benchmark specification present | 62 / 62 | 100.0% |
| Direct requirement-to-assertion map | 5 / 62 | 8.1% |
| Direct benchmark-requirement-to-scenario map | 5 / 62 | 8.1% |

## Declared dependency graph

| Measure | Result |
|---|---:|
| Source-declared capability nodes | 15 |
| Source-declared typed edges | 8 |
| Required-edge graph acyclic | true |

Graph counts cover only explicit declarations. Missing nodes or edges are unknown, not proof of independence.

The first two rows prove specification presence only. The mapping rows prove complete planned links only for counted domains. None proves executable assertions, benchmark runs, passing provider results, or performance budgets.

## Cross-cutting analysis form

| Evidence form | Domains | Coverage |
|---|---:|---:|
| Dedicated `cross-cutting.md` | 27 / 62 | 43.5% |
| Embedded/unreviewed | 35 / 62 | 56.5% |

Keyword mentions are discovery hints only. The [quality matrix](quality-matrix.md) does not treat them as reviewed coverage.

## Findings

- Structural validation currently passes with 0 errors.
- Every capability domain has conformance and benchmark planning artifacts.
- 0 domain README files lack the canonical table-form status field; this is recorded as a migration-quality issue, not silently interpreted as Stable.
- 5 domain(s) have a complete direct planned requirement-to-assertion map; repository-wide migration remains open.
- 5 domain(s) have complete benchmark-requirement-to-scenario maps across 33 stable semantic scenarios; run evidence remains absent by design.
- 5 domain(s) have both complete planned assertion and benchmark traceability.
- 3 domain(s) are currently eligible for Experimental promotion; generated scorecards cannot authorize promotion.
- 3 domain(s) have schema-valid Proposed promotion reviews and 0 have Accepted reviews.
- Semantic contradiction review remains human-governed and is tracked in the [closure backlog](closure-backlog.md).

## Readiness conclusion

The knowledge base is **architecture-definition ready** and structurally indexable. It is **not implementation-release ready**: all domain analyses remain Draft, direct assertion traceability is incomplete repository-wide, provider/platform evidence does not yet exist, and benchmark baselines cannot exist before qualified implementations. These are explicit gates rather than defects hidden by a percentage.
