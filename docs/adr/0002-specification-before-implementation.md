# ADR-0002: Specification before implementation

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

The platform spans many OS domains and is expected to evolve over years. Early code can accidentally freeze vocabulary, boundaries, and platform assumptions before they are understood.

## Decision

The AKB is the initial source of truth. Capability semantics, dependencies, behavioral contracts, profile impact, and verification expectations are reviewed before public APIs or implementation repositories are established.

## Alternatives considered

- Code-first prototypes as de facto specification: fast locally, but decisions become implicit and hard to unwind.
- Complete all specifications before any experiment: too rigid; experiments are allowed when clearly disposable and do not establish stable interfaces.

## Consequences

- Initial visible progress is documentation and research.
- Focused spikes may test uncertainty, but their interfaces are non-binding.
- Promotion from specification to implementation requires explicit exit criteria.

## Verification

Implementation proposals must link accepted contracts and include planned conformance and benchmark coverage.
