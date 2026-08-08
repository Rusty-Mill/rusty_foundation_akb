# ADR-0089: Channel promotion moves an authenticated reference to the same digest

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Rebuilding or repackaging for preview, candidate, and stable channels makes promotion evidence ambiguous: source, toolchain, timestamps, signatures, and bytes can change after testing. Mutable tags alone are also vulnerable to unobserved movement and replay.

## Decision

Promotion creates a new signed, monotonic channel-metadata generation referencing the exact previously published artifact digest and evidence set after satisfying target-channel gates. It does not rebuild, repack, or silently resign changed claims. Any byte or claim change is a new release candidate and publication. Consumers record both immutable digest and channel-metadata generation.

## Consequences

- The artifact tested in an earlier channel is the artifact promoted.
- Channel history, demotion, hold, and emergency exclusion remain auditable metadata.
- Build-on-promotion pipelines are prohibited.
- Ecosystem tag/alias mappings must preserve digest evidence and declared variance.

