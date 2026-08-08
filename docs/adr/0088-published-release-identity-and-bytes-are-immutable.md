# ADR-0088: Published release identity and bytes are immutable

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Replacing assets, tags, package versions, source archives, or metadata under an existing release identity breaks lockfiles, signatures, provenance, advisories, caches, mirrors, and incident reconstruction. Deleting a compromised release can also erase evidence while failing to protect clients that already possess it.

## Decision

Once publication metadata makes a release visible, its version identity and canonical artifact/evidence bytes are immutable and never reused. Corrections publish a new version or signed metadata/advisory revision. Yanking, deprecation, channel removal, emergency exclusion, and legal/security tombstones are authenticated policy overlays that preserve historical identity and never serve different bytes under the old digest/version.

## Consequences

- Publication requires complete preflight because in-place correction is unavailable.
- Consumers and mirrors can rely on stable digests and reconstruct history.
- Retention and exceptional takedown need explicit policy and tombstones.
- Provider-generated archives are not canonical unless their bytes are captured and verified.

