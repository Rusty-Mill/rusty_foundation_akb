# Attempts, checkpoints, retries, and results

Each `ExecutionAttempt` has schedule/service, definition/package, principal/security-context, trigger/subscription, and attempt generations plus start evidence, deadline, budget, cancellation, checkpoint lineage, deduplication/work-claim identity, and terminal result.

**RM-BACKGROUND-ATTEMPT-0001:** `admitted`, `launch_requested`, `started`, `ready`, `work_claimed`, `checkpointed`, `side_effect_committed`, `completion_reported`, and `broker_acknowledged` MUST remain distinct milestones.

**RM-BACKGROUND-ATTEMPT-0002:** Exactly-once execution MUST NOT be claimed. Domain work requiring exactly-once effects uses transactional idempotency, durable claims, deduplication, and reconciliation at the authoritative data boundary.

**RM-BACKGROUND-ATTEMPT-0003:** Retry policy MUST classify failures, state whether an effect may have committed, bound attempts/time/backoff/jitter, respect deadline and policy, and route poison/permanent work to explicit terminal handling.

**RM-BACKGROUND-ATTEMPT-0004:** Cancellation, timeout, quota expiration, termination, crash, power loss, and broker loss do not prove rollback. Results report last durable checkpoint and effect ambiguity.

**RM-BACKGROUND-ATTEMPT-0005:** Checkpoints MUST be versioned, integrity-protected, bounded, principal/work/definition-bound, atomically published at their claimed durability, and compatible across an explicitly declared range.

**RM-BACKGROUND-ATTEMPT-0006:** Overlap policy MUST select prohibit, skip, queue boundedly, replace/cancel, or run concurrently with declared work partition and resource fairness.

**RM-BACKGROUND-ATTEMPT-0007:** Result retention, access control, redaction, expiration, and cleanup MUST be explicit. Broker status is not the application's durable result store.
