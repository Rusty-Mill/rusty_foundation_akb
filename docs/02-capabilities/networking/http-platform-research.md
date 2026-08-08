# HTTP protocol and platform research

## Primary protocol sources

- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) separates shared request/response semantics from version-specific messaging.
- [RFC 9111: HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111.html) defines cache storage, freshness, validation, invalidation, and field calculations.
- [RFC 9112: HTTP/1.1](https://www.rfc-editor.org/rfc/rfc9112.html) defines textual messaging, framing, connection management, and parsing requirements.
- [RFC 9113: HTTP/2](https://www.rfc-editor.org/rfc/rfc9113.html) defines binary framing, multiplexed streams, flow control, HPACK, settings, and connection/stream errors.
- [RFC 9114: HTTP/3](https://www.rfc-editor.org/rfc/rfc9114.html) maps HTTP semantics to QUIC streams with QPACK and HTTP/3 control streams.

## Portability conclusion

Native stacks can provide valuable proxy, credential, cache, power, policy, and platform integration, while portable stacks can provide tighter protocol control. Provider selection is therefore workload- and policy-based. Every provider must disclose supported protocol versions, redirect/auth/cache behavior, proxy provenance, streaming/backpressure quality, cancellation precision, connection pooling/coalescing, diagnostics, and native configuration it cannot override.

