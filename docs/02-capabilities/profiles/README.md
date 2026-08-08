# Foundation profile comparison

**Status:** Draft profiles at version 1.0.0

These manifests validate profile resolution against the currently specified vertical slices. `R` is required, `C` conditional, `O` optional, and `—` not selected by the profile.

| Member | CLI | Desktop | Server | Headless |
|---|---:|---:|---:|---:|
| `rm.time.monotonic-clock` | R | R | R | R |
| `rm.time.deadline-timer` | R | R | R | O |
| `rm.runtime.cancellation` | R | R | R | R |
| `rm.filesystem.directory` | R | R | R | O |
| `rm.filesystem.resolve` | R | R | R | O |
| `rm.filesystem.file` | R | R | R | O |
| `rm.filesystem.metadata` | R | R | R | O |
| `rm.filesystem.atomic-replace` | O | R | C | O |
| `rm.security.random` | R | R | R | R |
| `rm.security.attenuate` | O | O | O | O |
| `rm.security.secret-store` | O | R | R | O |
| `rm.process.spawn` | R | R | R | O |
| `rm.process.control` | R | R | R | O |
| `rm.process.executable-resolve` | O | O | O | O |
| `rm.ipc.byte-pipe` | O | O | O | O |
| Orderly shutdown service | O | O | R | O |
| Process supervision service | O | O | C | O |
| Restricted execution service | O | O | O | O |

The table is only a view. Each manifest defines exact contract ranges, predicates, and quality constraints.

## Interactive CLI extension

[`rm.profile.foundation.interactive-cli` 0.1.0](foundation-interactive-cli.md) extends CLI 1.0.0 with `rm.terminal.pseudoterminal` and the terminal session service. It is a separate identity because terminal hosting is not required by redirected/batch CLI workloads and still has emulator, input, Unicode-layout, rendering, and accessibility gaps.

## Version transition

Version 1.0.0 adds direct process launch/control to CLI, Desktop, and Server. This is deliberately a profile-major change from 0.1.0 because it can invalidate a previously satisfied provider set. Byte pipes and executable resolution remain optional. Server supervision is conditional on launching managed workers.

## Explicit gaps

These profiles are incomplete for real applications because terminal, networking, configuration, observability, wall/calendar time, windowing, graphics, input, accessibility, i18n, and audio contracts are not yet all specified. Resolution reports must preserve those gaps; the foundation profile name prevents a false completeness claim.

## Shared prohibitions

- Silent plaintext secret-file fallback.
- Hidden async runtime creation by sync paths.
- Silent capability degradation or emulation.
- Security decisions based solely on OS name.
- Ambient current-directory authority for security-sensitive filesystem resolution.
