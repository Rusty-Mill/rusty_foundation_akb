# Observability and diagnostics conformance specification

| Area | Required evidence |
|---|---|
| Events | Schema compatibility, typed fields/units, canonical rendering, disabled-path behavior |
| Context | Explicit async/process propagation, invalid remote carriers, identifier reuse, baggage bounds |
| Pipeline | Generation swap, filtering/sampling, byte/count bounds, overflow/loss accounting, exporter outage |
| Metrics | Instrument semantics, reset/temporality, cardinality enforcement, missing-versus-zero |
| Tracing | parent/link distinction, async migration, nonrecording propagation, clock discontinuity |
| Privacy | field classification, forbidden-value canaries, redaction before export, retention/deletion |
| Bundles | allowlist, consent/policy, cancellation, atomic publication, integrity and cleanup |
| Crash | real subprocess crashes, recursion, corrupted allocator/locked thread scenarios where safe, truncation, exact-symbol matching, handler coexistence |
| Lifecycle | startup before exporter, reconfiguration, bounded flush, abrupt termination, spool recovery |

## Failure injection

Conformance uses isolated subprocesses and disposable accounts/containers. It forces full disks, denied permissions, slow/dead exporters, queue overflow, clock steps, malformed context, high-cardinality input, signal/exception crashes, missing symbols, corrupt artifacts, and interrupted bundle creation. Tests never crash the harness process or collect unrelated user data.

## Platform evidence

Reports state OS/build, native facility and configuration, privileges/entitlements, store/retention settings, symbol format/tool versions, dump/core policy, debugger presence, container/session context, and every degraded or unavailable assertion.

