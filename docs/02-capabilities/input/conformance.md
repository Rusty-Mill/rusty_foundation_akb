# Input conformance specification

**Status:** Draft

| ID | Requirements | Method |
|---|---|---|
| INPUT-KEY-001 | KEYBOARD-0001–0005 | Versioned layouts cover physical/logical identity, left/right and latched/locked modifiers, dead keys, groups, press/release/repeat, and mid-stream layout change |
| INPUT-KEY-002 | KEYBOARD-0006–0010 | Exercise IME consumption, media/system/accessibility keys, focus/device/reset loss, denied background/injection, secure fields, and diagnostic canaries |
| INPUT-POINTER-001 | POINTER-0001–0004 | High-rate absolute/relative motion and all axis sources across scale/rotation; verify transforms, coalesced coverage, precision, and nonlost transitions |
| INPUT-POINTER-002 | POINTER-0005–0008 | Race capture/lock/confine with focus/destruction/authority loss; saturate queues and scan identity/location telemetry |
| INPUT-TOUCH-001 | TOUCH-0001–0007 | Multi-contact frame vectors, crossing identities, coalescing, gesture takeover, emulated mouse, focus/removal/overflow cancellation, and privacy scan |
| INPUT-TEXT-001 | TEXT-0001–0004 | IME corpora cover preedit replacement, candidate selection, commit/cancel, reconversion, surrogate/combining/emoji/bidi, and checked UTF-8/UTF-16/scalar mappings |
| INPUT-TEXT-002 | TEXT-0005–0009 | Surrounding-text minimization, secure fields, candidate geometry, focus-race target binding, consumed keys, and native callback reentrancy |
| INPUT-TEXT-003 | TEXT-0010–0012 | Destroy/overflow/service failure, assistive/voice/handwriting input, and secure-input degradation/nonclaims |
| INPUT-ROUTE-001 | ROUTING-0001–0008 | Cross-window focus/capture traces with hardware, accessibility, remote, replay, synthetic, and unknown provenance; verify authority separation and loss reset |

## Required platform matrix

Evidence runs with US and non-US layouts; dead-key and compose layouts; Chinese/Japanese/Korean IMEs; emoji and supplementary scalars; right-to-left text; screen readers/switch control; mouse, high-rate mouse, precision touchpad, touch, and remote sessions where supported. Tests record unavailable platform facts instead of filling them with inferred values.

Terminal integration proves that one committed text action is encoded once, IME preedit remains host UI unless the terminal protocol explicitly negotiates it, physical/logical extended keys retain exact mode revision, and stale pointer-to-cell transforms are rejected or reconciled.

