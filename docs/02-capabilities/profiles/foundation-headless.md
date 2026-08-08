# `rm.profile.foundation.headless`

| Field | Value |
|---|---|
| Status | Draft |
| Version | 0.1.0 |
| Purpose | Minimal non-interactive foundation for constrained or appliance-style deployments |

## Workload assumptions

Memory, binary-size, startup, thread, allocation, and power budgets are supplied by the deployment rather than invented by the profile. There is no assumption of a filesystem, persistent store, user session, heap allocator shape, or full async executor.

## Required capabilities

| ID | Capability | Contract | Constraints |
|---|---|---|---|
| RM-PROFILE-FOUNDATION-HEADLESS-0001 | `rm.time.monotonic-clock` | `>=0.1.0,<0.2.0` | Required clock domain explicitly selected |
| RM-PROFILE-FOUNDATION-HEADLESS-0002 | `rm.runtime.cancellation` | `>=0.1.0,<0.2.0` | Allocation/resource behavior within deployment budget |
| RM-PROFILE-FOUNDATION-HEADLESS-0003 | `rm.security.random` | `>=0.1.0,<0.2.0` | OS/platform cryptographic source ready before secret-dependent work |

## Optional members

- **RM-PROFILE-FOUNDATION-HEADLESS-0004:** Deadline timers are optional when the workload has deadlines.
- **RM-PROFILE-FOUNDATION-HEADLESS-0005:** Filesystem capabilities are selected as a coherent conditional group beginning with directory authority and resolution; presence of a filesystem is never inferred.
- **RM-PROFILE-FOUNDATION-HEADLESS-0006:** Secret storage is optional and must be non-interactive.
- **RM-PROFILE-FOUNDATION-HEADLESS-0007:** Atomic replacement requires a writable filesystem with declared support; platform services are optional and individually budgeted.

## Prohibitions and evidence

Interactive prompts, desktop-service dependencies, hidden background threads, hidden async runtimes, unbounded allocation, network fallback, and silent persistent writes are prohibited. Evidence reports code/data size contribution, allocations, threads, handles/descriptors, timer overhead, entropy readiness, power-sensitive wakeups, and all optional members included in the resolved graph.
