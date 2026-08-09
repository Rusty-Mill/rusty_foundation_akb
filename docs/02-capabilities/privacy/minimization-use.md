# Collection, minimization, and use limitation

**RM-PRIVACY-MINIMIZE-0001:** Before collection, the plan justifies each element/category, precision, granularity, frequency, duration, subject population, source, linkability, and whether local/on-device, ephemeral, aggregated, sampled, delayed, or user-provided alternatives can satisfy the purpose.

**RM-PRIVACY-MINIMIZE-0002:** Collection endpoints enforce schema allowlists, field projection, size/rate/time bounds, purpose token, tenant/subject partition, source/recipient identity, consent/preference/policy generation, and rejection of undeclared extra fields.

**RM-PRIVACY-MINIMIZE-0003:** Optional fields remain optional through UI, APIs, schemas, storage, analytics, and exports. Dark patterns, permission bundling, silent fallback collection, and using denial as unrelated service degradation are product-policy violations surfaced by conformance.

**RM-PRIVACY-MINIMIZE-0004:** Accuracy, completeness, and freshness requirements are purpose-specific; overcollection “just in case” is prohibited. Derived/inferred values expose uncertainty, provenance, correction limits, and whether consequential decisions may use them.

**RM-PRIVACY-MINIMIZE-0005:** Use enforcement checks purpose/action/data/subject/actor/recipient/location/time/plan generations at the data-access boundary and records actual projections. A service account's broad storage authority is not purpose authority.

**RM-PRIVACY-MINIMIZE-0006:** Debugging, telemetry, support, security, fraud, quality, personalization, analytics, model training, advertising, and product improvement are separate purposes unless an exact reviewed plan composes them.

**RM-PRIVACY-MINIMIZE-0007:** Temporary buffers, queues, retries, spill, caches, indexes, logs, traces, crash data, clipboard, exports, and third-party SDK paths are included in minimization and retention rather than treated as invisible implementation detail.
