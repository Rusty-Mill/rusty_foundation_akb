# HTTP proxies, gateways, tunnels, and caching

**RM-HTTP-INTERMEDIARY-0001:** A route plan distinguishes origin, forward/reverse proxy, gateway, CONNECT tunnel, authentication boundary, DNS locus, secure-channel hop, address exposure, bypass rule, and configuration provenance.

**RM-HTTP-INTERMEDIARY-0002:** Proxy auto-configuration and environment/system settings are bounded untrusted policy inputs with evaluation limits, network authority, revision, and explicit direct/fail behavior. Bypass cannot be inferred from a failed proxy.

**RM-HTTP-INTERMEDIARY-0003:** Hop-by-hop and end-to-end fields are processed per protocol. Translation between HTTP versions preserves semantic meaning or fails with evidence; it cannot copy forbidden connection-specific fields blindly.

**RM-HTTP-CACHE-0001:** Cache lookup binds method, normalized target, selected request fields, partition, authorization/privacy policy, representation metadata, validator, freshness calculation, request directives, and stored-response generation.

**RM-HTTP-CACHE-0002:** Fresh, stale-allowed, requires-validation, validation-success, validation-failure, only-if-cached miss, partial, and unusable are distinct outcomes. Heuristic freshness and disconnected use are explicit policy.

**RM-HTTP-CACHE-0003:** Cache entries have byte/count/time bounds, tenant and credential partitioning, sensitive-response rules, atomic metadata/content commitment, corruption detection, eviction evidence, and invalidation. Cache presence grants no origin authority.

**RM-HTTP-CACHE-0004:** Collapsed forwarding and stale-while-revalidate coordinate work without merging callers whose authorization, privacy partition, content negotiation, or cancellation semantics differ.

