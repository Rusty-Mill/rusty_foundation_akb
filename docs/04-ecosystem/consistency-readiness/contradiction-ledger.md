# Cross-domain contradiction ledger

**Status:** Active reviewed evidence  
**Scope:** Architecture model 1.74.0 and domain sources through audit-evidence 0.1.0

The ledger records proposition-level review. “No contradiction found” is bounded to named sources and rules; it is not a repository-wide proof.

| ID | Proposition under review | Sources | Result | Disposition |
|---|---|---|---|---|
| CL-001 | Acceptance must remain distinct from effect completion. | [Architecture model](../../01-architecture/architecture-model.md), [API governance](../../02-capabilities/api-governance/README.md), [communications](../../02-capabilities/application-communications/README.md), [synchronization](../../02-capabilities/application-sync/README.md) | Consistent | Preserve boundary-qualified receipts and outcomes. |
| CL-002 | Evidence must not become domain truth or effect authority. | [Audit evidence](../../02-capabilities/audit-evidence/README.md), [workflow](../../02-capabilities/workflow-orchestration/README.md), [tenant governance](../../02-capabilities/tenant-service-governance/README.md), [repository operations](../repository-operations/README.md) | Consistent | Apply canonical `fact`, `event`, `evidence`, and `claim` roles. |
| CL-003 | Retry/replay must not imply safe repeated effects. | [Behavioral contracts](../../01-architecture/behavioral-contracts.md), [messaging/RPC](../../02-capabilities/messaging/README.md), [workflow](../../02-capabilities/workflow-orchestration/README.md), [communications](../../02-capabilities/application-communications/README.md) | Consistent | Preserve logical effect identity, attempts, idempotency, fencing, and reconciliation. |
| CL-004 | Corrections must preserve history and provenance. | [Audit evidence](../../02-capabilities/audit-evidence/append-corrections.md), [tenant metering](../../02-capabilities/tenant-service-governance/metering-events.md), [privacy](../../02-capabilities/privacy/retention-erasure.md), [analytics](../../02-capabilities/analytics/README.md) | Consistent with scoped tension | Erasure may remove protected material, but must leave policy-authorized evidence of action/nonavailability rather than silently rewrite unrelated facts. |
| CL-005 | Readiness/health observations must not authorize effects. | [Service traffic](../../02-capabilities/service-traffic/README.md), [lifecycle](../../02-capabilities/lifecycle/README.md), [background services](../../02-capabilities/background-services/README.md), [readiness model](README.md) | Consistent | Use expiring boundary scope and separate authorization. |
| CL-006 | Machine-readable representations must not fork Markdown authority during the foundation phase. | [RFC-0001](../../rfc/0001-capability-specification-system.md), [traceability](../traceability.md), [ADR-0146](../../adr/0146-machine-readable-indexes-are-derived-evidence.md) | Consistent | Keep generated records source-linked and fail on staleness. |
| CL-007 | Profile/version descriptions in the profiles catalog reflect current profile files. | [Profiles catalog](../../02-capabilities/profiles/README.md), [current profiles](../../02-capabilities/profiles/foundation-server.md) | Resolved | Catalog now names desktop 0.61.0, server 1.33.0, repository 0.29.0, and CA 0.28.0 and preserves product-choice nonclaims. |
| CL-008 | Existing conformance case identities and repository-scale semantic assertion identities can coexist without ambiguous authority. | [Runtime/time conformance](../../02-capabilities/runtime-time/conformance.md), [windowing conformance](../../02-capabilities/windowing/conformance.md), [audit traceability](../../02-capabilities/audit-evidence/traceability.md), [ADR-0150](../../adr/0150-semantic-assertions-and-executable-cases-have-distinct-identities.md) | Resolved | Preserve suite-local cases; map them beneath portable `rm.assertion.*` propositions and record all three identity layers in results. |

## Finding rules

**RM-READINESS-CONTRADICTION-0001:** Each entry MUST name the exact proposition, sources, review frontier, result, and disposition.

**RM-READINESS-CONTRADICTION-0002:** A contradiction is closed only by changing the conflicting authority, qualifying its scope, or recording an accepted decision; editorial similarity is insufficient.

**RM-READINESS-CONTRADICTION-0003:** New or changed normative sources invalidate affected `Consistent` entries until their frontier is reviewed.

**RM-READINESS-CONTRADICTION-0004:** Review tooling MAY propose candidate collisions, but a human-governed semantic review determines whether propositions actually conflict.
