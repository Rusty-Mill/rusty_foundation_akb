# Service and endpoint identity

**RM-TRAFFIC-IDENTITY-0001:** Service identity binds authority/trust domain, namespace, name, logical protocol/port, tenant/environment, and generation; DNS names, URLs, cluster names, VIPs, and provider resource IDs are representations or locators.

**RM-TRAFFIC-IDENTITY-0002:** Endpoint identity binds service generation, workload/application instance generation, transport address candidates, protocol capabilities, security identity expectations, locality/fault domain, metadata generation, and lifecycle state.

**RM-TRAFFIC-IDENTITY-0003:** Address reuse does not preserve endpoint identity, and endpoint restart/replacement creates a new generation even at the same IP/port or Unix/native endpoint.

**RM-TRAFFIC-IDENTITY-0004:** Alias, SVCB/HTTPS target, SRV target, service VIP, proxy hop, gateway, and backend address do not replace original origin/service authority; secure channels validate the selected authority mapping.

**RM-TRAFFIC-IDENTITY-0005:** Endpoint metadata has typed namespaces, provenance, visibility, size/cardinality limits, criticality, and routing authorization; untrusted labels cannot create privileged routes.

**RM-TRAFFIC-IDENTITY-0006:** Dual-stack, multiple transports/protocol versions, proxy routes, and alternative services remain ordered compatible candidates tied to the service rather than distinct identities unless product policy says otherwise.

**RM-TRAFFIC-IDENTITY-0007:** Tenant, user, credential, experiment, data-region, compliance, and session-affinity scopes are explicit route-partition inputs and protected from logs, cross-request caches, or spoofed metadata.
