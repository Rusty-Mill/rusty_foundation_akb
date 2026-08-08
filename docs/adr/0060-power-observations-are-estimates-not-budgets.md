# ADR-0060: Power observations are estimates, not budgets

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Battery percentage, remaining time, charge/discharge rate, saver mode, thermal state, and energy attribution vary by hardware, firmware, sampling, workload, aggregation, and platform policy. Their precision and meaning differ, and several may be unavailable or stale.

## Decision

Portable power observations are revisioned qualified estimates with units, source, age, and uncertainty/unknown state. They inform explicit application adaptation but never represent guaranteed energy allocations, performance, deadlines, durability, or exact per-operation consumption. Budgets require a named measurement boundary and evidence method.

## Consequences

- Product policy handles estimate volatility and hysteresis.
- Performance/energy claims require sustained measured evidence.
- Critical correctness never depends on remaining-time predictions.
