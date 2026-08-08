# Platform and provider research

## Standards and native evidence

- [RFC 9111](https://www.rfc-editor.org/rfc/rfc9111.html) defines HTTP storage eligibility, cache keys including `Vary`, freshness/age, validation, ranges, authenticated responses, stale reuse, and invalidation effects. Rusty Mill composes rather than weakens those semantics.
- Windows, Linux, and macOS provide filesystem, memory mapping, clocks, synchronization, networking, credential protection, and storage-pressure signals from existing foundation capabilities; none supplies a universal application-cache coherence contract.

## Managed edge evidence

- [Amazon CloudFront documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html) exposes versioning/invalidation, cache policy, regional edge caches, origin shield, signed access, and provider-specific propagation/cost behavior.
- [Google Cloud CDN caching](https://cloud.google.com/cdn/docs/caching) exposes configurable cache keys, freshness, validation, ranges, negative caching, signed access, and distributed edge behavior; [invalidation](https://cloud.google.com/cdn/docs/cache-invalidation-overview) is rate-limited distributed control with scoped matchers.
- [Azure Front Door caching](https://learn.microsoft.com/azure/frontdoor/front-door-caching) exposes independent edge caches, query-string behavior, freshness, validation, compression, and purge; [purge](https://learn.microsoft.com/azure/frontdoor/cache-purge) has provider-specific scope and propagation.

## Portability conclusions

**RM-CACHE-RESEARCH-0001:** The portable contract preserves exact semantic decisions and provider evidence; it does not normalize every provider knob into a false common guarantee.

**RM-CACHE-RESEARCH-0002:** Provider completion, TTL precision, eviction, invalidation reach, key normalization, range fill, negative caching, transformation, shield, signed access, logging, and billing differentials remain observable.

**RM-CACHE-RESEARCH-0003:** Products use versioned immutable identifiers for routine releases and reserve broad purge for exceptional correction or emergency response where feasible.
