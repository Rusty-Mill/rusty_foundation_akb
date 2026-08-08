# Channel model and readiness

**RM-SECURE-CHANNEL-0001:** A channel intent binds client/server role, original typed service identity, transport and proxy/tunnel context, TLS/QUIC/profile policy, application protocol identifiers, peer/client authentication, credential authority, trust/reference identity, resumption/early-data, privacy, deadlines, exporters, and closure requirements.

**RM-SECURE-CHANNEL-0002:** Channel states distinguish `transport-ready`, `crypto-negotiating`, `peer-presented`, `peer-verified`, `client-auth-requested`, `application-protocol-selected`, `early-data-sent/accepted/rejected`, `application-ready`, `key-updating`, `closing`, `cleanly-closed`, `truncated`, `aborted`, `failed`, and `indeterminate`.

**RM-SECURE-CHANNEL-0003:** Application readiness requires handshake completion/confirmation, every required peer/client authentication and original-identity check, compatible ALPN/application protocol, authenticated transport parameters where applicable, and current policy acceptance.

**RM-SECURE-CHANNEL-0004:** A channel identity includes channel generation, role, original service reference, local/peer endpoints and changes, proxy/tunnel chain, protocol/version, cipher/hash/group/signature schemes, authentication/trust evidence, ALPN, resumption/early-data, provider, policy generations, and handshake transcript/exporter context identifiers.

**RM-SECURE-CHANNEL-0005:** Authentication establishes only protocol-scoped peer evidence. It does not establish user/account authorization, application readiness beyond negotiated protocol, safe content, message framing, durable delivery, or current control after channel termination.

**RM-SECURE-CHANNEL-0006:** Channel handles are linear generation-scoped resources. Raw provider handles, traffic keys, master secrets, ticket keys, and private credentials are not exposed through the common contract.

**RM-SECURE-CHANNEL-0007:** Client and server listeners resolve policy/credential/trust snapshots per accepted channel under declared caching. Rotation affects new channels and optional controlled reauthentication/reconnect, not silent mutation of established evidence.

**RM-SECURE-CHANNEL-0008:** Result evidence is immutable and preserves every negotiated, verified, declined, unsupported, overridden, unknown, and nonclaimed property. Convenience success cannot erase weaker-than-requested or unavailable qualities.

