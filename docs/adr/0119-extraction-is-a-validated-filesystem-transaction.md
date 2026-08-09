# ADR-0119: Extraction is a validated filesystem transaction

## Status

Accepted

## Context

Archive entries contain attacker-controlled paths, links, metadata, sizes, ordering, and content. Writing each entry as it is decoded permits traversal, link races, collision ambiguity, partial replacement, privilege exposure, decompression exhaustion, and irrecoverable cancellation. Lexical path cleanup alone cannot defend a concurrently changing filesystem namespace.

## Decision

Rusty Mill separates inert enumeration and validation from an immutable extraction plan, isolated staging, destination revalidation, and policy-authorized commit. Filesystem operations are relative to a held destination capability with no-follow semantics. Atomic publication is claimed only when proven; weaker journaled commits expose partial and recovery evidence.

## Consequences

- Listing never grants filesystem mutation authority.
- Destination mapping, conflicts, limits, links, metadata, and overwrite behavior are reviewable before effects.
- Safe extraction may require additional storage and filesystem/provider support.
- Direct streaming to final paths is limited to explicitly weaker profiles whose risks and residuals are accepted.
