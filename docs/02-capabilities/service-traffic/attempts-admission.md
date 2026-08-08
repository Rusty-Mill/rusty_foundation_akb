# Attempts, retries, hedges, and admission

**RM-TRAFFIC-ATTEMPT-0001:** An attempt inherits original service authority, request identity, absolute deadline, cancellation, trace context, replay/effect classification, tenant, route generation, and total resource budget while receiving a unique attempt identity.

**RM-TRAFFIC-ATTEMPT-0002:** Retry policy names eligible failure/milestone, maximum attempts/time, per-attempt timeout, backoff/jitter, same/alternate endpoint/subset/locality, retry-after, body replay, credential refresh, and idempotency/reconciliation.

**RM-TRAFFIC-ATTEMPT-0003:** Hedging starts bounded concurrent attempts only for replay-safe work, defines delay/trigger/diversity, cancels losers after one selected terminal result, and handles simultaneous/ambiguous effects explicitly.

**RM-TRAFFIC-ATTEMPT-0004:** Retries, hedges, connection races, auth challenges, redirects, proxy attempts, and failover share one visible attempt tree and amplification budget.

**RM-TRAFFIC-ADMIT-0001:** Admission bounds global/service/route/endpoint/tenant connection, request, stream, pending, retry, hedge, probe, and byte/work budgets with priority/fairness and explicit reject/queue/shed behavior.

**RM-TRAFFIC-CIRCUIT-0001:** Circuit breakers are local overload/failure controls with scope, measured signals, thresholds/windows, closed/open/probe states, minimum volume, timeout, recovery, and configuration generation; they do not prove endpoint health.

**RM-TRAFFIC-ADMIT-0002:** Queues are bounded by count/bytes/work/deadline, shed expired or low-priority work, preserve cancellation, and expose queue time separately from service latency.

**RM-TRAFFIC-ATTEMPT-0005:** Overload responses, transport refusal, local shedding, and endpoint failures remain distinguishable so policy does not create retry storms or unfair ejection.
