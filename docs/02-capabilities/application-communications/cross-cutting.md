# Cross-cutting qualities

**RM-COMMS-CROSS-0001:** Sender/operator/service authority is least-privilege and tenant/purpose/channel scoped; provider credentials, webhook secrets, signing keys, and push subscription secrets use governed secret lifecycles.

**RM-COMMS-CROSS-0002:** Recipient endpoints, preferences, inferred engagement, message content, attachments, conversations, provider metadata, and telemetry are classified, minimized, purpose/region/retention controlled, export/correction/erasure/hold aware, and protected from cross-tenant access.

**RM-COMMS-CROSS-0003:** Logs/traces avoid full addresses/numbers/tokens/content/links by default; stable pseudonymous correlation has rotation and access policy. Metrics bound cardinality and small-population disclosure.

**RM-COMMS-CROSS-0004:** Every human-facing channel preserves language/direction, readability, semantic structure, alternatives, operable actions, clear sender/purpose, preference controls, and accessible error/correction paths.

**RM-COMMS-CROSS-0005:** Limits cover audience, template complexity, payload/attachment, recipients/message, schedules, attempts, callbacks, inbound depth, redirects, cardinality, queue/storage, CPU/network/cost, and hostile decompression/parsing.

**RM-COMMS-CROSS-0006:** Async paths preserve cancellation, deadline, streaming/backpressure, partial results, and shutdown. Sync counterparts are complete where meaningful and never create hidden runtimes.

**RM-COMMS-CROSS-0007:** Security, account recovery, privacy rights, tenant closure, and emergency communications have explicit availability and fallback policy and do not depend blindly on promotional providers or shared suppression classes.
