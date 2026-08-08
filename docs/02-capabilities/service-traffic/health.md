# Health, readiness, draining, and outliers

**RM-TRAFFIC-HEALTH-0001:** Health evidence identifies endpoint generation, observer and boundary, active/passive/control-plane/application source, check generation, observed time/age, state, reason, latency, consecutive evidence, and expiry.

**RM-TRAFFIC-HEALTH-0002:** Liveness, startup, readiness, serving, accepting-new, draining, terminating, dependency health, saturation, protocol readiness, and product correctness are distinct signals.

**RM-TRAFFIC-HEALTH-0003:** Active probes use ordinary authenticated least-privilege protocol paths where possible, bounded frequency/time/concurrency/payload, jitter, locality, and overload protection; probes cannot amplify outages.

**RM-TRAFFIC-HEALTH-0004:** Passive observations classify connect, secure-channel, protocol, status, reset, timeout, local cancellation, overload, and domain errors; caller-caused failures do not automatically indict an endpoint.

**RM-TRAFFIC-HEALTH-0005:** Outlier detection declares statistical window, minimum volume/hosts, error/latency classes, thresholds, ejection percentage/duration/backoff, success-rate bias, locality, probation, and panic behavior.

**RM-TRAFFIC-HEALTH-0006:** Ejection and recovery are routing-policy decisions based on evidence, not endpoint lifecycle authority; control-plane readiness and local passive evidence reconcile without oscillation or permanent quarantine.

**RM-TRAFFIC-HEALTH-0007:** Drain stops new eligible work under policy while preserving bounded existing requests/streams/sessions; deadline, forced termination, re-registration, and completion evidence are explicit.

**RM-TRAFFIC-HEALTH-0008:** All-unhealthy behavior is explicit: fail, degraded/panic routing, last-known-good, alternate locality/service, queue, or shed. It cannot silently convert health policy into unrestricted routing.
