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

