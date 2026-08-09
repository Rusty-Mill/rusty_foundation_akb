# ADR-0159: Domain readiness reviews use schema-validated Markdown

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill architecture governance

## Context

The runtime/time and application-synchronization pilots showed that common review artifacts can express the same gates across native and distributed domains. Merely detecting a `Pass` string, however, is too weak, while choosing a separate metadata serialization before more repository trials would violate existing deferral decisions.

## Decision

Use conventional authoritative Markdown artifacts with schema-validated fields, sections, dimensions, dates, evidence links, and decision boundaries. Generate indexes and scorecards from them. Keep generated eligibility distinct from human-governed maturity and trial authorization.

## Options considered

- Keep informal domain-specific prose: flexible but cannot fail closed or scale review consistently.
- Adopt YAML/TOML/JSON now: machine-friendly but prematurely selects a broader repository metadata format.
- Schema-validate Markdown conventions: preserves authority and reviewability while exposing enough structure for deterministic validation.

## Consequences

Domains gain a reusable template and stronger audit failures. Some review structure is intentionally uniform. Future machine-readable formats must project the same semantics and cannot silently become a second authority.

## Verification

The audit validates required metadata, dates/expiry, quality dimensions, source links, ownership sections, and Proposed promotion nonauthorization. Both pilot domains must pass; unreviewed domains remain unknown.

## Follow-up

- Scale review artifacts by thematic domain batch.
- Revisit external serialization only after the implementation-trial evidence required by RM-DEV-EVIDENCE-0005 exists.

