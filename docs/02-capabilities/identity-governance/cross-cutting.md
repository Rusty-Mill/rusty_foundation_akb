# Cross-cutting qualities

**RM-IDENTITY-GOV-XCUT-0001:** Security applies least connector authority, tenant isolation, anti-enumeration, conditional writes, protected connector credentials, approval independence, privileged separation, immutable audit evidence, and fail-closed handling of stale or ambiguous security inputs.

**RM-IDENTITY-GOV-XCUT-0002:** Privacy applies purpose-bound projections, attribute minimization, consent or other product-policy evidence where applicable, sensitive-attribute controls, query/feed disclosure limits, retention, rights workflows, and processor/region lineage.

**RM-IDENTITY-GOV-XCUT-0003:** Accessibility and internationalization apply to invitation, request, approval, review, exception, emergency, and recovery workflows; names are Unicode data with locale-aware presentation but identity comparisons use declared provider semantics.

**RM-IDENTITY-GOV-XCUT-0004:** Async operations are cancellation-safe and bounded. Sync APIs are complete where the provider offers bounded synchronous work, but never create a hidden runtime or block indefinitely on network/control-plane convergence.

**RM-IDENTITY-GOV-XCUT-0005:** Observability uses correlation and generation identifiers, redacts directory payloads and credentials, separates requested/protocol/observed/effective milestones, and reports freshness, lag, residuals, unknowns, throttling, and provider failures.

**RM-IDENTITY-GOV-XCUT-0006:** Performance preserves provider bulk/delta/native filtering where semantics match, bounds memory and concurrency, avoids per-object round trips where safe, and never trades away authorization revalidation or tenant isolation.
