# Conformance

**RM-TRAFFIC-CONFORMANCE-0001:** Identity/discovery suites test address reuse/restart generations, aliases/original authority, dual stack/transports, TTL/lease/negative caches, snapshots/watch gaps/duplicates, multiple endpoint slices/sources, network changes, stale/offline, rollback, and bounds.

**RM-TRAFFIC-CONFORMANCE-0002:** Health suites inject startup/readiness/drain/terminate, active/passive disagreement, slow/error/overload/caller failures, outlier thresholds/ejection/recovery, all-unhealthy panic, partitions, probes under overload, and stale evidence.

**RM-TRAFFIC-CONFORMANCE-0003:** Routing suites cover precedence/ambiguity/normalization, protected metadata, weighted/subset/canary/shadow, deterministic allocation, rewrites/original authority, missing/stale fields, privacy, and policy-version replay.

**RM-TRAFFIC-CONFORMANCE-0004:** Balancing suites use deterministic traces for algorithms, weights/capacity/load staleness, connection/request multiplexing, affinity/failover, endpoint churn, skew/fairness, hot keys, slow start, and synchronized reconnect prevention.

**RM-TRAFFIC-CONFORMANCE-0005:** Attempt/admission suites test every transport/security/protocol/effect milestone, body replay, deadline/cancellation, retry-after/backoff, hedges/races, auth/redirect/proxy/failover amplification, queues, circuits, and ambiguous effects.

**RM-TRAFFIC-CONFORMANCE-0006:** Locality/failover suites test asymmetric region/zone/network partitions, capacity exhaustion, data/security readiness, progressive failover/failback, split views, affinity/session handling, brownout, and objectives.

**RM-TRAFFIC-CONFORMANCE-0007:** Control-plane suites test coherent dependency graphs, incremental/state-of-world reconciliation, invalid/rejected resources, warm/apply acknowledgments, mixed generations, last-known-good expiry/revocation, staged rollout/rollback, restart, failover, and audit.

**RM-TRAFFIC-CONFORMANCE-0008:** Security/privacy/accessibility suites test forged registration/metadata/health/routes, authority downgrades, cross-tenant affinity/cache, proxy delegation, destination/topology leakage, emergency revocation, accessible failure/recovery, and cleanup.

**RM-TRAFFIC-CONFORMANCE-0009:** Provider reports publish unsupported semantics, emulations, weaker guarantees, configuration/version prerequisites, algorithm/propagation differentials, resource/cost measurements, and waivers.
