# Explanation, audit, and privacy

**RM-POLICY-EXPLAIN-0001:** Explanation levels distinguish decision summary, contributing policy IDs, reason codes, attribute dependencies, rule trace, expression values, and full evaluator profile with separate authority and cost.

**RM-POLICY-EXPLAIN-0002:** Explanations are derived diagnostic evidence, not stable policy semantics or proof of causal intent; optimizers/providers may differ while preserving the decision contract.

**RM-POLICY-EXPLAIN-0003:** User-facing reasons are versioned localized product messages mapped from safe reason codes, actionable where possible, accessible, and prevented from exposing hidden policy, sensitive attributes, other principals/resources, or attack guidance.

**RM-POLICY-AUDIT-0001:** Decision records bind decision ID, entry point, policy/schema/data/function/evaluator generations, request/subject/resource/action fingerprints, result/reason/obligation classes, enforcement correlation, time, and causal context.

**RM-POLICY-AUDIT-0002:** Logs minimize/mask inputs, values, entity data, policy source, secrets, health/risk/location, obligations, and explanations according to field-level classification before export.

**RM-POLICY-AUDIT-0003:** Sampling cannot omit required high-risk/deny/error/break-glass/legal audit events and declares denominator/selection; lost/delayed/duplicate log delivery is observable and does not change the decision.

**RM-POLICY-AUDIT-0004:** Audit storage uses access control, integrity, time/source evidence, retention/legal hold, export/erasure boundaries, tenant separation, and independently tested recovery.

**RM-POLICY-EXPLAIN-0004:** Debug traces and decision logs are never accepted as policy data or replayed decisions without explicit validation and authority.
