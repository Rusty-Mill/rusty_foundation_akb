# Architecture consistency and readiness audit report

**Status:** Generated evidence  
**Authority:** [Consistency and readiness model](README.md)  
**Generator:** `tools/akb_audit.py`  
**Index:** [Machine-readable inventory](index.json)

This report is deterministic and contains no claim that file presence proves semantic coverage.

## Inventory

| Measure | Result |
|---|---:|
| Markdown documents | 1,058 |
| Resolved internal links | 1,688 |
| Unique normative requirements | 4,931 |
| Capability domains | 62 |
| Indexed ADRs | 149 |
| Structural errors | 0 |
| Structural warnings | 0 |

## Artifact coverage

| Evidence | Domains | Coverage |
|---|---:|---:|
| Conformance specification present | 62 / 62 | 100.0% |
| Benchmark specification present | 62 / 62 | 100.0% |
| Direct requirement-to-assertion map | 1 / 62 | 1.6% |

## Declared dependency graph

| Measure | Result |
|---|---:|
| Source-declared capability nodes | 15 |
| Source-declared typed edges | 8 |
| Required-edge graph acyclic | true |

Graph counts cover only explicit declarations. Missing nodes or edges are unknown, not proof of independence.

The first two rows prove specification presence only. The third proves complete planned requirement-to-assertion mapping only for the counted domains. None proves executable assertions, passing provider results, or benchmark coverage.

## Findings

- Structural validation currently passes with 0 errors.
- Every capability domain has conformance and benchmark planning artifacts.
- 0 domain README files lack the canonical table-form status field; this is recorded as a migration-quality issue, not silently interpreted as Stable.
- 1 domain(s) have a complete direct planned requirement-to-assertion map; repository-wide migration remains open.
- Semantic contradiction review remains human-governed and is tracked in the [closure backlog](closure-backlog.md).

## Readiness conclusion

The knowledge base is **architecture-definition ready** and structurally indexable. It is **not implementation-release ready**: all domain analyses remain Draft, direct assertion traceability is incomplete repository-wide, provider/platform evidence does not yet exist, and benchmark baselines cannot exist before qualified implementations. These are explicit gates rather than defects hidden by a percentage.
