# Networking benchmark specification

| Workload | Metrics |
|---|---|
| Resolution | cold/warm latency, allocations, query count, cancellation latency |
| Connection racing | time to transport/secure/app-ready, attempts, loser lifetime, resource peak |
| Stream | throughput, one-way/round-trip latency, tail latency, CPU, allocations, copies, syscall transitions |
| Datagram | messages/second, latency, drops, batch efficiency, truncation handling |
| Listener | accepts/second, connection latency, backlog/overload behavior, memory/handle use |
| Secure channel | full/resumed handshake latency, CPU, bytes, memory, bulk overhead, key-operation latency |
| Path change | detection and reconnection/reconciliation latency |
| Cancellation/shutdown | terminal latency, residual resources, accepted-progress classification |

Compare portable paths with idiomatic native baselines under identical protocol, payload, socket options, security policy, and network impairment. Record hardware, OS/build, runtime/compiler, topology, MTU, link speed/latency/loss, DNS and trust providers, TLS version/cipher/group, address family, proxy/VPN, buffer/batch sizes, concurrency, warm/cold state, and statistical variance. Loopback results cannot substantiate wide-area or encrypted-production claims.

Detailed TLS/QUIC handshake, credential/trust, ticket/early-data, exporter, protected-data, overload, closure, and migration measurements are specified in [secure-transport benchmarks](secure-transport-benchmarks.md).
