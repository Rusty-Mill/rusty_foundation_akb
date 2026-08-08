# `rm.input.keyboard`

| Field | Value |
|---|---|
| Status | Draft |
| Contract version | 0.1.0 |

**RM-INPUT-KEYBOARD-0001:** Each event identifies press/release/repeat, normalized physical control where known, logical key meaning, modifier snapshot, location, layout/group revision, device class/identity policy, monotonic observation time, focus-routing revision, sequence, and provenance.

**RM-INPUT-KEYBOARD-0002:** Physical identity describes a control position/usage and is independent of active layout. Logical meaning describes the platform-resolved key under a layout. Neither is represented as committed text.

**RM-INPUT-KEYBOARD-0003:** Modifier state distinguishes depressed, latched, locked, and effective state where the provider exposes them. Left/right identity and AltGraph-like semantics are retained rather than guessed from aggregate flags.

**RM-INPUT-KEYBOARD-0004:** Repeat identifies the originating press when possible and reports provider repeat timing/provenance. Providers do not synthesize repeat unless the selected contract permits it, and release is never fabricated to balance a lost stream silently.

**RM-INPUT-KEYBOARD-0005:** Layout/group changes publish a new revision. Events carry the revision used for logical interpretation; stale consumers may use recorded meaning but cannot reinterpret physical keys under the current layout without disclosure.

**RM-INPUT-KEYBOARD-0006:** Dead keys, compose sequences, IME-consumed keys, media/system keys, accessibility filters, and secure-attention sequences are classified without fabricating ordinary text/key delivery.

**RM-INPUT-KEYBOARD-0007:** Focus loss, device removal, overflow, suspend, and backend reset terminate the affected pressed-state epoch. A state-reset event identifies that subsequent transitions cannot be paired reliably.

**RM-INPUT-KEYBOARD-0008:** Global/background keyboard observation is outside the base contract and requires separate authority, user-visible purpose, platform support, and security review.

**RM-INPUT-KEYBOARD-0009:** Key injection is a separate capability. Observing key events grants no injection authority, and synthetic events retain origin/assurance through routing.

**RM-INPUT-KEYBOARD-0010:** Diagnostics omit text and minimize physical-key sequences by default because timing and shortcuts may reveal sensitive activity.

