# ADR-0050: Device identity is generation-scoped evidence

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Windows device instances/interfaces/containers, Linux sysfs and device nodes, and macOS I/O Registry services name different kinds of objects. Paths and identifiers can be reused; serials may be absent, duplicated, privacy-sensitive, or report a component rather than a whole physical product.

## Decision

Portable device references identify one provider object generation within an observation scope. Persistent or cross-provider matching is an explicit evidence-based policy that exposes confidence and ambiguity. No individual native identifier or property is universal physical identity, and identity never conveys authority.

## Consequences

- Removal/republication and material uncertainty invalidate prior references.
- Products must define confirmation/fallback policy for saved-device preferences.
- Class-specific opens revalidate generation and authority.
