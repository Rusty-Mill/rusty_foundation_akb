# Audit-evidence assertion traceability

**Status:** Draft assertion pilot  
**Authority:** [Audit-evidence domain analysis](README.md) and [consistency/readiness model](../../04-ecosystem/consistency-readiness/README.md)

This pilot gives verification intentions stable identities without claiming executable provider evidence. Each table row covers every normative capability requirement declared in the named source files. The derived index expands those source sets to individual requirement records, making the mapping bidirectional and mechanically checkable.

## Assertion identity

Assertion identifiers use `rm.assertion.<domain>.<semantic-scope>@<major>`. Identity names the portable proposition being tested, not a test function, fixture, provider, operating system, or CI job. Compatible scenario additions retain the major; changed expected semantics require a new major and preserved migration record.

| Assertion | Covered normative source files | Verification intention |
|---|---|---|
| `rm.assertion.audit-evidence.schema@1` | `model.md`, `event-schema.md` | Validate evidence-class separation, stable identity, schemas, required/forbidden fields, hostile values, evolution, and canonical views. |
| `rm.assertion.audit-evidence.capture-effect@1` | `capture-boundaries.md`, `append-corrections.md` | Fault every capture/effect/append/correction boundary and verify exact durable, ambiguous, duplicate, orphan, and supersession states. |
| `rm.assertion.audit-evidence.sequence-completeness@1` | `sequence-time.md` | Exercise partitions, restarts, gaps, duplicates, reordering, clock uncertainty, causality, frontiers, reconciliation, and qualified completeness. |
| `rm.assertion.audit-evidence.integrity@1` | `integrity-proofs.md` | Mutate, delete, reorder, truncate, insert, fork, rotate, revoke, and partially validate evidence while preserving proof-scope nonclaims. |
| `rm.assertion.audit-evidence.privacy-retention@1` | `privacy-redaction.md`, `retention-holds.md` | Verify isolation, minimization, tokenization, disclosure, holds, rights, erasure, disposal, backup, and proof-survivability policy. |
| `rm.assertion.audit-evidence.assessment-reporting@1` | `query-reporting.md`, `controls-assessments.md`, `external-mappings.md`, `cases-incidents.md` | Verify privileged investigation, loss-aware export, control scope, sampling, findings, attestations, mappings, cases, expiry, and nonclaims. |
| `rm.assertion.audit-evidence.operations-qualities@1` | `operations-recovery.md`, `cross-cutting.md`, `platform-research.md`, `traceability.md` | Verify recovery/migration plus security, performance, accessibility, i18n, observability, provider/platform variance, and traceability-governance evidence. |

## Pilot rules

**RM-AUDIT-TRACE-0001:** Every capability requirement in this domain MUST map to at least one stable assertion identity before Experimental promotion.

**RM-AUDIT-TRACE-0002:** An assertion definition MUST state its semantic oracle, scenarios, fixtures, environment dimensions, required artifacts, and nonclaims before it can produce provider evidence.

**RM-AUDIT-TRACE-0003:** A source-set mapping is valid only while each listed file has one coherent verification scope; a requirement that needs a different oracle MUST receive an explicit assertion mapping rather than inherit an unsuitable file mapping.

**RM-AUDIT-TRACE-0004:** The mapping proves planned traceability only. It does not prove executable coverage, a passing provider, cross-platform conformance, or promotion readiness.
