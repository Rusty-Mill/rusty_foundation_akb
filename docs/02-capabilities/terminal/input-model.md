# Structured terminal input and IME model

**Status:** Draft component contract 0.1.0

This component consumes the platform [input foundation](../input/README.md). It does not observe native devices or run an IME itself; it translates already structured key, committed-text, pointer, paste, focus, and protocol-reply events into the negotiated terminal wire dialect.

Paste payloads originate from the shared [data-transfer offer and clipboard service](../data-transfer/README.md). The terminal host chooses and materializes an exact text representation under size, encoding, control/newline, sensitivity, confirmation, and cancellation policy before this component applies terminal-mode encoding.

## Event classes

| Event | Meaning |
|---|---|
| Text commit | Final Unicode text intended for the child |
| Composition start/update/commit/cancel | IME preedit lifecycle; preedit is host UI unless protocol explicitly carries it |
| Key | Physical/logical key, press/release/repeat, modifiers, layout context, timestamp domain |
| Pointer | Position/cell, button, wheel/axis, modifiers, precision, capture context |
| Paste | Explicit payload with provenance, size, sensitivity, and confirmation/sanitization policy |
| Focus | Host focus transition when the negotiated terminal mode requests reporting |
| Protocol reply | Emulator-generated response, never user-originated input |

Text commits and key events are independent. A host must not send both for one logical action unless the selected input dialect explicitly requires both.

## Requirements

- **RM-TERMINAL-INPUT-0001:** Encoding **MUST** consume a structured event, exact emulator mode revision, wire dialect/version, and policy snapshot.
- **RM-TERMINAL-INPUT-0002:** A stale mode revision **MUST** be rejected, re-evaluated under an explicit ordering mechanism, or encoded under a documented snapshot rule; it **MUST NOT** silently use current state.
- **RM-TERMINAL-INPUT-0003:** IME preedit text **MUST NOT** be sent as committed child input unless a negotiated protocol explicitly supports composition updates.
- **RM-TERMINAL-INPUT-0004:** Text commit **MUST** apply the wire encoding and malformed/unrepresentable policy exactly once and avoid duplicate key-derived text.
- **RM-TERMINAL-INPUT-0005:** Physical key identity, logical key meaning, produced text, modifiers, layout, repeat, and press/release **MUST** remain distinguishable where the source provides them.
- **RM-TERMINAL-INPUT-0006:** Unsupported keys, modifiers, pointer detail, or protocol modes **MUST** return unavailable/degraded disclosure rather than fabricate fidelity.
- **RM-TERMINAL-INPUT-0007:** Paste **MUST** be distinct from typing and apply bracketed-paste state, maximum size, control-character, newline, confirmation, and sensitivity policy.
- **RM-TERMINAL-INPUT-0008:** Pointer coordinates **MUST** identify cell/viewport transform revision; out-of-range and stale geometry **MUST** follow explicit clamp/reject/re-evaluate policy.
- **RM-TERMINAL-INPUT-0009:** Emulator-generated replies **MUST** use a separate bounded queue and authority path so untrusted UI events cannot forge a trusted reply classification.
- **RM-TERMINAL-INPUT-0010:** Focus, mouse, paste, and extended-key reporting **MUST** occur only when the exact negotiated mode enables them and policy permits them.
- **RM-TERMINAL-INPUT-0011:** Input logging/recording **MUST** default to off; password/secure-input mode and host sensitivity policy **MUST** suppress capture without claiming the child cannot echo/store input.
- **RM-TERMINAL-INPUT-0012:** Backpressure, cancellation, focus loss, session close, and IME cancellation **MUST** define queued-event disposition and never split an encoded protocol sequence into a falsely successful event.

## Accessibility and interaction

Every host action is keyboard reachable without requiring pointer precision. Key bindings distinguish host commands from child input, expose conflicts, support remapping, and never trap focus without an escape path. IME candidate/preedit UI belongs to the host platform integration and follows zoom, contrast, reading order, and assistive-technology requirements.
