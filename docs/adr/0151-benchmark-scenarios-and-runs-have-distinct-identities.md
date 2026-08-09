# ADR-0151: Benchmark scenarios and runs have distinct identities

**Status:** Accepted  
**Date:** 2026-08-08

## Context

A benchmark workload must remain comparable across platforms and implementations, while every execution varies by artifacts, hardware, OS, provider, configuration, data, noise, and time. Using one identity for both encourages overwritten results or incomparable trend lines.

## Decision

`rm.benchmark.<domain>.<scope>@<major>` identifies a semantic scenario contract. Each execution produces a separate immutable run identity bound to exact scenario version, artifacts, environment, inputs, raw samples, statistics, and provenance. Regression conclusions bind comparable run sets and versioned budgets.

## Alternatives considered

- Identify only benchmark functions: rejected because harness names do not define semantic equivalence or measured boundaries.
- Identify only result files: rejected because comparable runs cannot be grouped safely.
- Reuse conformance assertion identities: rejected because correctness assertions and quantitative experiment contracts evolve differently.

## Consequences

- Performance claims can trace from requirement to scenario to runs without implying current evidence.
- Legacy suite IDs remain reserved and may map to semantic scenarios.
- Storage and reporting must preserve raw evidence and superseded conclusions.
