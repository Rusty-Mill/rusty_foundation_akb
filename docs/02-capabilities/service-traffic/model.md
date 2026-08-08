# Model, entities, and milestones

**RM-TRAFFIC-MODEL-0001:** A traffic domain binds service identity, discovery/control-plane source, endpoint snapshot, routing/balancing policy, security context, locality/fault model, health/admission, retry/effect, connection, observability, and configuration generations.

**RM-TRAFFIC-MODEL-0002:** Distinct entities include service, logical port/protocol, endpoint instance/generation, address candidate, registration, discovery record/snapshot, health observation, route/subset, load-balancer state, attempt, connection/session, request/stream, and domain effect.

**RM-TRAFFIC-MODEL-0003:** Milestones distinguish registration accepted/visible, discovery received/applied, endpoint eligible, route selected, attempt admitted/started/connected/authenticated/ready, request accepted/response started/completed, effect committed, drain begun/completed, and deregistration propagation.

**RM-TRAFFIC-MODEL-0004:** Outcomes preserve service/endpoint/route/policy generations, discovery/health ages, locality, selection reason, attempt lineage, connection reuse, admission/circuit/outlier state, protocol milestone, partial progress, retry/effect safety, and reconciliation.

**RM-TRAFFIC-MODEL-0005:** Control plane, data plane, origin/proxy/client balancing, service protocol, and product effect are separate boundaries with explicit failure and trust relationships.

**RM-TRAFFIC-MODEL-0006:** Async observation/routing/attempts are bounded and cancellation-safe; sync equivalents never create hidden runtimes and disclose blocking, resolution, callback, and thread behavior.
