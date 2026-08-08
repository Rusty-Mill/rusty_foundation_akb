# `rm.process.spawn` — Direct process launch and child lifecycle

| Field | Value |
|---|---|
| Status | Draft |
| Contract version | 0.1.0 |
| Domain | Process |
| Owner | Unassigned |
| Candidate profiles | CLI, Desktop, Server; optional Embedded/headless |

## Purpose

Launch an explicitly identified executable without implicit shell interpretation or path search, under a deterministic argument/environment/inheritance manifest, and return an owned child resource with truthful startup and termination observations.

## Requirements

- **RM-PROCESS-SPAWN-0001:** The executable **MUST** be explicit and separate from arguments; the base operation **MUST NOT** invoke a shell or search path.
- **RM-PROCESS-SPAWN-0002:** Arguments **MUST** use the launch model's structured native values; provider conversion loss or an unsupported target parsing convention **MUST** fail before launch.
- **RM-PROCESS-SPAWN-0003:** Environment construction **MUST** use an immutable explicit snapshot/mode and report provider-mandated additions or rewrites.
- **RM-PROCESS-SPAWN-0004:** Native handles, descriptors, standard streams, control channels, current directory, environment, and other inheritable resources **MUST** be deny-by-default and allowlisted.
- **RM-PROCESS-SPAWN-0005:** A requested working directory **MUST** use explicit directory authority and **MUST NOT** change the parent process current directory.
- **RM-PROCESS-SPAWN-0006:** Launch **MUST** distinguish preparation failure, native creation, image-confirmation status where observable, optional application readiness, and early child exit.
- **RM-PROCESS-SPAWN-0007:** A child resource **MUST** bind to the native process object with the strongest available race resistance; a numeric process identifier alone **MUST NOT** authorize control.
- **RM-PROCESS-SPAWN-0008:** Waiting **MUST** be multi-observer safe or explicitly single-consumer; the terminal status **MUST** be stable after observation.
- **RM-PROCESS-SPAWN-0009:** Termination status **MUST** distinguish normal exit, native signal/exception/forced termination, unknown/lost observation, and provider startup failure where distinguishable.
- **RM-PROCESS-SPAWN-0010:** Dropping/closing a child resource **MUST** declare whether the child continues, is supervised elsewhere, or is terminated; no default may silently kill a running child.
- **RM-PROCESS-SPAWN-0011:** Cancellation of launch or wait **MUST** not fabricate child termination; ambiguous creation/ownership outcomes **MUST** be surfaced and reconciled.
- **RM-PROCESS-SPAWN-0012:** Sync launch and wait paths **MUST NOT** create or nest a hidden async runtime; async wait **MUST** avoid occupying a worker solely to block where native notification is available.
- **RM-PROCESS-SPAWN-0013:** Concurrent launches **MUST NOT** leak resources intended for another child, including when the parent is multithreaded.
- **RM-PROCESS-SPAWN-0014:** Errors **MUST** use portable semantic categories and preserve sanitized native diagnostics.
- **RM-PROCESS-SPAWN-0015:** Arguments, environment, paths, and diagnostics **MUST** follow field-level sensitivity/redaction policy.
- **RM-PROCESS-SPAWN-0016:** Restricted identity, sandboxing, resource limits, descendant control, and durable service registration **MUST NOT** be claimed unless a composing service applies and verifies them before child-controlled code executes.

## Child operations

The base child resource supports identity observation, nonblocking status query, sync/async wait, and deterministic handle close. Graceful interrupt, force termination, process-group/tree control, suspend/resume, priority, affinity, accounting, and debugging are separately discoverable operations or later capabilities because native semantics and authority differ.

## Error categories

Executable not found, executable changed/policy mismatch, format/architecture unsupported, access denied, invalid argument/environment, unsupported argument convention, invalid inherited resource, resource/quota exhausted, provider unavailable, creation failed, startup outcome indeterminate, confirmed canceled, and other provider failure with sanitized context.

## Dependencies

The base capability has no required capability dependency. It optionally uses filesystem resources for executable/working-directory/stdio authority, runtime cancellation, and monotonic timestamps. Restricted execution composes it as a service rather than changing its minimum contract.

