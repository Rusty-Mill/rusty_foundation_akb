# ADR-0073: Activation acceptance is not handler completion

**Status:** Accepted  
**Date:** 2026-08-08

## Context

An OS broker may accept a launch request while showing a chooser, starting or routing to an app, crossing a sandbox portal, or failing later. Many mechanisms provide no end-to-end acknowledgment. Process creation, foreground focus, window appearance, and elapsed time cannot prove that the target was received, opened, or acted upon.

## Decision

Activation results are milestone- and boundary-scoped: validation, resolution, user choice, broker acceptance, process/instance routing, app receipt, readiness, target open, and domain handled remain distinct. Providers report only evidenced milestones. Unknown delivery stays unknown; retries require explicit duplicate/side-effect policy. Application-defined acknowledgment is a separate optional protocol.

## Consequences

- APIs cannot return an unqualified `opened = true`.
- Cancellation cannot recall delivered activation or reverse handler effects.
- Products needing workflow completion use a cooperative protocol rather than observing processes or windows.
