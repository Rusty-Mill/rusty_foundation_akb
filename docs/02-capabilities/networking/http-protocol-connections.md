# HTTP protocol selection and connection management

**RM-HTTP-PROTOCOL-0001:** Selection binds scheme/origin, route and proxy plan, secure-channel ALPN, advertised alternatives and freshness, allowed HTTP versions, address/path policy, privacy partition, and fallback budget. A version change cannot weaken origin authentication or request policy.

**RM-HTTP-PROTOCOL-0002:** HTTP/1.1 persistence and pipelining, HTTP/2 streams over one ordered connection, and HTTP/3 streams over QUIC are different concurrency contracts. The common API cannot imply equal head-of-line blocking or failure isolation.

**RM-HTTP-PROTOCOL-0003:** A pool key includes origin authorization, proxy chain, network/privacy partition, credential and client-certificate scope, protocol, secure-channel policy, local binding, and provider generation. Connection coalescing requires explicit origin authority and certificate/route/policy proof.

**RM-HTTP-PROTOCOL-0004:** HTTP/1.1 parsing rejects request smuggling ambiguity, conflicting framing, invalid transfer coding, obs-fold, forbidden whitespace, and premature reuse. A connection is reusable only after its prior message boundary is proven complete.

**RM-HTTP-PROTOCOL-0005:** HTTP/2 settings, stream state, concurrency, flow control, HPACK state, GOAWAY last-stream evidence, reset, priority quality, and connection errors are bounded and observable.

**RM-HTTP-PROTOCOL-0006:** HTTP/3 control/QPACK streams, settings, blocked-stream limits, QUIC stream state, GOAWAY, resets, connection migration, and transport/application error scopes are bounded and observable.

**RM-HTTP-PROTOCOL-0007:** Draining prevents new assignments while allowing policy-bounded in-flight completion. Idle, lifetime, request-count, health, graceful-close, and forced-close limits are explicit and monotonic-time based.

