# Quota admission, reservations, and enforcement

**RM-TENANT-GOV-QUOTA-0001:** Quota definitions bind resource dimension/unit, tenant/subject/resource scope, hard/soft/burst/reserved limits, window/reset, concurrency semantics, precedence, overage, borrowing, grace, consistency, enforcement points, and version.

**RM-TENANT-GOV-QUOTA-0002:** Capacity, entitlement allowance, safety limit, abuse rate limit, budget alert, and billable included quantity are separate controls even when they share a number.

**RM-TENANT-GOV-QUOTA-0003:** Admission atomically checks current policy/evidence and creates a bounded reservation or rejects with safe explanation. It records requested/granted quantity, scope, generation, expiry, fencing/idempotency, and consistency.

**RM-TENANT-GOV-QUOTA-0004:** Reservation, effect start, measured consumption, effect completion, release, expiration, reconciliation, and billing remain separate; crashes and ambiguous outcomes cannot leak quota indefinitely or double-spend silently.

**RM-TENANT-GOV-QUOTA-0005:** Distributed enforcement declares overshoot bound, partition behavior, escrow/lease allocation, staleness, fail-open/closed policy, fairness, and reconciliation. Approximate counters cannot claim exact hard quotas.

**RM-TENANT-GOV-QUOTA-0006:** Limit reductions state treatment of existing resources/reservations, draining/eviction, grandfathering, deadlines, protected workloads, notification, and appeal; new-admission denial does not imply existing consumption was removed.

**RM-TENANT-GOV-QUOTA-0007:** Quota exhaustion is not an authorization denial or billing failure. APIs expose typed retry/reset/upgrade/cleanup choices without leaking other tenants' usage or capacity.
