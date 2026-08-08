# ADR-0030: Data transfer uses immutable lazy typed offers

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

Windows OLE, Wayland, X11 selections, and macOS pasteboards all advertise multiple representations and may render content only when requested. Eagerly copying every format wastes memory/CPU, can trigger unsafe parsers or network work during inspection/hover, and fails for large or promised data. A single byte blob loses format fidelity and conversion provenance.

## Decision

Clipboard and drag services compose a shared immutable data-offer capability. Offers enumerate items and typed/versioned representations without materialization. A target requests one exact representation under size/time/resource, authority, destination, and conversion policy and receives a bounded async stream. Conversion is explicit evidence; offer generation/lifetime and source disappearance are first-class.

## Options considered

### Eager universal payload

Simple lifetime but expensive, unsafe for inspection, and cannot model promises or huge data.

### Platform-native opaque objects

Maximum fidelity but leaks COM/Wayland/X11/AppKit lifetimes and prevents portable security policy.

### Portable typed offers with backend materializers

Matches native strengths while preserving bounds, provenance, async behavior, and testability.

## Consequences

- Enumeration is cheap and side-effect free.
- Sources must remain available or explicitly request system persistence.
- Targets validate selected representations as untrusted input.
- Clipboard and drag reuse data semantics without sharing lifecycle policy.

## Verification

Enumerate and transfer multi-format/large/lazy/promised/malformed fixtures across native applications while faulting source, conversion, stream, and target stages.

