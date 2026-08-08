# HTTP cross-cutting requirements

**RM-HTTP-CROSS-0001:** Logs, traces, metrics, errors, and diagnostics redact credentials, cookies, tokens, signed URLs, personal content, cache keys, and sensitive fields by default. Opt-in capture is bounded, access-controlled, and auditable.

**RM-HTTP-CROSS-0002:** Observability correlates logical exchange, attempt, redirect/auth/retry transition, connection, protocol stream, proxy hop, secure channel, DNS/path, cache decision, and server handler without treating correlation IDs as authority.

**RM-HTTP-CROSS-0003:** Metrics separate queueing, resolution, connect, secure negotiation, request-head/body, first/last response byte, decoding, handler, cache, retry, and drain time; cardinality and tenant leakage are bounded.

**RM-HTTP-CROSS-0004:** User-visible authentication, redirect, certificate, proxy, download/upload, and error decisions expose original origin, destination, consequence, progress, cancellation quality, and recovery through accessible localized interfaces.

**RM-HTTP-CROSS-0005:** Protocol tokens, field names, methods, URIs, and wire values are locale-independent. Human language, content coding, filenames, and error presentation use explicit locale/Unicode contexts and resist bidi/spoofing confusion.

**RM-HTTP-CROSS-0006:** Security review covers request smuggling/splitting, cache poisoning, credential leakage, SSRF, redirect downgrade, decompression bombs, header compression exhaustion, cross-origin reuse, proxy confusion, timing/oracle leakage, and denial of service.

