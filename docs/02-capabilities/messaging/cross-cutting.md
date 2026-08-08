# Messaging cross-cutting requirements

**RM-MESSAGING-CROSS-0001:** Authentication evidence and operation/topic authorization are evaluated at dispatch and, for long streams/subscriptions, at declared revalidation points. Transport/channel identity, broker login, schema validity, message signature, and reply possession do not independently authorize domain work.

**RM-MESSAGING-CROSS-0002:** Envelopes, payloads, metadata, credentials, identifiers, topics, routing keys, filters, errors, schemas, dead letters, traces, and replay stores are classified, minimized, encrypted, partitioned, redacted, retained, exported, and erased according to declared policy.

**RM-MESSAGING-CROSS-0003:** Untrusted-input review covers parser differentials, schema bombs, unknown-field smuggling, operation confusion, reply-route injection, SSRF, filter/routing injection, unauthorized subscription, confused deputy, replay, dedup-key abuse, compression bombs, queue exhaustion, poison messages, and dead-letter leakage.

**RM-MESSAGING-CROSS-0004:** Causal context is explicit immutable data with bounded baggage and trust levels. Trace identifiers correlate evidence but grant no authority, force no sampling, and cannot become unbounded metric dimensions or cross-tenant linkability.

**RM-MESSAGING-CROSS-0005:** Observability separates logical intent, transport/broker/consumer attempts, schema and policy generations, queue/flow time, handler/domain time, settlement, retry/redelivery/dedup/reconciliation, and ambiguous outcomes while preserving sampling/drop evidence.

**RM-MESSAGING-CROSS-0006:** User-facing approvals, subscriptions, background messaging, failures, duplicates/conflicts, and reconciliation expose service/topic purpose, data/recipient, consequences, current state, progress, cancellation limits, and recovery accessibly and locally. Protocol tokens and schemas remain locale-independent.

**RM-MESSAGING-CROSS-0007:** Resource policy bounds schemas, messages, metadata, attachments, calls/streams/subscriptions, queues/in-flight deliveries, retries/hedges, decode/validation/handler time, memory/disk/network/CPU, dead letters, telemetry, and per-tenant fairness with overload shedding before exhaustion.

