# Messaging and RPC conformance specification

**RM-MESSAGING-CONFORMANCE-0001:** Reports bind schema/IDL/compiler/runtime/protocol/provider/broker builds, interaction profiles, client/server/producer/consumer roles, topology/transports/proxies, identity/authority/tenant, limits, clocks, fixtures, fault schedule, and canonical causal traces.

**RM-MESSAGING-CONFORMANCE-0002:** Schema matrices cover old/new producer/consumer directions; binary/text/JSON differences; presence/defaults; unknown fields/enums/unions; reserved/reused tags; type/range/unit changes; canonicalization; invalid/nested/oversize input; registry rollback/freeze/cache; and semantic-validation failures.

**RM-MESSAGING-CONFORMANCE-0003:** RPC tests cover unary and all streaming cardinalities, metadata, compression, flow control, half-close, status/details, deadline propagation/skew, cancellation at every milestone, client/server divergent terminals, load balancing/failover, partial request/response, and overload/drain.

**RM-MESSAGING-CONFORMANCE-0004:** Broker tests cover routing/filtering, partitions/order, durability/replication, settlement dispositions, ack leases, expiry/priority, redelivery/dead letters, consumer groups/rebalance/fencing, transactions/uncertain commit, failover/split brain, admin isolation, and resource exhaustion.

**RM-MESSAGING-CONFORMANCE-0005:** Replay tests fault every boundary before/during/after send, broker acceptance, replication, delivery, handler/domain commit, response, acknowledgment, and cleanup; they verify attempt lineage, unknown effect, no unsafe automatic retry, dedup races/expiry/collision, inbox/outbox recovery, hedging, and reconciliation.

**RM-MESSAGING-CONFORMANCE-0006:** Security/privacy tests cover cross-tenant/topic/operation authority, credential/context forwarding, reply injection, SSRF, schema/parser confusion, poison/compression/resource attacks, sensitive logging/dead letters/dedup stores, trace baggage, accessible diagnostics, and denial-of-service fairness.

**RM-MESSAGING-CONFORMANCE-0007:** Crash/power/network/clock/provider faults occur across clients, servers, brokers, schema registries, dedup/inbox/outbox/domain stores, relays, and consumers under restart/failover/restore/upgrade/rollback with invariant and residual-state checks.

**RM-MESSAGING-CONFORMANCE-0008:** Cross-platform/provider differential tests compare canonical semantic/evidence traces across in-process, IPC, HTTP, real-time, selected RPC, and selected broker bindings; unsupported qualities remain explicit and no adapter may strengthen a native guarantee.

