# ADR-0065: Print completion is boundary-scoped evidence

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Applications, renderers, spoolers, servers, printers, finishing units, and users observe different boundaries. A native `completed` state may mean data processing or queue completion and cannot universally prove that every intended mark reached the correct sheet, finishing succeeded, output remained private, or the intended user collected it. Failures and lost responses also make submission ambiguous.

## Decision

Every print milestone names its reporting boundary and provenance. Provider completion, counters, receipts, and device status are evidence with declared quality, not universal proof of physical or semantic output. Ambiguous submission remains unknown; retry requires explicit duplicate policy and a new linked attempt identity.

## Consequences

- User messages say what is known—such as “submitted” or “queue reports completed”—instead of “printed” without stronger evidence.
- Cancellation and retry expose partial/duplicate-output risk.
- Regulated workflows need a separate attestation, secure-release, accounting, or human-confirmation service.
