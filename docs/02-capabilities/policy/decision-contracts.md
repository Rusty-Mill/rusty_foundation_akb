# Policy domains and decision contracts

**RM-POLICY-DECISION-0001:** Every policy entry point has a stable purpose-scoped identity, typed request schema, result algebra, combining/default/error rules, obligation/advice schema, enforcement boundary, and sensitivity classification.

**RM-POLICY-DECISION-0002:** Authorization requests bind authenticated principal/subject evidence, action, resource generation, environment/context, delegation, tenant, and enforcement intent; absent identity is an explicit principal class rather than an empty value.

**RM-POLICY-DECISION-0003:** Authorization results distinguish permit, deny, not-applicable, and indeterminate with reason classes and obligations/advice. Boolean projection is allowed only under an explicit fail-closed mapping that retains diagnostic evidence.

**RM-POLICY-DECISION-0004:** Business, validation, routing, admission, configuration, and feature decisions use domain-specific typed results and do not inherit authorization semantics merely because they use the same evaluator.

**RM-POLICY-DECISION-0005:** Decision identity binds request and all evaluation generations plus result and expiry/revalidation scope; replaying an old decision against changed resource, principal, data, time, or policy is prohibited unless a capability contract explicitly permits it.

**RM-POLICY-DECISION-0006:** A decision is not a credential, capability, proof of enforcement, transaction commit, or business outcome. Enforcement revalidates current authority and required generations.

**RM-POLICY-DECISION-0007:** Batch decisions preserve per-item inputs/outcomes and any shared snapshot boundary; batch transport/evaluation success does not imply each decision is applicable or enforced.
