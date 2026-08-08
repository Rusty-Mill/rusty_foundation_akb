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
| [0048](0048-audio-stream-time-follows-the-device-sample-clock.md) | Audio stream time follows the device sample clock | Accepted |
| [0049](0049-realtime-audio-callbacks-are-a-restricted-execution-domain.md) | Realtime audio callbacks are a restricted execution domain | Accepted |
| [0050](0050-device-identity-is-generation-scoped-evidence.md) | Device identity is generation-scoped evidence | Accepted |
| [0051](0051-device-notifications-trigger-reconciliation.md) | Device notifications trigger reconciliation | Accepted |
| [0052](0052-portable-asynchronous-io-is-completion-oriented.md) | Portable asynchronous I/O is completion-oriented | Accepted |
| [0053](0053-cancellation-does-not-end-operation-lifetime.md) | Cancellation does not end operation lifetime | Accepted |
| [0054](0054-a-mount-is-a-namespace-relationship-not-volume-identity.md) | A mount is a namespace relationship, not volume identity | Accepted |
| [0055](0055-safe-removal-is-coordination-not-a-durability-guarantee.md) | Safe removal is coordination, not a durability guarantee | Accepted |
| [0056](0056-capture-authority-is-session-scoped-and-revocable.md) | Capture authority is session-scoped and revocable | Accepted |
| [0057](0057-raw-capture-is-not-recording-or-encoding.md) | Raw capture is not recording or encoding | Accepted |
| [0058](0058-notification-submission-is-not-presentation.md) | Notification submission is not presentation | Accepted |
| [0059](0059-notification-actions-are-untrusted-activation.md) | Notification actions are untrusted activation | Accepted |
| [0060](0060-power-observations-are-estimates-not-budgets.md) | Power observations are estimates, not budgets | Accepted |
| [0061](0061-power-assertions-are-scoped-leases-not-guarantees.md) | Power assertions are scoped leases, not guarantees | Accepted |
| [0062](0062-authentication-results-are-scoped-evidence.md) | Authentication results are scoped evidence | Accepted |
| [0063](0063-impersonation-is-a-restricted-operation-boundary.md) | Impersonation is a restricted operation boundary | Accepted |
| [0064](0064-print-plans-bind-destination-generation-and-format.md) | Print plans bind destination generation and document format | Accepted |
| [0065](0065-print-completion-is-boundary-scoped-evidence.md) | Print completion is boundary-scoped evidence | Accepted |
| [0066](0066-color-is-an-immutable-semantic-description.md) | Color is an immutable semantic description | Accepted |
| [0067](0067-display-color-is-compositor-negotiation-not-appearance-proof.md) | Display color is compositor negotiation, not appearance proof | Accepted |
| [0068](0068-image-format-detection-is-evidence-not-trust.md) | Image format detection is evidence, not trust | Accepted |
| [0069](0069-decoded-images-are-bounded-immutable-resources.md) | Decoded images are bounded immutable resources | Accepted |
| [0070](0070-media-time-is-exact-domain-tagged-and-discontinuous.md) | Media time is exact, domain-tagged, and discontinuous | Accepted |
| [0071](0071-media-seek-is-a-negotiated-discontinuity.md) | Media seek is a negotiated discontinuity | Accepted |
| [0072](0072-activation-is-untrusted-intent-not-authority.md) | Activation is untrusted intent, not authority | Accepted |
| [0073](0073-activation-acceptance-is-not-handler-completion.md) | Activation acceptance is not handler completion | Accepted |
| [0074](0074-capture-authority-binds-an-exact-selected-source-generation.md) | Capture authority binds an exact selected source generation | Accepted |
| [0075](0075-capture-frames-are-provider-observations-not-content-proof.md) | Capture frames are provider observations, not content proof | Accepted |
| [0076](0076-remote-control-authority-is-participant-session-and-action-scoped.md) | Remote-control authority is participant-, session-, and action-scoped | Accepted |
| [0077](0077-injected-input-is-a-privileged-attributed-side-effect.md) | Injected input is a privileged attributed side effect | Accepted |
| [0078](0078-durable-schedules-persist-intent-not-execution-guarantees.md) | Durable schedules persist intent, not execution guarantees | Accepted |
| [0079](0079-background-triggers-are-reconciliation-hints-not-work-authority.md) | Background triggers are reconciliation hints, not work authority | Accepted |
| [0080](0080-key-handles-authorize-operations-not-key-material.md) | Key handles authorize operations, not key material | Accepted |
| [0081](0081-cryptographic-policy-precedes-provider-selection.md) | Cryptographic policy precedes provider selection | Accepted |
| [0082](0082-presented-certificates-are-candidates-not-a-chain.md) | Presented certificates are candidates, not a chain | Accepted |
| [0083](0083-trust-results-are-context-bound-evidence-not-identity-or-authority.md) | Trust results are context-bound evidence, not identity or authority | Accepted |
| [0084](0084-signatures-bind-versioned-signed-views-and-declared-intent.md) | Signatures bind versioned signed views and declared intent | Accepted |
| [0085](0085-artifact-acceptance-composes-independent-evidence.md) | Artifact acceptance composes independent evidence | Accepted |
| [0086](0086-deployment-plans-are-immutable-generation-bound-authority.md) | Deployment plans are immutable generation-bound authority | Accepted |
| [0087](0087-rollback-is-a-compensating-deployment-not-an-inverse.md) | Rollback is a compensating deployment, not an inverse | Accepted |
| [0088](0088-published-release-identity-and-bytes-are-immutable.md) | Published release identity and bytes are immutable | Accepted |
| [0089](0089-channel-promotion-moves-an-authenticated-reference-to-the-same-digest.md) | Channel promotion moves an authenticated reference to the same digest | Accepted |
| [0090](0090-certificate-requests-prove-key-possession-not-issuance-authority.md) | Certificate requests prove key possession, not issuance authority | Accepted |
| [0091](0091-renewal-creates-a-new-credential-generation-with-explicit-continuity.md) | Renewal creates a new credential generation with explicit continuity | Accepted |
| [0092](0092-secure-channels-become-ready-only-after-authentication-and-protocol-negotiation.md) | Secure channels become ready only after authentication and protocol negotiation | Accepted |
| [0093](0093-resumption-creates-a-new-channel-and-early-data-is-separate-replay-authority.md) | Resumption creates a new channel and early data is separate replay authority | Accepted |
| [0094](0094-http-semantics-are-stable-while-protocol-mechanics-remain-explicit.md) | HTTP semantics are stable while protocol mechanics remain explicit | Accepted |
| [0095](0095-http-replay-is-an-explicit-domain-authority.md) | HTTP replay is an explicit domain authority | Accepted |
| [0096](0096-real-time-transports-share-session-policy-not-a-data-abstraction.md) | Real-time transports share session policy, not a data abstraction | Accepted |
| [0097](0097-reconnect-creates-a-new-session-and-resume-is-application-evidence.md) | Reconnect creates a new session and resume is application evidence | Accepted |
| [0098](0098-a-remote-call-is-an-asynchronous-interaction-not-a-local-procedure.md) | A remote call is an asynchronous interaction, not a local procedure | Accepted |
| [0099](0099-delivery-acknowledgment-is-not-domain-effect.md) | Delivery acknowledgment is not domain effect | Accepted |
| [0100](0100-exclusive-coordination-requires-resource-enforced-fencing.md) | Exclusive coordination requires resource-enforced fencing | Accepted |
| [0101](0101-consistency-is-a-history-property-not-a-strength-label.md) | Consistency is a history property, not a strength label | Accepted |
| [0102](0102-database-commit-is-boundary-scoped-evidence.md) | Database commit is boundary-scoped evidence | Accepted |
| [0103](0103-schema-migration-is-a-compatibility-rollout.md) | Schema migration is a compatibility rollout | Accepted |
| [0104](0104-content-addresses-bind-exact-bytes-not-provider-object-identity.md) | Content addresses bind exact bytes, not provider object identity | Accepted |
| [0105](0105-multipart-completion-is-a-conditional-object-commit.md) | Multipart completion is a conditional object commit | Accepted |
| [0106](0106-cache-presence-is-not-reuse-authority.md) | Cache presence is not reuse authority | Accepted |
| [0107](0107-invalidation-completion-is-boundary-scoped-evidence.md) | Invalidation completion is boundary-scoped evidence | Accepted |
| [0108](0108-search-visibility-is-a-versioned-projection-milestone.md) | Search visibility is a versioned projection milestone | Accepted |
| [0109](0109-ranking-scores-are-policy-scoped-ordering-evidence.md) | Ranking scores are policy-scoped ordering evidence | Accepted |
| [0110](0110-watermarks-are-progress-assertions-not-completeness-proof.md) | Watermarks are progress assertions, not completeness proof | Accepted |
| [0111](0111-exactly-once-is-scoped-to-named-state-and-effect-boundaries.md) | Exactly-once is scoped to named state and effect boundaries | Accepted |
| [0112](0112-logical-schema-identity-is-distinct-from-wire-encoding.md) | Logical schema identity is distinct from wire encoding | Accepted |
| [0113](0113-canonicalization-is-an-explicit-signed-view-profile.md) | Canonicalization is an explicit signed-view profile | Accepted |
| [0114](0114-health-is-expiring-evidence-not-success-authority.md) | Health is expiring evidence, not success authority | Accepted |
| [0115](0115-routing-binds-a-policy-generation-and-endpoint-snapshot.md) | Routing binds a policy generation and endpoint snapshot | Accepted |
| [0116](0116-policy-decisions-are-evidence-not-effect-authority.md) | Policy decisions are evidence, not effect authority | Accepted |
| [0117](0117-policy-evaluation-binds-immutable-policy-and-input-snapshots.md) | Policy evaluation binds immutable policy and input snapshots | Accepted |

Use the [ADR template](../05-governance/adr-template.md) for new decisions.
