# ADR-0113: Canonicalization is an explicit signed-view profile

## Status

Accepted

## Context

Many formats allow multiple byte representations for the same perceived value. Some libraries offer deterministic output only within one binary or version, while standards such as JCS, deterministic CBOR, and DER define different canonical domains and rules. Signing ordinary serialization or assuming “deterministic” is universally canonical creates unverifiable signatures and substitution ambiguity.

## Decision

Rusty Mill treats canonicalization as an immutable named profile over an exact logical schema/value domain and format mapping. It uniquely specifies included fields, ordering, numbers, text, time, defaults, duplicates, unknowns, extensions, rejection, domain separation, and output bytes. Signatures and hashes bind the profile and schema/type generation plus declared intent.

## Consequences

- Ordinary wire bytes may differ from signed-view bytes.
- Out-of-domain values fail instead of receiving ad hoc normalization.
- Cross-language conformance uses exact canonical vectors.
- Deterministic implementation output cannot claim canonicality without the full profile.
