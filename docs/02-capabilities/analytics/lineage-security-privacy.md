# Lineage, security, and privacy

**RM-ANALYTICS-LINEAGE-0001:** Lineage binds source dataset/field generations through logical expressions, joins/aggregates/windows/functions, plans/attempts, checkpoints, and sink result generations with declared granularity and gaps.

**RM-ANALYTICS-LINEAGE-0002:** Lineage is evidence, not authorization or proof of semantic correctness; dynamic code, external lookups, nondeterminism, opaque provider operators, and manual changes remain explicit gaps.

**RM-ANALYTICS-SECURITY-0001:** Authorization applies at catalog, dataset/snapshot, partition/row, field, function, model, query/operator, source/sink, resource, diagnostic, and administrative boundaries and is revalidated for long jobs under policy.

**RM-ANALYTICS-SECURITY-0002:** Row/column masking and filtering occur before unauthorized data reaches functions, joins, statistics, errors, profiles, caches, shuffle, spill, state, checkpoints, outputs, or side channels unless a privileged trusted boundary is selected.

**RM-ANALYTICS-SECURITY-0003:** Query text/plans, formats, functions/code, connectors, credentials, manifests/catalog metadata, serialized state, checkpoints, and results are untrusted or privileged inputs with validation, isolation, least authority, and supply-chain evidence.

**RM-ANALYTICS-PRIVACY-0001:** Source/intermediate/result data, statistics, queries, lineage, logs, profiles, spills/shuffles/state/checkpoints, samples, and evaluation sets are classified, minimized, encrypted, retained, erased/exported, and region-bound under governance.

**RM-ANALYTICS-PRIVACY-0002:** Aggregation is not automatic anonymization. Small groups, joins, repeated queries, differencing, sketches, sampling, and model outputs require disclosure controls, budgets, review, and audit where applicable.

**RM-ANALYTICS-SECURITY-0004:** Errors and diagnostics prevent data, schema, path, credential, plan, tenant, statistics, or row leakage while preserving privileged forensic evidence.
