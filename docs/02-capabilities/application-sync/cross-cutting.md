# Cross-cutting qualities

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Review frontier | Application synchronization 0.1.1; architecture model 1.81.0 |
| Accountable owner | Application synchronization capability owner |
| Open blocking findings | None for planning eligibility; provider and product evidence remain required |

| Dimension | Exact requirements | Planned evidence | Qualification |
|---|---|---|---|
| Security/privacy | CROSS-0001–0003, 0007 | adversarial identity/tenant/token/context/payload suites; threat/privacy review; encrypted transport/storage evidence | Offline residuals, metadata inference, revoked peers, and diagnostics remain product/provider risks |
| Performance | CROSS-0006–0007 and BENCH-0001–0006 | semantic scenarios across backlog, topology, conflict, selection, migration, attachment, energy, and recovery matrices | no budget or native-performance claim exists before comparable runs |
| Accessibility | CROSS-0004 | keyboard and assistive-technology flows for pending, rejected, conflicted, recovery, and destructive actions | provider UI is not portable proof; product presentation remains responsible |
| Internationalization | CROSS-0004 | localized status/error/action review, bidirectional/pseudolocale layouts, locale-independent identifiers and wire data | conflict semantics never depend on localized labels or collation implicitly |
| Observability | CROSS-0003, 0005 | schema/redaction/cardinality/loss review; causal and frontier correlation; failure injection | telemetry is evidence, never sync authority or completeness proof |
| Operations | OPS-0001–0006, CROSS-0007 | pause/drain/rebase/resnapshot/repair/migration/DR exercises with receipts and recovery objectives | exact RPO/RTO and operator authority remain product inputs |

The review establishes a falsifiable evidence plan, not implemented quality.

**RM-APP-SYNC-CROSS-0001:** Authentication binds peer replica/incarnation, workload/device/account, keys, channel, dataset, direction, and session; authorization is re-evaluated for upload, download, merge, resolution, attachment, and administrative operations.

**RM-APP-SYNC-CROSS-0002:** Replicas minimize fields and causal metadata, enforce tenant/purpose/residency policy, protect at rest/in transit, support remote revocation, and disclose offline residuals honestly.

**RM-APP-SYNC-CROSS-0003:** Change payloads, errors, conflicts, logs, traces, diagnostic exports, and benchmark corpora are classified and redacted. Stable technical IDs avoid embedding personal data.

**RM-APP-SYNC-CROSS-0004:** User-visible pending/conflict/rejection/progress/storage/network states are keyboard and assistive-technology accessible, localizable, non-color-only, and operable without unsafe time pressure.

**RM-APP-SYNC-CROSS-0005:** Telemetry correlates dataset/replica/session/change/schema/policy generations, frontiers, lag, backlog, transfer, merges/conflicts, rejections, retries, compaction, and resource use without becoming authority.

**RM-APP-SYNC-CROSS-0006:** Async paths preserve cancellation, deadlines, streaming, backpressure, and bounded memory. Complete sync counterparts exist where meaningful and never create hidden runtimes.

**RM-APP-SYNC-CROSS-0007:** Limits cover object/change/batch/dependency graph/causal metadata/conflict/attachment/backlog/disk/network/CPU and hostile expansion; failure preserves recoverable local intent.
