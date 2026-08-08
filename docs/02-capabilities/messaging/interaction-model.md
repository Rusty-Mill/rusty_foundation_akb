# Messaging interaction and capability model

**RM-MESSAGING-INTERACTION-0001:** Interaction kinds are command, query, event/fact, notification, unary request/response, client stream, server stream, bidirectional stream, publish, subscription, and control. Each declares initiator/responders, direction, cardinality, ordering, reply/acknowledgment, side-effect, replay, durability, and completion semantics.

**RM-MESSAGING-INTERACTION-0002:** An interaction intent binds stable operation/topic identity and revision, typed input/output/error schemas, audience/purpose, principal and authority, tenant/privacy partition, deadline, cancellation, priority, resource limits, delivery policy, idempotency/reconciliation policy, and transport constraints.

**RM-MESSAGING-INTERACTION-0003:** Logical interaction, transport attempt, broker delivery, consumer attempt, handler execution, domain transaction, and response/publication have separate immutable identities and causal links. Correlation identifiers are evidence, never authority or proof of uniqueness.

**RM-MESSAGING-INTERACTION-0004:** Authority attenuates per service/method/topic/partition/tenant/operation and direction. Discovery, schema possession, endpoint knowledge, subscription name, message identifier, reply address, or receipt grants no operation authority.

**RM-MESSAGING-INTERACTION-0005:** In-process, IPC, HTTP, WebSocket, SSE, WebTransport, and broker bindings are explicit adapters. A binding declares framing, metadata, ordering, flow control, cancellation, error, retry, durability, addressing, security, and failure evidence; fallback cannot silently change semantics.

**RM-MESSAGING-INTERACTION-0006:** Client accepted, encoded, locally queued, transport handed-off, peer/broker received, admitted, dispatched, handler started/returned, domain committed, reply published/received, acknowledged/settled, and externally observed are distinct milestones with boundary and provenance.

**RM-MESSAGING-INTERACTION-0007:** Async-first operations are bounded and cancellation-safe. Sync-complete equivalents use the same semantics and never create a hidden runtime, nested event loop, unbounded buffer, or implicit retry worker.

