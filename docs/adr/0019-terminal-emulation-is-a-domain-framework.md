# ADR-0019: Terminal emulation is a domain framework

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

A terminal host combines OS-backed PTY sessions with portable parsing, logical screen state, Unicode policy, structured input, rendering, accessibility, clipboard/link security, and optional recording. Treating the whole host as an OS capability would push application policy into backends. Treating parsing as a backend would duplicate deterministic portable logic and make conformance platform-dependent.

## Decision

Terminal emulation is a domain framework above terminal session capabilities/services. Its parser/emulator, input encoder, renderer adapter, accessibility adapter, and recording policy have narrow contracts and evidence. OS backends supply PTY/session mechanisms and platform UI/accessibility adapters; they do not redefine emulator semantics.

Control-protocol effects are parsed into policy requests, never executed directly. Renderer and accessibility consumers use versioned logical state deltas, not independent raw-byte parsing.

## Options considered

### One terminal capability

Simple consumption but conflates native mechanism with parser, UI, security, and product policy.

### Backend-specific terminal emulators

Matches platform history but duplicates portable state logic and prevents shared deterministic corpora.

### Portable domain framework over narrow session capability

Preserves layer boundaries, shared conformance, and platform-specific adapters.

## Consequences

- Terminal product profiles need both platform and framework evidence.
- A headless emulator can be tested without windowing/graphics.
- Dialect and Unicode policy are explicit versioned inputs.
- Accessibility and rendering remain separate consumers of shared logical truth.

## Verification

Run identical chunked protocol/Unicode/input corpora across platforms and providers, compare canonical logical-state revisions/checkpoints, then separately verify renderer and accessibility adapter mappings.

