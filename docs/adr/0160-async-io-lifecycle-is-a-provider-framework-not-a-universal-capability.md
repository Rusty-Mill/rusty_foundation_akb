# ADR-0160: Async I/O lifecycle is a provider framework, not a universal capability

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill architecture governance

## Context

Filesystem I/O, byte pipes, process waits, networking, and later device operations share difficult lifecycle mechanics: generation-safe submission, readiness or completion translation, cancellation races, retained buffers/native state, bounded queues, waking, and shutdown draining. They do not share one honest application-facing operation. Their progress units, EOF/message rules, ordering, side effects, errors, authority, and provider support differ materially.

Treating the shared machinery as a universal capability would either erase those differences or create an untyped mechanism-oriented API. Treating every domain as entirely independent would duplicate memory-safety, ABA, cancellation, overload, and shutdown invariants.

## Decision

Async I/O lifecycle is a reusable provider-integration framework. It defines lifecycle and safety invariants and accepts explicit cancellation, monotonic time where needed, wake/executor adapters, limits, and shutdown policy. Domain capability providers retain operation, progress, EOF/message, ordering, side-effect, error, and authority semantics.

The framework is not a stable capability-graph node merely because multiple capabilities use it. A graph node requires an independently selectable capability contract with explicit source declaration. Native completion, readiness translation, and bounded blocking adaptation remain provider strategies reported per operation/resource/platform generation; none selects a universal executor or runtime.

## Options considered

- Universal `rm.async-io` capability: superficially uniform, but makes illegal cross-domain assumptions and risks an untyped operation API.
- Per-domain lifecycle implementations with no shared framework: preserves semantics but duplicates the hardest safety and shutdown rules.
- Shared provider framework with domain-owned semantics: reuses invariants while keeping capability contracts honest and independently selectable.

## Consequences

- Domain specifications must map their operations onto the shared lifecycle without surrendering semantic ownership.
- Framework conformance and provider evidence are qualified by operation/resource/platform, not one engine-wide badge.
- Dependency graphs do not acquire framework-use edges unless a later independently selectable capability is accepted.
- Executors, runtimes, reactors, and provider libraries remain implementation/profile choices behind separate gates.
- Cross-domain trials can reuse lifecycle model tests while retaining distinct domain oracles.

## Verification

The [foundation-batch integration review](../04-ecosystem/consistency-readiness/foundation-batch-integration-review.md) checks ownership, lifecycle milestones, cancellation, progress, identity, backpressure, sync completeness, shutdown, dependency classification, and evidence boundaries across runtime/time, filesystem, process, IPC, and async I/O.

## Follow-up

- Require future I/O-like domains to identify domain-owned semantics and the exact lifecycle invariants reused.
- Reconsider a capability node only when at least two consumers need an independently selectable, typed capability contract rather than internal provider composition.
