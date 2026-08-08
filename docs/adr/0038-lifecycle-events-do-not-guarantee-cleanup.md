# ADR-0038: Lifecycle events do not guarantee cleanup opportunity

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Platforms may send cooperative termination queries, short final notifications, forced termination indications, or nothing before crash, resource-pressure kill, power loss, or administrative force. Treating a callback as guaranteed makes correctness depend on an event the OS may omit.

## Decision

Lifecycle contracts expose the exact observed request and deadline quality. Durable domain data is committed during normal operation. Cooperative requests may invoke orderly shutdown, but missing or forced termination is a supported outcome and no portable `will terminate` guarantee exists.

## Options considered

- Universal final callback: simple but false.
- Ignore lifecycle notifications: safe for durability but loses useful cooperation and UX.
- Explicit quality plus continuous persistence: truthful and permits bounded optimization.

## Consequences

- Products design crash-consistent persistence before lifecycle integration.
- Cleanup and telemetry flush remain best effort under external termination.
- Conformance must include absent callbacks and abrupt death.

