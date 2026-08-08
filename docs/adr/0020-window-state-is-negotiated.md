# ADR-0020: Window state is negotiated and revisioned

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

Win32, Wayland/X11, and AppKit differ in placement authority, callback behavior, scale changes, and surface configuration. A synchronous setter-shaped API would either lie on compositor-controlled systems or make stronger platforms define the common semantics accidentally. Independently delivered size, scale, and surface changes also allow impossible mixed-revision states.

## Decision

Portable window mutation is request/observation based. Effective logical extent, scale/transform, pixel extent, display association, and surface generation are published atomically as monotonically revisioned committed snapshots. Native synchronous/reentrant callbacks are contained behind an ordered non-reentrant event stream. Exact placement and global coordinates are optional extensions.

## Options considered

### Synchronous property setters

Familiar but cannot truthfully guarantee compositor acceptance or atomic cross-property state.

### Lowest-common-denominator event bag

Portable but permits mixed revisions and pushes reconciliation races onto every consumer.

### Requests plus committed snapshots

Truthful across platforms, supports deterministic reconciliation, and gives graphics/input one generation boundary.

## Consequences

- Applications distinguish intent from observed state.
- Providers may expose stronger placement quality without changing base semantics.
- Graphics and input bind conversions to snapshot revisions.
- Event coalescing is allowed only with complete final state and disclosed gaps.
- Provider implementations must adapt native affinity and immediate-reply rules internally.

## Verification

Run request/rejection, resize storm, mixed-scale migration, surface-loss, reentrancy, overflow, and destruction races. Compare canonical snapshot/event traces across providers rather than native callback counts.

