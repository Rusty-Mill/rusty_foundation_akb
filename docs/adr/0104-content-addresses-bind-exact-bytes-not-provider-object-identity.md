# ADR-0104: Content addresses bind exact bytes, not provider object identity

## Status

Accepted

## Context

Object services expose keys, version IDs, generations, ETags, multipart validators, checksums, and timestamps whose meaning varies by provider, API, encryption, copy, and upload method. Content-addressed systems instead use a named collision-resistant digest over exact bytes. Treating provider validators as hashes or hashes as complete object identity causes integrity, portability, metadata, and lifecycle errors.

## Decision

Rusty Mill models namespace/key plus provider generation as stored-object identity and a separate descriptor of algorithm, digest, length, and representation as content identity. Content is trusted under a descriptor only after independent length and digest verification. A content address proves exact-byte equality under its algorithm assumptions, not provenance, semantic safety, authorization, metadata, or availability.

## Consequences

- Provider objects with identical bytes remain different stored versions.
- Multipart ETags and provider checksums cannot silently become content addresses.
- Portable content graphs can verify bytes from untrusted mirrors.
- Algorithm transition and descriptor authentication require explicit lifecycle policy.

