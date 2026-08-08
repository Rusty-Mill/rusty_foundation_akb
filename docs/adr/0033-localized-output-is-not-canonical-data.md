# ADR-0033: Localized output is not canonical data

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

Human-readable number, date, time, currency, unit, duration, message, and collated text changes with locale, user overrides, CLDR/tzdb/provider versions, context, precision, and style. Display formats can be ambiguous or lossy and do not universally round-trip. Reusing them as protocol/database/signature/identifier values causes corruption and security errors.

## Decision

Localized formatting is presentation only. Canonical serialization, protocol tokens, database values, identifiers, signatures, filesystem names, and security comparisons use separately specified locale-neutral semantic formats. Parsing is a separate strictness/ambiguity-bearing contract and is never inferred as the inverse of display formatting. Collation equality/order is not domain identity.

## Consequences

- Domain models retain typed values alongside display strings.
- Currency, units, zones, calendars, and precision remain explicit.
- Import fields state locale and parsing policy.
- UI/data boundaries become reviewable and testable.

