# Configuration conformance specification

## Required evidence

| Area | Evidence |
|---|---|
| Schema | Type boundaries, unknown keys, cross-key constraints, compatible and breaking evolution |
| Precedence | Exhaustive source-order matrix with provenance and policy locks |
| Snapshots | Atomic coherent reads, monotonic revisions, deterministic replay, no partial activation |
| Invalid change | Last-known-good behavior, rejection diagnostics, no lower-source secret fallback |
| Observation | External/self writes, delete/recreate, atomic file replacement, burst/coalescing, overflow and resynchronization |
| Reload | Live, coordinated commit/abort, restart-required, immutable-key behavior |
| Security | Least privilege, malicious inputs, path redirection, size/depth bounds, secret-reference redaction |
| Lifecycle | Cancellation, shutdown, observer/source loss, recovery, repeated registration cleanup |

## Platform matrix

Every supported provider runs the same semantic suite plus native cases for Registry, XDG/file observation, or UserDefaults. Reports identify OS build, filesystem/store, schema/parser/provider versions, source authority, observer mechanism, and unsupported quality claims.

## Model-based test

A reference resolver model consumes an ordered sequence of source states and invalidations. The provider trace must yield equivalent active snapshots and permitted diagnostic/coalescing traces. Intermediate native writes need not be preserved, but the final resynchronized state must converge.

