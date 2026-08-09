# Capture boundaries and atomicity

**RM-AUDIT-CAPTURE-0001:** Each required event type names the exact semantic boundary: request receipt, authorization decision, plan approval, native acceptance, durable commit, external effect receipt, read/disclosure, administrative action, or evidence operation.

**RM-AUDIT-CAPTURE-0002:** Capture-at-effect uses the same transaction/outbox where possible or a reconciled receipt protocol. Logging before an effect cannot claim completion; logging after without atomicity exposes an explicit loss window.

**RM-AUDIT-CAPTURE-0003:** Required events define fail-closed, bounded-spool/degraded, or continue-with-alert behavior under audit-pipeline failure. The mode depends on event class/risk and cannot deadlock emergency/security recovery silently.

**RM-AUDIT-CAPTURE-0004:** Producers receive an append receipt with collection/partition, event ID/digest, accepted schema, sequence/frontier, durability/protection state, and ambiguity. Receipt timeout does not prove rejection.

**RM-AUDIT-CAPTURE-0005:** Reads, searches, exports, support impersonation, break-glass, policy changes, audit configuration, key/proof operations, retention/hold, and audit-record access are themselves audited under recursion-safe policy.

**RM-AUDIT-CAPTURE-0006:** Sampling is prohibited for mandatory high-risk/deny/error/break-glass/disclosure/evidence-administration classes. Permitted sampling declares population, selection algorithm/seed, denominator, weight, and loss.

**RM-AUDIT-CAPTURE-0007:** Reconciliation compares domain/source populations and audit frontiers and produces gap/duplicate/orphan evidence without inventing original event-time facts.
