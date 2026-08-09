# Policy administration and distribution

**RM-APP-AUTHZ-ADMIN-0001:** Policy administration separates author, reviewer, approver, publisher, distributor, evaluator operator, enforcement owner, and auditor roles under product-defined separation of duties.

**RM-APP-AUTHZ-ADMIN-0002:** A release binds policy/schema/function/data-contract source and digest, compiler/toolchain, tests, simulation/change analysis, approvals, compatibility, activation scope/time, predecessor, rollback plan, signature/provenance, and immutable generation.

**RM-APP-AUTHZ-ADMIN-0003:** Validation checks types, actions/resources/relations, attribute authorities, unreachable or shadowed rules, cycles, broad selectors, conflicting grants/denies, missing defaults, unsupported obligations, nondeterminism, resource limits, and migration compatibility.

**RM-APP-AUTHZ-ADMIN-0004:** Distribution is authenticated, coherent, tenant-scoped, monotonic under product policy, rollback-protected, observable, and capable of staged rollout, emergency withdrawal, and mixed-generation detection.

**RM-APP-AUTHZ-ADMIN-0005:** Configuration acceptance, evaluator loading, enforcement adoption, cache invalidation, traffic coverage, and observed decision convergence are separate milestones.

**RM-APP-AUTHZ-ADMIN-0006:** Break-glass policy changes declare incident, scope, issuer, quorum/bypass, expiry, notification, precedence, audit, rollback, and after-action review and cannot silently become permanent policy.
