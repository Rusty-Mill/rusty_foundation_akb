# Activities, commands, signals, and events

**RM-WORKFLOW-ACTIVITY-0001:** An activity plan binds type/version, input schema/value digest, target/resource, subject/actor/workload, authority, attempt/idempotency identity, deadline, heartbeat, retry, cancellation, resource limits, privacy, and expected effect milestones.

**RM-WORKFLOW-ACTIVITY-0002:** Dispatch, transport delivery, worker acceptance, start, heartbeat/progress, external effect, result production, result persistence, and workflow observation are separate milestones.

**RM-WORKFLOW-ACTIVITY-0003:** Commands request an instance transition and return accepted/rejected/duplicate/conflict plus committed frontier; they do not synchronously claim workflow or domain completion unless the exact contract proves it.

**RM-WORKFLOW-ACTIVITY-0004:** Signals are durable asynchronous facts that may be buffered, deduplicated, rejected, expired, correlated, or remain unhandled; signal delivery does not grant transition or domain authority.

**RM-WORKFLOW-ACTIVITY-0005:** Queries are read-only projections over named history/state frontiers and cannot mutate state, consume signals, invoke activities, or be treated as linearizable unless the selected consistency contract proves it.

**RM-WORKFLOW-ACTIVITY-0006:** Updates combine request and workflow-mediated response but retain separate acceptance, validation, history commit, orchestration transition, activity/effect, and response milestones with cancellation ambiguity.
