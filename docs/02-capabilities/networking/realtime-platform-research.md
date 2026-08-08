# Real-time protocol and platform research

## Primary sources

- [RFC 6455: The WebSocket Protocol](https://www.rfc-editor.org/rfc/rfc6455.html) defines the HTTP/1.1 handshake, messages/frames, masking, control frames, security, and closing behavior.
- [RFC 7692: Compression Extensions for WebSocket](https://www.rfc-editor.org/rfc/rfc7692.html) defines per-message compression and context/window negotiation.
- [RFC 8441: Bootstrapping WebSockets with HTTP/2](https://www.rfc-editor.org/rfc/rfc8441.html) and [RFC 9220: Bootstrapping WebSockets with HTTP/3](https://www.rfc-editor.org/rfc/rfc9220.html) map WebSocket to extended CONNECT streams.
- The living [WHATWG server-sent events specification](https://html.spec.whatwg.org/multipage/server-sent-events.html) defines EventSource processing, UTF-8 event streams, `Last-Event-ID`, and reconnect behavior.
- [RFC 9297: HTTP Datagrams and the Capsule Protocol](https://www.rfc-editor.org/rfc/rfc9297.html) supplies HTTP datagram/capsule foundations used by WebTransport profiles.
- The current [IETF WebTransport over HTTP/3 draft](https://datatracker.ietf.org/doc/draft-ietf-webtrans-http3/) and [W3C WebTransport Working Draft](https://www.w3.org/TR/webtransport/) remain revision-sensitive inputs, not frozen Rusty Mill guarantees.

## Portability conclusion

Browser APIs deliberately mediate headers, cookies, origins, certificates, proxies, connection sharing, and background behavior. Native frameworks vary in HTTP/2-/3 WebSocket bootstrapping, SSE reconnection, WebTransport draft versions, compression, keepalive, queue limits, cancellation, and diagnostics. Providers therefore publish exact protocol/profile revisions and behavior matrices; platform availability never implies semantic conformance.

