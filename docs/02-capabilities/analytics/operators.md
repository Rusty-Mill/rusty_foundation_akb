# Operators, joins, windows, and aggregates

**RM-ANALYTICS-OP-0001:** Scan, filter, projection, sort, limit, union/intersection/difference, explode/unnest, distinct, and top-k operators preserve declared bag/set, order, null, error, and early-termination semantics across vectorized and row execution.

**RM-ANALYTICS-JOIN-0001:** Joins declare inner/outer/semi/anti/cross/as-of/interval semantics, key equality/collation/null behavior, temporal bounds, duplicate multiplicity, residual predicates, output identity, and boundedness.

**RM-ANALYTICS-JOIN-0002:** Hash, merge, nested-loop, broadcast, lookup, interval, and provider join algorithms are physical choices whose prerequisites, skew/spill, build/probe authority, and failure behavior remain observable.

**RM-ANALYTICS-AGG-0001:** Aggregates declare input/filter/distinct, grouping sets, null/empty behavior, accumulator and merge types, associativity/commutativity, order sensitivity, overflow/precision, approximation/error, and deterministic finalization.

**RM-ANALYTICS-WINDOW-0001:** Analytical windows bind partition/order/frame type and bounds, peer/null behavior, tie ordering, functions, and memory/spill limits.

**RM-ANALYTICS-OP-0002:** Approximate distinct, percentile, sample, sketch, heavy-hitter, and similar operators name algorithm/version, parameters, seed, merge compatibility, error/confidence contract, adversarial limits, and unsupported interpretations.

**RM-ANALYTICS-OP-0003:** User-defined operators/functions declare type/state/lifecycle, determinism, side effects, authority, serialization/upgrades, resource quotas, isolation, cancellation, checkpoint, and replay behavior.

**RM-ANALYTICS-OP-0004:** CPU/GPU/SIMD/native kernels are selected only when their numeric, null, error, ordering, determinism, memory-safety, and device-failure differentials satisfy the logical contract.
