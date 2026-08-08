# Partial evaluation, caching, and freshness

**RM-POLICY-PARTIAL-0001:** Partial evaluation binds known inputs/data, unknown variables, policy/schema/function/evaluator generations, entry point, limits, and semantics into a residual policy/expression plus dependency manifest.

**RM-POLICY-PARTIAL-0002:** Residual policy is validated, authenticated, sandboxed, versioned, and semantically equivalent for the declared unknown domain; it does not gain functions/data/authority absent from the source evaluation.

**RM-POLICY-CACHE-0001:** Decision-cache keys include every semantic input and policy/schema/data/function/evaluator/time/tenant/security generation; sensitive keys use protected fingerprints and partitions.

**RM-POLICY-CACHE-0002:** Cacheability declares result classes, expiry, dependency invalidation, policy/data/identity/resource/time change, obligations, nondeterministic functions, negative/indeterminate caching, and emergency revocation.

**RM-POLICY-CACHE-0003:** Cached permit cannot outlive credential/resource/delegation/policy/data validity or bypass current enforcement preconditions; high-risk actions may forbid decision reuse.

**RM-POLICY-CACHE-0004:** Decision, compiled-policy, data, partial-result, explanation, and function caches are separate with independent identity, privacy, size, eviction, and corruption rules.

**RM-POLICY-PARTIAL-0003:** Planning/indexing optimizations publish dependency/unknown analysis and fall back safely when provider or function support differs.

**RM-POLICY-CACHE-0005:** Distributed invalidation completion remains boundary-scoped evidence; security emergency response composes revocation, short expiry, version rejection, purge, enforcement denial, and observation.
