# ADR-0071: Media seek is a negotiated discontinuity

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Containers may have sparse/inexact indexes; inter-frame codecs require decoding from earlier random-access points; audio needs priming/trim; live sources expose moving seekable ranges; remote ranges add latency; sinks and clocks hold old state. Platform seek APIs therefore accept tolerances and can complete at different boundaries.

## Decision

A seek is a target/tolerance/accuracy/latency request that creates a new discontinuity generation. The provider resolves an attainable demux/decode start, cancels or flushes old work, repositions, prerolls, trims/drops, rebases the presentation clock, rebuilds buffers, and reports actual per-track and presentation-ready milestones. Old-generation output is always rejected.

## Consequences

- “Seek complete” always names its boundary; acceptance is not visible output.
- Exact seeking may be slower or unsupported and never silently becomes fast-keyframe seeking.
- Superseded/canceled seeks cannot publish stale frames, samples, cues, or clock updates.
