# Content delivery and edge behavior

**RM-CACHE-EDGE-0001:** Edge configuration binds distribution/provider generation, origins, host/path routing, cache-key policy, allowed methods/statuses, headers/cookies/query dimensions, TTLs, compression/transformation, regions, and authority.

**RM-CACHE-EDGE-0002:** Origin request identity and viewer request identity remain distinct across rewrites, normalization, redirects, signed access, proxies, and host/TLS termination.

**RM-CACHE-EDGE-0003:** Origin shield and hierarchical fills expose which tier served, validated, or failed and prevent unbounded retry amplification toward the origin.

**RM-CACHE-EDGE-0004:** Edge transformations bind exact input representation and transformation/configuration generation; transformed bytes have their own descriptor, validation, range, and purge identity.

**RM-CACHE-EDGE-0005:** Signed URLs/cookies/tokens are bearer authority with bounded scope, audience, method, path, variant, time, key generation, client constraints where safe, and log/referrer redaction.

**RM-CACHE-EDGE-0006:** Geo, device, language, experiment, personalization, authorization, and consent variation either enters the cache key/partition or bypasses shared caching.

**RM-CACHE-EDGE-0007:** Edge failover names origin health evidence, routing generation, stale policy, write exclusion, recovery, and split-view risk; an edge hit does not prove origin health.

**RM-CACHE-EDGE-0008:** Propagation objectives and measurements distinguish configuration, DNS/routing, certificate, content fill, and invalidation convergence.
