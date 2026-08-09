# Tenant lifecycle and ownership

**RM-TENANT-GOV-LIFECYCLE-0001:** Tenant creation binds sponsor/customer identity, legal/organizational context, owners, regions/residency, isolation tier, resource and identity mappings, initial policy, service objectives, and idempotent request identity.

**RM-TENANT-GOV-LIFECYCLE-0002:** Requested, validated, provisioned, initialized, ready, active, restricted, suspended, closing, retained, deleted, and residual-reconciled are distinct lifecycle states.

**RM-TENANT-GOV-LIFECYCLE-0003:** Suspension policy distinguishes authentication, reads, writes, administration, export, support, security response, billing, background work, inbound events, and data-retention effects; it is not equivalent to tenant deletion.

**RM-TENANT-GOV-LIFECYCLE-0004:** Ownership transfer, merger, split, parent/subtenant change, domain change, and billing-account reassignment use staged plans with approvals, resource/identity mappings, conflicts, coexistence, rollback horizons, and audit.

**RM-TENANT-GOV-LIFECYCLE-0005:** Closure inventories identities/sessions, resources, data/replicas/backups, keys/secrets, integrations, workflows, meters/charges/invoices, holds, exports, and unknown frontiers before effects.

**RM-TENANT-GOV-LIFECYCLE-0006:** Tenant identifiers are never silently reused. Re-creation receives a new generation and cannot revive stale credentials, resources, meter events, webhooks, or tombstoned data.
