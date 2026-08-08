# WebSocket contract

**RM-REALTIME-WS-0001:** Establishment validates ws/wss URI, original host/resource, HTTP/1.1 Upgrade or HTTP/2-/3 extended CONNECT mapping, nonce/accept proof, Origin where applicable, selected subprotocol, extensions, credentials, redirect/replay policy, and secure-channel evidence before open.

**RM-REALTIME-WS-0002:** The server selects at most one offered subprotocol and only compatible extension parameters. Missing, unsolicited, duplicated, malformed, or policy-incompatible selections fail rather than falling back to untyped application bytes.

**RM-REALTIME-WS-0003:** Application delivery preserves complete text or binary message boundaries across frames. Fragmentation, masking, control-frame interleaving, UTF-8 validation, reserved bits/opcodes, and extension processing remain protocol concerns and are bounded before exposure.

**RM-REALTIME-WS-0004:** Send acceptance, queued, partially framed, handed to transport, peer protocol receipt, application acknowledgment, and domain effect are distinct. WebSocket provides reliable ordered transport within one live channel but no durable or exactly-once delivery.

**RM-REALTIME-WS-0005:** Incoming/outgoing message and byte sizes, fragment count, queue bytes/count/time, compression ratio/context memory, control rate, outstanding work, and slow-peer behavior are bounded with backpressure or explicit rejection/close.

**RM-REALTIME-WS-0006:** Ping and pong are protocol liveness observations with nonce, deadline, unsolicited/matched state, and RTT evidence. They prove neither application health nor end-to-end domain readiness.

**RM-REALTIME-WS-0007:** Close sent/received, code/reason validity, clean handshake, transport EOF/reset/timeout, peer application acknowledgment, and residual queued messages are separate. After sending Close, new application data is rejected.

**RM-REALTIME-WS-0008:** Per-message compression is off unless selected by policy with exact extension parameters, context-takeover and window limits, sensitive-content separation, decompression bounds, and side-channel review.

