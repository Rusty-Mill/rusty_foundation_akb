# Sessions, checkpoints, and reconnect

**RM-APP-SYNC-SESSION-0001:** A session binds authenticated peer replicas/incarnations, dataset/schema/policy generations, selection, direction, protocol/profile, negotiated limits, encryption, compression, start frontiers, and cancellation/deadline.

**RM-APP-SYNC-SESSION-0002:** Capability negotiation is authenticated and downgrade-resistant. Unsupported schema, causal, merge, deletion, or security semantics fail before applying changes.

**RM-APP-SYNC-SESSION-0003:** A checkpoint is scoped progress evidence with issuer, dataset/partition/selection, replica pair or topology, history lineage, frontier, expiry, integrity, and compatibility. It is not global completeness.

**RM-APP-SYNC-SESSION-0004:** Resume validates checkpoint ancestry and current authorization. Missing, expired, rolled-back, foreign, or unverifiable checkpoints trigger bounded snapshot/rebase recovery rather than skipped history.

**RM-APP-SYNC-SESSION-0005:** Connectivity notifications are retry hints. Sessions use bounded backoff, jitter, reachability probes, budgets, and product policy; a network-available signal never proves peer readiness.

**RM-APP-SYNC-SESSION-0006:** Cancellation stops local waiting and future work under explicit rules but does not retract accepted peer changes; terminal session evidence reports in-flight and ambiguous outcomes.
