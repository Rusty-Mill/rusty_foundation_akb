# Architecture Decision Records

| ADR | Title | Status |
|---|---|---|
| [0001](0001-capability-first-platform.md) | Capability-first platform model | Accepted |
| [0002](0002-specification-before-implementation.md) | Specification before implementation | Accepted |
| [0003](0003-layered-architecture-pyramid.md) | Layered architecture pyramid | Accepted |
| [0004](0004-authoritative-architecture-model.md) | Authoritative architecture model | Accepted |
| [0005](0005-orderly-shutdown-is-a-platform-service.md) | Orderly shutdown is a platform service | Accepted |
| [0006](0006-paths-are-lossless-native-values.md) | Paths are lossless native values | Accepted |
| [0007](0007-directory-relative-resolution-is-the-security-boundary.md) | Directory-relative resolution is the filesystem security boundary | Accepted |
| [0008](0008-atomic-replacement-is-a-capability.md) | Atomic namespace replacement is a capability | Accepted |
| [0009](0009-identity-is-not-authority.md) | Identity is not authority | Accepted |
| [0010](0010-native-operation-is-the-authorization-point.md) | The native operation is the authorization point | Accepted |
| [0011](0011-restricted-execution-is-a-platform-service.md) | Restricted execution is a platform service | Accepted |
| [0012](0012-secret-protection-is-a-vector.md) | Secret protection is a vector, not a level | Accepted |
| [0013](0013-profiles-select-contracts-not-domains.md) | Profiles select exact contracts, not domains | Accepted |
| [0014](0014-direct-process-launch-is-the-base-contract.md) | Direct process launch is the base contract | Accepted |
| [0015](0015-process-set-supervision-is-a-service.md) | Process-set supervision is a platform service | Accepted |
| [0016](0016-executable-search-uses-explicit-authority.md) | Executable search uses explicit directory authority | Accepted |
| [0017](0017-byte-pipes-are-independent-ipc-capabilities.md) | Byte pipes are independent IPC capabilities | Accepted |
| [0018](0018-pseudoterminals-are-not-byte-pipes.md) | Pseudoterminals are not byte pipes | Accepted |
| [0019](0019-terminal-emulation-is-a-domain-framework.md) | Terminal emulation is a domain framework | Accepted |
| [0020](0020-window-state-is-negotiated.md) | Window state is negotiated and revisioned | Accepted |
| [0021](0021-coordinate-spaces-are-typed.md) | Window coordinate spaces are typed and revision-bound | Accepted |
| [0022](0022-graphics-selection-uses-workload-contracts.md) | Graphics selection uses workload contracts, not API names | Accepted |
| [0023](0023-presentation-is-a-graphics-service.md) | Presentation is a graphics service over a window surface | Accepted |
| [0024](0024-text-input-is-not-keyboard-input.md) | Text input is not keyboard input | Accepted |
| [0025](0025-input-provenance-is-not-authority.md) | Input provenance is not authority | Accepted |
| [0026](0026-semantic-text-is-not-glyph-output.md) | Semantic text is not glyph output | Accepted |
| [0027](0027-font-resolution-precedes-shaping.md) | Font resolution precedes reproducible shaping | Accepted |
| [0028](0028-accessibility-semantics-are-domain-state.md) | Accessibility semantics are domain state, not adapter output | Accepted |
| [0029](0029-accessibility-actions-use-domain-command-path.md) | Accessibility actions use the ordinary domain command path | Accepted |
| [0030](0030-data-transfer-uses-lazy-typed-offers.md) | Data transfer uses immutable lazy typed offers | Accepted |
| [0031](0031-move-is-a-committed-transfer.md) | Move is a committed transfer, not a pointer gesture | Accepted |
| [0032](0032-locale-sensitive-operations-use-explicit-context.md) | Locale-sensitive operations use immutable explicit context | Accepted |
| [0033](0033-localized-output-is-not-canonical-data.md) | Localized output is not canonical data | Accepted |
| [0034](0034-configuration-publishes-validated-snapshots.md) | Configuration publishes validated immutable snapshots | Accepted |
| [0035](0035-configuration-notifications-trigger-reconciliation.md) | Configuration notifications trigger reconciliation | Accepted |
| [0036](0036-observability-producers-are-exporter-independent.md) | Observability producers are exporter independent | Accepted |
| [0037](0037-fatal-capture-is-a-minimal-separated-path.md) | Fatal capture is a minimal separated path | Accepted |
| [0038](0038-lifecycle-events-do-not-guarantee-cleanup.md) | Lifecycle events do not guarantee cleanup opportunity | Accepted |
| [0039](0039-restoration-state-is-disposable-continuity-metadata.md) | Restoration state is disposable continuity metadata | Accepted |
| [0040](0040-resolution-results-are-candidates-not-authority.md) | Resolution results are candidates, not authority or identity | Accepted |
| [0041](0041-secure-channels-compose-over-transports.md) | Secure channels compose over transports | Accepted |
| [0042](0042-address-reservation-is-not-memory-commitment.md) | Address reservation is not memory commitment | Accepted |
| [0043](0043-executable-memory-is-a-separate-authorized-service.md) | Executable memory is a separate authorized service | Accepted |
| [0044](0044-in-process-native-plugins-are-fully-trusted.md) | In-process native plugins are fully trusted components | Accepted |
| [0045](0045-plugin-updates-use-generation-replacement.md) | Plugin updates use immutable generation replacement | Accepted |
| [0046](0046-scheduling-controls-are-scoped-requests.md) | Scheduling controls are scoped requests, not execution guarantees | Accepted |
| [0047](0047-poisoning-is-consistency-policy-not-lock-semantics.md) | Poisoning is consistency policy, not lock semantics | Accepted |

Use the [ADR template](../05-governance/adr-template.md) for new decisions.
