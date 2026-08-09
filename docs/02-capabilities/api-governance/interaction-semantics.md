# Request, result, and interaction semantics

**RM-API-GOV-INTERACTION-0001:** Request contracts distinguish absent, null, default, empty, invalid, unknown, and redacted values and define normalization before authorization or idempotency comparison.

**RM-API-GOV-INTERACTION-0002:** Collection queries define filter grammar, sort keys and total ordering, field masks/projections, maximum complexity, authorization filtering, and stable point-in-time pagination or explicit drift semantics.

**RM-API-GOV-INTERACTION-0003:** Idempotency keys bind caller, operation, normalized request, retention window, result/effect identity, concurrent duplicate behavior, and mismatch rejection. Retryability is outcome-specific.

**RM-API-GOV-INTERACTION-0004:** Optimistic concurrency identifies the compared generation and reports conflicts without silently overwriting newer state.

**RM-API-GOV-INTERACTION-0005:** Errors have stable machine type/code, safe human detail, field/operation context, correlation identity, retry guidance, and cause policy. HTTP problem details and RPC statuses are bindings, not the domain error taxonomy.

**RM-API-GOV-INTERACTION-0006:** Long-running operations return stable operation identity, accepted authority and input generation, progress/result/error state, polling/watch semantics, cancellation request state, retention, and terminal effect evidence.

**RM-API-GOV-INTERACTION-0007:** Rate limits and quotas name subject, resource dimension, window/algorithm, observed usage, remaining/reset evidence, enforcement scope, retry policy, and whether charging follows attempts, accepted work, or effects.
