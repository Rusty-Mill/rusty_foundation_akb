# ADR-0024: Text input is not keyboard input

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

Windows, Wayland, and AppKit all distinguish key observations from text-service composition and commit. IMEs, compose/dead keys, voice, handwriting, software keyboards, accessibility services, and paste can produce text without a one-to-one hardware key. Mapping keys to characters in the base input backend duplicates platform text services and causes double insertion.

## Decision

Keyboard capability reports physical/logical key state. A separate text-input platform service manages focused editable targets, surrounding text, selection/caret geometry, preedit/marked text, candidates, commits, cancellation, and security policy. Streams may carry causal associations but neither substitutes for the other. Provisional text is never committed implicitly.

## Options considered

### Key events with optional character field

Simple for Latin layouts but ambiguous for IME, dead keys, alternate input, and consumed shortcuts.

### Text-only input

Correct for editors but loses shortcuts, games, terminals, and physical controls.

### Separate coordinated streams

Matches native systems and preserves both semantic fidelity and accessibility/i18n.

## Consequences

- UI frameworks consume commits/composition for editing and keys for commands.
- Terminal hosts encode committed text once and extended keys separately.
- Text offsets and caret geometry are revision-bound conversion boundaries.
- Secure text policy can minimize surrounding context independently of key observation.

## Verification

Run layout, dead-key, compose, IME, voice/accessibility, focus-race, Unicode-offset, and duplicate-delivery corpora on every provider.

