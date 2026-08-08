# HTTP semantic message and exchange model

**RM-HTTP-MESSAGE-0001:** A request binds method, normalized target URI, original origin, authority, ordered field multimap, optional bounded content stream, trailers policy, protocol constraints, deadline, cancellation scope, and immutable request-attempt identity. URI userinfo is rejected.

**RM-HTTP-MESSAGE-0002:** Field names and values are validated before transmission with per-field, total-section, count, encoding, sensitive-value, and logging bounds. Repeated fields remain distinct unless their registered semantics permit combination.

**RM-HTTP-MESSAGE-0003:** Content length known, unknown, absent, zero, malformed, exceeded, truncated, and forbidden are distinct states. HEAD, informational, CONNECT, and status-specific content rules are enforced independently of framing.

**RM-HTTP-MESSAGE-0004:** A response exchange preserves zero or more informational responses, one final response head, a bounded content stream, optional trailers, and completion evidence. Receiving a final status does not prove that the request body was fully received or applied.

**RM-HTTP-MESSAGE-0005:** Method properties such as safe, idempotent, cacheable, and content-defined are registry-/extension-profile facts, not guesses from spelling. Application idempotency requires a typed domain contract in addition to method semantics.

**RM-HTTP-MESSAGE-0006:** Extensions declare affected fields, methods, statuses, framing, negotiation, intermediaries, security limits, and unknown-extension behavior. Unknown fields are preserved or rejected according to policy without inventing semantics.

**RM-HTTP-MESSAGE-0007:** Client and server APIs expose async-first exchange and content operations plus sync-complete equivalents that do not create hidden runtimes or nested event loops.

