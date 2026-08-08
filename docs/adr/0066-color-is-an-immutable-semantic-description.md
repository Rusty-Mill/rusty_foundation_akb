# ADR-0066: Color is an immutable semantic description

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Platforms and content formats represent color using named spaces, ICC profiles, primaries, white points, transfer functions, matrices, ranges, luminance values, mastering data, and compositor-specific descriptions. `sRGB`, `HDR`, an ICC filename, or a pixel format alone cannot define how numeric components map to color and light. Mutable or partial tagging also permits pixels to be silently reinterpreted.

## Decision

Rusty Mill models color with immutable image descriptions containing explicit encoding, colorimetry, luminance semantics, metadata, provenance, and unknowns. ICC is one validated representation, not the universal type. Pixels and description bind atomically by generation; transforms key the complete normalized semantics and engine/version.

## Consequences

- Unknown color data remains unknown instead of silently becoming sRGB.
- Named spaces resolve to exact versioned definitions.
- Caches, capture, printing, graphics, and codecs can share semantic descriptions without sharing native profile objects.
