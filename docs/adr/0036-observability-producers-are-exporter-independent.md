# ADR-0036: Observability producers are exporter independent

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Windows ETW, Linux journals, Apple Unified Logging, OpenTelemetry protocols, files, and vendor SDKs differ in schema, retention, control, privacy, and failure behavior. Coupling application instrumentation to one destination turns operational policy into domain dependencies and makes exporter outage an application concern.

## Decision

Producers emit stable typed events, metrics, and spans to narrow portable sinks. A pipeline service owns filtering, sampling, transformation, buffering, native/protocol mapping, retention, and export. No exporter is required by the producer contract, and every mapping discloses loss or degradation.

## Options considered

- Standardize one exporter/protocol: interoperable but couples production semantics to an evolving external format.
- Expose native logging directly: efficient but platform-shaped and hard to compose.
- Stable producer contracts plus adapters: preserves semantics and allows native and protocol exporters.

## Consequences

- Instrumentation remains testable without network or platform services.
- Pipeline generations and delivery milestones require explicit contracts.
- Adapters carry mapping complexity and cannot claim lossless equivalence automatically.

