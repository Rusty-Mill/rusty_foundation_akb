# Terminal session platform service

| Field | Value |
|---|---|
| Status | Draft service contract |
| Contract version | 0.1.0 |
| Layer | Platform services |

## Purpose

Compose a pseudoterminal resource with direct process launch, optional supervision, and host-channel lifecycle so an interactive child begins execution attached to the intended terminal state.

## Requirements

- **RM-TERMINAL-SESSION-0001:** The service **MUST** resolve pseudoterminal, spawn, attachment, authority, wire profile, size, and lifecycle policy before child release.
- **RM-TERMINAL-SESSION-0002:** Child standard channels and controlling-console/terminal relationship **MUST** be established atomically or while the child cannot execute application code.
- **RM-TERMINAL-SESSION-0003:** Preparation failure/cancellation **MUST** close transport/session resources and reconcile any created child without ambiguous ownership.
- **RM-TERMINAL-SESSION-0004:** Readiness **MUST** distinguish terminal created, child created, attachment confirmed, image confirmed, and optional application/shell handshake.
- **RM-TERMINAL-SESSION-0005:** Stop policy **MUST** order input closure/EOF, cooperative control, hangup, bounded wait, escalation, output drain, and final close explicitly.
- **RM-TERMINAL-SESSION-0006:** Session completion **MUST** retain child terminal status, transport/hangup outcome, output-drain completeness, and supervision-set status.
- **RM-TERMINAL-SESSION-0007:** Multiple attached processes, foreground process groups, console sharing, and job control **MUST** be unavailable unless the provider declares and verifies their exact semantics.
- **RM-TERMINAL-SESSION-0008:** Host failure/drop **MUST** follow a declared detach, transfer, hangup, or terminate policy.

## Composition boundary

The service may use process supervision for descendant lifecycle and restricted execution for authority isolation. Neither terminal attachment nor a PTY alone constitutes sandboxing. A terminal emulator/renderer consumes the host channels above this service and owns accessible presentation.

