# ADR-0153: Cross-cutting keywords are discovery, not coverage

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Automated scans can find words such as security, accessibility, performance, locale, telemetry, and recovery. Their presence does not show that the domain states a normative claim, evidence method, owner, or justified non-applicability.

## Decision

Generated keyword matrices are discovery evidence only. Cross-cutting coverage requires reviewed links to exact normative requirements, verification methods or non-applicability rationale, owners, and exceptions. Dedicated and embedded analysis remain distinguishable forms.

## Alternatives considered

- Mark any keyword occurrence as covered: rejected because it rewards superficial prose.
- Require a dedicated file in every domain: rejected because small domains may remain clearer with embedded analysis.
- Keep no aggregate view: rejected because omissions cannot be prioritized at repository scale.

## Consequences

- The matrix can route work without producing false green status.
- Embedded analysis needs explicit review links before promotion.
- A dedicated file improves discoverability but is not automatically sufficient.
