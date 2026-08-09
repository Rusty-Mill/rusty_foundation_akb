# Conformance

**RM-TENANT-GOV-CONFORMANCE-0001:** Tenant suites cover create/retry, partial provisioning, readiness, suspension modes, ownership transfer, merge/split, account/billing reassignment, closure/holds/export/deletion, identifier reuse, repair, and disaster recovery.

**RM-TENANT-GOV-CONFORMANCE-0002:** Isolation suites inject missing/wrong tenant context across queries, caches, queues, indexes, objects, logs, backups, admin tools, jobs, meters, and side channels; they validate each declared tier and placement migration.

**RM-TENANT-GOV-CONFORMANCE-0003:** Entitlement matrices cover plan/add-on/trial/contract/grant/deny/geography/lifecycle/time precedence, stale/missing provider evidence, webhook duplicate/reorder/gaps, cache expiry/revocation, offline leases, simulation, and rollout convergence.

**RM-TENANT-GOV-CONFORMANCE-0004:** Quota histories cover concurrent admission, reservation crash/expiry/reconcile, exact and approximate distributed modes, partition/overshoot, limit reduction, existing resources, fairness/starvation, overage/grace, overflow, and upgrade races.

**RM-TENANT-GOV-CONFORMANCE-0005:** Meter/rating histories cover every event boundary, duplicates, late/future/out-of-order/negative/overflow/unit errors, high cardinality, aggregation windows/time zones, tiers/rounding, rerating, corrections, closed periods, disputes, and invoice reconciliation.

**RM-TENANT-GOV-CONFORMANCE-0006:** Migration suites cover catalog/schema/provider/topology changes with open subscriptions, cached entitlements, reservations, late usage, dual meters, open/closed billing periods, rollback, and no double grant/admission/billing.

**RM-TENANT-GOV-CONFORMANCE-0007:** Evidence records fixtures/seeds, tenant/catalog/agreement/policy/meter/quota/provider/tool generations, clocks/periods/currencies/rounding, topology/fault schedule, source frontiers, outputs/adjustments/residuals, privacy redaction, and artifact digests.
