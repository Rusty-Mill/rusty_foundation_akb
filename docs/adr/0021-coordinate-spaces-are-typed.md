# ADR-0021: Window coordinate spaces are typed and revision-bound

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

Mixed-scale displays, rotated outputs, Wayland's lack of portable global coordinates, and backing-store recreation make a single numeric point/rectangle type unsafe. Treating scale as physical DPI is also incorrect on modern composited desktops.

## Decision

Window logical, surface pixel, display logical, and backend-native coordinates are distinct semantic spaces. Conversions require an explicit transform from a committed revision, transform rectangle edges with declared rounding, and reject or identify stale revisions. Physical size/DPI and global placement are optional provenance-bearing observations.

## Consequences

- Cross-space arithmetic becomes an explicit correctness boundary.
- Rendering and hit testing can prove which geometry revision they used.
- Providers do not invent global coordinates for Wayland.
- APIs are slightly more verbose, but accumulated rounding drift and stale-scale ambiguity become testable.

