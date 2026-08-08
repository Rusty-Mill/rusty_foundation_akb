# Protected data and closure

**RM-SECURE-DATA-0001:** TLS preserves an ordered protected byte stream, not write boundaries or messages. QUIC preserves per-stream byte ordering and optional datagram boundaries with independent loss/order semantics. Application framing remains above the channel.

**RM-SECURE-DATA-0002:** Reads/writes expose partial progress, backpressure, direction concurrency, cancellation, provider buffering, record/packet limits, plaintext/ciphertext buffer ownership, copy behavior, and accepted-versus-peer-processed nonclaims.

**RM-SECURE-DATA-0003:** Authenticated plaintext is released only after record/packet authentication and protocol validation. Failed records, invalid tags, key phase errors, and unauthenticated early input cannot leak partial plaintext through ordinary established-data APIs.

**RM-SECURE-DATA-0004:** Traffic-key/record/packet number limits, nonce construction, sequence exhaustion, key update, and connection termination follow cryptographic/protocol policy. Counter wrap or snapshot reuse is fatal rather than reset.

**RM-SECURE-DATA-0005:** TLS close-notify sent, peer close-notify received, bidirectional clean close, transport FIN/EOF without alert, reset, fatal/warning alert, timeout, local abort, QUIC connection/application close, stateless reset, idle timeout, and path loss remain distinct.

**RM-SECURE-DATA-0006:** EOF without required authenticated closure reports possible truncation even if all received records authenticated. Application protocols with independent length/completion may refine consequences but cannot rewrite channel evidence.

**RM-SECURE-DATA-0007:** Graceful shutdown is bounded and cancellable, flushes according to policy without promising peer receipt, sends the protocol close signal where possible, optionally waits for peer confirmation, and releases all transport/provider/key/ticket resources.

**RM-SECURE-DATA-0008:** Alerts and errors are mapped without creating padding/oracle/user-enumeration distinctions across the network. Local evidence retains actionable category and provider detail under redaction policy.

