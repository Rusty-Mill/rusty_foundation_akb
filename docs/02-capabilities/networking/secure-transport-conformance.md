# Secure-transport conformance

Every report binds TLS/QUIC/provider/build, role, original service identity, transport/proxy/network topology, policy/trust/credential generations, protocol parameters, clocks, fixtures, and result evidence.

**RM-SECURE-CONFORMANCE-0001:** Handshake corpora cover valid TLS 1.3 and selected legacy profiles plus malformed/truncated/reordered/duplicate/unknown messages/extensions, huge ClientHello/certificates, fragmentation/coalescing, HelloRetry/Retry, version/cipher/group/signature mismatch, downgrade/fallback, alerts, and timeout/cancel.

**RM-SECURE-CONFORMANCE-0002:** Authentication tests cover original DNS/IP/URI/service identity through proxies/canonical names, alternate/cross-signed/untrusted/expired/revoked/weak certificates, raw-key/PSK profiles, missing/optional/required/post-handshake client auth, credential selection/privacy, provider interaction, rotation, and mapping nonclaims.

**RM-SECURE-CONFORMANCE-0003:** Negotiation tests cover version intolerance, ALPN absent/unknown/incompatible/privacy, SNI/ECH accepted/rejected/retry/fallback, policy/provider generations, disabled legacy algorithms/renegotiation/compression, authenticated transport parameters, and no silent weakening.

**RM-SECURE-CONFORMANCE-0004:** Resumption tests cover scoped/fresh/stale/expired/rotated/corrupt/replayed/cross-service/cross-ALPN/cross-tenant tickets, trust/credential/policy changes, full-handshake fallback, PSK modes, cache bounds, snapshot/fork, and new-channel evidence.

**RM-SECURE-CONFORMANCE-0005:** Early-data tests cover replay, distributed anti-replay failure, operation type/size/identity/authorization, ALPN/policy change, accept/reject/partial/indeterminate, client-auth absence, automatic-retry prohibition, application deduplication, and unsafe side-effect rejection.

**RM-SECURE-CONFORMANCE-0006:** Data/close tests cover partial bidirectional I/O, backpressure, record boundaries, invalid tags, limits/key exhaustion/update, cancel races, clean close, one-sided close-notify, EOF truncation, alerts/reset/abort/timeout, suspend/network/provider changes, and resource cleanup.

**RM-SECURE-CONFORMANCE-0007:** Exporter/binding tests cover registered labels/context encoding, lengths, authority/lifetime/one-use, pre-ready/closed/wrong-channel/resumed/early contexts, uniqueness, higher-layer verification, secret redaction, and unavailable provider behavior.

**RM-SECURE-CONFORMANCE-0008:** QUIC tests cover Initial/Handshake/1-RTT levels, version negotiation/Retry/amplification, transport parameters, stream limits/flow/reset/finish, datagrams, packet/key phases, loss/PTO/congestion, NAT rebinding/migration/path validation, connection IDs/stateless reset, MTU, idle/draining/close, and network change.

**RM-SECURE-CONFORMANCE-0009:** Cross-platform matrices cover Schannel/SSPI, Apple Network.framework, selected Linux/portable providers, software/hardware/remote credentials, IPv4/IPv6/proxy/VPN, and declared provider/OS variance without weakening expected semantics.

