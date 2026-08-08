# Routing policy and subsets

**RM-TRAFFIC-ROUTE-0001:** A routing decision binds request/service intent, principal/tenant, protocol/method/path/message class where relevant, endpoint snapshot revision, health/admission evidence, locality, subset metadata, immutable route-policy generation, and attempt budget.

**RM-TRAFFIC-ROUTE-0002:** Route matching defines normalization, precedence, specificity, ambiguity, default/no-match, case/Unicode, headers/metadata/query, protected attributes, and limits; untrusted request fields cannot select privileged backends.

**RM-TRAFFIC-ROUTE-0003:** Weighted subsets, versions, canaries, blue/green, experiments, shadow/mirror, and gradual delivery bind immutable endpoint/configuration generations, allocation unit, deterministic/random seed scope, minimum sample, hold/rollback, and exclusion rules.

**RM-TRAFFIC-ROUTE-0004:** Shadow/mirror traffic has independent authority, privacy, load, timeout, response-discard, side-effect prohibition/idempotency, credentials, and observability; it cannot inherit production mutation authority silently.

**RM-TRAFFIC-ROUTE-0005:** Header/metadata/path rewrites, original destination/authority, forwarded identity, protocol translation, and response rewriting preserve provenance and security validation across proxy/gateway hops.

**RM-TRAFFIC-ROUTE-0006:** Route action may select direct endpoint, cluster/subset, redirect, reject, queue, local response, failover, or delegated proxy with explicit terminal/nonterminal semantics.

**RM-TRAFFIC-ROUTE-0007:** Policy evaluation is bounded, deterministic where sticky/reproducible routing is claimed, versioned, auditable, and safe under missing/stale/unknown metadata.

**RM-TRAFFIC-ROUTE-0008:** Route selection grants no domain authority; endpoint authentication and application authorization revalidate at their boundaries.
