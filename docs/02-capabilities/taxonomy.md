# Initial capability taxonomy

This is an inventory for domain analysis, not an API or crate list.

| Domain | Initial concerns |
|---|---|
| Runtime | initialization, execution context, task scheduling, cancellation, shutdown |
| Process | spawn, identity, environment, stdio, signals/control, isolation |
| Threading | threads, synchronization, affinity, priorities, thread-local state |
| Async I/O | reactors/completion, readiness, timers, cancellation, backpressure |
| IPC | anonymous/named channels, byte streams, messages, handle transfer, shared memory |
| Terminal | pseudoterminals, modes, terminal protocol, sessions, emulation, accessible presentation |
| Memory | allocation, mapping, protection, shared memory, locking, large pages |
| Filesystem | paths, files, directories, metadata, watching, atomicity, permissions |
| Networking | resolution, sockets, transports, interfaces, routing awareness, security |
| Security | identity, credentials, authorization, secrets, sandboxing, cryptographic services |
| Windowing | surfaces, lifecycle, display topology, DPI, accessibility integration |
| Graphics | devices, presentation, synchronization, resource transfer, compute |
| Input | keyboard, pointer, touch, pen, game controllers, IME |
| Audio | devices, streams, routing, timing, formats, real-time constraints |
| Time | clocks, instants, duration, calendar, timezone, timers |
| Plugins | discovery, compatibility, isolation, authority, lifecycle |
| Configuration | sources, precedence, schema, change notification, secrets separation |
| Observability | logs, traces, metrics, diagnostics, crash/error reporting |

Each domain will be decomposed into common, optional/advanced, and platform-specific capabilities. Platform-specific features may remain explicit extensions when a truthful common contract is impossible.

## Active domain analyses

- [Runtime and time vertical slice](runtime-time/README.md) — Draft
- [Filesystem foundations vertical slice](filesystem/README.md) — Draft
- [Security and authority foundations vertical slice](security/README.md) — Draft
- [Process foundations vertical slice](process/README.md) — Draft
- [IPC foundations vertical slice](ipc/README.md) — Draft
- [Terminal foundations vertical slice](terminal/README.md) — Draft
- [Windowing foundations vertical slice](windowing/README.md) — Draft
- [Graphics and presentation vertical slice](graphics/README.md) — Draft
- [Input foundations vertical slice](input/README.md) — Draft
- [Text, fonts, and layout vertical slice](text/README.md) — Draft
- [Accessibility foundations vertical slice](accessibility/README.md) — Draft
- [Clipboard and drag-and-drop data-transfer vertical slice](data-transfer/README.md) — Draft
- [Internationalization and localization vertical slice](internationalization/README.md) — Draft
- [Configuration and change-notification vertical slice](configuration/README.md) — Draft
- [Observability, diagnostics, and crash-reporting vertical slice](observability/README.md) — Draft
- [Application lifecycle and session-integration vertical slice](lifecycle/README.md) — Draft
- [Networking foundations vertical slice](networking/README.md) — Draft
- [Memory and mapping foundations vertical slice](memory/README.md) — Draft
- [Plugin and module lifecycle vertical slice](plugins/README.md) — Draft
