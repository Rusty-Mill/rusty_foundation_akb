# ADR-0072: Activation is untrusted intent, not authority

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Operating systems route files, URLs, notifications, share actions, commands, and custom protocol payloads from many origins. Paths, URIs, claimed types, source identities, association selection, and user gestures can be stale, spoofed, attacker-controlled, duplicated, or stripped of authority. Treating delivery as an authorized command would bypass normal domain security.

## Decision

Activation carries typed immutable intent plus provenance and only the explicit file/object capability supplied by a validated platform adapter. It is never itself authority. Incoming requests are untrusted, at-least-once inputs that revalidate schema, freshness, target generation, content/scheme policy, capability authority, replay/idempotency, state, and domain preconditions before ordinary command execution.

## Consequences

- URI activation never grants network, account, payment, messaging, or execution authority.
- File paths and type associations do not replace handle/object authority or parser validation.
- Notification and accessibility actions converge on the same domain command security path.
