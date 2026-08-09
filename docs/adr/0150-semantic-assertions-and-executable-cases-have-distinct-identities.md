# ADR-0150: Semantic assertions and executable cases have distinct identities

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Early conformance specifications already reserve suite-local case identifiers such as `CT-TIME-MONO-001` and `WINDOW-001`. Repository-scale traceability also needs stable identities for portable semantic propositions that may require many cases across providers, platforms, environments, and fault schedules.

## Decision

`rm.assertion.<domain>.<scope>@<major>` identifies a portable semantic assertion. Suite-local case identifiers identify executable or review procedures. A case maps to one or more assertions and requirements; an assertion maps to one or more cases. Existing case identities remain reserved and are not renamed.

## Alternatives considered

- Rename all cases into the assertion namespace: rejected because it destroys historical identity and confuses proposition with procedure.
- Treat every case as a portable assertion: rejected because provider/environment variants and decomposed procedures multiply independently of semantics.
- Keep only requirement-to-case links: rejected because cross-suite coverage and semantic evolution would lack a stable aggregation identity.

## Consequences

- Existing conformance documents remain compatible.
- Results must record assertion, requirement, and case identities.
- Assertion-major evolution is independent from compatible case additions or implementation refactoring.
