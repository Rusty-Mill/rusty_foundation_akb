# ADR-0099: Delivery acknowledgment is not domain effect

## Status

Accepted

## Context

Transports and brokers expose send completion, acceptance, replication, delivery, settlement, acknowledgments, offsets, and transactions. Applications then validate, authorize, execute, persist, publish follow-up work, and affect external systems. Collapsing these boundaries into at-most-once, at-least-once, or exactly-once labels hides the classic crash windows between domain commit and acknowledgment and overstates external effects.

## Decision

Rusty Mill records each transport, broker, consumer, handler, transaction, response, and domain milestone separately. Portable profiles do not promise exactly-once effects. A product may claim a precisely named effect boundary only when it specifies and proves the participating state stores, transaction/fencing/idempotency/deduplication mechanism, retention and recovery assumptions, reconciliation, and excluded effects.

## Consequences

- Acknowledgment APIs require exact delivery and boundary evidence.
- Unknown outcomes survive rather than becoming success or failure guesses.
- Inbox/outbox and deduplication become explicit domain infrastructure.
- Marketing-quality delivery labels cannot substitute for conformance evidence.

