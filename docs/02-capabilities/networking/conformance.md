# Networking conformance specification

| Area | Required evidence |
|---|---|
| Endpoints | IPv4/IPv6/scoped parsing, formatting, IDN policy, interface-index reuse |
| Resolution | positive/negative/multiple answers, expiry, network change, cancellation/deadline, DNS64, malformed names |
| Racing | stagger/order, IPv4/IPv6, delayed/broken candidates, exactly-one commit, loser cleanup |
| Streams | partial I/O, backpressure, EOF/half-close/reset, cancellation races, concurrent directions, option disclosure |
| Datagrams | boundary preservation, truncation, zero-length, loss/reorder/duplicate injection, batch outcomes, metadata |
| Listeners | exact/wildcard/loopback/dual-stack, ephemeral port, overload, close/accept race, reuse nonclaims |
| Connectivity | constrained/expensive/unknown, route/interface changes, captive or unreachable destination nonclaims |
| Security | original-name binding, invalid/expired/untrusted certificates, ALPN, resumption, early-data replay policy, truncation |
| Lifecycle | suspend/resume, network epoch change, shutdown, resource cleanup, exporter-safe diagnostics |

Testing uses isolated namespaces/VMs and controllable DNS, proxy, TCP/UDP, and TLS peers. Fault injection covers delay, blackhole, reset, half-open, packet loss/reorder/duplication, MTU constraints, certificate rotations, clock changes, full buffers, port exhaustion, and interface removal. Reports include OS/build, network topology, resolver and trust configuration, address families, proxy/VPN/container state, async provider, protocol versions, and every unsupported quality.

