# Cross-cutting qualities

**RM-TENANT-GOV-CROSS-0001:** Every control-plane and data-plane operation binds authenticated tenant/actor/workload plus independent resource authorization; support and automation delegation are attenuated and audited.

**RM-TENANT-GOV-CROSS-0002:** Tenant, subscription, entitlement, usage, cost, invoice, payment, tax, dispute, device, and operator data are classified, purpose-limited, minimized, region/retention governed, exportable, correctable where appropriate, and erasure/hold aware.

**RM-TENANT-GOV-CROSS-0003:** User and operator experiences provide localized, accessible lifecycle/eligibility/quota/usage/charge explanations, effective dates, progress, correction/appeal paths, and non-color-only status without exposing sensitive policy or other tenants.

**RM-TENANT-GOV-CROSS-0004:** Observability correlates tenant/partition/catalog/agreement/entitlement/quota/reservation/meter/aggregate/rating/provider generations and reconciliation frontiers while bounding high-cardinality cost and data leakage.

**RM-TENANT-GOV-CROSS-0005:** Limits cover tenants/resources/features/rules/dimensions/events/reservations/overrides/adjustments/provider backlog/cardinality and hostile values; checked decimal/integer arithmetic and explicit rounding prevent overflow or drift.

**RM-TENANT-GOV-CROSS-0006:** Async operations expose cancellation, deadlines, streaming/backpressure, partial/ambiguous outcomes, and recovery. Sync counterparts are complete where meaningful and do not create hidden runtimes.

**RM-TENANT-GOV-CROSS-0007:** Security and privacy enforcement continue when commercial systems fail; telemetry and billing pipelines cannot become a privileged bypass into tenant data planes.
