# Cross-cutting qualities

**RM-APP-AUTHZ-XCUT-0001:** Security uses deny-by-default product policy, least authority, explicit actor/subject/audience, tenant isolation, attenuation-only delegation, confused-deputy defenses, native enforcement, bounded evaluation, authenticated distribution, and fail-closed unknown handling for protected effects.

**RM-APP-AUTHZ-XCUT-0002:** Privacy minimizes subject/resource attributes, relation graphs, effective-access enumeration, explanations, simulations, logs, and cross-tenant correlation; query purpose and authority are enforced and sensitive existence is not disclosed through decisions or timing.

**RM-APP-AUTHZ-XCUT-0003:** Accessibility and internationalization provide clear localized request/share/deny/expiry/revocation explanations and safe correction paths without exposing policy internals; stable typed identifiers remain separate from localized labels.

**RM-APP-AUTHZ-XCUT-0004:** Observability correlates request/decision/enforcement/obligation/effect generations and latency, records policy/data freshness and cache use, redacts sensitive attributes and graph paths, distinguishes policy deny from system failure, and measures revocation convergence.

**RM-APP-AUTHZ-XCUT-0005:** Async-first evaluation supports cancellation/deadlines/batching/backpressure and never leaves partially applied obligations; sync completeness covers bounded local evaluation without hidden runtimes or blocking remote graph/policy calls indefinitely.

**RM-APP-AUTHZ-XCUT-0006:** Performance preserves compiled/partial evaluation, dependency-complete caches, native batch/vector/index filtering, relation indexes, locality, and bounded parallelism while retaining point enforcement and semantic equivalence.
