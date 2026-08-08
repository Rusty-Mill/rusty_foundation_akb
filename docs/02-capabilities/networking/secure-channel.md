# Secure-channel boundary

A secure-channel service composes a connected transport with cryptographic protocol, peer-authentication, credential, trust, and application-protocol policy. TLS is an initial realization, not the only possible protocol.

**RM-NETWORK-SECURE-0001:** Inputs include original service identity, role, protocol/version policy, trust roots/provider identity, peer-name rules, application protocol identifiers, credential authority, resumption/early-data policy, deadline, and underlying transport.

**RM-NETWORK-SECURE-0002:** Cryptographic handshake completion, peer authentication, hostname/service-identity validation, client authentication, and application-protocol negotiation are distinct outcomes.

**RM-NETWORK-SECURE-0003:** Validation binds the original service identity. A DNS canonical name, resolved IP address, proxy endpoint, or redirect cannot silently replace it.

**RM-NETWORK-SECURE-0004:** Trust evaluation records policy/provider/version, chain or identity evidence, validity time source, revocation/online-check quality, user/admin override provenance, and failure category without exposing private keys.

**RM-NETWORK-SECURE-0005:** Private keys remain in the selected secret/key-operation boundary where possible. Export of raw key material is not required by the channel contract.

**RM-NETWORK-SECURE-0006:** Session resumption and zero/early data are optional qualities. Early data is disabled by default unless the application operation is explicitly replay-safe and policy permits it.

**RM-NETWORK-SECURE-0007:** Secure close, transport EOF, truncation suspicion, peer alert, local policy failure, and abort remain distinct. Encryption does not supply application message framing or durable delivery.

The detailed TLS/QUIC handshake, negotiation, authentication, resumption/early-data, exporter/channel-binding, protected-data, closure, migration, conformance, and benchmark contracts are in the [secure transport and channel foundation](secure-transport-README.md). This boundary summary does not override those requirements.
