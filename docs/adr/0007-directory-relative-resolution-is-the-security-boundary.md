# ADR-0007: Directory-relative resolution is the filesystem security boundary

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

Checking or canonicalizing a path and opening it later creates a time-of-check/time-of-use race: links, mount points, reparse points, or ancestor bindings can change between operations. Process current directory is mutable ambient state and does not express authority. Native platforms expose different levels of handle-relative and constrained lookup.

## Decision

Portable security-sensitive resolution begins from an explicit opened directory authority and resolves a relative path under declared traversal policy. Lexical normalization is useful for syntax but never proves containment. Object-kind checks occur on the opened result. Providers declare the strength of link, reparse, mount, and ancestor-race protections and expose weakened fallbacks.

Absolute paths and device namespace prefixes are outside the base relative-resolution contract unless an explicit authority-bearing extension enables them.

## Options considered

### Canonicalize then open

Easy to explain but vulnerable to namespace mutation between check and use.

### Process-current-directory relative paths

Portable at a superficial level but relies on mutable ambient policy and weak authority boundaries.

### Directory-relative handle-based resolution

Supports least authority and race resistance, though protection strength differs by platform and may require careful fallback reporting.

## Consequences

- Directory resources become foundational to filesystem composition.
- Strong containment may be unavailable on some platform/version combinations.
- Providers must expose resolution quality rather than silently emulate it.
- Path-based convenience APIs cannot claim the strongest security level.

## Verification

Adversarial tests race ancestor renames, link/reparse swaps, mount changes, final-object replacement, and parent traversal against resolution. Each provider's declared containment level must match observed behavior.
