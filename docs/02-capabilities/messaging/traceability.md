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
