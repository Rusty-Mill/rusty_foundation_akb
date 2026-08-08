# ADR-0069: Decoded images are bounded immutable resources

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Image dimensions do not bound total decode work: frame counts, planes, bit depth, metadata, profiles, tiles, reference graphs, entropy complexity, animation disposal, progressive revisions, and intermediate transforms can dominate memory and time. Mutable generic bitmaps also obscure stride, alpha, color, orientation, ownership, and provisional state.

## Decision

Every decode runs under a multidimensional budget enforced before allocation and throughout processing. Published outputs are immutable, self-describing, generation-scoped pixel resources with exact layout, color, alpha, orientation, memory, provenance, and completeness. Progressive outputs are replaceable provisional revisions; animation composition is a separate bounded service.

## Consequences

- There is no unqualified portable “decode to RGBA” contract.
- Region/hardware/progressive claims require evidence of actual bounded behavior.
- Consumers cannot retain borrowed native buffers beyond their lease or treat previews as final silently.
