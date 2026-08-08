# Terminal accessibility and semantic presentation model

**Status:** Draft cross-cutting contract 0.1.0

## Principle

The accessibility surface is derived from the emulator's logical state and trusted semantic annotations, not pixels and not reparsing raw escape sequences. A terminal is highly dynamic and two-dimensional; naïvely announcing every cell mutation is unusable.

## Semantic views

- **Viewport text:** logical lines/cells with selection, cursor/focus, style only where semantically useful, and stable revision.
- **History/log view:** ordered accessible text history with navigation, search, copy, truncation disclosure, and append notifications.
- **Live updates:** coalesced status/output announcements governed by user preference, focus, rate, severity, and trusted semantic marks.
- **Host controls:** tabs/panes, search, settings, copy/paste prompts, connection/session status, and recording indicators as ordinary accessible controls.

## Requirements

- **RM-TERMINAL-ACCESS-0001:** Accessibility updates **MUST** bind to emulator revisions and never expose a mixed screen state.
- **RM-TERMINAL-ACCESS-0002:** Logical reading order, cursor/focus, selection, viewport, and history boundaries **MUST** be explicit; visual coordinates alone are insufficient.
- **RM-TERMINAL-ACCESS-0003:** High-frequency output **MUST** be coalesced/rate-limited under user policy while retaining a navigable history and indicating omitted announcements.
- **RM-TERMINAL-ACCESS-0004:** Color, inverse, blinking, cursor shape, and position **MUST NOT** be the sole representation of actionable host state.
- **RM-TERMINAL-ACCESS-0005:** Zoom, font, contrast, reduced motion, cursor visibility, audible/visual bell, and animation preferences **MUST** be honored by the renderer/host without changing emulator truth.
- **RM-TERMINAL-ACCESS-0006:** Keyboard-only navigation **MUST** reach host controls, viewport/history, selection, search, and an unambiguous return-to-child-input action.
- **RM-TERMINAL-ACCESS-0007:** Password/secure-input state **MUST** minimize announcements and history capture under policy while disclosing that terminal protocols cannot prove remote secrecy.
- **RM-TERMINAL-ACCESS-0008:** Semantic shell/application annotations **MUST** be untrusted by default, allowlisted by dialect/policy, and unable to inject privileged accessibility roles or host actions.
- **RM-TERMINAL-ACCESS-0009:** Platform accessibility adapters **MUST** expose equivalent semantic outcomes while documenting API-specific variance; a web ARIA mapping is not the universal model.

WAI-ARIA's `log` and live-region concepts are useful mappings for web hosts, while Windows UI Automation and macOS Accessibility require native adapters. The semantic contract above them remains platform-neutral.

