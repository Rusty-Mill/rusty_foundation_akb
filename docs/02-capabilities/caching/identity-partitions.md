# Identity and privacy partitions

**RM-CACHE-IDENTITY-0001:** Cache keys are typed canonical values, not ad hoc string concatenations, and include every request property that can change the reusable representation.

**RM-CACHE-IDENTITY-0002:** Key construction names normalization, encoding, case, Unicode, query ordering, header/vary dimensions, locale, content negotiation, compression, authorization class, tenant, experiment, and version semantics.

**RM-CACHE-IDENTITY-0003:** Private, user-, tenant-, credential-, region-, policy-, and consent-dependent representations use non-colliding partitions. Shared caching is forbidden unless policy explicitly proves safe reuse.

**RM-CACHE-IDENTITY-0004:** Secrets and personal data are not exposed in keys, logs, metrics, traces, filenames, or purge interfaces; opaque keyed fingerprints preserve necessary correlation.

**RM-CACHE-IDENTITY-0005:** Representation identity distinguishes source entity, selected variant, encoded bytes, partial ranges, transformation generation, and encryption context.

**RM-CACHE-IDENTITY-0006:** Negative results bind exact authority scope, status/reason class, dependency generation, and short explicit policy; absence in one cache or replica is not global nonexistence.

**RM-CACHE-IDENTITY-0007:** Key/schema evolution uses versioned namespaces or dual-read/dual-write migration with collision, rollback, and old-generation retirement evidence.
