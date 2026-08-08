# ADR-0004: Authoritative architecture model

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

The foundational architecture existed across the charter, principles, overview, capability model, graph model, profiles, governance, ecosystem, delivery, and evidence documents. Each contained useful detail, but no single document stated the complete current model or defined precedence. Readers could not identify one authoritative answer, and duplicated rules could drift.

## Decision

Maintain `docs/01-architecture/architecture-model.md` as the normative source of truth for the current Rusty Mill architecture. It consolidates system boundaries, layers, entities, dependencies, contracts, profiles, execution semantics, quality obligations, governance, evidence, ecosystem, and delivery constraints.

Supporting documents elaborate focused subjects. Accepted ADRs preserve decision rationale. RFCs propose changes. When wording conflicts, the architecture model governs unless a later accepted ADR explicitly supersedes the relevant rule.

Architecture changes update the decision record, authoritative model, and affected elaborations together.

## Options considered

### Distributed authority

Keep each focused document independently normative.

**Advantages:** Shorter documents and local ownership.  
**Disadvantages:** Ambiguous precedence, duplication, difficult onboarding, and drift.

### Generated model

Generate one model from machine-readable fragments.

**Advantages:** Automated consistency.  
**Disadvantages:** Prematurely commits to tooling and schema before the information model is proven.

### Hand-maintained authoritative model

Use one reviewed Markdown model with linked elaborations.

**Advantages:** Immediately understandable, reviewable, and version-controlled without new tooling.  
**Disadvantages:** Requires disciplined synchronization and periodic contradiction checks.

## Consequences

- Readers have one canonical architecture entry point.
- Some intentional summary-level duplication remains, but precedence is explicit.
- Model changes require greater review discipline.
- Machine-readable generation may replace manual synchronization later without changing authority semantics.

## Verification

- Documentation indexes link to the model first.
- Supporting model documents carry authority notices.
- Internal-link and contradiction checks are part of documentation review.
- Future architecture changes identify the exact model sections affected.

The model uses a combination of a reusable SVG for the stable architecture pyramid and Mermaid for evolving relationships, flows, and lifecycles. Normative prose and tables remain the accessible source when a renderer is unavailable.
