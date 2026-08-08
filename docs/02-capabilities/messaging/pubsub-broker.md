# Publish/subscribe and broker boundary

**RM-MESSAGING-BROKER-0001:** A broker profile binds product/protocol/version, namespace/virtual host, topic/queue/exchange/subscription semantics, routing/filter language and revision, partitioning, ordering, durability/replication, settlement, transactions, quotas, and management authority.

**RM-MESSAGING-BROKER-0002:** Topic, queue, subscription, consumer group, partition, routing key, filter, and reply destination are distinct typed resources with generation, owner, tenant, authorization, lifecycle, retention, and collision policy. User-controlled names are untrusted.

**RM-MESSAGING-BROKER-0003:** Publish binds exact destination generation, message/envelope schema, authority, partition/routing selection, ordering key, priority/expiry, durability, settlement, transaction, idempotency, and return/unroutable policy before bytes leave the producer.

**RM-MESSAGING-BROKER-0004:** Subscribe binds destination/filter generation, start position, snapshot/stream relation, consumer/group identity, exclusivity/sharing, prefetch/in-flight limits, acknowledgment/lease policy, redelivery/dead-letter, replay, and authorization.

**RM-MESSAGING-BROKER-0005:** Ordering is declared per message stream, producer epoch, session, partition, key, subscription, or transaction and may change across retry, failover, repartition, priority, expiry, dead-letter, or multiple consumers. No global order is inferred.

**RM-MESSAGING-BROKER-0006:** Consumer groups/load sharing expose assignment generation, rebalance/revoke/acquire, fencing, checkpoint/offset state, in-flight work, drain, duplicate window, and handoff evidence. Revocation can race handler/domain completion.

**RM-MESSAGING-BROKER-0007:** Broker discovery/failover preserves authenticated cluster identity, namespace, policy generation, endpoint provenance, partition leadership, consistency, split-brain/fencing, credential scope, and ambiguous publish/commit reconciliation.

**RM-MESSAGING-BROKER-0008:** Broker administration—create/delete/purge/move/replay/retention/ACL/schema/partition operations—is separately privileged from data publish/consume and uses immutable plans, impact previews, audit, idempotency, and recovery.

