# Platform and provider research

## Representation and embedded execution

- [Apache Arrow columnar format](https://arrow.apache.org/docs/format/Columnar.html) specifies typed arrays, buffers, validity, nesting, dictionaries, alignment, IPC-oriented relocatability, and extension types; it intentionally does not define mutation coordination or query semantics.
- [DuckDB Parquet support](https://duckdb.org/docs/stable/data/parquet/overview) demonstrates embedded vectorized analytical execution with projection/filter pushdown and row-group pruning over file data.
- Windows, Linux, and macOS supply memory, file, I/O, threading, process, clock, GPU, power, and isolation primitives through existing foundation capabilities, not a universal analytical plan/effect contract.

## Distributed batch and streaming

- [Apache Flink event-time and watermarks](https://nightlies.apache.org/flink/flink-docs-stable/docs/dev/datastream/event-time/generating_watermarks/) and [fault tolerance](https://nightlies.apache.org/flink/flink-docs-stable/docs/learn-flink/fault_tolerance/) expose partitioned event-time progress, state checkpoints, replay, and the source/sink conditions required for end-to-end effects.
- [Apache Spark Structured Streaming](https://spark.apache.org/docs/latest/streaming/getting-started.html) exposes incremental result tables, source offsets, checkpoint/write-ahead progress, watermarks/late state, output modes, and sink idempotency/transactions.

## Portability conclusions

**RM-ANALYTICS-RESEARCH-0001:** Portable contracts preserve typed logical semantics, versioned plans/frontiers/state/effects, resource and result evidence; they do not promise identical SQL, physical plans, byte layouts, floating reductions, timing, or costs.

**RM-ANALYTICS-RESEARCH-0002:** Providers disclose types/coercions, function/null/time/numeric behavior, source and format snapshot semantics, pushdown, optimizer/adaptive execution, shuffle/state/checkpoint, watermark/late data, sink effects, partial results, recovery, and resource limits.

**RM-ANALYTICS-RESEARCH-0003:** Provider-native extensions remain typed escape hatches with discovery, security review, configuration generation, semantic/recovery consequences, conformance exclusions, and migration evidence.
