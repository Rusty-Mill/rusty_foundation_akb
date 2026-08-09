# Messaging and RPC assertion traceability

**Status:** Draft assertion mapping  
**Authority:** [Messaging and RPC domain](README.md)

| Assertion | Covered normative source files | Verification intention |
|---|---|---|
| `rm.assertion.messaging.schema-envelope@1` | `schema-envelope.md` | Verify schema identity/evolution, envelope identity, provenance, bounded decoding, unknown fields, and hostile inputs. |
| `rm.assertion.messaging.interaction@1` | `interaction-model.md`, `rpc.md` | Verify unary/streaming interaction roles, deadlines, cancellation, progress, errors, readiness, authorization, and effect boundaries. |
| `rm.assertion.messaging.streaming@1` | `streaming.md` | Verify directionality, ordering, half-close, flow control, cancellation, partial progress, and bounded resource use. |
| `rm.assertion.messaging.delivery-settlement@1` | `delivery-settlement.md`, `pubsub-broker.md` | Verify broker acceptance, delivery, visibility/lease, settlement, redelivery, ordering, consumer groups, fanout, and rebalance evidence. |
| `rm.assertion.messaging.replay-effects@1` | `retries-idempotency.md` | Fault retry/redelivery/deduplication/outbox/inbox/reconciliation boundaries and preserve attempt versus logical-effect identity. |
| `rm.assertion.messaging.qualities@1` | `cross-cutting.md`, `traceability.md` | Verify security, privacy, accessibility, i18n, observability, performance, operational policy, and traceability governance. |

**RM-MESSAGING-TRACE-0001:** Every messaging/RPC capability requirement MUST map to a stable semantic assertion before Experimental promotion.

**RM-MESSAGING-TRACE-0002:** Executable cases MUST state transport/broker/provider topology, fault schedule, schema generations, delivery/settlement policy, attempt/effect identity, and observation frontier.

**RM-MESSAGING-TRACE-0003:** A case MUST NOT infer exactly-once effects from exactly-once transport, broker settlement, deduplication, or a successful RPC response.

## Benchmark scenarios

| Scenario | Benchmark requirements | Comparison contract |
|---|---|---|
| `rm.benchmark.messaging.environment@1` | `RM-MESSAGING-BENCH-0001` | Pin topology, builds, security, persistence, payload distribution, limits, impairment, clocks, samples, variance, and raw artifacts. |
| `rm.benchmark.messaging.workload-matrix@1` | `RM-MESSAGING-BENCH-0002` | Exercise RPC forms, payload classes, cold/warm paths, publish/consume/fanout, partitions/groups, durability, transactions, acknowledgements, retries, and drain. |
| `rm.benchmark.messaging.boundary-cost@1` | `RM-MESSAGING-BENCH-0003` | Measure end-to-end and boundary latency, goodput, codec/validation/queue/handler/settlement cost, resource high-water marks, energy, and telemetry. |
| `rm.benchmark.messaging.saturation-fairness@1` | `RM-MESSAGING-BENCH-0004` | Vary tenants, priorities, sizes, flows, slow/poison consumers, retries, rebalances, failover, and backpressure with rejection/drop accounting. |
| `rm.benchmark.messaging.durability-recovery@1` | `RM-MESSAGING-BENCH-0005` | Compare fsync/quorum/ack/transaction boundaries under crash, failover, redelivery, dedup, outbox/inbox, ambiguity, reconciliation, and recovery. |
| `rm.benchmark.messaging.native-equivalence@1` | `RM-MESSAGING-BENCH-0006` | Compare native/provider and Rusty Mill paths only under equivalent schema, security, durability, flow, retry, observability, and completion semantics. |
