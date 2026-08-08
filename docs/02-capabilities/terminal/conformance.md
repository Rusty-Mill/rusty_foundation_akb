# Terminal foundation conformance specification

**Status:** Draft

| ID | Requirements | Method |
|---|---|---|
| TERM-PTY-001 | 0001, 0002 | Fault every creation stage and size boundary; prove no partial resource and exact pre-release initial size |
| TERM-PTY-002 | 0003, 0011 | Verify channel direction, blocking/async realization, independent bidirectional progress, and hidden-runtime prohibition |
| TERM-PTY-003 | 0004 | Replay versioned encoding/control vectors, malformed input/output, split sequences, and translation disclosures for W0–W3 |
| TERM-PTY-004 | 0005, 0006 | Attempt reuse/serialization/leakage of attachment and inventory child resources before release |
| TERM-PTY-005 | 0007, 0012 | Race resize sequences with output, input, child exit, and close; validate ordering and accepted/application-observed distinction |
| TERM-PTY-006 | 0008–0010 | Exercise partial I/O, backpressure, EOF, hangup, broken peer, child exit, host close, and session close permutations |
| TERM-PTY-007 | 0013 | Set/get every advertised mode and verify effective state; unsupported/ignored properties cannot report success |
| TERM-PTY-008 | 0014 | Inject content/title/path/command canaries and scan diagnostics, telemetry, crash, and evidence artifacts |
| TERM-PTY-009 | 0015 | Confirm raw capability evidence makes no renderer, width, input-event, shell, or accessibility claim |
| TERM-SESSION-001 | SESSION-0001–0004 | Fault/cancel every composition milestone; no unattached running child or leaked session remains |
| TERM-SESSION-002 | SESSION-0005–0008 | Exercise stop, host failure, detach/hangup/terminate, output drain, multiple-process, and job-control policies |

## Cross-cutting evidence

Protocol vectors include ASCII, combining sequences, emoji/variation selectors, wide/ambiguous characters, bidirectional controls, invalid UTF-8 where applicable, long escape sequences, mouse/paste/focus encodings, and resize storms. These vectors test transport and parsing claims; they do not by themselves prove font rendering, grapheme width, bidirectional layout, IME, or accessibility.

An emulator/accessibility provider adds separate evidence for logical text preservation, focus/cursor mapping, reading order, update announcements, selection, high contrast, reduced motion, screen-reader interaction, and keyboard-only operation.

## Emulator and input assertions

| ID | Assertion |
|---|---|
| TERM-EMU-001 | Every split of each corpus byte stream yields identical state revisions, replies, effects, and final checkpoint |
| TERM-EMU-002 | Malformed/oversized/unterminated sequences remain bounded and recover at the exact declared boundary |
| TERM-EMU-003 | Resize, reset, alternate-screen, wide/combining/orphan cell, history, and mode vectors preserve invariants |
| TERM-EMU-004 | Privileged sequences produce policy requests only and cannot execute clipboard/link/host effects directly |
| TERM-INPUT-001 | Text/key/IME vectors avoid duplicate text and never send preedit without negotiated support |
| TERM-INPUT-002 | Mode/geometry revision races reject, serialize, or re-evaluate exactly as declared |
| TERM-INPUT-003 | Paste, mouse, focus, extended keys, replies, and backpressure follow negotiated modes and policy |

## Accessibility and recording assertions

| ID | Assertion |
|---|---|
| TERM-ACCESS-001 | Logical state revision, reading order, cursor/focus, selection, viewport, and history map consistently to each platform adapter |
| TERM-ACCESS-002 | Output storms coalesce announcements without losing navigable history or omission disclosure |
| TERM-ACCESS-003 | Keyboard-only, zoom/contrast/reduced-motion, secure-input, and screen-reader scenarios satisfy host policy |
| TERM-RECORD-001 | Capture cannot start without complete authority/purpose/destination policy and independent data-class choices |
| TERM-RECORD-002 | Password/secure input, redaction, loss/gap, truncation, corruption, partial-finalization, and delete scenarios match claims |
| TERM-RECORD-003 | R1/R2 replay reproduces checkpoint/state and reports first divergence across artifact/configuration mutations |
| TERM-RECORD-004 | Ordinary playback cannot deliver recorded input to a live process |

## Renderer assertions

| ID | Assertion |
|---|---|
| TERM-RENDER-001 | Every delta/chunking/coalescing path produces the same final pixels and hit-test mapping as full redraw at the same revision |
| TERM-RENDER-002 | Versioned Unicode/font corpus covers combining, wide/ambiguous, emoji, variation, fallback, bidi/control, ligature, and missing-glyph policies |
| TERM-RENDER-003 | Fractional scale, resize, display migration, padding, and long pointer round trips show no cumulative cell drift |
| TERM-RENDER-004 | Attribute/color precedence, forced colors, high contrast, reduced motion, blink, bell, selection, cursor, and hyperlink cases match policy |
| TERM-RENDER-005 | Surface/device loss at every frame phase reconstructs from logical state without emulator mutation or stale-frame claim |
| TERM-RENDER-006 | Capture canaries remain absent from unauthorized screenshots, thumbnails, GPU diagnostics, crash artifacts, and telemetry |

Golden images are scoped to exact renderer, font artifacts, rasterizer, scale, color space, platform, and driver class. Semantic cell/run comparisons remain the cross-provider oracle; pixel equality is not claimed across unrelated text stacks.
