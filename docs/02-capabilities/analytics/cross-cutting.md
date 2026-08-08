# Cross-cutting qualities

**RM-ANALYTICS-XCUT-0001:** Secure defaults deny ambient connector/function authority, unrestricted code, dynamic unreviewed schemas, cross-tenant execution, unbounded query/regex/nesting/cardinality, plaintext spill/state, raw diagnostics, and unverified plans/checkpoints.

**RM-ANALYTICS-XCUT-0002:** Performance budgets cover planning, scan/decode, pushdown/pruning, operator/kernel, exchange, spill, state/checkpoint, sink, startup/warmup, recovery, CPU/memory/disk/network/GPU, energy, and monetary cost without weakening semantics silently.

**RM-ANALYTICS-XCUT-0003:** Accessibility exposes job/query state, progress and uncertainty, partial/stale/late/corrected results, errors and recovery, tables/charts through semantic alternatives, keyboard operation, non-color encoding, reduced motion, and controllable updates.

**RM-ANALYTICS-XCUT-0004:** Internationalization preserves Unicode, locale/collation, calendar/time-zone/DST, numeric/date display versus computation, translated metadata/diagnostics, directionality, and multilingual field semantics without hidden locale-dependent plans.

**RM-ANALYTICS-XCUT-0005:** Observability records job/plan/stage/task/attempt/configuration generations, source/sink/checkpoint/frontier/watermark, operator rows/bytes/state/backpressure/spill, resources/cost, partial/retry/recovery, lineage, and causal context with classification and cardinality controls.

**RM-ANALYTICS-XCUT-0006:** Progress distinguishes estimated and exact source discovery, input read, stages, watermark, checkpoint, sink/materialization commit, and convergence; percentages never imply semantic completeness beyond their denominator.

**RM-ANALYTICS-XCUT-0007:** Lifecycle drains or cancels sources/tasks/sinks, coordinates final checkpoints only when authorized, reconciles prepared effects, preserves declared state, and bounds orphan cleanup.
