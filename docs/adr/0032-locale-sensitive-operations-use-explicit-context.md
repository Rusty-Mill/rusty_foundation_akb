# ADR-0032: Locale-sensitive operations use immutable explicit context

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

Operating systems, POSIX, ICU, and Foundation expose mutable default locale/time-zone behavior with different scopes. Language, region, script, calendar, numbering, hour cycle, collation, measurement, resource matching, and time zone can vary independently and can change during a session. Ambient defaults make output nondeterministic, introduce concurrency hazards, and hide fallback/data versions.

## Decision

OS/user preferences are observed as versioned snapshots. Application policy resolves them with supported resources and exact Unicode/CLDR/tzdb/provider versions into an immutable locale context. Every locale-sensitive operation accepts that context explicitly. Updates create a new context and are committed through coordinated semantic/layout/accessibility state; code never mutates process-global locale to request behavior.

## Options considered

### Read platform defaults per call

Convenient but nondeterministic, race-prone, and impossible to reproduce exactly.

### One application-global current locale

Better consistency but still conflates services and prevents concurrent/per-document locales.

### Immutable explicit locale context

Makes preferences, fallback, actual service locales, data versions, caching, and transitions testable.

## Consequences

- APIs are more explicit and cache keys complete.
- Multiple windows/documents can use different contexts safely.
- OS preference changes require deliberate reformat/re-layout.
- Release evidence identifies exact resource and locale-data generations.

## Verification

Run concurrent contexts, mid-operation preference/data updates, per-service fallback, and deterministic replay across all providers.

