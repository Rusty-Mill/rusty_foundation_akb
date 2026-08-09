# Migration and lifecycle

**RM-COMMS-MIGRATE-0001:** Template/content schema evolution declares compatibility across pending plans, stored in-app messages, provider templates, localized variants, clients, action handlers, and audit previews.

**RM-COMMS-MIGRATE-0002:** Provider/channel migration maps sender/endpoints/templates/statuses/suppressions/cursors/charges, runs shadow/differential delivery only to controlled targets, stages traffic, reconciles unknowns, and preserves rollback.

**RM-COMMS-MIGRATE-0003:** Sender domain/number/application/project/key migration proves authentication, registration, reputation warmup, callback ownership, endpoint/token refresh, unsubscribe continuity, and old-credential revocation.

**RM-COMMS-MIGRATE-0004:** Preference/taxonomy changes map purposes/topics/channels, simulate affected recipients, preserve denials conservatively, notify where appropriate, and prove cache/provider convergence before retiring old semantics.

**RM-COMMS-MIGRATE-0005:** Tenant/account merge, split, transfer, closure, and region move reconcile endpoints, consent/preferences/suppressions, pending deliveries, conversations, content, providers, metering, retention, and cross-tenant correlation.

**RM-COMMS-MIGRATE-0006:** Disaster recovery validates attempt/idempotency state, schedules, suppressions, provider cursors, sender credentials, templates/content digests, inbound routing, and recipient eligibility before resuming sends.
