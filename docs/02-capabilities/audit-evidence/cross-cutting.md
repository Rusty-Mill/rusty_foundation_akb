# Cross-cutting qualities

**RM-AUDIT-CROSS-0001:** Producers, collectors, verifiers, indexers, investigators, auditors, administrators, key custodians, exporters, and report approvers have narrow separated authority; storage administrators cannot silently forge trusted events.

**RM-AUDIT-CROSS-0002:** Audit services protect confidentiality, integrity, availability, tenant isolation, source authentication, least disclosure, anti-enumeration, and denial-of-service resistance under hostile producers and queries.

**RM-AUDIT-CROSS-0003:** Event and evidence schemas are localizable only in presentation; stable identifiers, numeric values/units, timestamps, names, and canonical bytes never depend on display locale.

**RM-AUDIT-CROSS-0004:** Investigator/operator/report experiences provide keyboard and assistive-technology operation, semantic tables/timelines/graphs, non-color-only severity/integrity state, accessible proofs and exports, and safe error correction.

**RM-AUDIT-CROSS-0005:** Limits cover event/field/payload, schema, sources, sequence gaps, buffers/backlog, segments, proof graph, query complexity/result/export, correlations, cardinality, reports/evidence, retention, CPU/memory/storage/network, and verification work.

**RM-AUDIT-CROSS-0006:** Async ingestion/query/export/verification preserves cancellation, deadlines, streaming/backpressure, partial results, and shutdown; sync counterparts are complete where meaningful and do not create hidden runtimes.

**RM-AUDIT-CROSS-0007:** Audit pipeline health and failures are observable through an independently protected path; recursive failure reporting is bounded and cannot create an unbounded logging storm.
