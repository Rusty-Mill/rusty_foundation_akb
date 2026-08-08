# ADR-0059: Notification actions are untrusted activation

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Notification responses may arrive after content changes, expiry, process restart, instance redirection, duplication, or external payload manipulation. System presentation authenticates neither the current domain state nor the authority to execute an operation.

## Decision

Default taps, buttons, and text responses enter as untrusted typed lifecycle activations. The application validates notification/action revision, freshness, schema, replay/idempotency, current state, authority, and required confirmation before invoking the same domain command path used by other interfaces.

## Consequences

- Destructive or sensitive actions cannot bypass confirmation/authentication.
- Cold-start and running-instance responses share one semantic path.
- Stale and duplicate responses converge safely.
