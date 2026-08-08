# Real-time cross-cutting requirements

**RM-REALTIME-CROSS-0001:** Origin is untrusted request context checked against explicit server policy; it is neither peer authentication nor authorization. Non-browser clients declare origin behavior, and missing/null/opaque origins have explicit policy.

**RM-REALTIME-CROSS-0002:** Cookies, bearer credentials, query tokens, subprotocol values, cursors, close reasons, application payloads, stream names, URLs, and peer identifiers are secret/personal unless classified otherwise and are redacted from logs, traces, metrics, crash data, and user-visible diagnostics by default.

**RM-REALTIME-CROSS-0003:** Security review covers cross-site hijacking, CSRF-like handshakes, confused deputies, DNS rebinding, proxy/cache confusion, credential/cursor leakage, compression oracles/bombs, malformed frames/events/capsules, queue exhaustion, reconnect storms, slow consumers, amplification, and cross-session pooling.

**RM-REALTIME-CROSS-0004:** Observability correlates logical subscription/session, connection attempt, HTTP exchange, secure channel, protocol stream/message/datagram, reconnect generation, application acknowledgment, and close without using identifiers as authority or unbounded metric dimensions.

**RM-REALTIME-CROSS-0005:** Metrics separate establishment stages, open duration, queue delay/bytes/drops, message/event/stream/datagram sizes and rates, flow-control stalls, compression cost, heartbeat/RTT, reconnect/gap/duplicate outcomes, close scopes, CPU/memory/network/energy, and sampling loss.

**RM-REALTIME-CROSS-0006:** User-visible long-lived connections expose service identity, purpose, active/reconnecting/degraded state, data/cost/privacy implications, progress, accessible pause/stop/retry, and recovery. Status is localized, but protocol tokens, UTF-8 validation, identifiers, URIs, and wire parsing remain locale-independent.

**RM-REALTIME-CROSS-0007:** Background and constrained-network operation is product policy. Providers cannot silently keep a connection alive, wake a device, consume metered data, or convert it to platform push; degradation and unavailable states are explicit.

