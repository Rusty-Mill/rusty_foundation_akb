# ADR-0043: Executable memory is a separate authorized service

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Generated code requires protection transitions, instruction-cache coherence, platform entitlements, code provenance, and strong exploitation controls. Exposing execute as an ordinary mapping flag would make writable/executable memory ambient and obscure hardened-runtime failures.

## Decision

Executable-memory orchestration is a separate opt-in service over memory regions. It requires explicit authority and platform evidence, defaults to write-xor-execute publication, commits immutable generations, and reports entitlements, aliases, signing, and cache synchronization separately.

## Consequences

- Ordinary mapping profiles cannot accidentally request executable pages.
- JIT workloads remain possible with explicit security and packaging requirements.
- Platforms unable to satisfy the selected W^X/provenance quality report unavailable rather than weakening silently.

