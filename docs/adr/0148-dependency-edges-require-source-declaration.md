# ADR-0148: Dependency edges require source declaration

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Mermaid diagrams, prose links, profiles, data flows, and co-location often show relationships without proving that one capability's minimum contract depends on another.

## Decision

The derived capability graph includes an edge only when the source capability specification declares its type, target, condition, and rationale. Absence means undeclared or unknown, not independent. Service/profile composition remains a separate graph view.

## Alternatives considered

- Infer edges from links or diagrams: rejected because arrow direction and intent vary.
- Treat all cross-references as optional dependencies: rejected because references also express examples, evidence, authority, or related work.
- Delay all graph validation: rejected because even partial declared graphs can catch cycles and invalid endpoints.

## Consequences

- The first graph is deliberately partial but trustworthy.
- Domain owners must promote implicit dependencies into explicit records.
- Automation can validate declared structure without inventing architecture.
