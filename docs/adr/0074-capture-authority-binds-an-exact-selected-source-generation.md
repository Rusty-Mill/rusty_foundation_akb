# ADR-0074: Capture authority binds an exact selected source generation

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Desktops expose window identifiers, display topology, titles, thumbnails, coordinates, restore tokens, and platform selectors with different privacy and lifetime properties. These observations can be stale, reused, spoofed, or broader than the content a user meant to share. Treating enumeration or a native identifier as permission enables silent capture and unintended retargeting.

## Decision

Screen capture authority is an opaque, purpose-bound, revocable grant produced or confirmed by a trusted platform selection flow. It binds the requesting application and session to an exact source kind and provider generation plus explicitly selected cursor, audio, and output qualities. Enumeration, labels, thumbnails, native handles, coordinates, and restored hints are non-authoritative evidence. Source replacement or unproven identity continuity invalidates the grant rather than silently retargeting it.

## Consequences

- Selection can be canceled, denied, restricted, revoked, or made unavailable without inventing a source.
- One-shot screenshots follow the same authority model as streaming sessions.
- Session restoration is a hint subject to current platform validation and reconfirmation.
- Remote input, camera, microphone, recording, storage, transmission, and analysis remain separate authorities.
