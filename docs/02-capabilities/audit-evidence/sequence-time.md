# Sequencing, time, causality, and completeness

**RM-AUDIT-SEQUENCE-0001:** Sequence claims name source/partition/tenant/collection scope, issuer/incarnation, monotonicity, gaps, duplicates, wrap/reset, reservation, and persistence. A global total order is not inferred from distributed timestamps.

**RM-AUDIT-SEQUENCE-0002:** Causal links use authenticated request/trace/workflow/effect/context identities and explicit parent/derived/triggered-by relations. Correlation IDs group evidence but do not prove causality by themselves.

**RM-AUDIT-SEQUENCE-0003:** Source event time carries clock synchronization state, accuracy/uncertainty, clock domain and rollback evidence; collection observed/append times provide separate ordering evidence.

**RM-AUDIT-SEQUENCE-0004:** Completeness is a qualified claim over exact expected source populations, event classes, sequence ranges/frontiers, time interval, capture configuration, pipeline health, exclusions, and reconciliation result.

**RM-AUDIT-SEQUENCE-0005:** Heartbeats, signed empty intervals, sequence manifests, source inventories, and control-plane configuration evidence can strengthen gap detection but never prove uninstrumented effects absent.

**RM-AUDIT-SEQUENCE-0006:** Late, duplicated, backfilled, recovered, imported, and corrected events preserve original and observation times, source/frontier, processing generation, and reason; ordering views remain reproducible.
