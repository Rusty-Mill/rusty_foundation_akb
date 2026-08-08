# Orderly shutdown platform service

| Field | Value |
|---|---|
| Status | Draft |
| Service specification version | 0.1.0 |
| Domain | Runtime |
| Owner | Unassigned |
| Decision | [ADR-0005](../../adr/0005-orderly-shutdown-is-a-platform-service.md) |
| Suggested workloads | CLI, Desktop, Server; optional for Embedded/headless |

## Purpose

Coordinate a bounded transition from accepting work to a stopped state while preserving dependency order, cleanup obligations, diagnostics, and explicit escalation policy.

This is a platform-service specification. It composes capabilities and policy; it is not a capability, provider, or member of the capability dependency graph.

## Non-goals

- Terminating the process or killing threads.
- Guaranteeing cleanup after external process termination, power loss, or kernel failure.
- Inventing one universal ordering for every application.

## State model

```text
running -> quiescing -> draining -> stopping -> stopped
   |           |           |           |
   +-----------+-----------+-----------+--> failed (diagnosed, policy-controlled)
```

- **Quiescing:** reject or redirect new work.
- **Draining:** allow owned in-flight work to complete within policy.
- **Stopping:** request cancellation, release resources in dependency order, and collect failures.
- **Stopped:** no owned work may begin or continue.

## Requirements

- **RM-RUNTIME-SHUTDOWN-0001:** Initiating shutdown **MUST** be idempotent and produce one shared terminal report.
- **RM-RUNTIME-SHUTDOWN-0002:** After quiescing is visible, governed components **MUST NOT** accept new ordinary work.
- **RM-RUNTIME-SHUTDOWN-0003:** Components **MUST** stop in reverse dependency order unless an explicit ordering constraint overrides it.
- **RM-RUNTIME-SHUTDOWN-0004:** Each phase **MUST** support a monotonic deadline and explicit escalation policy.
- **RM-RUNTIME-SHUTDOWN-0005:** A component failure **MUST NOT** silently prevent independent components from receiving shutdown notification.
- **RM-RUNTIME-SHUTDOWN-0006:** The terminal report **MUST** preserve each component's outcome, timeout/escalation, and relevant diagnostic context.
- **RM-RUNTIME-SHUTDOWN-0007:** Shutdown **MUST** be awaitable asynchronously and synchronously observable without nesting an async runtime.
- **RM-RUNTIME-SHUTDOWN-0008:** Registration after quiescing begins **MUST** fail explicitly except for resources created by the shutdown procedure itself.
- **RM-RUNTIME-SHUTDOWN-0009:** Reentrant initiation **MUST** join the existing shutdown operation rather than start another sequence.
- **RM-RUNTIME-SHUTDOWN-0010:** A deadline expiry **MUST NOT** imply that arbitrary work can be safely killed; escalation options and residual risk **MUST** be explicit.

## Dependencies

| Relationship | Capability | Reason |
|---|---|---|
| requires | `rm.runtime.cancellation` | Signals governed work during escalation |
| requires | `rm.time.deadline-timer` | Bounds graceful phases |

## Policy inputs

Phase deadlines, component ordering, failure aggregation, escalation actions, and whether termination is delegated to an application/process supervisor. Policy is supplied; it is not compiled into the mechanism.

## Observability

Emit structured phase transitions, elapsed time, outstanding component counts, escalations, and per-component terminal outcomes. Component names must be stable but avoid embedding secrets or user data.

## Conformance plan

Test normal drain, dependency ordering, concurrent initiation, reentrancy, late registration, component failure aggregation, deadline escalation, non-cooperating work, async and sync observation, and exactly-once terminal reporting.

## Open questions

- How are dynamically changing dependency graphs frozen for shutdown?
- Which escalation policies belong in common contracts versus application frameworks?
