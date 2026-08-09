# Roles, attributes, and relationships

**RM-APP-AUTHZ-COMPOSE-0001:** Roles are issuer-, tenant-, and resource-domain-scoped bundles or policy labels with immutable definition generations; identical names across issuers do not imply equivalent permissions.

**RM-APP-AUTHZ-COMPOSE-0002:** Role assignment, group-derived eligibility, role activation, session privilege, resource relation, and native credential state remain distinct. Hierarchies detect cycles and declare inheritance and deny interaction.

**RM-APP-AUTHZ-COMPOSE-0003:** Attributes carry authority/source, subject/resource/environment scope, schema/type, value, generation, effective and observed times, expiry, confidence/unknown, privacy classification, and revocation semantics.

**RM-APP-AUTHZ-COMPOSE-0004:** Relationship tuples bind typed subject or subject-set, relation, resource, tenant, generation, issuer, condition, validity, provenance, and caveats. Traversal declares allowed rewrites, depth/fan-out, cycles, exclusions, and consistency frontier.

**RM-APP-AUTHZ-COMPOSE-0005:** Combining RBAC, ABAC, ReBAC, ownership, explicit grants, and denies uses a named deterministic policy generation with explicit precedence, defaults, missing data, conflicts, and mandatory constraints.

**RM-APP-AUTHZ-COMPOSE-0006:** Dynamic groups, computed attributes, relation rewrites, derived roles, and policy functions expose all semantic dependencies so cache invalidation and effective-access explanations remain sound.
