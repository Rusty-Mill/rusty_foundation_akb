# Grace, offline, and degraded operation

**RM-TENANT-GOV-GRACE-0001:** Grace policy binds trigger, eligible tenants/features/operations, start/end, maximum extension, evidence freshness, offline lease, risk/quantity caps, notification, revocation, reconciliation, and authority.

**RM-TENANT-GOV-GRACE-0002:** Billing-provider unavailability, entitlement-service failure, meter outage, quota-store partition, offline client, and tenant delinquency are distinct causes with separate fail-open/closed behavior.

**RM-TENANT-GOV-GRACE-0003:** Offline entitlement/quota leases are signed or integrity-protected, tenant/device/workload/feature scoped, nontransferable, expiry-bound, rollback-resistant, revocable where connectivity permits, and never silently renewed by wall-clock rollback.

**RM-TENANT-GOV-GRACE-0004:** Locally accepted use records stable operation/effect and meter identities, reserved allowance, causal/effective time, and authority for later deduplication, quota and billing reconciliation.

**RM-TENANT-GOV-GRACE-0005:** Reconnect handles overuse, plan expiry, revoked grants, conflicting leases, late meter events, and clock uncertainty without erasing usage or retroactively forging authorization.

**RM-TENANT-GOV-GRACE-0006:** Safety, security response, tenant export/closure, and legally required access are not casually disabled by commercial outages; exact exceptions remain product/legal policy.
