# HTTP benchmark specification

**RM-HTTP-BENCH-0001:** Benchmarks publish hardware, OS/provider/build, topology, protocol/security/proxy/cache policy, connection state, payload/field distributions, concurrency, limits, impairment, clocks, sample method, variance, and raw results.

**RM-HTTP-BENCH-0002:** Workloads include small/large and streaming uploads/downloads, many fields, informational/trailers, cold/warm connections, HTTP/1.1 persistence, HTTP/2 and HTTP/3 multiplexing, slow peers, cancellation, reset, GOAWAY/drain, proxies, and cache hit/validation/miss.

**RM-HTTP-BENCH-0003:** Report throughput, goodput, request and byte latency distributions, first/last-byte time, queue time, CPU, allocations/copies, memory high-water, connection/stream counts, flow-control stalls, compression-table cost, packet/byte overhead, and energy where available.

**RM-HTTP-BENCH-0004:** Head-of-line and fairness experiments vary one large stream among small streams, loss/reorder, stream count, tenant mix, and connection count; results retain protocol failure/isolation differences rather than reducing them to aggregate throughput.

**RM-HTTP-BENCH-0005:** Redirect/auth/retry/cache/alternative-service benefits include extra round trips, bytes, duplicated server work, unknown effects, credential interaction, cache correctness, and tail latency. Unsafe automatic behavior cannot be benchmarked as the default winner.

**RM-HTTP-BENCH-0006:** Native/provider and Rusty Mill paths use identical semantics, security, proxy, cache, decoding, validation, observability, limits, and completion boundaries. Omitting a guarantee is reported, not counted as a speedup.

