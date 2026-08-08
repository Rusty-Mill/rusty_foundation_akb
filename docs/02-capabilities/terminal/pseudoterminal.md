# `rm.terminal.pseudoterminal` — Pseudoterminal resource

| Field | Value |
|---|---|
| Status | Draft |
| Contract version | 0.1.0 |
| Domain | Terminal |
| Owner | Unassigned |
| Candidate profiles | CLI, Desktop, Server; optional Embedded/headless |

## Purpose

Create an owned pseudoterminal resource with host input/output channels, a single-use child-attachment resource, initial character-cell size, declared wire profile, and lifecycle/resize semantics.

## Requirements

- **RM-TERMINAL-PTY-0001:** Creation **MUST** return a complete session resource, host channels, and attachment resource or fail without partially usable state.
- **RM-TERMINAL-PTY-0002:** Initial columns and rows **MUST** be positive, range-checked, and applied before attached child code is released.
- **RM-TERMINAL-PTY-0003:** Host input/output direction and channel blocking/async quality **MUST** be explicit and **MUST NOT** inherit byte-pipe guarantees automatically.
- **RM-TERMINAL-PTY-0004:** The provider **MUST** declare W0–W3 wire profile, encoding, control dialect, decoder/encoder error policy, and translation boundaries.
- **RM-TERMINAL-PTY-0005:** The attachment resource **MUST** be authority-bearing, non-serializable by default, and consumable only according to its declared single/multi-attach policy.
- **RM-TERMINAL-PTY-0006:** Attachment **MUST** bind the intended child before release and **MUST NOT** leak unrelated session/transport handles or descriptors.
- **RM-TERMINAL-PTY-0007:** Resize **MUST** preserve operation order, report exact accepted size, and distinguish provider acceptance from application observation/redraw.
- **RM-TERMINAL-PTY-0008:** Input writes and output reads **MAY** be partial and backpressured; accepted bytes are never rolled back by cancellation.
- **RM-TERMINAL-PTY-0009:** EOF, hangup, broken peer, child exit, host-channel close, and session close **MUST** have distinct provider-mapped lifecycle outcomes where observable.
- **RM-TERMINAL-PTY-0010:** Closing the host channels **MUST** state whether it sends hangup, closes the session, or only removes that reference; drop cannot invent policy.
- **RM-TERMINAL-PTY-0011:** Sync paths **MUST** be complete without a hidden runtime; async paths **MUST** disclose native versus adapted blocking and resource budgets.
- **RM-TERMINAL-PTY-0012:** Concurrent input, output, resize, control, child exit, and close **MUST** define ordering and terminal outcomes without deadlock.
- **RM-TERMINAL-PTY-0013:** Provider-specific mode operations **MUST** enumerate supported properties and return effective state; ignored settings **MUST NOT** be reported as applied.
- **RM-TERMINAL-PTY-0014:** Diagnostics and recordings **MUST** exclude stream content and sensitive title/path/command metadata unless explicit capture authority and retention policy allow them.
- **RM-TERMINAL-PTY-0015:** The capability **MUST NOT** claim rendering, Unicode cell width, input-event fidelity, shell semantics, or accessibility conformance.

## Dependencies

No required capability dependency for native resource creation. The terminal session service composes it with `rm.process.spawn`; runtime cancellation is optional. Providers may internally use pipe-like transports without changing this contract's terminal semantics.

