# Delivery, acknowledgment, and settlement

**RM-MESSAGING-DELIVERY-0001:** Delivery quality is a vector: volatile/durable storage, accepted boundary, replication/quorum, ordering scope, attempt count, expiry, priority, routing, redelivery, acknowledgment/settlement mode, transaction, dead-letter policy, and evidence freshness. Scalar at-most/at-least/exactly-once labels are insufficient.

**RM-MESSAGING-DELIVERY-0002:** Producer accepted locally, broker accepted, durably stored, replicated, routed, delivered to consumer, consumer accepted/rejected/released/modified, acknowledged/settled, domain committed, and retention released are distinct milestones with named reporting boundary.

**RM-MESSAGING-DELIVERY-0003:** Producer, broker, and consumer settlement can be unsettled, accepted, rejected, released/requeued, modified, expired, dead-lettered, transactionally committed/aborted, unknown, or lost. Provider-specific states map without collapsing ambiguity.

**RM-MESSAGING-DELIVERY-0004:** Consumer acknowledgment authority binds exact delivery/message generation, subscription/partition, consumer/session, attempt, handler outcome, domain transaction evidence, and disposition. An acknowledgment token is opaque and cannot acknowledge another delivery.

**RM-MESSAGING-DELIVERY-0005:** Acknowledging before domain commit risks loss; after commit risks duplicate redelivery. Atomic consume-transform-produce or inbox/outbox patterns require a declared transaction boundary and recovery proof rather than an `exactly once` option.

**RM-MESSAGING-DELIVERY-0006:** Redelivery records original logical identity, delivery attempts, causes, delays, broker/consumer generations, prior dispositions, and effect ambiguity. Attempt counters are bounded hints because failover/retention can lose or change them.

**RM-MESSAGING-DELIVERY-0007:** Expiry, TTL, retention, scheduled availability, visibility/ack deadline, lease extension, and dead-letter timing use named clock domains and evidence. Expired messages may already have been delivered or acted upon.

**RM-MESSAGING-DELIVERY-0008:** Broker transactions declare resources/partitions included, isolation, producer fencing, consumer offsets/deliveries, timeout, commit evidence, uncertain outcome, failover/recovery, and external-system nonclaims.

