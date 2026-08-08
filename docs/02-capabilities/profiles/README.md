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

The table is only a view. Each manifest defines exact contract ranges, predicates, and quality constraints.

## Interactive CLI extension

[`rm.profile.foundation.interactive-cli` 0.1.0](foundation-interactive-cli.md) extends CLI 1.0.0 with `rm.terminal.pseudoterminal` and the terminal session service. It is a separate identity because terminal hosting is not required by redirected/batch CLI workloads and still has emulator, input, Unicode-layout, rendering, and accessibility gaps.

## Windowed desktop extension

[`rm.profile.foundation.windowed-desktop` 0.34.0](foundation-windowed-desktop.md) extends Desktop 1.0.0 with negotiated top-level windowing, graphics/color-managed presentation, focused input/text composition, exact text infrastructure, semantic accessibility/native adapters, data transfer, explicit localization/formatting, typed snapshot-based configuration, bounded structured observability, application lifecycle/session integration, conditional networking/audio/camera/screen-capture/remote-interaction/background-service/cryptographic/certificate-trust/enrollment/signed-artifact/package-deployment/notifications/power/general device/identity-session/printing/still-image/time-media/activation observation and completion-oriented async I/O/storage-volume workflows, optional scoped reauthentication and delegated credential operations, optional explicit memory/mapping, optional isolated plugins, and explicit native-thread/synchronization foundations. It remains intentionally incomplete until renderer/UI, editing and accessible-document authoring, adaptive streaming/license/application media policy, public-trust/CA and remote-vault policy, repository publication/operations and vulnerability policy, signaling/NAT traversal/unattended-access policy, remote push/application protocols and workflow acknowledgments, account/federation protocols, privileged display/system-power control, translated product resources/semantics/importers, plugin interfaces, and product-specific restoration/audio/capture/remote-control/background-work/crypto/trust/enrollment/signing/deployment/notification/power/device/storage/identity/printing/color/image/media/activation policy are selected.

[`rm.profile.foundation.server` 1.6.0](foundation-server.md) conditionally selects OS-managed service registration/demand activation, durable scheduling, cryptographic policy/key operations, certificate trust/path validation and enrollment/renewal, signed-artifact verification/production, and package deployment/update orchestration when deployment, work-survival, data protection, peer authentication, managed credentials, artifact publication/acceptance, or servicing requirements need them. It preserves explicit CA operation/public-trust policy, application protocol, repository operations, vulnerability/advisory policy, database/queue, distributed coordination, deployment topology, remote vault/HSM protocol, exactly-once domain effect, and operational policy gaps.

## Repository operator extension

[`rm.profile.foundation.repository-operator` 0.2.0](foundation-repository-operator.md) extends Server 1.6.0 with conditional release publication, authenticated repository metadata, channels, mirrors, advisory/disclosure, revocation/emergency, retention/backup, service-credential enrollment/renewal, conformance, and operational evidence. It intentionally leaves network APIs, storage/coordination topology, concrete interchange profiles/providers, service objectives, legal workflow, and staffing to product RFCs.

## Certificate-authority operator extension

[`rm.profile.foundation.ca-operator` 0.1.0](foundation-ca-operator.md) extends Server 1.6.0 with registration/validation, issuance policy and ledger, CA key ceremonies, status/transparency, renewal/revocation, hierarchy rotation, compromise/termination, recovery, conformance, and benchmarks. It leaves protocols, trust model, certificate policies/profiles, providers, topology, legal/audit regime, service objectives, and high-risk server-key/escrow/public-trust features explicit.

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
