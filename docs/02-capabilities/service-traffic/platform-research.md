# Platform and provider research

## Standards and native evidence

- Existing [network resolution foundations](../networking/resolution.md) treat results as expiring candidates rather than authority. [RFC 9460](https://www.rfc-editor.org/rfc/rfc9460.html) adds DNS SVCB/HTTPS service alternatives and parameters while preserving original origin authority and requiring bounded alias/fallback behavior.
- Windows DNS/service APIs, Linux resolver/system service stacks, and macOS Network/DNS-SD frameworks expose different discovery, caching, network-context, and callback behavior; none defines a universal service-routing policy.

## Control and data planes

- [gRPC load balancing](https://grpc.io/docs/guides/custom-load-balancing/) composes name resolution with client-side policy and channels/connections, illustrating that resolver candidates and balancer choice are separate.
- [Kubernetes EndpointSlices](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/) expose partitioned endpoint sets, address families, ready/serving/terminating conditions, topology, and multiple controllers that consumers must aggregate and reconcile.
- [Envoy outlier detection](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/upstream/outlier) exposes passive ejection as configurable statistical routing behavior rather than authoritative endpoint lifecycle.

## Portability conclusions

**RM-TRAFFIC-RESEARCH-0001:** Portability preserves service/endpoint identity, snapshot/policy generations, authority, health evidence, route/attempt semantics, propagation, and outcomes—not identical algorithms, connection pools, update timing, or provider topology.

**RM-TRAFFIC-RESEARCH-0002:** Providers disclose resolution/watch consistency, endpoint conditions, metadata, health, balancing/affinity, retry/circuit/outlier, locality/failover, control acknowledgments, mixed generations, security, and limits.

**RM-TRAFFIC-RESEARCH-0003:** DNS, native discovery, registries, orchestrators, meshes, gateways, and client libraries remain selectable adapters; no one becomes the portable semantic model.
