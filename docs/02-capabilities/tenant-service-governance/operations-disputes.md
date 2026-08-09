# Operations, disputes, and reconciliation

**RM-TENANT-GOV-OPS-0001:** Operators can inspect tenant lifecycle, placement/isolation, entitlement derivation, quota/reservations, meter ingestion/late data, aggregate/rating lineage, provider reconciliation, invoices, and residuals under least privilege.

**RM-TENANT-GOV-OPS-0002:** Create/suspend/resume/close, grant/deny/override, quota change, meter quarantine/replay, adjustment/rerate, placement move, and provider repair are authorized idempotent plans with preview, reason, expiry, approval, receipts, and audit.

**RM-TENANT-GOV-OPS-0003:** Break-glass service restoration is time- and scope-bound, independently approved where required, visible, reversible, and cannot rewrite payment, usage, or authorization history.

**RM-TENANT-GOV-OPS-0004:** Reconciliation compares authoritative source populations/frontiers and reports missing, duplicate, conflicting, stale, orphaned, and unallocated records; absence in a webhook stream is not proof of deletion.

**RM-TENANT-GOV-OPS-0005:** A dispute case preserves claimant, scope/period, challenged events/aggregates/charges, evidence and provenance, holds, communications, decisions/approvals, adjustments, deadlines, and appeal without mutating raw facts.

**RM-TENANT-GOV-OPS-0006:** Disaster recovery validates tenant mappings, placement, entitlements, reservations, meter dedup/frontiers, closed periods, adjustments, provider cursors, keys, and audit before resuming admission or billing exports.
