# `rm.profile.foundation.cli`

| Field | Value |
|---|---|
| Status | Draft |
| Version | 1.0.0 |
| Purpose | Non-interactive command workload using explicit filesystem authority and bounded operations |

## Workload assumptions

Single-user invocation, no GUI event loop, terminal/stdio contract not yet selected, and no secret prompt permitted by default. The caller supplies directory authority; process current directory is not the security boundary.

## Required capabilities

| ID | Capability | Contract | Constraints |
|---|---|---|---|
| RM-PROFILE-FOUNDATION-CLI-0001 | `rm.time.monotonic-clock` | `>=0.1.0,<0.2.0` | Domain disclosed; never wall time |
| RM-PROFILE-FOUNDATION-CLI-0002 | `rm.time.deadline-timer` | `>=0.1.0,<0.2.0` | Sync and async paths; no hidden runtime |
| RM-PROFILE-FOUNDATION-CLI-0003 | `rm.runtime.cancellation` | `>=0.1.0,<0.2.0` | Cooperative terminal outcomes |
| RM-PROFILE-FOUNDATION-CLI-0004 | `rm.filesystem.directory` | `>=0.1.0,<0.2.0` | Explicit owned/borrowed authority |
| RM-PROFILE-FOUNDATION-CLI-0005 | `rm.filesystem.resolve` | `>=0.1.0,<0.2.0` | At least R1; requested traversal policy preserved |
| RM-PROFILE-FOUNDATION-CLI-0006 | `rm.filesystem.file` | `>=0.1.0,<0.2.0` | Positioned I/O and sync completeness |
| RM-PROFILE-FOUNDATION-CLI-0007 | `rm.filesystem.metadata` | `>=0.1.0,<0.2.0` | Unknown fields preserved |
| RM-PROFILE-FOUNDATION-CLI-0008 | `rm.security.random` | `>=0.1.0,<0.2.0` | OS cryptographic source; fail closed |
| RM-PROFILE-FOUNDATION-CLI-0013 | `rm.process.spawn` | `>=0.1.0,<0.2.0` | Direct explicit launch; allowlisted inheritance |
| RM-PROFILE-FOUNDATION-CLI-0014 | `rm.process.control` | `>=0.1.0,<0.2.0` | Owned-child targeting; dispatch distinct from terminal state |

## Optional members

- **RM-PROFILE-FOUNDATION-CLI-0009:** `rm.filesystem.atomic-replace` is optional for configuration/output publication and requires a declared durability level.
- **RM-PROFILE-FOUNDATION-CLI-0010:** `rm.security.secret-store` is optional only when interaction is prohibited and the provider remains available; otherwise secret-dependent features are unavailable.
- **RM-PROFILE-FOUNDATION-CLI-0011:** Authority attenuation, orderly shutdown, and restricted execution are optional.
- **RM-PROFILE-FOUNDATION-CLI-0012:** Networking and synchronization side effects are prohibited.
- **RM-PROFILE-FOUNDATION-CLI-0015:** `rm.process.executable-resolve` is optional and, when selected, uses explicit directory authority rather than ambient `PATH` or current directory.
- **RM-PROFILE-FOUNDATION-CLI-0016:** `rm.ipc.byte-pipe` is optional for redirection/pipeline work; async use requires Q2 or Q3 unless a bounded Q1 worker budget is explicitly accepted.

## Budgets and evidence

Startup and first-use latency are reported separately. Provider initialization cannot emit user-facing prompts. Every selected provider has evidence for the exact OS/filesystem/store context. No networking or synchronization side effect is permitted by this foundation profile.

## History

- **1.0.0:** Adds required direct process launch and owned-child control; adds optional executable resolution and byte pipes. Major because provider satisfiability changes.
- **0.1.0:** Initial runtime, filesystem, random, and optional service trial.
