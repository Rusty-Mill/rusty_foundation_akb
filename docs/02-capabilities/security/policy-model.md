# Security policy and decision model

**Status:** Draft

## Separation of concerns

Policy evaluation answers what configured rules and currently observed facts indicate. Native enforcement determines whether an operation actually proceeds. Rusty Mill must not convert an advisory evaluation into a promise of future access.

An evaluation input may include subject claims, requested operation, resource attributes, environment, provider evidence, sandbox state, and explicit authority. Inputs carry provenance and observation time.

## Decision result

| Result | Meaning |
|---|---|
| Permit | Observed policy allows the request; the operation can still fail |
| Deny | Observed policy rejects the request |
| Indeterminate | Required facts, evaluator support, or trustworthy evidence are unavailable |
| Not applicable | The evaluated policy does not govern this request |

A result also carries applicable policy/version identifiers, reasons suitable for the caller's disclosure level, obligations, evidence freshness, and audit correlation. `Indeterminate` defaults to denial at an enforcement boundary unless an explicit higher-level policy chooses otherwise.

## Composition

Security constraints compose by intersection. Provider eligibility, authority scope, sandbox limits, discretionary permissions, mandatory controls, and application policy must all permit the requested behavior. A provider cannot treat one successful check as authority to bypass another layer.

## Race rule

Filesystem names, credentials, policy, membership, labels, entitlements, and object state may change after evaluation. Therefore:

1. preflight decisions are for explanation, UI planning, and provider selection;
2. protected operations revalidate through the native enforcement mechanism;
3. denial and failure remain normal operation outcomes;
4. check-then-use sequences cannot claim atomic authorization unless a native primitive and capability contract prove it.

## Audit and privacy

Audit events record action category, decision, policy identity, provider, correlation, and sanitized reason. Secret values, raw credentials, cryptographic material, and excessive resource names are excluded by default. Policy may permit more detail only for a defined audience and retention period.

