# Pipeline, processing, and export

## Platform service

The telemetry pipeline service composes event production, filtering, sampling, transformation, buffering, and one or more exporters.

**RM-OBSERVE-PIPELINE-0001:** Producers depend on the portable event sink contract, never a native facility, collector daemon, vendor SDK, network endpoint, or serialization protocol.

**RM-OBSERVE-PIPELINE-0002:** Pipeline configuration is an immutable revisioned snapshot. Reconfiguration swaps generations; records accepted by an old generation follow its declared drain/drop policy.

**RM-OBSERVE-PIPELINE-0003:** Every queue and batch is bounded by record count and bytes. Overflow policy is explicit per event class and reports aggregate loss without recursively generating unbounded telemetry.

**RM-OBSERVE-PIPELINE-0004:** Filtering and sampling occur only after fields needed for security/privacy classification are known. Tail-based or cross-record sampling is a separate service quality that declares memory and latency bounds.

**RM-OBSERVE-PIPELINE-0005:** Export failure cannot block unrelated application work indefinitely. Retry uses bounded storage, backoff, cancellation, expiry, and shutdown budgets; retained data has explicit protection and deletion policy.

**RM-OBSERVE-PIPELINE-0006:** Export acknowledges acceptance, durable local persistence, remote receipt, and backend indexing as distinct milestones. No adapter claims a stronger milestone than it can prove.

**RM-OBSERVE-PIPELINE-0007:** Shutdown defines a bounded flush attempt and an exact terminal report of exported, retained, expired, filtered, sampled, and dropped records. Flush is not a guarantee against process termination or system failure.

**RM-OBSERVE-PIPELINE-0008:** Exporters preserve stable schema identity, units, correlation, sensitivity decisions, and loss metadata or disclose a typed degradation.

