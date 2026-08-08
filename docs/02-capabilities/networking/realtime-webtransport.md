# WebTransport contract

**RM-REALTIME-WT-0001:** WebTransport support is versioned experimental capability until its selected IETF/W3C profiles are stable. Resolution records exact draft/standard revisions, settings/codepoints, provider, interoperability set, and incompatible-version failure; no generic `webtransport` claim is sufficient.

**RM-REALTIME-WT-0002:** Establishment binds HTTPS resource, HTTP/3 extended CONNECT profile, Origin where applicable, secure original service, application authentication/authorization, required HTTP/3/QUIC settings and transport parameters, session limits, pooling policy, and response evidence.

**RM-REALTIME-WT-0003:** A session exposes incoming/outgoing unidirectional streams, bidirectional streams, datagrams, drain, and close as distinct operations. It does not invent a common ordered message channel across them.

**RM-REALTIME-WT-0004:** Each reliable stream has session association, initiator/direction, generation, ordered bytes, send/receive flow-control state, final size, reset/stop codes, partial progress, and independent lifecycle. Session, HTTP/3 connection, and QUIC connection failures remain distinct scopes.

**RM-REALTIME-WT-0005:** Datagrams preserve one bounded payload boundary but may be dropped, reordered, duplicated, or size-limited. Send means queue admission, not network transmission or peer receipt; incoming/outgoing queues expose drop policy and counters.

**RM-REALTIME-WT-0006:** Maximum datagram size is a time/path/provider-qualified observation. Oversize behavior, path change, proxy translation, fragmentation prohibition, expiry, priority, queue count/bytes/time, and congestion interaction are explicit.

**RM-REALTIME-WT-0007:** Session-, connection-, and stream-level flow controls compose without deadlock or unfair starvation. Pre-establishment/out-of-order streams and datagrams use strict byte/count/time bounds and deterministic reject/drop evidence.

**RM-REALTIME-WT-0008:** Pooling multiple sessions on one HTTP/3 connection requires compatible origin authority, credentials/privacy partition, security/transport policy, congestion/fairness, migration, and failure-coupling policy; a shared connection grants no cross-session authority.

**RM-REALTIME-WT-0009:** Drain/GOAWAY prevents or discourages new session/stream admission according to the selected profile while bounding existing work. Session close code/reason, per-stream resets, datagram loss, connection close, and application completion remain separate.

