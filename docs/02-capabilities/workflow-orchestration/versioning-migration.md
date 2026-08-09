# Definition evolution and in-flight migration

**RM-WORKFLOW-MIGRATE-0001:** Changes classify compatibility for new starts, replay of every retained history, current state schemas, outstanding activities/tasks/timers/signals/children, search projections, compensation, and rollback.

**RM-WORKFLOW-MIGRATE-0002:** Version markers or patch decisions are recorded deterministically in history before behavior diverges and remain supported until all referencing histories expire or are migrated.

**RM-WORKFLOW-MIGRATE-0003:** In-flight migration uses an immutable plan mapping source/target definitions, state/events/nodes, outstanding work, timers, retries, authority, compensation, data transformation, validation, rollback limits, and audit.

**RM-WORKFLOW-MIGRATE-0004:** Migration is conditional on exact history/state frontier, quiesces or explicitly handles concurrent stimuli, stages transformed state, validates invariants, commits atomically, and never rewrites prior history silently.

**RM-WORKFLOW-MIGRATE-0005:** Worker/activity version routing is explicit and generation-bound; old and new implementations coexist under rollout policy without nondeterministic selection during replay or retry.

**RM-WORKFLOW-MIGRATE-0006:** Continue-as-new creates a linked instance/run with explicit carried state, outstanding-event policy, authority and definition generations, deduplication horizon, retention, and search/audit continuity.
