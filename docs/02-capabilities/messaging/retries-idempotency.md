# Retries, idempotency, deduplication, and reconciliation

**RM-MESSAGING-REPLAY-0001:** Every retry, hedge, redelivery, republish, and replay is a new attempt linked to one logical intent. Policy binds trigger/evidence, operation semantics, payload availability, deadline/attempt budget, backoff/jitter, destination generation, authority, and duplicate-effect risk.

**RM-MESSAGING-REPLAY-0002:** Idempotency is scoped to a named domain operation, principal/tenant, target resource/generation, canonical request semantics, deduplication key, validity window, concurrent duplicates, stored result/failure policy, authorization changes, and side effects. A transport method or message identifier is insufficient.

**RM-MESSAGING-REPLAY-0003:** Deduplication records are durable domain state with atomic relation to the protected effect, bounded retention/capacity, key collision/abuse controls, privacy, result replay, in-progress ownership/lease, crash recovery, replication, backup/restore, and policy migration.

**RM-MESSAGING-REPLAY-0004:** Inbox/outbox patterns declare source transaction, event identity, publication state, consumer checkpoint, atomic boundary, polling/relay leases, ordering, duplicate handling, cleanup, schema evolution, failover, and reconciliation. They do not make external effects transactional.

**RM-MESSAGING-REPLAY-0005:** Hedging requires separate authority because multiple handlers may execute concurrently. Winner selection and loser cancellation cannot erase committed loser effects; capacity, fairness, billing, deduplication, and audit impacts are explicit.

**RM-MESSAGING-REPLAY-0006:** Retryable classifications are profile- and operation-specific. Unavailable, overload, redirect/failover, refused stream, broker release, timeout, cancellation, transaction uncertainty, and malformed response are not universally replay-safe.

**RM-MESSAGING-REPLAY-0007:** Reconciliation reads authoritative domain state using the logical intent and attempt lineage, classifies not-applied/applied/partially-applied/conflicting/unknown, and chooses converge, compensate, retry, quarantine, or human review. Compensation is a new authorized effect, not rollback.

**RM-MESSAGING-REPLAY-0008:** “Exactly once” claims name the precise boundary, failure model, state stores, transaction/fencing/deduplication mechanism, retention and recovery assumptions, excluded external effects, conformance evidence, and invalidation conditions; otherwise the claim is prohibited.

