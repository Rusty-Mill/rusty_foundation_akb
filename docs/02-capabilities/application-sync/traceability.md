# Application synchronization assertion traceability

**Status:** Draft assertion mapping  
**Authority:** [Application synchronization domain](README.md)

| Assertion | Covered normative source files | Verification intention |
|---|---|---|
| `rm.assertion.application-sync.identity-session@1` | `model.md`, `datasets-replicas.md`, `sessions-checkpoints.md` | Verify dataset/replica/member/object/change identity, generations, authenticated sessions, ancestry, checkpoints, negotiation, and frontiers. |
| `rm.assertion.application-sync.snapshot-change@1` | `snapshots-changes.md` | Verify snapshot consistency, atomic change application, prerequisites, ordering, duplication, rejection, and resumable transfer. |
| `rm.assertion.application-sync.convergence-conflict@1` | `causality-convergence.md`, `conflicts-merge.md` | Verify causal context, topology-qualified convergence, typed CRDT/OT/custom merge policy, explicit conflicts, determinism, and authority. |
| `rm.assertion.application-sync.offline-effect@1` | `offline-effects.md` | Verify durable local intent, optimistic projections, attempt/effect milestones, idempotency, rejection, correction, and reconciliation. |
| `rm.assertion.application-sync.selection-deletion@1` | `selective-sync.md`, `deletion-compaction.md` | Verify selection boundaries, authorization, completeness, tombstones, resurrection prevention, retirement frontiers, and safe compaction. |
| `rm.assertion.application-sync.evolution-attachment@1` | `schema-migration.md`, `attachments.md` | Verify directional schema evolution, mixed-version replicas, migration, opaque/large attachment identity, chunking, integrity, and garbage collection. |
| `rm.assertion.application-sync.operations-qualities@1` | `operations-recovery.md`, `cross-cutting.md`, `platform-research.md`, `traceability.md` | Verify backup/restore, replica replacement, corruption/partition recovery, privacy/security/accessibility/i18n/observability/performance, platform variance, and traceability governance. |

**RM-SYNC-TRACE-0001:** Every synchronization capability requirement MUST map to a stable semantic assertion before Experimental promotion.

**RM-SYNC-TRACE-0002:** Executable histories MUST bind topology, membership, policy/schema generations, initial state, operations, causal schedule, partitions, clocks, faults, expected admissible outcomes, and final comparison frontier.

**RM-SYNC-TRACE-0003:** A convergence assertion MUST quantify eligible replicas and quiescence/fair-delivery assumptions and MUST NOT treat wall-clock equality, arrival order, or silent last-writer-wins as universal conflict authority.

**RM-SYNC-TRACE-0004:** Local durability, upload acceptance, authoritative application, remote observation, and convergence MUST remain distinct case milestones.
