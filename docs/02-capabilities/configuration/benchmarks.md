# Configuration benchmark specification

Benchmarks measure the abstraction and the native baseline under identical source content.

| Workload | Primary metrics |
|---|---|
| Cold resolve | wall time, allocations, bytes read, keys/second |
| Warm snapshot read | latency distribution, throughput, contention |
| Single-key reload | invalidation-to-publication latency, bytes reparsed, allocations |
| Burst changes | convergence latency, coalescing ratio, peak queue/memory |
| Large schema/source | scaling by keys, depth, document bytes, constraint edges |
| Rejection path | validation/diagnostic latency and retained memory |
| Observer lifecycle | registrations, handles/descriptors, cancellation/shutdown latency |

Results record hardware, power state, OS build, filesystem/native store, parser/provider versions, source count and sizes, schema shape, reader/writer concurrency, and whether caches are cold or warm. Tail latency and memory bounds are release gates; averages alone are insufficient. No benchmark fixture contains production secrets.

