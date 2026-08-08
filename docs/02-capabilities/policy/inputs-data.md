# Typed inputs, schemas, and data

**RM-POLICY-INPUT-0001:** Request schemas define subject/principal, resource, action, context, entity references, attributes, presence/null/unknown, types, constraints, provenance, freshness, sensitivity, and allowed relationships per action/purpose.

**RM-POLICY-INPUT-0002:** Request validation is distinct from policy validation and evaluation; malformed, schema-invalid, missing-required, stale, unauthorized, and indeterminate attributes remain distinct.

**RM-POLICY-DATA-0001:** Policy data resolves to an immutable snapshot with namespace/content generation, source/provenance, authority, schema, freshness/expiry, completeness, tenant/region, classification, and failure behavior.

**RM-POLICY-DATA-0002:** Identity, group, resource hierarchy, entitlement, risk, time, device, network, feature, quota, and domain data retain their own authoritative generations and cannot be collapsed into unproven attribute bags.

**RM-POLICY-DATA-0003:** Missing data behavior is selected per attribute/rule as deny, indeterminate, not-applicable, unknown propagation, explicit default, or bounded fetch; silent false/default substitution is forbidden for security-sensitive facts.

**RM-POLICY-DATA-0004:** Entity graphs bound nodes, edges, depth, cycles, fanout, duplicate identity, cross-tenant references, stale edges, and traversal work; hierarchy membership is provenance-bearing evidence.

**RM-POLICY-DATA-0005:** Data acquisition and enrichment occur outside pure evaluation under least authority, deadlines, batching, cache/freshness, privacy, circuit/admission, and partial-failure policy.

**RM-POLICY-INPUT-0003:** Time, random, IP/network, geolocation, locale, device, risk, and request observations bind exact source and scope; evaluator host state is not ambient input.
