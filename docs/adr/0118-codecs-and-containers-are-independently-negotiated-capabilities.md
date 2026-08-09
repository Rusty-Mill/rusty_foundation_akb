# ADR-0118: Codecs and containers are independently negotiated capabilities

## Status

Accepted

## Context

Compression algorithms can appear in raw streams, algorithm-specific frames, transport content codings, and multiple archive containers. Containers may store entries uncompressed or use different codecs per entry. File suffixes and convenience APIs commonly blur these identities, causing interoperability failures, unsafe guessing, and hidden buffering or resource behavior.

## Decision

Rusty Mill models codec/framing identity and container/profile identity as independent capabilities with separate negotiation, parameters, limits, provider evidence, and lifecycle. A composition explicitly binds the selected codec to a container field or transport context; neither identity is inferred as authority from a suffix.

## Consequences

- Raw DEFLATE, zlib, gzip, ZIP methods, tar-plus-codec compositions, and transport content codings remain distinguishable.
- Applications can require streaming, dictionaries, determinism, random access, metadata, or interoperability independently.
- Provider convenience APIs may implement compositions but adapters must expose semantic gaps.
- Product RFCs still select supported formats, profiles, and defaults.
