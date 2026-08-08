# Terminal emulator state model

**Status:** Draft component contract 0.1.0

## Inputs and outputs

The emulator consumes ordered output-byte chunks, resize events, configuration changes, and reset events. Chunk boundaries have no semantic meaning. It emits logical state revisions, bounded render/accessibility deltas, protocol-reply requests, privileged-effect requests, diagnostics, and checkpoints.

## State

At minimum, a declared W2/W3 dialect defines:

- primary and alternate screen grids with character-cell dimensions;
- cursor position, visibility, shape request, and saved states;
- rendition attributes and color references;
- margins, origin/wrap/insert modes, tab stops, and erase semantics;
- input-relevant modes such as cursor/keypad, mouse, focus, and bracketed paste;
- title/icon metadata under sensitivity policy;
- ordered scrollback/history policy separate from the active screen;
- parser state for incomplete control functions and strings;
- monotonically increasing state/mode revision.

## Requirements

- **RM-TERMINAL-EMULATOR-0001:** Parsing **MUST** be incremental and invariant to arbitrary input chunk boundaries, including boundaries inside UTF-8 and control sequences.
- **RM-TERMINAL-EMULATOR-0002:** The selected dialect/version and every supported extension **MUST** be explicit; unknown sequences **MUST** follow a declared ignore, replacement, visible-escape, or error policy.
- **RM-TERMINAL-EMULATOR-0003:** Parser memory, parameter count/value, string payload, nesting, image/link metadata, history, and generated reply sizes **MUST** be bounded by policy.
- **RM-TERMINAL-EMULATOR-0004:** Malformed encoding and unterminated/oversized sequences **MUST** recover deterministically without unbounded buffering or treating payload bytes as trusted host commands.
- **RM-TERMINAL-EMULATOR-0005:** Every state mutation **MUST** produce one ordered revision; deltas **MUST** identify their base/result revisions or require a full snapshot.
- **RM-TERMINAL-EMULATOR-0006:** Resize **MUST** state reflow/no-reflow, cursor, margin, alternate-screen, wide-cell, and history behavior and remain deterministic.
- **RM-TERMINAL-EMULATOR-0007:** Wide, combining, zero-width, invalid, and orphaned cell content **MUST** preserve structural invariants; the selected Unicode data/version and width policy **MUST** be recorded.
- **RM-TERMINAL-EMULATOR-0008:** Protocol queries and replies **MUST** be allowlisted, bounded, causally correlated, and separated from user input.
- **RM-TERMINAL-EMULATOR-0009:** Clipboard, hyperlink, notification, title, working-directory, image, and host-command sequences **MUST** emit policy requests; parsing alone **MUST NOT** execute effects.
- **RM-TERMINAL-EMULATOR-0010:** Reset **MUST** define which parser, grid, mode, metadata, palette, history, and security state returns to defaults.
- **RM-TERMINAL-EMULATOR-0011:** Snapshots/checkpoints **MUST** include schema, dialect, Unicode/width policy, dimensions, revision, and all state needed for deterministic continuation or declare omitted state.
- **RM-TERMINAL-EMULATOR-0012:** Diagnostics **MUST** avoid raw payload disclosure and terminal control injection; escaped bounded summaries are used.
- **RM-TERMINAL-EMULATOR-0013:** The emulator **MUST NOT** infer application semantics, reading order, or command boundaries absent a trusted/allowlisted semantic protocol.

## Standards baseline

ECMA-48 supplies a control-function baseline, not a complete modern terminal dialect. Each provider publishes a dialect manifest with the ECMA-48 subset, DEC/xterm-derived features, Windows VT behavior, private extensions, precedence, defaults, and test corpus. “VT compatible” alone is not a conformance claim.

Unicode behavior records versions of [grapheme segmentation](https://www.unicode.org/reports/tr29/), [East Asian Width](https://www.unicode.org/reports/tr11/), and [bidirectional text](https://www.unicode.org/reports/tr9/) policies; implementing one does not automatically specify terminal cell layout.

