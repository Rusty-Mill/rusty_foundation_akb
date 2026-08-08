# `rm.process.control` — Owned-child control

| Field | Value |
|---|---|
| Status | Draft |
| Contract version | 0.1.0 |
| Domain | Process |
| Owner | Unassigned |
| Candidate profiles | CLI, Desktop, Server; optional Embedded/headless |

## Purpose

Request a control action against one owned child process without targeting by a reusable numeric identifier and without implying that request acceptance equals process termination.

## Action classes

| Action | Portable meaning | Non-guarantee |
|---|---|---|
| Cooperative stop | Deliver a named, pre-negotiated application or platform request | Target observes, handles, or exits |
| Interrupt | Deliver the provider's declared interactive-interrupt event | Uniform mapping to POSIX `SIGINT` or Windows console events |
| Terminate | Request prompt OS termination without application cleanup guarantees | Immediate disappearance, descendant termination, or resource durability |
| Query liveness | Observe whether the bound child object has reached a terminal state | Application health or readiness |

Provider-specific signals, exceptions, console events, suspend/resume, debugging, and arbitrary native control codes are extensions with explicit authority and semantics.

## Requirements

- **RM-PROCESS-CONTROL-0001:** Every action **MUST** target an owned child resource or equally strong provider object binding; a numeric PID alone **MUST NOT** be accepted as authority.
- **RM-PROCESS-CONTROL-0002:** The requested action, target scope, required authority, and provider mapping **MUST** be discoverable before dispatch.
- **RM-PROCESS-CONTROL-0003:** A successful dispatch **MUST** mean only that the provider accepted/delivered the request at its declared boundary; terminal state is confirmed through child wait/status.
- **RM-PROCESS-CONTROL-0004:** Cooperative stop and interrupt **MUST NOT** silently degrade to forced termination.
- **RM-PROCESS-CONTROL-0005:** Termination **MUST** disclose application-cleanup, finally/destructor, buffer-flush, and durability non-guarantees.
- **RM-PROCESS-CONTROL-0006:** Single-process scope **MUST NOT** claim descendant, process-group, console-group, job, or service containment.
- **RM-PROCESS-CONTROL-0007:** Control racing with natural exit **MUST** produce accepted, already terminal, access denied, stale/lost target, or indeterminate—not fabricated causality.
- **RM-PROCESS-CONTROL-0008:** Repeated actions **MUST** document idempotency and behavior after terminal observation.
- **RM-PROCESS-CONTROL-0009:** Cancellation **MUST** stop waiting for dispatch confirmation where possible but **MUST NOT** retract a request already delivered.
- **RM-PROCESS-CONTROL-0010:** Audit and errors **MUST** identify action class and sanitized target correlation without exposing credentials or sensitive command data.

## Platform direction

Windows process handles and `TerminateProcess`, Linux pidfds and `pidfd_send_signal` where available, and macOS/POSIX process lifecycle mechanisms are candidate single-target mappings. Windows console control events require console/process-group preconditions and therefore are not a universal interrupt mapping.

## Dependencies

Requires `rm.process.spawn`'s owned child resource contract. It optionally observes `rm.runtime.cancellation`. Multi-process containment belongs to the [supervision service](supervision.md).

