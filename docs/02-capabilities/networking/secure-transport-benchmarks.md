# Secure-transport benchmarks

**RM-SECURE-BENCH-0001:** Measure transport establishment, full/resumed/failed handshake, certificate/path/status and credential key operation, application readiness, first/early/established byte, exporter, key update, graceful/abort close, reconnect, and QUIC migration separately and end to end.

**RM-SECURE-BENCH-0002:** Workloads cover TLS-over-TCP and QUIC, client/server and mutual authentication, small/large chains, software/hardware/remote keys, cold/warm trust/ticket caches, multiple ALPNs, ECH where available, loss/latency/reorder/MTU, IPv4/IPv6 racing, proxies/VPN, many streams, datagrams, and network change.

**RM-SECURE-BENCH-0003:** Report latency distributions, handshakes/connections/streams per second, bytes/flights/packets/retransmits, CPU/memory/allocations/copies/syscalls, provider/key/trust/network waits, record/packet overhead, bulk/stream/datagram throughput, loss/congestion, cancellation/close/migration latency, and residual resources.

**RM-SECURE-BENCH-0004:** Server saturation tests report admission/amplification, handshake CPU/memory/key-operation limits, queue fairness, slowloris/pending-auth impact, ticket/anti-replay store contention, QUIC connection-ID/stream state, overload rejection, recovery, and established-channel isolation.

**RM-SECURE-BENCH-0005:** Early data reports latency benefit against full and resumed 1-RTT, acceptance/rejection/replay/deduplication rates, added anti-replay coordination cost, fallback/retry application time, and unsafe-operation rejection without using early data as the default benchmark winner.

**RM-SECURE-BENCH-0006:** Compare native/provider and Rusty Mill paths only under identical protocol/version/cipher/group/signature, trust/status/client-auth, ALPN, resumption/early-data, proxy/path, close, key-update, QUIC transport/congestion, and diagnostic guarantees.

Initial budgets remain RFC-owned after representative Windows, macOS, and Linux providers, software/hardware credentials, TLS/QUIC workloads, and impaired-network baselines exist.

