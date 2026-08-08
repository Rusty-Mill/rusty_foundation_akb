# Initial capability taxonomy

This is an inventory for domain analysis, not an API or crate list.

| Domain | Initial concerns |
|---|---|
| Runtime | initialization, execution context, task scheduling, cancellation, shutdown |
| Process | spawn, identity, environment, stdio, signals/control, isolation |
| Activation | typed intents, handlers, associations, file/URI handoff, instance routing |
| Threading | threads, synchronization, affinity, priorities, thread-local state |
| Async I/O | reactors/completion, readiness, timers, cancellation, backpressure |
| IPC | anonymous/named channels, byte streams, messages, handle transfer, shared memory |
| Terminal | pseudoterminals, modes, terminal protocol, sessions, emulation, accessible presentation |
| Memory | allocation, mapping, protection, shared memory, locking, large pages |
| Filesystem | paths, files, directories, metadata, watching, atomicity, permissions |
| Storage | media, regions, filesystems, volumes, mounts, capacity, removable-media coordination |
| Networking | resolution, sockets, transports, interfaces, routing awareness, secure channels, HTTP semantics/mechanics, real-time sessions |
| Messaging | schemas/envelopes, RPC, streams, publish/subscribe, broker settlement, retry/deduplication, reconciliation |
| Coordination | membership, failure evidence, leases/fencing, election/locks, consensus, consistency, distributed transactions |
| Persistence | logical data/query models, sessions/pools, transactions, constraints/indexes, migrations, change streams, backup/restore, replication |
| Object storage | namespaces/keys/versions, streaming/multipart, conditions, content addressing, delegation, lifecycle/retention, replication/recovery |
| Caching and delivery | canonical keys/partitions, freshness/validation, tiers/eviction, collapse, invalidation/coherence, CDN/edge behavior |
| Search and retrieval | document projections, schemas/analyzers, lexical/vector/spatial indexes, query/ranking, pagination/facets, migration/recovery |
| Security | identity, credentials, authorization, secrets, sandboxing, cryptographic policy/operations/keys/providers |
| Signed artifacts | signed views, code/package/document signatures, timestamps, transparency, provenance, reproducibility, acceptance policy |
| Package management | package identity, repositories, dependency resolution, install/update transactions, rollout, rollback, removal, recovery |
| Windowing | surfaces, lifecycle, display topology, DPI, accessibility integration |
| Graphics | devices, presentation, synchronization, resource transfer, compute |
| Display color | image descriptions, display evidence, transforms, HDR, profiles, calibration |
| Still image | probing, containers, decode/encode, pixels, metadata, animation, transforms |
| Time media | containers, tracks, codecs, timelines, playback, synchronization, muxing |
| Input | keyboard, pointer, touch, pen, game controllers, IME |
| Audio | devices, streams, routing, timing, formats, real-time constraints |
| Capture | cameras, authorization, raw frames, controls, timing, privacy, backpressure |
| Screen capture | trusted display/window/application/region selection, revocable sessions, compositor observations, cursor/audio, protection boundaries |
| Remote interaction | participant/session grants, remote presentation, controlled input, coordinate/keymap mapping, local override, emergency revocation |
| Background services | definitions, registration, execution scopes, demand activation, durable schedules, triggers, attempts, checkpoints, updates |
| Notifications | content, attention policy, presentation requests, actions, scheduling, badges |
| Power | sources, batteries, saver policy, thermal pressure, sleep assertions, energy evidence |
| Printing | destinations, capability negotiation, pagination, job tickets, spooling, document artifacts |
| Devices | enumeration, identity evidence, properties, topology, hotplug, class handoff |
| Time | clocks, instants, duration, calendar, timezone, timers |
| Plugins | discovery, compatibility, isolation, authority, lifecycle |
| Configuration | sources, precedence, schema, change notification, secrets separation |
| Observability | logs, traces, metrics, diagnostics, crash/error reporting |

Each domain will be decomposed into common, optional/advanced, and platform-specific capabilities. Platform-specific features may remain explicit extensions when a truthful common contract is impossible.

