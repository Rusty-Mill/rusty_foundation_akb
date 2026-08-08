# ADR-0048: Audio stream time follows the device sample clock

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Audio devices and engines advance sample positions on clocks that can drift from, reset relative to, or be observed with different precision than the system monotonic clock. Treating monotonic duration multiplied by nominal sample rate as stream position hides discontinuities and makes synchronization claims unsound.

## Decision

The generation-scoped device/engine sample clock is authoritative for stream progress. Portable deadlines continue to use the monotonic clock. Providers expose explicit correlation snapshots with uncertainty, age, drift, source quality, and discontinuity state; no contract assumes the clocks are identical.

## Consequences

- Audiovisual and multi-device synchronization depend on measured correlation quality.
- Route migration or clock reset starts a new stream-clock generation.
- Latency evidence names measurement boundaries and clock domains.
