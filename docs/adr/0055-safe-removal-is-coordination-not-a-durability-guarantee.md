# ADR-0055: Safe removal is coordination, not a durability guarantee

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Operating systems can request client quiescence, flush caches, unmount filesystems, and ask a device to eject, but physical unplug and power loss remain possible. Filesystems, controllers, bridges, and media expose different durability guarantees, and veto mechanisms cannot ensure continued presence.

## Decision

Safe removal is an observable staged coordination service: quiesce, requested durability, unmount, and native eject/removal request. Results report completed stages, vetoes, skipped work, and current observed state. Success cannot strengthen underlying durability or guarantee against surprise removal.

## Consequences

- Force removal requires explicit authority and data-loss acknowledgment.
- Applications still design for sudden disappearance and ambiguous writes.
- User interfaces communicate milestones and safe-to-remove evidence precisely.
