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

## Normative requirements

**RM-SECURITY-POLICY-0001:** Every evaluation MUST bind the exact policy identity/version, evaluator/provider, subject and resource evidence with provenance, requested operation, environment/security context, observation time, and evidence freshness.

**RM-SECURITY-POLICY-0002:** Results MUST be typed as `Permit`, `Deny`, `Indeterminate`, or `NotApplicable` and carry applicable reasons, obligations, evidence limitations, expiry/invalidation conditions, and sanitized correlation.

**RM-SECURITY-POLICY-0003:** `Permit` MUST mean only that the evaluated policy allowed the observed request; it MUST NOT promise native access, operation success, future access, or authority transfer.

**RM-SECURITY-POLICY-0004:** `Indeterminate` and unsupported evaluation MUST fail closed at an enforcement boundary unless an explicitly selected higher-level policy owns and records a narrower alternative.

**RM-SECURITY-POLICY-0005:** Independent grants and constraints MUST compose by intersection; one permit MUST NOT bypass provider eligibility, explicit authority, sandbox, discretionary, mandatory, product, or domain controls.

**RM-SECURITY-POLICY-0006:** Cached or reused decisions MUST bind all decision-affecting input generations and expiration conditions and MUST be invalidated on relevant policy, claim, resource, environment, provider, clock, or revocation change.

**RM-SECURITY-POLICY-0007:** A protected operation MUST use its native or otherwise contractually identified enforcement point; a check-then-use sequence MUST NOT claim atomic authorization without an exact primitive and evidence.

**RM-SECURITY-POLICY-0008:** Explanations and audit records MUST distinguish configured policy, observed evidence, derived decision, enforcement result, operation outcome, and disclosure redactions.
