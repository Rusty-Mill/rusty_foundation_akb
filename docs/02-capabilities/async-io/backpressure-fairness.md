# Backpressure and fairness

Every stage is bounded: submitted operations, kernel queue entries, registered resources, readiness retry budget, completion batches, wake queues, blocking fallbacks, and retained buffers.

**RM-ASYNC-LOAD-0001:** Providers MUST publish hard or configured bounds and return explicit saturation/backpressure before unbounded memory or thread growth.

**RM-ASYNC-LOAD-0002:** Submission saturation MUST distinguish retryable capacity pressure from unsupported operation, resource failure, shutdown, and authority denial.

**RM-ASYNC-LOAD-0003:** Completion draining and readiness retry MUST use bounded batches/work budgets so a hot resource cannot indefinitely starve timers, cancellation, control work, or other tenants.

**RM-ASYNC-LOAD-0004:** Fairness quality MUST name the scope—operation, resource, tenant, priority class, or engine—and disclose nonclaims. FIFO queueing does not imply FIFO completion or scheduling.

**RM-ASYNC-LOAD-0005:** Priority/QoS MAY affect service policy but MUST NOT silently reorder domain operations whose contract requires ordering.

**RM-ASYNC-LOAD-0006:** Overload telemetry MUST be aggregate and bounded; instrumentation cannot create a second unbounded queue or include unrestricted resource identifiers.

Admission policy may reserve capacity for cancellation, shutdown, and recovery so overload cannot prevent the operations needed to converge safely.
