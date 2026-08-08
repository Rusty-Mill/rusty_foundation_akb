# ADR-0075: Capture frames are provider observations, not content proof

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Platform capture paths differ in whether they observe pre- or post-composition content and whether they include occlusion, decorations, popups, cursors, hardware overlays, protected media, secure UI, accessibility overlays, remote surfaces, HDR processing, and capture-excluded windows. Blank output is ambiguous; visible output may still be incomplete or transformed.

## Decision

A capture frame is an immutable, exact, generation-bound observation made by a named provider path. Its contract describes pixels, color, geometry, timing, source boundary, transformations, protection evidence, and known exclusions. It never proves what the user physically saw, semantic completeness, faithful appearance, effective confidentiality, secure redaction, or absence of hostile observation.

## Consequences

- Window/display capture semantics and nonclaims are conformance evidence, not normalized assumptions.
- Capture-exclusion flags are policy requests unless an end-to-end path proves enforcement.
- Protected or secure output may be denied, blank, frozen, substituted, or unknown without creating a confidentiality claim.
- Recording, OCR, accessibility semantics, remote sharing, and trusted UI verification remain separate concerns.
