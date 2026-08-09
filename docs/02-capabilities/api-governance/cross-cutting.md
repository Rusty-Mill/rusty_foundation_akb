# Cross-cutting qualities

**RM-API-GOV-CROSS-0001:** Authentication, authorization, tenant/purpose boundaries, delegated authority, field-level disclosure, audit, and abuse controls are contract semantics and compatibility inputs.

**RM-API-GOV-CROSS-0002:** Sensitive fields, examples, errors, traces, generated logs, registries, consumer inventories, and replay corpora apply classification, minimization, redaction, retention, deletion, and access policy.

**RM-API-GOV-CROSS-0003:** Contracts define bounded sizes, depths, cardinalities, query complexity, concurrency, buffering, timeouts, and resource budgets; unbounded generator or parser behavior is nonconforming.

**RM-API-GOV-CROSS-0004:** Client-facing documentation and diagnostics are localizable and accessible; machine identifiers remain stable while human text may vary by locale.

**RM-API-GOV-CROSS-0005:** Telemetry correlates contract/operation/deployment generations, outcome, latency, size, retries, throttling, deprecation use, and compatibility cohort without making logs an effect authority.

**RM-API-GOV-CROSS-0006:** Async APIs expose cancellation, deadlines, streaming, and backpressure. Sync counterparts are complete where blocking is meaningful and do not create hidden runtimes.
