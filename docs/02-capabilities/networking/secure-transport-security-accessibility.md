# Security, privacy, and accessibility

**RM-SECURE-CROSS-0001:** Handshake messages, extensions, certificates, PSK identities/tickets, SNI/ECH, ALPN, transport parameters, alerts, record/packet lengths, timing, connection IDs, migration, and errors are privacy surfaces classified before use and telemetry.

**RM-SECURE-CROSS-0002:** ECH or another privacy mechanism is a negotiated quality with configuration source/freshness, public/inner name, acceptance/retry/fallback, provider, and failure evidence. Failure cannot silently expose a protected name when policy requires confidentiality.

**RM-SECURE-CROSS-0003:** Implementations bound CPU, memory, certificates, extensions, tickets, PSKs, streams, connection IDs, retransmits, retries, key operations, trust network I/O, pending callbacks, early data, and amplification before authentication.

**RM-SECURE-CROSS-0004:** Error timing/content, alerts, retry behavior, certificate/client-identity selection, ticket acceptance, PSK lookup, padding, and closure are reviewed for identity, tenant, account, policy, and cryptographic oracles.

**RM-SECURE-CROSS-0005:** Diagnostics never log traffic/master/exporter/ticket/PSK/private keys, plaintext, reusable credentials, full certificates, SNI/ALPN/client identity, endpoints, or connection IDs by default. Structured redaction and correlation preserve operational value.

**RM-SECURE-CROSS-0006:** Interactive trust/client-credential decisions are exceptional policy surfaces that identify original service, presented identity, requesting application, credential purpose/scope, consequences, duration, and recovery accessibly; inaccessible or unattended contexts fail according to declared policy.

**RM-SECURE-CROSS-0007:** User/admin status distinguishes transport failure, handshake/policy negotiation, peer identity/trust, client credential, application protocol, replay/early data, truncation, and network migration using localized text and non-color indicators without exposing attacker-controlled strings unsafely.

**RM-SECURE-CROSS-0008:** Security overrides are narrow, authenticated, time-bound, service/policy/digest constrained, auditable, and unavailable to untrusted content. “Accept any certificate,” disabled hostname checks, and silent version/cipher fallback are prohibited stable behavior.

