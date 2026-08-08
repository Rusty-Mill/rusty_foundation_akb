# Service activation, readiness, and IPC

Demand activation binds an addressable service endpoint to a definition generation. A broker may reserve/listen on the endpoint before a worker exists and launch a compatible generation on demand.

**RM-BACKGROUND-SERVICE-0001:** Endpoint availability, activation request, process creation, runtime initialization, request acceptance, service readiness, request handling, and response completion MUST be separate milestones.

**RM-BACKGROUND-SERVICE-0002:** Service identity MUST bind endpoint namespace, definition/package generation, server principal, interface compatibility, security policy, and broker provenance. A process name or PID is insufficient.

**RM-BACKGROUND-SERVICE-0003:** Activation requests MUST be authenticated, authorized, bounded, replay-aware, and safe under duplicate launch. Request payloads are validated at the service boundary and never become implicit launch arguments.

**RM-BACKGROUND-SERVICE-0004:** Concurrent activation MUST resolve to declared singleton, per-user, per-session, per-client, pooled, or multi-instance policy with deterministic endpoint routing and generation selection.

**RM-BACKGROUND-SERVICE-0005:** Readiness MUST be explicit application evidence tied to instance and definition generations; process existence, open endpoint, broker acceptance, or elapsed time does not prove readiness.

**RM-BACKGROUND-SERVICE-0006:** Idle termination, demand restart, crash restart, backoff, circuit breaking, and permanent failure MUST be observable policies. Restart loops are bounded and cannot mask a bad generation.

**RM-BACKGROUND-SERVICE-0007:** Client cancellation or disconnect does not prove worker cancellation. Request lifetime, deduplication key, ownership, deadline, terminal outcome, and orphan policy are explicit.
