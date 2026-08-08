# `rm.profile.foundation.interactive-cli`

| Field | Value |
|---|---|
| Status | Draft |
| Version | 0.1.0 |
| Extends | `rm.profile.foundation.cli` 1.0.0 without weakening |
| Purpose | Host an interactive character-cell child session under explicit terminal and process lifecycle semantics |

## Workload assumptions

The application acts as or embeds a terminal host for a directly launched child. It owns bidirectional progress, resize, control, shutdown, output drain, and sensitive-session policy. A full terminal emulator, renderer, structured input encoder, and accessibility adapter remain required higher-layer gaps.

## Requirements

- **RM-PROFILE-FOUNDATION-INTERACTIVE-CLI-0001:** Every requirement and prohibition of CLI foundation 1.0.0 remains in force.
- **RM-PROFILE-FOUNDATION-INTERACTIVE-CLI-0002:** Requires `rm.terminal.pseudoterminal` `>=0.1.0,<0.2.0` with W2 or W3 for a portable UTF-8 VT host; W0/W1 requires an explicitly provider-specific host.
- **RM-PROFILE-FOUNDATION-INTERACTIVE-CLI-0003:** Requires terminal session service `>=0.1.0,<0.2.0` with atomic pre-release attachment and complete child/session/output-drain results.
- **RM-PROFILE-FOUNDATION-INTERACTIVE-CLI-0004:** Host input and output must make independent progress; a bounded Q1 blocking adaptation is permitted only with dedicated-thread, queue, shutdown, and saturation budgets.
- **RM-PROFILE-FOUNDATION-INTERACTIVE-CLI-0005:** Positive initial rows/columns, resize ordering, accepted-versus-observed distinction, and malformed-wire policy are explicit.
- **RM-PROFILE-FOUNDATION-INTERACTIVE-CLI-0006:** Raw session recording is prohibited unless capture authority, user disclosure, encryption/storage provider, retention, export, and deletion policy are supplied.
- **RM-PROFILE-FOUNDATION-INTERACTIVE-CLI-0007:** The profile remains unsatisfied for an end-user terminal product until the terminal host framework contracts are selected/evidenced and concrete windowing, graphics/text, and platform accessibility adapters are available.

## Optional composition

Process supervision is optional for multi-process terminal jobs and must retain exact containment claims. Restricted execution is optional and does not follow from terminal attachment. Byte pipes may support side channels but cannot substitute for the pseudoterminal.

## Evidence gates

Conformance spans ConPTY and POSIX PTY providers; bidirectional saturation; attachment and early-exit races; resize storms; W2 protocol corpus; emulator/input/accessibility/renderer/recording component suites; hangup/shutdown; sensitive capture canaries; and explicit windowing/graphics adapter gaps. Performance reports synchronous transport resources separately from native readiness paths.
