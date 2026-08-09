# Caching, consistency, and revocation

**RM-APP-AUTHZ-CACHE-0001:** Cache keys include every semantic dependency: subject/account/session and actor/delegation generations, tenant, action, resource generation, context projection, policy/schema/data/function/evaluator, relation/attribute/role/grant/deny frontiers, obligations, provider, and purpose.

**RM-APP-AUTHZ-CACHE-0002:** Cached permits never outlive any credential/session/delegation/grant/resource/policy/data validity and may be prohibited for destructive, privileged, recovery, or transaction-bound actions. Deny caching preserves not-applicable/indeterminate distinctions.

**RM-APP-AUTHZ-CACHE-0003:** Consistency modes name the minimum required revision or causal token, exact snapshot, bounded staleness, or best-effort frontier and define unavailable behavior rather than advertising strong/eventual labels alone.

**RM-APP-AUTHZ-CACHE-0004:** Mutation responses return a revision or consistency token that dependent checks, list filters, and writes can require to avoid evaluating before the caller's own authorization change.

**RM-APP-AUTHZ-CACHE-0005:** Revocation invalidates by affected dependency and propagates to evaluators, enforcement caches, tokens/sessions where relevant, indexes, edges, devices, and downstream services with measured accepted/applied/observed frontiers.

**RM-APP-AUTHZ-CACHE-0006:** Outage modes explicitly choose fail closed, bounded stale read, emergency policy, or service-specific degraded behavior by action class; an old permit is never reused merely because evaluation is unavailable.
