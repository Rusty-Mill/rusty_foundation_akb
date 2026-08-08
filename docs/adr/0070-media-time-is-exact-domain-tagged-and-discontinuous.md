# ADR-0070: Media time is exact, domain-tagged, and discontinuous

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Containers and codecs use different integer time bases, decode and presentation order can differ, edit lists create offsets/gaps, live streams discontinuously reset, and playback maps media time through a selected clock and rate. Floating-point seconds or a bare timestamp cannot preserve exact ordering, origin, epoch, rounding, or clock correlation.

## Decision

All media time values carry an exact rational/integer time base, named domain and epoch, validity/precision, and discontinuity generation. Mappings between container, decode, presentation, running, device, and wall domains are explicit checked values with declared rounding and uncertainty. Missing or contradictory timestamps remain evidence gaps.

## Consequences

- DTS, PTS, duration, running time, and clock time cannot be compared accidentally.
- Seek, loop, rate, live discontinuity, and track/configuration change create explicit generations.
- UI seconds are derived presentation, never canonical scheduling or serialization values.
