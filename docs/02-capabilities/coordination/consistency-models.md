# Consistency and read/write semantics

**RM-COORDINATION-CONSISTENCY-0001:** A consistency claim names objects/keys/ranges/transactions, operation semantics, client/session/process scope, invocation/response and commit boundaries, replica/configuration scope, failure model, real-time/causal/session ordering, and allowed histories/anomalies.

**RM-COORDINATION-CONSISTENCY-0002:** Linearizable, sequential, serializable, strict-serializable/external, snapshot, repeatable-read, read-committed, causal, monotonic-read/write, read-your-writes, bounded-staleness, eventual/convergent, and local-cache claims remain distinct and are never summarized as `strong`.

**RM-COORDINATION-CONSISTENCY-0003:** Read results include requested/effective consistency, data version/index/timestamp/vector, replica/leader/quorum path, snapshot/transaction, staleness bound or estimate, cache, clock uncertainty, configuration, and warnings/unknowns.

**RM-COORDINATION-CONSISTENCY-0004:** Conditional writes bind expected version/value/fence/schema and atomically report applied/current/conflict/unknown under the selected model. Compare-and-swap cannot safely coordinate external effects that do not enforce the resulting generation.

**RM-COORDINATION-CONSISTENCY-0005:** Causal context and version vectors are bounded typed evidence with actor/incarnation identity, merge/dominance/concurrency semantics, compaction, forged-context protection, and privacy. Wall-clock timestamps or trace order cannot substitute for causality.

**RM-COORDINATION-CONSISTENCY-0006:** Convergent replicated types declare algebra, payload/state/op delta form, delivery assumptions, duplicate/reorder handling, tombstones, actor retirement, causal context, conflict policy, bounds, garbage collection, schema evolution, and irreconcilable states.

**RM-COORDINATION-CONSISTENCY-0007:** Stale/local/eventual reads cannot authorize destructive, exclusive, billing, security, uniqueness, or irreversible operations unless a product proves a safe monotonic/fenced design under the declared staleness and partition model.

**RM-COORDINATION-CONSISTENCY-0008:** Session guarantees are scoped to an exact client/session token and storage domain; reconnect, failover, cache eviction, restored snapshot, credential/tenant change, and token loss expose downgrade or fail rather than silently resetting history.

