# Cross-cutting qualities

**RM-APP-SYNC-CROSS-0001:** Authentication binds peer replica/incarnation, workload/device/account, keys, channel, dataset, direction, and session; authorization is re-evaluated for upload, download, merge, resolution, attachment, and administrative operations.

**RM-APP-SYNC-CROSS-0002:** Replicas minimize fields and causal metadata, enforce tenant/purpose/residency policy, protect at rest/in transit, support remote revocation, and disclose offline residuals honestly.

**RM-APP-SYNC-CROSS-0003:** Change payloads, errors, conflicts, logs, traces, diagnostic exports, and benchmark corpora are classified and redacted. Stable technical IDs avoid embedding personal data.

**RM-APP-SYNC-CROSS-0004:** User-visible pending/conflict/rejection/progress/storage/network states are keyboard and assistive-technology accessible, localizable, non-color-only, and operable without unsafe time pressure.

**RM-APP-SYNC-CROSS-0005:** Telemetry correlates dataset/replica/session/change/schema/policy generations, frontiers, lag, backlog, transfer, merges/conflicts, rejections, retries, compaction, and resource use without becoming authority.

**RM-APP-SYNC-CROSS-0006:** Async paths preserve cancellation, deadlines, streaming, backpressure, and bounded memory. Complete sync counterparts exist where meaningful and never create hidden runtimes.

**RM-APP-SYNC-CROSS-0007:** Limits cover object/change/batch/dependency graph/causal metadata/conflict/attachment/backlog/disk/network/CPU and hostile expansion; failure preserves recoverable local intent.
