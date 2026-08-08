# Cross-cutting qualities

**RM-INTERCHANGE-XCUT-0001:** Security defaults use strict bounded parsers, explicit formats/schemas, no ambient constructors/code, unique field/key semantics, authenticated schema resolution, safe canonical profiles, protected registries, and isolated extensions.

**RM-INTERCHANGE-XCUT-0002:** Privacy classifies values/schemas/unknowns, payloads, errors, samples/vectors, registries, logs/traces, buffers/pools, and generated code; minimizes collection/retention and supports redaction/erasure/export boundaries.

**RM-INTERCHANGE-XCUT-0003:** Performance budgets cover encode/decode/validate/canonicalize/transcode, allocations/copies, peak/retained memory, bytes, compression, streaming latency/backpressure, schema resolution, generated/reflection paths, and pathological input.

**RM-INTERCHANGE-XCUT-0004:** Accessibility provides localized stable diagnostics with semantic field labels, paths and remediation; tools expose structure, unknown/loss/canonical state, keyboard navigation, non-color status, and bounded progressive updates.

**RM-INTERCHANGE-XCUT-0005:** Internationalization distinguishes protocol tokens from localized display, preserves Unicode validity/normalization/direction/language, locale-neutral numbers/time on wire, and translated schema/documentation metadata where selected.

**RM-INTERCHANGE-XCUT-0006:** Observability records operation, format/schema/profile/implementation generations, sizes/fields/depth, streaming/zero-copy/copy path, duration/allocations, unknown/loss/validation/error classes, and causal context without payload or high-cardinality sensitive paths.

**RM-INTERCHANGE-XCUT-0007:** Shutdown/cancellation releases borrowed buffers, parsers/encoders, registry requests and spills; partial output is never promoted to a complete frame or signed artifact.
