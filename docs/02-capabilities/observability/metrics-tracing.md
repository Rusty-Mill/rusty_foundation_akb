# Metrics and tracing

## Metrics

**RM-OBSERVE-METRIC-0001:** Instruments declare stable identity, semantic description, unit, monotonicity/aggregation intent, attribute schema, and cardinality budget.

**RM-OBSERVE-METRIC-0002:** Counter, up/down counter, gauge observation, histogram/distribution, and event-derived measurement remain distinct. Exporter temporality or aggregation cannot silently change instrument meaning.

**RM-OBSERVE-METRIC-0003:** Attribute values are bounded and schema controlled. Unbounded user IDs, paths, URLs, error text, stack traces, and arbitrary configuration values are prohibited as metric dimensions.

**RM-OBSERVE-METRIC-0004:** Collection reports reset, process epoch, missed observation, overflow, and aggregation degradation. A missing series is not automatically a zero.

## Tracing

**RM-OBSERVE-TRACE-0001:** A span records an interval with explicit start/end timestamps, status, kind, attributes, events, links, and resource/execution identity. Ended spans are immutable.

**RM-OBSERVE-TRACE-0002:** Parent/child edges, links, and ordinary event correlation are distinct relationships. A provider cannot invent parentage from temporal overlap alone.

**RM-OBSERVE-TRACE-0003:** Sampling decisions and recording/export decisions are distinct. Nonrecording context may still propagate correlation without allocating a full span.

**RM-OBSERVE-TRACE-0004:** Async operations preserve logical causal context independent of thread migration. Sync instrumentation does not introduce hidden async work on the caller's critical path.

