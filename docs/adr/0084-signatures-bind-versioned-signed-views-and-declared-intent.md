# ADR-0084: Signatures bind versioned signed views and declared intent

**Status:** Accepted  
**Date:** 2026-08-08

## Context

“Sign this file” is ambiguous across PE files, application bundles, archives, packages, documents, manifests, and attestations. Formats exclude or normalize different regions, and some permit post-sign mutation. Digest-only APIs can also detach a signature from artifact identity, purpose, target, or release channel.

## Decision

Every signature binds a versioned format-specific signed-view profile plus exact artifact digest/identity and declared semantic intent. The profile defines covered bytes or canonical claims, excluded/mutable regions, normalization, parser bounds, and transformation behavior. Signer role, purpose, target, policy generation, and referenced provenance are explicit signed claims where the native format permits, or are bound by an authenticated companion envelope.

## Consequences

- Format adapters preserve native coverage rather than promising one universal canonicalization.
- Unknown profiles and ambiguous covered/interpreted bytes fail closed.
- Embedded, detached, catalog, repository, document, package, and attestation signatures remain distinguishable.
- Repacking, normalization, and allowed document revisions require explicit profiles and evidence.

