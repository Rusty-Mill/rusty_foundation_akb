# Decision and enforcement contracts

**RM-APP-AUTHZ-ENFORCE-0001:** The policy decision point evaluates immutable request and dependency snapshots without performing protected domain effects. External reads, nondeterminism, and side effects are explicit bounded providers.

**RM-APP-AUTHZ-ENFORCE-0002:** The enforcement point owns the protected operation, validates decision applicability and freshness, current authority, resource generation, action/parameters, tenant, delegation, and every mandatory obligation immediately before effect.

**RM-APP-AUTHZ-ENFORCE-0003:** Obligations are typed enforcement requirements with responsible component, ordering, atomicity, failure behavior, evidence, privacy, and idempotency. Unsupported or failed mandatory obligations prevent the effect.

**RM-APP-AUTHZ-ENFORCE-0004:** Advice and presentation hints are non-authoritative and cannot weaken denial, current preconditions, native access checks, or mandatory obligations.

**RM-APP-AUTHZ-ENFORCE-0005:** Native operating-system, database, object-store, broker, repository, CA, and application-domain checks remain authorization points. A portable permit is never a guarantee that the effect will or should succeed.

**RM-APP-AUTHZ-ENFORCE-0006:** Check-then-use races use handle-relative/native atomic enforcement, conditional resource generations, transactional domain checks, or explicit residual risk; time proximity alone does not establish atomicity.
