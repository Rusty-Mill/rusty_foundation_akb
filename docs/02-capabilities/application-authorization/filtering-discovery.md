# Filtering, batch checks, and permission discovery

**RM-APP-AUTHZ-FILTER-0001:** A filter request binds subject/actor/delegation, action, resource type and query, tenant, context, policy/data frontier, pagination/order, maximum work, completeness mode, and authority.

**RM-APP-AUTHZ-FILTER-0002:** Sound filtering returns no resource that a point check under the declared frontier would deny or classify indeterminate. Incomplete filtering may omit allowed resources but reports that limitation.

**RM-APP-AUTHZ-FILTER-0003:** Candidate generation, authorization filtering, ranking, pagination, hydration, and point enforcement preserve a consistent security frontier or recheck before disclosure/effect. Post-filtering cannot expose counts, facets, snippets, order, or timing for unauthorized candidates.

**RM-APP-AUTHZ-FILTER-0004:** Batch checks retain per-item typed results, dependencies, and errors; a batch permit/deny cannot mask mixed outcomes, duplicate resources, cross-tenant items, stale generations, or partial evaluation.

**RM-APP-AUTHZ-FILTER-0005:** Permission discovery answers product-scoped questions such as available actions or reason categories under a named snapshot; it does not mint authority or guarantee future operations.

**RM-APP-AUTHZ-FILTER-0006:** Pagination tokens bind authorization frontier and query semantics. Policy, relation, tenant, or subject changes cause explicit invalidation, restart, or weaker consistency disclosure rather than silent mixed pages.
