# ADR-0018: Pseudoterminals are not byte pipes

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

Both pipes and pseudoterminals expose byte-oriented host channels, but PTYs add terminal line discipline, modes, control characters, window size, hangup, controlling-session/process-group behavior, and terminal protocol translation. Windows ConPTY specifically carries UTF-8 plus virtual-terminal sequences over synchronous channels, while POSIX PTYs expose native terminal byte semantics.

## Decision

`rm.terminal.pseudoterminal` is independent from `rm.ipc.byte-pipe`. It owns session resource, attachment, size, wire-profile, terminal-state, transport, resize, and hangup semantics. A terminal session platform service composes it with direct process launch and optional supervision.

Terminal emulation, rendering, input-event encoding, Unicode cell layout, and accessible presentation remain higher layers. Raw terminal transport cannot claim their conformance.

## Consequences

- Process stdio can bind either plain byte resources or a terminal attachment without conflating them.
- Windows synchronous ConPTY transport is surfaced honestly instead of labeled native async.
- Portable mode presets expand into explicit properties with effective-state reporting.
- Accessibility/i18n requirements attach to emulator/renderer layers as well as transport error policy.

## Verification

Cross-platform tests cover wire profiles, terminal modes, attachment, resize, bidirectional deadlock, EOF/hangup, process groups, malformed encodings/sequences, shutdown, sensitive recordings, and explicit absence of higher-layer claims.