## Active domain analyses

- [Runtime and time vertical slice](runtime-time/README.md) — Draft
- [Filesystem foundations vertical slice](filesystem/README.md) — Draft
- [Security and authority foundations vertical slice](security/README.md) — Draft
- [Cryptographic operations and key-management foundations](security/crypto-README.md) — Draft
- [Certificate, trust-store, and PKI-validation foundations](security/pki-README.md) — Draft
- [Certificate issuance, enrollment, and CA-lifecycle foundations](security/pki-issuance-README.md) — Draft
- [Signed-artifact and provenance foundations](signed-artifacts/README.md) — Draft
- [Package installation and update-orchestration foundations](package-management/README.md) — Draft
- [Process foundations vertical slice](process/README.md) — Draft
- [Application activation and association foundations vertical slice](activation/README.md) — Draft
- [IPC foundations vertical slice](ipc/README.md) — Draft
- [Terminal foundations vertical slice](terminal/README.md) — Draft
- [Windowing foundations vertical slice](windowing/README.md) — Draft
- [Graphics and presentation vertical slice](graphics/README.md) — Draft
- [Display and color-management foundations vertical slice](display-color/README.md) — Draft
- [Still-image and image-codec foundations vertical slice](still-image/README.md) — Draft
- [Time-based media foundations vertical slice](time-media/README.md) — Draft
- [Input foundations vertical slice](input/README.md) — Draft
- [Text, fonts, and layout vertical slice](text/README.md) — Draft
- [Accessibility foundations vertical slice](accessibility/README.md) — Draft
- [Clipboard and drag-and-drop data-transfer vertical slice](data-transfer/README.md) — Draft
- [Internationalization and localization vertical slice](internationalization/README.md) — Draft
- [Configuration and change-notification vertical slice](configuration/README.md) — Draft
- [Observability, diagnostics, and crash-reporting vertical slice](observability/README.md) — Draft
- [Application lifecycle and session-integration vertical slice](lifecycle/README.md) — Draft
- [Networking foundations vertical slice](networking/README.md) — Draft
- [TLS/QUIC secure transport and channel foundations](networking/secure-transport-README.md) — Draft
- [HTTP client and server foundations](networking/http-README.md) — Draft
- [Real-time application transport foundations](networking/realtime-README.md) — Draft
- [Application messaging and RPC foundations](messaging/README.md) — Draft
- [Distributed coordination and consistency foundations](coordination/README.md) — Draft
- [Application data persistence and database foundations](persistence/README.md) — Draft
- [Object, blob, and content-addressed storage foundations](object-storage/README.md) — Draft
- [Caching and content-delivery foundations](caching/README.md) — Draft
- [Search, indexing, and retrieval foundations](search/README.md) — Draft
- [Memory and mapping foundations vertical slice](memory/README.md) — Draft
- [Plugin and module lifecycle vertical slice](plugins/README.md) — Draft
- [Threading and synchronization foundations vertical slice](threading/README.md) — Draft
- [Audio foundations vertical slice](audio/README.md) — Draft
- [Device discovery and hardware-change foundations vertical slice](devices/README.md) — Draft
- [Asynchronous I/O foundations vertical slice](async-io/README.md) — Draft
- [Storage volumes and removable-media foundations vertical slice](storage/README.md) — Draft
- [Camera and media-capture foundations vertical slice](capture/README.md) — Draft
- [Notifications and user-attention foundations vertical slice](notifications/README.md) — Draft
- [Power and energy-management foundations vertical slice](power/README.md) — Draft
- [Credential and identity-session foundations vertical slice](identity-session/README.md) — Draft
- [Printing and document-output foundations vertical slice](printing/README.md) — Draft
- [Screen and window capture foundations vertical slice](screen-capture/README.md) — Draft
- [Remote presentation and controlled input foundations vertical slice](remote-interaction/README.md) — Draft
- [Application services, background execution, and durable scheduling foundations vertical slice](background-services/README.md) — Draft
