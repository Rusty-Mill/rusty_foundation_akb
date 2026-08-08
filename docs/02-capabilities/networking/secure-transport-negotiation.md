# Policy and negotiation

**RM-SECURE-NEGOTIATION-0001:** Channel policy is immutable/versioned and declares allowed/minimum protocol versions, cipher suites/AEAD/hash, groups/KEMs, signature schemes, certificate/key profiles, PSK modes, renegotiation/post-handshake authentication, ALPN, SNI/ECH/privacy, compression/padding, resumption/early data, record/key limits, and provider requirements.

**RM-SECURE-NEGOTIATION-0002:** Policy resolution precedes provider selection and produces exact allowed/required sets plus unsupported qualities. Provider or OS defaults cannot broaden them or re-enable prohibited legacy protocols, algorithms, compression, renegotiation, fallback, or anonymous modes.

**RM-SECURE-NEGOTIATION-0003:** The client offers only policy-authorized parameters and protocols. The server selects only compatible values under its current policy; no overlap or incompatible ALPN fails rather than retrying with weaker constraints.

**RM-SECURE-NEGOTIATION-0004:** Downgrade detection, fallback signaling, version intolerance workarounds, middlebox compatibility, and provider fallback are explicit evidence. A lower version is accepted only when it independently satisfies policy, never merely because a higher attempt failed.

**RM-SECURE-NEGOTIATION-0005:** SNI/routing name, original reference identity, certificate identity, DNS canonical name, endpoint IP, proxy authority, ECH public/inner name, and application authority are distinct. Routing disclosure cannot silently replace authentication identity.

**RM-SECURE-NEGOTIATION-0006:** ALPN identifiers are ordered policy inputs and potentially observable metadata. The selected value binds application framing/semantics before application bytes; absent/unrecognized/incompatible selection is a typed failure where required.

**RM-SECURE-NEGOTIATION-0007:** HelloRetryRequest, QUIC Retry/version negotiation, stateless retry/cookie, and provider retry are protocol phases with transcript/address-validation evidence, bounded attempts, and anti-downgrade checks—not new unrestricted negotiation.

**RM-SECURE-NEGOTIATION-0008:** Negotiated limits include record/stream/datagram sizes, QUIC transport parameters, idle timeout, flow control, stream counts, connection IDs/migration, early-data maximum, and key usage. Peer-advertised values remain bounded untrusted inputs.

