# Asynchronous I/O errors and observability

Portable infrastructure failures include invalid operation/resource generation, unsupported asynchronous mode, admission saturation, provider unavailable, registration failure, cancellation unsupported/failed-to-request, deadline policy failure, completion corruption, and shutdown. Domain/native failures remain attached without becoming raw portable semantics.

**RM-ASYNC-ERROR-0001:** Submission failure and terminal operation failure MUST be distinguishable and MUST identify whether native work may exist.

**RM-ASYNC-ERROR-0002:** A provider MUST quarantine or fail closed on duplicate, unknown, malformed, or generation-mismatched completion records and expose bounded diagnostics.

**RM-ASYNC-OBSERVE-0001:** Traces MUST correlate submit, native issue/retry, cancel request, terminal completion, wake, and consumer observation without exposing pointer values or sensitive handles.

**RM-ASYNC-OBSERVE-0002:** Metrics MUST cover in-flight and queued operations, queue bounds, submission rejection, completion batches, readiness retries/would-block, cancellations by terminal outcome, stale events, wake coalescing, and shutdown survivors.

**RM-ASYNC-OBSERVE-0003:** Hot-path instrumentation MUST be allocation-bounded, exporter-independent, and safe against observability recursion.

**RM-ASYNC-OBSERVE-0004:** Timing evidence MUST identify submit, native issue, native completion/readiness, engine dequeue, wake, and consumer-resume boundaries with clock quality.
