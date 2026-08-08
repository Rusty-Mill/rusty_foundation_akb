# ADR-0077: Injected input is a privileged attributed side effect

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Native injection APIs insert events into platform input paths with different integrity, session, focus, compositor, accessibility, and secure-input restrictions. They may partially accept a sequence, route it to an unexpected target after a focus race, or make it indistinguishable from physical input to applications. Replaying remote events does not reproduce user intent or application state.

## Decision

Every remote event is untrusted intent validated into a short-lived, generation-bound native injection command. Rusty Mill preserves participant and virtual-device attribution internally, validates again at execution, models key/button/contact state, and treats native acceptance as boundary-scoped evidence only. Injection cannot authorize secure attention, credentials, consent, elevation, domain actions, or another capability.

## Consequences

- Partial, blocked, stale, unsupported, rate-limited, and unknown outcomes remain distinct.
- Focus, coordinate, keymap, and session changes retire incompatible queued input.
- Revocation attempts bounded release/cancel but reports residual state ambiguity.
- Applications cannot rely solely on the OS event stream to identify remote origin.
