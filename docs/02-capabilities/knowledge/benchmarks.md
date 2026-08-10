# Benchmark specification

No capability contract is accepted yet (see [RFC-0003](../../rfc/0003-rusty-knowledge-domain-framework.md)). This plan states the native baseline and comparison the implementation trial must use, per RFC-0002's requirement that trials bind performance claims to a benchmark plan before implementation begins.

## Native baseline

The existing Python `knowledge-mcp` server (SQLite + FTS5 + optional `sqlite-vec`, `fastmcp`/Starlette transport) is the native baseline. The trial does not benchmark against an idealized target; it benchmarks against this running system on the same corpus and hardware.

- **RM-KNOWLEDGE-BENCH-0001:** Benchmarks **MUST** publish hardware/OS, corpus size and domain count, query mix (lookup vs. search vs. cross-cutting), warmup, repetitions, and uncertainty, matching the same fixed corpus used for conformance evidence.
- **RM-KNOWLEDGE-BENCH-0002:** Ingestion/reindex benchmarks report documents and constructs indexed per second, and end-to-end time from ingestion to search-visible, for both the Python baseline and the Rust trial.
- **RM-KNOWLEDGE-BENCH-0003:** Query benchmarks report end-to-end latency distributions (lookup, hybrid search, cross-cutting traceability) for both implementations under identical query mixes, cold and warm.

## Representative workload

Derived from the Python server's existing test corpus and the UAF 1.3 domain content (the only fully populated domain today); `data_mesh`/`udra` stub domains are out of scope for benchmarking until they carry real content.

## Regression budget

Not yet set. A provisional budget is proposed only after the trial's first comparable measurement exists; asserting a target before any Rust implementation runs would be an unfounded claim.

## Status

No benchmarks have been run. This document defines the plan the trial's entry review must satisfy before authorized code begins, per RFC-0002.
