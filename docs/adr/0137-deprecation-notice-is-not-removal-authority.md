# ADR-0137: Deprecation notice is not removal authority

- **Status:** Accepted
- **Date:** 2026-08-08

## Context

A version annotation, warning, header, or sunset date can notify consumers but cannot prove that an alternative exists, consumers received notice, migrations completed, or remaining use is acceptable.

## Decision

Deprecation is a governed migration workflow. Removal requires recorded readiness evidence and accountable authorization; notices and dates are inputs, never authority by themselves.

## Consequences

The platform needs consumer inventory, privacy-safe use telemetry, migration status, exception handling, and emergency-retirement policy. Retirement can be delayed or deprecation withdrawn when evidence is insufficient.
