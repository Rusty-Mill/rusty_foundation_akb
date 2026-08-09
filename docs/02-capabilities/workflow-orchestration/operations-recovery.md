# Operations, repair, and recovery

**RM-WORKFLOW-OPS-0001:** Operational views expose instance/run/definition, status/history frontier, outstanding activities/tasks/timers/children/signals, attempts/deadlines, effects/residuals, policy/worker/provider generations, and privacy-qualified search fields.

**RM-WORKFLOW-OPS-0002:** Pause, resume, cancel, terminate, retry, reset, replay, migrate, reassign, force-complete, inject event, skip, compensate, and delete are separate privileged operations with exact preconditions, authority, consequences, and audit.

**RM-WORKFLOW-OPS-0003:** Repair never edits committed history in place. It appends an authorized repair event or creates a new run/instance from a validated frontier with links, justification, simulation, and residuals.

**RM-WORKFLOW-OPS-0004:** Backup/restore binds history, snapshots, definitions, schemas, payloads, task/assignment state, timers, deduplication/idempotency, search projections, encryption/keys, audit, and external-effect reconciliation.

**RM-WORKFLOW-OPS-0005:** Disaster recovery prevents split-brain orchestration and stale worker effects through fenced ownership, restores consistent history frontiers, rebuilds projections, reconciles dispatch/timers, and verifies target effects before retry.

**RM-WORKFLOW-OPS-0006:** Deletion distinguishes visibility, search projection, active orchestration, payload redaction, history retention, legal hold, backups, external systems, and audit evidence; it cannot erase external effects by deleting the workflow record.
