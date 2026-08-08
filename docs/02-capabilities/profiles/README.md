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

[`rm.profile.foundation.windowed-desktop` 0.47.0](foundation-windowed-desktop.md) extends Desktop 1.0.0 with negotiated windowing/graphics/input/text/accessibility, data transfer, i18n/configuration/observability/lifecycle, and conditional networking/service-traffic/security/policy/messaging/coordination/application-persistence/object-storage/caching/search/analytics/interchange/audio/capture/background/deployment/device/document/media capabilities. It retains optional reauthentication/delegation, memory, plugins, and threading foundations. It remains incomplete until product services/endpoints/routes/policies and schemas/formats/queries/database/object-store/cache/search/analytics and broker providers/topologies, canonical/evolution/migration/sync/recovery/retention/freshness/relevance/time/retry/effect/domain policy, UI/document/media, trust/repository/account/push/signaling, translations/importers, plugin interfaces, and other product policy are selected.

[`rm.profile.foundation.server` 1.19.0](foundation-server.md) conditionally selects managed services/schedules, cryptographic/certificate lifecycle, network/application protocols, service discovery/routing/load balancing, typed policy/rules evaluation, messaging/RPC, coordination/consistency, application persistence/databases, object/blob and content-addressed storage, caching/content delivery, search/indexing/retrieval, analytical batch/stream processing, structured interchange/serialization, signed artifacts, and deployment. It preserves exact services/endpoints/routes/policies and IDLs, schemas/formats/canonical profiles/registries, engines/drivers/dialects/providers/topologies/algorithms, logical queries/functions/state machines, object/cache/search/analytics namespaces/keys/partitions/retention/freshness/relevance/time/retry/effects, fault domains, domain transactions/effects, migration/recovery policy, and operational gaps.

## Repository operator extension

[`rm.profile.foundation.repository-operator` 0.15.0](foundation-repository-operator.md) extends Server 1.19.0 with conditional publication, authenticated metadata, channels/mirrors/advisories/emergency/retention, credentials, and optional traffic/policy/protocol/messaging/coordination/database/object-storage/cache/edge/search/analytics/interchange evidence. It leaves service identities/routes/balancers/policies and IDLs/schemas/formats/canonical profiles/queries/functions/brokers/databases/object stores/caches/CDNs/search/analytics engines and relevance/time/retry/effect policy, storage/coordination topology, interchange providers, objectives, legal workflow, and staffing to product RFCs.

## Certificate-authority operator extension

[`rm.profile.foundation.ca-operator` 0.14.0](foundation-ca-operator.md) extends Server 1.19.0 with registration/validation, issuance ledger/policy, key ceremonies, status/transparency, credential/hierarchy lifecycle, and optional traffic/policy/protocol/messaging/coordination/database/object-storage/cache/edge/search/analytics/interchange evidence. It leaves service identities/routes/balancers/policies and mappings/IDLs/schemas/formats/canonical profiles/queries/functions/brokers/databases/object stores/caches/CDNs/search/analytics engines, algorithms/topology, trust/certificate/time/retry/effect policy, providers, legal/audit regime, objectives, and high-risk features explicit.

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
