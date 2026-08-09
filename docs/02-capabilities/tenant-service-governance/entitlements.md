# Feature entitlements and effective eligibility

**RM-TENANT-GOV-ENTITLE-0001:** A feature definition binds stable feature ID, semantic contract, parameter/value schema, scope, dependencies/conflicts, lifecycle, and compatibility; boolean flags are only one value form.

**RM-TENANT-GOV-ENTITLE-0002:** Effective entitlement is a versioned derivation over catalog/agreement, contract overrides, trials, promotions, administrative grants/denies, tenant lifecycle, geography, product policy, and time.

**RM-TENANT-GOV-ENTITLE-0003:** Results distinguish eligible, ineligible, conditional, grace, expired, suspended, denied, unknown, and stale and include explanation/provenance safe for the caller.

**RM-TENANT-GOV-ENTITLE-0004:** Entitlement does not replace actor/resource authorization, data classification, consent, platform capability resolution, capacity admission, safety policy, or effect-specific validation.

**RM-TENANT-GOV-ENTITLE-0005:** Precedence and conflict rules are deterministic, versioned, testable, and deny or remain unknown on missing mandatory evidence; a billing provider status cannot silently override security policy.

**RM-TENANT-GOV-ENTITLE-0006:** Cached/offline entitlement evidence binds dependencies, evaluation time, expiry, revocation frontier, permitted operations, and risk. High-impact effects require fresh evaluation or scoped delegated leases.

**RM-TENANT-GOV-ENTITLE-0007:** Plan changes use simulation/diff, staged activation, consumer inventory, notification, rollback/exception, and observed enforcement convergence.
