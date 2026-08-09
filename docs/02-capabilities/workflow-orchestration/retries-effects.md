# Retries, idempotency, fencing, and effects

**RM-WORKFLOW-EFFECT-0001:** Each retry is a new attempt linked to one logical activity intent. Policy binds retryable outcomes, maximum attempts/time, backoff/jitter, non-retryable errors, expiration, authority freshness, target generation, and duplicate-effect risk.

**RM-WORKFLOW-EFFECT-0002:** Activity timeout, cancellation, worker loss, transport failure, or missing heartbeat does not prove the external effect did not occur. Ambiguous attempts reconcile by stable target operation identity before retry where possible.

**RM-WORKFLOW-EFFECT-0003:** Durable idempotency records are domain state atomically related to the protected effect, with collision/abuse controls, in-progress ownership/fencing, result replay, retention, replication, backup, and schema migration.

**RM-WORKFLOW-EFFECT-0004:** Exclusive activity or effect ownership uses resource-enforced fencing generations; coordinator leases or worker uniqueness alone cannot prevent stale external effects.

**RM-WORKFLOW-EFFECT-0005:** Exactly-once claims identify workflow state, activity result, message, and each external effect boundary separately. Replay-safe orchestration and idempotent activity dispatch do not prove exactly-once business effects.

**RM-WORKFLOW-EFFECT-0006:** Heartbeats/checkpoints carry bounded progress and cancellation hints, are monotonic within an attempt, and cannot claim committed external effect unless verified by the target boundary.
