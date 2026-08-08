# ADR-0022: Graphics selection uses workload contracts, not API names

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

Direct3D, Vulkan, Metal, OpenGL, and software renderers expose different feature models, queue/memory semantics, formats, robustness, timing, and platform reach. A universal immediate-mode graphics API would either be a lowest common denominator or a disguised native API. Selecting only “hardware accelerated” says nothing useful about renderer compatibility.

## Decision

Graphics providers are resolved against an exact versioned workload vector covering operation families, limits, formats, memory, queues, synchronization, presentation, robustness, power, color, protection, and acceptable degradation. Resolution publishes immutable device-epoch evidence. Rusty Mill does not define a general rendering command API until concrete renderer workloads justify one through RFC evidence.

## Options considered

### Standardize one native-style API

Fast initial design but privileges one platform model and leaks its evolution constraints.

### Lowest-common-denominator 2D/3D API

Portable but blocks native performance and advanced renderer needs.

### Workload-contract provider model

Preserves truthful negotiation and lets domain renderers standardize only proven shared semantics.

## Consequences

- Terminal, UI, media, and compute renderers can request different exact contracts.
- Software fallback is a provider change with explicit quality disclosure.
- Provider adapters may target different native APIs without changing domain semantics.
- Initial interfaces remain intentionally unresolved until two real consumers establish shared calls.

## Verification

Resolve representative terminal/UI workloads against deliberately incomplete native/software providers and prove every required feature, limit, format, recovery, and quality constraint is either evidenced or diagnosed unsatisfied.

