# Cross-cutting qualities

**RM-TRAFFIC-XCUT-0001:** Secure defaults require authenticated authority, bounded discovery/metadata, strict route matching, least-privilege endpoints, conservative retries, admission/circuit budgets, no cross-tenant affinity, and rollback-resistant control state.

**RM-TRAFFIC-XCUT-0002:** Performance budgets cover discovery-to-applied, route/pick/admission, connection/auth/readiness, request/stream latency, queue/retry/hedge, control propagation, health probes, CPU/memory/network, cross-zone/region, energy, and provider cost.

**RM-TRAFFIC-XCUT-0003:** Accessibility exposes connectivity/degraded/offline/retry/wait state and user recovery without flashing, forced focus, color-only status, inaccessible countdowns, or endless silent retries.

**RM-TRAFFIC-XCUT-0004:** Internationalization keeps protocol/service/route tokens locale-neutral, handles Unicode/IDNA only under explicit network-name rules, and localizes/redacts user/operator diagnostics without altering matching.

**RM-TRAFFIC-XCUT-0005:** Observability records service/endpoint/route/policy/configuration generations, locality, discovery/health age, balancer/admission/circuit/outlier state, attempt tree, connection reuse, milestones, resource/cost, and causal context with privacy and cardinality controls.

**RM-TRAFFIC-XCUT-0006:** Metrics distinguish offered/admitted/shed/queued/attempted/completed/effected work; endpoint versus route versus client failures; discovery/control lag; health/ejection; retry/hedge amplification; and latency excluding/including queue.

**RM-TRAFFIC-XCUT-0007:** Shutdown marks not-ready/draining before stopping admission, propagates under bounded grace, completes/cancels work by protocol, closes pools/sessions, releases registrations/leases, and reconciles ambiguous effects.
