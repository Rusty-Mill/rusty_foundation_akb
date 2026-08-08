# ADR-0067: Display color is compositor negotiation, not appearance proof

**Status:** Accepted  
**Date:** 2026-08-08

## Context

On modern desktops an application commonly tags a surface and the OS compositor maps it through current display mode, profile, brightness, HDR/reference-white, ambient, accessibility, power, and hardware behavior. A window may move or span displays. Surface acceptance therefore cannot prove the final transform, physical luminance, calibration, or viewer appearance.

## Decision

Display-color presentation is a generation-scoped negotiation among content description, rendering intent/fidelity, surface/buffer format, compositor capabilities/policy, and revisioned display evidence. The result names conversion ownership and degradations. Presentation acceptance is boundary-scoped evidence; measured appearance and calibration claims require a separate instrumented contract.

## Consequences

- Display/profile/headroom changes cause explicit renegotiation and redraw.
- `HDR supported` and `color managed` are prohibited as sufficient claims.
- Direct scan-out, exclusive control, calibration, and hardware adjustment stay separate privileged capabilities.
