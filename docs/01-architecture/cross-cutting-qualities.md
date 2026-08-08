# Cross-cutting quality model

These qualities are mandatory review dimensions for every capability, profile, backend, and release.

## Security

Define authorities rather than ambient access; default to least privilege; isolate unsafe/native boundaries; validate external input; document threat assumptions; support audit without leaking secrets.

## Performance

Specify latency, throughput, memory, allocation, startup, and binary-size expectations where relevant. Benchmark abstraction overhead against an idiomatic native baseline and publish the environment and variance.

## Accessibility

User-facing capabilities must preserve semantic roles, focus and input behavior, assistive-technology interoperability, user preferences, and accessible fallback paths.

## Internationalization

Text, locale, time, collation, input, and layout capabilities must avoid implicit host-locale assumptions. Encoding and normalization behavior must be explicit.

## Observability

Use stable, structured events with correlation and causal context. Instrumentation must be low overhead, optional where appropriate, privacy-aware, and independent of a single exporter.

## Review gate

A proposal must state either its requirements in each dimension or why a dimension is not applicable. “Not applicable” is reviewable, not assumed.
