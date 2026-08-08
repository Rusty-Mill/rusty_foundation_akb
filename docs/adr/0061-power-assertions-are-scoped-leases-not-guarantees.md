# ADR-0061: Power assertions are scoped leases, not guarantees

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Windows Power Requests, Linux inhibitor locks, and macOS power assertions/activities can defer selected automatic power actions, but targets, privilege, override, expiry, lifecycle, and user-visible policy differ. None prevents abrupt suspension, shutdown, battery exhaustion, lid/policy action, or failure.

## Decision

Portable power assertions are narrow, purpose-bound, attributed, time-bounded leases with explicit effective state and automatic owner-lifetime release. Display, automatic system sleep, idle, shutdown delay, and other targets remain separate. Correctness assumes any lease can be denied, degraded, overridden, expired, or invalidated.

## Consequences

- Long-running work checkpoints and remains interruption-safe.
- Products request only the minimum target for a user-visible need.
- Leaked or indefinite background assertions are conformance failures.
