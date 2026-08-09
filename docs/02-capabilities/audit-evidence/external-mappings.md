# SIEM, archive, and external mappings

**RM-AUDIT-MAP-0001:** Mappings to Syslog, OpenTelemetry logs, CloudEvents, provider audit feeds, SIEM schemas, data lakes, OSCAL, or archive packages bind exact source/target schema/profile versions and report semantic/representation loss.

**RM-AUDIT-MAP-0002:** Native event time/observed time, severity, facility/category, source/resource, actor, action, outcome, trace/correlation, tenant, sequence, classification, and integrity fields are preserved or marked unavailable rather than guessed.

**RM-AUDIT-MAP-0003:** Exporters use bounded authenticated/encrypted transport, batching/backpressure, retry/idempotency, checkpoint/frontier, dead-letter/quarantine, destination authorization, region, and delivery reconciliation.

**RM-AUDIT-MAP-0004:** External acceptance, durable storage, indexing, retention lock, archive transition, and successful query/restore are distinct provider milestones.

**RM-AUDIT-MAP-0005:** Provider-generated audit events remain issuer-qualified observations and are reconciled with configured sources, collection status, account/region/tenant scope, integrity facilities, and documented omissions.

**RM-AUDIT-MAP-0006:** Round-trip testing proves stable identity and required semantics; provider normalization/enrichment cannot overwrite original canonical evidence.
