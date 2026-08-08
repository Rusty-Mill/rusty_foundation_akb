# Security and privacy

**RM-TRAFFIC-SECURITY-0001:** Discovery and routing never replace secure-channel server identity. Original service/origin authority, target-name/ALPN/protocol binding, proxy hops, mutual authentication, workload identity, and authorization are validated explicitly.

**RM-TRAFFIC-SECURITY-0002:** Registration, endpoint metadata, health, routes, weights, locality, security policy, and administrative updates are authenticated, authorized, integrity-protected, freshness/rollback-checked, and audited according to risk.

**RM-TRAFFIC-SECURITY-0003:** Compromised endpoints cannot self-assign privileged service/subset/locality/capacity/health metadata, expand tenant reach, disable security, redirect original authority, or poison other endpoints.

**RM-TRAFFIC-SECURITY-0004:** Proxy/gateway/mesh delegation attenuates service, route, method, tenant, identity propagation, credentials, metadata, network, and administrative authority with explicit trust and failure boundaries.

**RM-TRAFFIC-PRIVACY-0001:** Service queries, endpoints, topology, user/session affinity, client location/network, route experiments, health, request metadata, and traffic telemetry are classified, minimized, encrypted, partitioned, retained, and region-bound.

**RM-TRAFFIC-PRIVACY-0002:** DNS/control-plane/proxy choices expose destinations to distinct parties; encrypted transports do not hide all metadata, and privacy modes document resolver/proxy correlation, address hints, logs, and fallback.

**RM-TRAFFIC-SECURITY-0005:** Internal addresses, topology, health reasons, route policy, credentials, and tenant identifiers are redacted from external errors and untrusted diagnostics.

**RM-TRAFFIC-SECURITY-0006:** Emergency revocation can remove endpoint/service/route/credential generations despite last-known-good caches and affinity, with fail-closed boundaries and propagation evidence.
