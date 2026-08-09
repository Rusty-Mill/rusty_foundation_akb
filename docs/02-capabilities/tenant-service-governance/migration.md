# Evolution and tenant migration

**RM-TENANT-GOV-MIGRATE-0001:** Catalog/feature/meter/quota/rating schema changes declare compatibility and coexistence across producers, consumers, cached entitlements, offline leases, open reservations, late usage, active periods, and reports.

**RM-TENANT-GOV-MIGRATE-0002:** Tenant topology or isolation-tier migration inventories data/resources/keys/identities/integrations/workflows/meters, stages replication, fences writers, validates isolation and semantic state, cuts over routing, and reconciles residuals.

**RM-TENANT-GOV-MIGRATE-0003:** Plan migration binds exact source/target offers, tenant cohort, feature and quota diff, price/term treatment, effective instant, consent/notice where required, exceptions, rollback horizon, and observed entitlement convergence.

**RM-TENANT-GOV-MIGRATE-0004:** Meter migration supports dual emission/aggregation, stable event identity, unit/dimension mapping, differential reconciliation, late-event routing, adjustment policy, and no double billing.

**RM-TENANT-GOV-MIGRATE-0005:** Billing-provider migration maps customer/subscription/price/invoice/payment identities, preserves historical provenance, stages webhook ownership, reconciles open periods, and keeps application eligibility policy independent.

**RM-TENANT-GOV-MIGRATE-0006:** Rollback never reuses retired tenant/partition/meter generations or discards newer events; it either preserves forward-compatible evidence or creates a new generation and reconciliation plan.
