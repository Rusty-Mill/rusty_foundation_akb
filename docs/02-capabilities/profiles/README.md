# Foundation profile comparison

**Status:** Draft foundation profiles

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
| Background service registration/activation | — | C | C | O |
| Durable scheduling service | — | C | C | O |
| Cryptographic policy/key-operation service | O | C | C | O |
| Certificate trust/path-validation service | O | C | C | O |
| Certificate enrollment/renewal service | O | C | C | O |
| TLS/QUIC secure-channel service | O | C | C | O |

The table is only a view. Each manifest defines exact contract ranges, predicates, and quality constraints.

## Interactive CLI extension

[`rm.profile.foundation.interactive-cli` 0.1.0](foundation-interactive-cli.md) extends CLI 1.0.0 with `rm.terminal.pseudoterminal` and the terminal session service. It is a separate identity because terminal hosting is not required by redirected/batch CLI workloads and still has emulator, input, Unicode-layout, rendering, and accessibility gaps.

## Windowed desktop extension

[`rm.profile.foundation.windowed-desktop` 0.40.0](foundation-windowed-desktop.md) extends Desktop 1.0.0 with negotiated windowing/graphics/input/text/accessibility, data transfer, i18n/configuration/observability/lifecycle, and conditional networking/security/messaging/coordination/application-persistence/audio/capture/background/deployment/device/document/media capabilities. It retains optional reauthentication/delegation, memory, plugins, and threading foundations. It remains incomplete until product schemas/queries/database and broker providers/topologies, migration/sync/recovery/domain effects, UI/document/media, trust/repository/account/push/signaling, translations/importers, plugin interfaces, and other product policy are selected.

[`rm.profile.foundation.server` 1.12.0](foundation-server.md) conditionally selects managed services/schedules, cryptographic/certificate lifecycle, network/application protocols, messaging/RPC, coordination/consistency, application persistence/databases, signed artifacts, and deployment. It preserves exact IDLs, engines/drivers/dialects/providers/topologies/algorithms, logical schemas/queries/state machines, fault domains, domain transactions/effects, migration/recovery policy, and operational gaps.

## Repository operator extension

[`rm.profile.foundation.repository-operator` 0.8.0](foundation-repository-operator.md) extends Server 1.12.0 with conditional publication, authenticated metadata, channels/mirrors/advisories/emergency/retention, credentials, and optional protocol/messaging/coordination/database evidence. It leaves routes/IDLs/schemas/queries/brokers/databases, storage/coordination topology, interchange providers, objectives, legal workflow, and staffing to product RFCs.

## Certificate-authority operator extension

[`rm.profile.foundation.ca-operator` 0.7.0](foundation-ca-operator.md) extends Server 1.12.0 with registration/validation, issuance ledger/policy, key ceremonies, status/transparency, credential/hierarchy lifecycle, and optional protocol/messaging/coordination/database evidence. It leaves mappings/IDLs/schemas/queries/brokers/databases, algorithms/topology, trust/certificate policy, providers, legal/audit regime, objectives, and high-risk features explicit.

## Version transition

Version 1.0.0 adds direct process launch/control to CLI, Desktop, and Server. This is deliberately a profile-major change from 0.1.0 because it can invalidate a previously satisfied provider set. Byte pipes and executable resolution remain optional. Server supervision is conditional on launching managed workers.

## Explicit gaps

These profiles are incomplete for real applications because terminal, application protocols, rendering/UI, editing, codecs/media graphs, and product-specific accessible semantics/data importers/translations/restoration/audio policy are not yet all specified. The windowed extension supplies window/presentation/input/text/accessibility/transfer/i18n/configuration/observability/lifecycle plus conditional networking/audio infrastructure but not those product layers. Resolution reports must preserve the gaps; the foundation profile name prevents a false completeness claim.

## Shared prohibitions

- Silent plaintext secret-file fallback.
- Hidden async runtime creation by sync paths.
- Silent capability degradation or emulation.
- Security decisions based solely on OS name.
- Ambient current-directory authority for security-sensitive filesystem resolution.
