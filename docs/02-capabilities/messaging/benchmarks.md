# Messaging and RPC benchmark specification

**RM-MESSAGING-BENCH-0001:** Benchmarks publish hardware, OS/provider/compiler/runtime/protocol/broker/schema builds, topology, security, persistence/replication/settlement, payload/schema distributions, concurrency, limits, impairment, clocks, samples, variance, and raw results.

**RM-MESSAGING-BENCH-0002:** Workloads cover unary and all streaming RPC forms, small/large/attachment messages, cold/warm channels and schemas, publish/consume and fanout, partitions/consumer groups, volatile/durable/replicated modes, transactions, acknowledgments, retries/redelivery/dedup, and graceful drain.

**RM-MESSAGING-BENCH-0003:** Report end-to-end and boundary-specific latency distributions, goodput, serialization/validation/compression cost, queue/flow/handler/domain/settlement time, CPU, allocations/copies, memory/disk/network high-water, replication, batching, wakeups, energy, and telemetry overhead.

**RM-MESSAGING-BENCH-0004:** Saturation/fairness varies tenants, priorities, payload sizes, streams/subscriptions/partitions, one large flow among small flows, slow consumers, poison messages, retry storms, rebalances, broker/server failover, and backpressure while reporting tail latency and rejected/dropped work.

**RM-MESSAGING-BENCH-0005:** Durability/delivery experiments include fsync/quorum boundaries, acknowledgment timing, transaction commit, crash/power/failover, redelivery, dedup retention, inbox/outbox relay, ambiguous results, reconciliation, backlog recovery, and storage amplification. Weaker persistence cannot win silently.

**RM-MESSAGING-BENCH-0006:** Provider and Rusty Mill paths use identical schema validation, security/authority, transport/broker qualities, payload semantics, flow/resource limits, retry/dedup policy, observability, and completion boundaries. Generated-code and warm-cache advantages are disclosed separately.

