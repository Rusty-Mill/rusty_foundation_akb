# Parallelism, joins, races, and child workflows

**RM-WORKFLOW-PARALLEL-0001:** Parallel and map constructs declare input collection snapshot/order, maximum concurrency, branch identity, isolation, completion threshold, result ordering, failure aggregation, cancellation, and partial-effect policy.

**RM-WORKFLOW-PARALLEL-0002:** Joins distinguish all, any, first-success, quorum, threshold, race, and custom deterministic conditions and define late branch outcomes, compensation, cancellation, and result selection.

**RM-WORKFLOW-PARALLEL-0003:** Event races register competing waits atomically or under an explicit ordering contract, record the winner in history, cancel or ignore losers by declared semantics, and retain already committed loser effects.

**RM-WORKFLOW-PARALLEL-0004:** Child workflows bind parent/child instance and definition generations, input/output schema, authority attenuation, start/cancellation/termination/retention policy, event propagation, search visibility, and failure/compensation boundary.

**RM-WORKFLOW-PARALLEL-0005:** Parent close does not imply child close unless the selected policy and observed child outcome prove it; detached children require independent ownership, retention, and operational visibility.

**RM-WORKFLOW-PARALLEL-0006:** Fan-out, recursive child creation, nested maps, outstanding events, payload/history size, and result aggregation are bounded and expose throttling/backpressure rather than exhausting orchestration infrastructure.
