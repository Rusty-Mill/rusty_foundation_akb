# Composition and conflict resolution

**RM-POLICY-COMPOSE-0001:** Policy composition declares module/set hierarchy, import/dependency generations, entry points, precedence, combining algorithm/version, defaults, conflict/ambiguity, obligations/advice combination, and order sensitivity.

**RM-POLICY-COMPOSE-0002:** Deny-overrides, permit-overrides, first-applicable, only-one-applicable, ordered variants, consensus/quorum, priority, merge, and domain algorithms retain exact truth/error/indeterminate tables.

**RM-POLICY-COMPOSE-0003:** Security policy uses explicit fail-closed rules for no-match, missing data, conflict, evaluator error, stale policy/data, unsupported obligation, and partial evaluation; deny-overrides alone does not define all cases.

**RM-POLICY-COMPOSE-0004:** Multiple permit/deny/typed results preserve contributing policy identities and deterministically combine obligations/advice or reject incompatible results.

**RM-POLICY-COMPOSE-0005:** Policy priority/order is stable metadata under governed authority, not filesystem load order, map iteration, discovery timing, or provider implementation detail.

**RM-POLICY-COMPOSE-0006:** Product business rules cannot weaken mandatory platform/security/legal policy; policy domains declare hierarchy and whether composition is intersection, union, override, refinement, or independent advice.

**RM-POLICY-COMPOSE-0007:** Delegated policy namespaces attenuate allowed subjects/resources/actions/results/functions/data/obligations and cannot define beyond their grant.

**RM-POLICY-COMPOSE-0008:** Cyclic dependencies, recursive policy/data references, and cross-domain result loops are rejected or executed only under a bounded formally specified fixed-point contract.
