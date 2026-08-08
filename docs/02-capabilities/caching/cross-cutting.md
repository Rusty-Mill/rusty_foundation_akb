# Cross-cutting qualities

**RM-CACHE-XCUT-0001:** Security defaults deny cross-principal reuse, protect cache administration, validate untrusted metadata/serialized values, bound decompression/deserialization, and isolate poisoned or corrupt entries.

**RM-CACHE-XCUT-0002:** Privacy classifies cached data, keys, tags, access logs, location and identity signals; minimizes retention and correlation; supports erasure/revocation limits; and prevents timing/key-probing leakage where required.

**RM-CACHE-XCUT-0003:** Performance budgets cover hit/miss/validation latency, origin amplification, throughput, memory/disk/network use, serialization/compression, tail latency, contention, and provider cost without hiding correctness failures.

**RM-CACHE-XCUT-0004:** Accessibility exposes offline/stale/error/loading/update state and recovery without relying on color, sound, motion, or transient timing; background refresh does not steal focus or erase user work.

**RM-CACHE-XCUT-0005:** Internationalization preserves locale/variant identity, Unicode normalization, time/age formatting, directionality, translated diagnostics, and avoids fragmenting caches accidentally through presentation-only differences.

**RM-CACHE-XCUT-0006:** Observability records tier, outcome, age, freshness decision, validator class, entry/configuration generation, origin attempt, collapse count, invalidation epoch, size/cost, and bounded causal context without raw sensitive keys or content.

**RM-CACHE-XCUT-0007:** Metrics distinguish request hit ratio from byte, latency, cost, and origin-offload ratios; cardinality is bounded and tenant/user identifiers are not labels.

**RM-CACHE-XCUT-0008:** Shutdown drains or cancels fills, persists only coherent entries, releases leases, and reconciles ambiguous distributed mutations without blocking indefinitely.
