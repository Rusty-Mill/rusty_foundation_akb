# Real-time transport benchmark specification

**RM-REALTIME-BENCH-0001:** Benchmarks publish hardware, OS/provider/protocol/draft builds, topology, HTTP/security/proxy/pooling policy, payload and fanout distributions, concurrency, limits, impairment, foreground/background state, clocks, samples, variance, and raw results.

**RM-REALTIME-BENCH-0002:** Workloads cover cold/warm establishment, small/large and fragmented WebSocket messages, SSE event rates and reconnect catch-up, WebTransport uni/bidirectional streams and datagrams, many sessions on shared/separate connections, slow consumers, heartbeats, compression, cancellation, drain, and reconnect storms.

**RM-REALTIME-BENCH-0003:** Report establishment and time-to-application-ready distributions, message/event/stream/datagram goodput and latency, queueing and flow-control stalls, drops/gaps/duplicates, reconnect/catch-up time, fairness, CPU, allocations/copies, memory high-water, network overhead, wakeups, and energy where available.

**RM-REALTIME-BENCH-0004:** Fanout and fairness vary tenants, session/stream counts, one large flow among small flows, loss/reorder/MTU, proxy hops, connection pooling, compression contexts, subscriber speed, and server admission limits while reporting tail behavior and collateral failure scope.

**RM-REALTIME-BENCH-0005:** Liveness/reconnect experiments include detection time, false positives, sleep/network transition, server drain/restart, credential rotation, state loss, backoff/jitter, duplicate work, backlog recovery, and fleet load; aggressive reconnect cannot win without its costs.

**RM-REALTIME-BENCH-0006:** Native/provider and Rusty Mill paths use identical protocol revisions, security/origin/auth, proxy, compression, queue/flow limits, payload semantics, completion boundaries, observability, and correctness checks. Missing guarantees are disclosed rather than scored as performance gains.

