# QUIC-specific secure transport

**RM-SECURE-QUIC-0001:** A QUIC intent jointly binds UDP/network authority, original service identity, QUIC version policy, TLS 1.3-or-later policy, ALPN, authenticated transport parameters, connection/stream/datagram limits, congestion/loss policy, migration, address validation, resumption/early data, and application profile.

**RM-SECURE-QUIC-0002:** QUIC Initial protection is not peer authentication or confidentiality against observers. Application data is unavailable until its encryption level and required handshake/authentication/confirmation milestone permit it.

**RM-SECURE-QUIC-0003:** Version negotiation and Retry are unauthenticated or specially authenticated protocol inputs with downgrade, token/address binding, attempt, amplification, and privacy policy. Retry changes connection state but not original service authority.

**RM-SECURE-QUIC-0004:** TLS carries authenticated QUIC transport parameters and ALPN. Missing, duplicate, illegal, incompatible, excessive, or changed parameters fail with precise QUIC/TLS evidence.

**RM-SECURE-QUIC-0005:** Streams have independent identity, direction, flow control, reset/stop-sending, finish, cancellation, priority quality, and application framing. Connection close and one-stream failure are distinct.

**RM-SECURE-QUIC-0006:** QUIC datagrams are optional bounded unreliable messages without retransmission, ordering, fragmentation/reassembly, or delivery guarantee beyond the negotiated application profile.

**RM-SECURE-QUIC-0007:** Connection IDs, stateless reset tokens, path challenges, preferred addresses, NAT rebinding, active migration, multipath extensions, and connection migration are privacy/security-sensitive evidence. New paths are validated and policy-authorized before substantive use.

**RM-SECURE-QUIC-0008:** Packet-number spaces, key phases/updates, loss detection, PTO, congestion control, amplification, MTU/fragmentation, idle timeout, and anti-abuse limits remain QUIC transport semantics and cannot be projected as TLS stream behavior.

**RM-SECURE-QUIC-0009:** QUIC connection close records transport/application error space, initiator, encryption level, reason redaction, draining/closing/idle/stateless-reset/path-loss state, stream residuals, and peer-receipt nonclaims.

