# Real-time session and establishment model

**RM-REALTIME-SESSION-0001:** Session intent binds protocol kind/profile/version, original service and resource URI, application audience/purpose, origin policy, secure-channel and HTTP policy, proxy/network/privacy partition, credentials, subprotocol/media type, extensions, deadlines, resource limits, reconnect policy, and explicit authority.

**RM-REALTIME-SESSION-0002:** Resolving, connecting, secure-channel ready, HTTP request accepted, protocol negotiated, application authenticated, subscription authorized, application-ready, draining, closing, closed, failed, suspended, and superseded are separate monotonic milestones.

**RM-REALTIME-SESSION-0003:** Every accepted session has an immutable identity and generation, exact peer/origin/route/protocol/security evidence, negotiated parameters, creation time/clock quality, limits, and parent attempt. Connection pooling or migration cannot merge session authority.

**RM-REALTIME-SESSION-0004:** Server admission binds listener/route generation, trusted origin rules, credentials and application authorization, protocol/extensions, tenant budgets, connection/session/stream/message limits, overload behavior, and shutdown policy before application dispatch.

**RM-REALTIME-SESSION-0005:** HTTP Upgrade, extended CONNECT, successful SSE response, and WebTransport CONNECT are different establishment mappings. Redirect, challenge, proxy, retry, and early-data behavior follows the HTTP replay contract and cannot be enabled implicitly for a long-lived session.

**RM-REALTIME-SESSION-0006:** Session handles attenuate send/receive/open-stream/datagram/close/observe/reconnect operations separately. A received peer message, cursor, stream identifier, or URL never grants authority.

**RM-REALTIME-SESSION-0007:** Providers disclose browser/native/runtime restrictions, handshake/header control, cookies and credential mediation, proxy and cache behavior, compression, queueing, cancellation, keepalive, suspension/background policy, connection sharing, migration, and diagnostic quality.

