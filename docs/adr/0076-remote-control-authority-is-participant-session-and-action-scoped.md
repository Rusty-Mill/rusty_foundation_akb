# ADR-0076: Remote-control authority is participant-, session-, and action-scoped

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Remote assistance composes capture, media, networking, identity, and input mechanisms. A participant may be allowed to view one source without controlling it, or to point without typing, transferring data, elevating, or retaining access after reconnect. Treating a connected or authenticated peer as globally authorized collapses all of these boundaries.

## Decision

Remote-control authority is an explicit local grant binding authenticated participant and secure channel evidence to local login/security-context and capture-source generations, purpose, role, permitted device/action classes, visibility, lifetime, and revocation. View, control, clipboard, file transfer, elevation, and unattended access are independently selected. Policy is revalidated on participant, channel, source, session, privilege, or scope changes.

## Consequences

- Authentication and screen-view authority never imply input authority.
- Reconnect or participant replacement creates new generations rather than inheriting ambient control.
- Consent expansion is conspicuous and accessible; emergency local revocation closes admission first.
- Unattended operation requires a separate privileged profile and governance.
