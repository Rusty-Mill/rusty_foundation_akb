# Exporters and channel binding

**RM-SECURE-EXPORTER-0001:** Exporter requests are separately attenuated channel operations available only after the protocol-defined milestone. They bind standard/application label, context bytes and presence, output length, channel generation, purpose, caller authority, and one-use/lifetime policy.

**RM-SECURE-EXPORTER-0002:** Labels are centrally domain-separated, stable, non-secret identifiers and cannot use reserved/internal namespaces. Context encoding is exact and versioned; absent and empty context remain distinguishable when the protocol does.

**RM-SECURE-EXPORTER-0003:** Exported keying material is a secret value with explicit storage, copy, logging, lifetime, derivation/use, and zeroization policy. It is not traffic key material and cannot be used as a generic password, channel identifier, or long-term key.

**RM-SECURE-EXPORTER-0004:** Channel-binding output follows an exact registered binding profile such as `tls-exporter`, binds one channel and authentication-mechanism instance, records TLS/version/exporter semantics, and is not reused across authentication attempts or connections.

**RM-SECURE-EXPORTER-0005:** Channel binding prevents credential forwarding only when the higher-layer authentication protocol correctly incorporates and verifies it. Availability of a binding does not prove that the application used it.

**RM-SECURE-EXPORTER-0006:** Early exporters, resumption exporters, ordinary exporters, QUIC secrets/APIs, and provider-specific bindings are distinct. Early exporter material is unavailable unless an RFC-selected higher protocol explicitly requires and safely handles it.

**RM-SECURE-EXPORTER-0007:** Unsupported, pre-ready, wrong-label/context, excessive-length, unauthorized, channel-changed/closed, provider-failed, and already-consumed outcomes remain distinct without revealing secret material.

