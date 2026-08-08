# ADR-0094: HTTP semantics are stable while protocol mechanics remain explicit

## Status

Accepted

## Context

HTTP/1.1, HTTP/2, and HTTP/3 share methods, status codes, fields, resources, and representation semantics, but differ materially in framing, multiplexing, flow control, compression state, connection reuse, head-of-line behavior, and failure isolation. Separate public APIs would fragment applications; pretending the transports are equivalent would hide correctness and performance behavior.

## Decision

Rusty Mill defines one version-independent typed HTTP message/exchange model and separate protocol mechanics beneath it. Protocol selection is policy-driven and observable. Stream and connection events retain their native scope, and no common abstraction promises equivalent concurrency, ordering, cancellation, reuse, or failure isolation.

## Consequences

- Applications can express semantic intent once across supported versions.
- Providers remain accountable for version-specific state and variance.
- Tests compare canonical semantic traces while preserving mechanical evidence.
- The API is more explicit than convenience clients that hide routing and retries.

