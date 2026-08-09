# ADR-0142: Provider acceptance is not recipient delivery

- **Status:** Accepted
- **Date:** 2026-08-08

## Context

Email, SMS, and push providers commonly return success when they accept or queue a request. Downstream relays, carriers, push services, devices, operating systems, clients, spam filters, expiration, collapse, user preferences, and offline state still determine later outcomes.

## Decision

Rusty Mill records every communications milestone at its exact evidence boundary. Provider acceptance never becomes recipient delivery, presentation, human reading, comprehension, response, or domain-effect completion. Unknown remains unknown.

## Options considered

- Treat successful API response as delivered: easy but systematically false.
- Normalize every channel to one final state: convenient but discards native uncertainty.
- Preserve boundary-qualified milestones: honest and testable; selected.

## Consequences

APIs, dashboards, conformance, and objectives use explicit denominators and confidence. Callback/reconciliation infrastructure is required. Products choose which boundary satisfies a business need without strengthening its meaning.
