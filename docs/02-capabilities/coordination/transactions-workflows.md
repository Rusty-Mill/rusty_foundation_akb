# Distributed transactions and workflows

**RM-COORDINATION-TXN-0001:** A transaction profile binds participants/resources, coordinator and transaction identity/generation, isolation/consistency, read/write sets or dynamic-enlistment rules, durability, locks/versions/fences, deadline, prepare/commit protocol, recovery, and external-effect exclusions.

**RM-COORDINATION-TXN-0002:** Begun, participant-enlisted, prepared, decision-durable, commit/abort sent, participant-applied, acknowledged, heuristic/in-doubt, forgotten, and externally reconciled are separate milestones. Coordinator response loss preserves uncertainty.

**RM-COORDINATION-TXN-0003:** Two-phase commit requires durable participant prepare state, stable coordinator decision, presumed-abort/commit policy, lock/resource limits, timeout behavior, coordinator failover, participant recovery, heuristic handling, and operator resolution; it does not remain available under every partition.

**RM-COORDINATION-TXN-0004:** A saga/workflow is a durable state machine of authorized steps and compensations with exact input/output schemas, preconditions, idempotency, deadlines, retries, human gates, causal attempt lineage, checkpoints, and reconciliation. It is not atomic isolation.

**RM-COORDINATION-TXN-0005:** Compensation is a new domain operation under current authority and state, can fail or be impossible, and may not erase observation, billing, messages, physical effects, or privacy disclosure. Compensated, partially compensated, conflicting, and manual-repair states remain visible.

**RM-COORDINATION-TXN-0006:** Orchestration and choreography profiles declare ownership, event ordering/delivery, duplicate/gap handling, versioned workflow definitions, concurrent transitions, migration, cancellation, timeout, observability, and termination detection.

**RM-COORDINATION-TXN-0007:** Transactional outbox/inbox composition declares the exact atomic local store boundary and fenced publisher/consumer ownership. Publication, broker settlement, remote domain commit, and external effects remain separate and reconciled.

**RM-COORDINATION-TXN-0008:** Distributed deadlock/livelock detection, victim selection, wound/wait policy, lease expiry, lock loss, retry, starvation, and fairness are profile-specific; timeout alone does not prove a deadlock or release external authority.

