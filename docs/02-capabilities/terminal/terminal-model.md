# Terminal semantic model

**Status:** Draft

## Roles

| Role | Responsibility |
|---|---|
| Session provider | Native PTY/pseudoconsole lifecycle, child attachment, byte transport, size and terminal-state operations |
| Protocol adapter | Declared encoding and control-sequence dialect; converts structured host input where supported |
| Emulator | Parses output into screen/cursor/style/history state and produces protocol input |
| Renderer | Presents glyphs, color, cursor, selection, and viewport |
| Accessibility adapter | Exposes semantic text, focus, navigation, announcements, and user preferences to assistive technology |

No lower role may claim guarantees owned by a higher role. In particular, a valid byte stream does not prove correct Unicode grapheme layout or accessibility.

## Wire profiles

| Profile | Meaning |
|---|---|
| W0 — Native opaque | Provider documents native bytes/state; no portable encoding or control dialect |
| W1 — Declared | Encoding and input/output control dialects are named and versioned |
| W2 — UTF-8 VT | UTF-8 text plus a specified virtual-terminal input/output profile and error policy |
| W3 — Negotiated | W2 plus explicit feature negotiation/disclosure and conformance corpus |

Profiles are not automatically ordered by fidelity for every native application. Translation may lose code-page, legacy console API, termios, or device-specific behavior and must be disclosed.

## Size and resize

Portable size is positive columns and rows. Pixel dimensions, cell size, DPI, and viewport history are optional metadata. Resize is an ordered session operation; providers state when the attached application can observe it and whether a native notification/event accompanies it. Resize success does not mean the application has redrawn.

## Terminal modes

Canonical/raw input, echo, signal-generating characters, flow control, output postprocessing, control characters, and job-control relationships are provider-scoped terminal properties. A portable preset expands to explicit supported properties and reports unsupported or ignored members. The model never serializes an opaque native `termios` structure as a portable contract.

## Text and internationalization

- The wire encoding and decoder error policy are explicit.
- Grapheme segmentation, East Asian/emoji width, normalization, bidirectional display, font fallback, locale, and input-method composition belong to host/emulator policy.
- Cell width is not derivable from Unicode scalar count alone.
- Raw session recording may contain secrets and personal data; retention and redaction are explicit.

## Accessibility

A terminal host cannot satisfy accessibility merely by exposing rendered pixels or raw escape sequences. The emulator/accessibility layer retains logical text, cursor/focus, selection, reading order, update regions, live announcements, contrast/user preferences, and a non-color-only representation where possible. Applications emitting only visual cursor motion may limit recoverable semantics; the limitation is disclosed rather than fabricated.

