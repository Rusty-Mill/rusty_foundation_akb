# Printing and document-output benchmarks

| Benchmark | Measures | Required parameters |
|---|---|---|
| PRINT-BENCH-001 | Destination enumeration and capability latency | queue count, local/network, online/offline, document format, cache state |
| PRINT-BENCH-002 | Whole-ticket resolution | dimension/constraint/override count, valid/conflicting, provider |
| PRINT-BENCH-003 | Page production throughput/tail | page complexity, vector/text/image mix, fonts, color, resolution, cold/warm resources |
| PRINT-BENCH-004 | Streaming memory/backpressure | page count/size, spool speed, in-flight bound, cancellation point |
| PRINT-BENCH-005 | Submission and state convergence | bytes/pages, local/network, protocol, failure/hold/restart, polling/event mode |
| PRINT-BENCH-006 | Artifact generation/durability | format/profile, tagging, compression, embedding, destination storage/cache state |

Measure CPU, wall time, allocations, peak committed/resident bytes, open resources, produced bytes, IPC/context switches, first-page latency, steady throughput, tail latency, cancellation convergence, and idle overhead. Separate application pagination, abstraction, format encoding, native spool, network, device, and user-interaction time.

Use deterministic synthetic corpora with recorded digests and complexity metadata. Compare identical native paths and effective tickets; do not call different formats, resolutions, color modes, filters, caches, or physical devices abstraction overhead. Sustained tests verify bounded memory and no document/spool/job/resource leakage under slow queues, repeated failures, cancellations, provider restart, and owner retirement.
