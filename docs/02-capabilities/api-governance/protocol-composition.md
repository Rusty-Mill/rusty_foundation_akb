# Protocol composition

**RM-API-GOV-PROTOCOL-0001:** HTTP bindings state method, URI-template variables, representation negotiation, headers, status semantics, conditional requests, caching, redirects, and problem details without redefining the logical operation.

**RM-API-GOV-PROTOCOL-0002:** RPC bindings state service/method identity, unary or streaming shape, deadlines, cancellation, metadata, status mapping, flow control, and schema evolution profile.

**RM-API-GOV-PROTOCOL-0003:** Event bindings state channel identity, publish/subscribe operation, envelope and payload schema, partition/order scope, delivery/settlement, replay, retention, and dead-letter behavior.

**RM-API-GOV-PROTOCOL-0004:** Callbacks and webhooks are receiver-facing contracts with endpoint verification, authentication, replay protection, delivery identity, retries, ordering, acknowledgement, disablement, and redelivery limits.

**RM-API-GOV-PROTOCOL-0005:** A gateway or transcoder records loss and semantic mapping; it cannot claim equivalence when streaming, presence, errors, metadata, ordering, or security context changes.

**RM-API-GOV-PROTOCOL-0006:** OpenAPI, AsyncAPI, protobuf, and similar descriptions are accepted protocol artifacts only when traceable to logical operations and the authoritative contract release.
