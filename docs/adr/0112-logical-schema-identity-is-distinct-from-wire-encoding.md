# ADR-0112: Logical schema identity is distinct from wire encoding

## Status

Accepted

## Context

One logical value can have multiple valid JSON or CBOR encodings, different ASN.1 encoding rules, binary and JSON Protocol Buffer projections, compressed/framed forms, and language-native objects. Conversely, identical bytes can mean different values under different schemas or types. Conflating schema, format, and bytes breaks evolution, signing, storage, negotiation, and transcoding.

## Decision

Rusty Mill models logical schema/type generation, logical value, format mapping profile, ordinary wire bytes, framing/envelope, canonical view, and decoded host representation as separate identities connected by evidence-bearing transformations. Every compatibility- or security-sensitive operation binds the required identities explicitly.

## Consequences

- Multiple encodings can implement one capability without pretending byte equality.
- Schema evolution is evaluated semantically and directionally.
- Content types and schema IDs cannot substitute for each other.
- Transcoding and host mapping must report loss.
