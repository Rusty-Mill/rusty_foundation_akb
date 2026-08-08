# Specification-led roadmap

Dates are intentionally absent until scope and capacity are known. Progress is controlled by evidence-based exit criteria.

## Phase 0 — Foundation

- Charter, principles, glossary, architecture pyramid, governance, and repository strategy accepted.
- ADR/RFC processes operational.

## Phase 1 — Domain inventory and meta-model

- Decompose the initial taxonomy into capabilities.
- Define graph schema, capability specification format, and seed profiles.
- Record platform research without designing APIs prematurely.

## Phase 2 — Contracts and verification design

- Specify behavioral contracts for a thin vertical slice across all three platforms.
- Define conformance report and benchmark schemas.
- Establish security, compatibility, and quality review gates.

## Phase 3 — Reference vertical slice

- Through an accepted RFC, select a small capability set with meaningful async, sync, resource, and platform variance.
- Only then create implementation and verification workspaces.
- Prove native mapping, conformance portability, performance methodology, packaging, and update assumptions.

## Phase 4 — Core profiles

- Expand verified capabilities toward CLI, server, desktop, and constrained/headless profiles.
- Stabilize only capabilities supported by evidence on Windows, Linux, and macOS.

## Phase 5 — Ecosystem scale-out

- Add domain frameworks, tooling, distribution channels, and additional repositories only when explicit forcing functions appear.
- Operate compatibility, deprecation, supply-chain, and governance processes continuously.

## Immediate next decisions

1. ~~Review RFC-0001 and exercise its templates.~~ Completed: [RFC-0001](../rfc/0001-capability-specification-system.md) is Accepted after the runtime/time trial.
2. Review the [runtime and time vertical slice](../02-capabilities/runtime-time/README.md), including its four candidate specifications and open questions.
3. ~~Decide whether orderly shutdown is a capability or a platform service.~~ Resolved as a platform service by [ADR-0005](../adr/0005-orderly-shutdown-is-a-platform-service.md).
4. Review the runtime/time [conformance specification](../02-capabilities/runtime-time/conformance.md) and [benchmark specification](../02-capabilities/runtime-time/benchmarks.md).
5. Define prototype experiments for timer scale, timing behavior, cancellation races, and shutdown ordering.
6. Choose a machine-readable graph format only after at least two reviewed capability specifications expose the requirements.

## Active second slice

The [filesystem foundations analysis](../02-capabilities/filesystem/README.md) now tests the model against path representation, directory-relative authority, file resources, metadata variance, atomic replacement, resolution quality, durability, conformance, and benchmarks. Its next gates are permissions/ACL inspection, directory enumeration, link semantics, and adversarial platform evidence.

## Active third slice

The [security and authority foundations analysis](../02-capabilities/security/README.md) separates identity, security context, explicit authority, policy advice, and native enforcement. It now covers attenuation, delegation, restricted execution, secure random, secret values, and protected stores with cross-domain review and evidence requirements. Its next gates are credential acquisition/brokering, cryptographic-key operation boundaries, and profile-specific authority manifests.

## Active profile trial

The four [foundation profiles](../02-capabilities/profiles/README.md) now exercise exact contract selection, conditional requirements, interaction policy, explicit workload gaps, deterministic resolution, evidence-bound reports, and profile-major evolution. Version 1.0.0 integrates direct process launch/control plus optional or conditional resolution, IPC, and supervision. They remain foundation—not complete application-platform—profiles.

## Active fourth slice

The [process foundations analysis](../02-capabilities/process/README.md) defines direct launch, native arguments/environment, explicit inheritance, standard-stream binding, child lifecycle/control, executable resolution, containment-aware supervision, shell-free pipelines, and startup milestones. The [IPC foundations analysis](../02-capabilities/ipc/README.md) supplies reusable anonymous byte pipes. Profile integration is at foundation version 1.0.0; next gates are terminal/PTY boundaries and measured process-control/pipe quality evidence.

## Active fifth slice

The [terminal foundations analysis](../02-capabilities/terminal/README.md) now separates and specifies PTY/session, emulator state, structured input/IME, accessibility semantics, renderer adapter, privileged effects, and recording/replay. The [interactive CLI foundation profile](../02-capabilities/profiles/foundation-interactive-cli.md) integrates the lower terminal layer while product completion awaits concrete graphics/text/accessibility adapters and whole-host evidence.

The [windowing foundations analysis](../02-capabilities/windowing/README.md) defines negotiated window lifecycle, atomic revisioned configuration, display topology, typed coordinate spaces, and generation-scoped presentation surfaces. Accepted ADRs reject global-coordinate/DPI assumptions.

The [graphics and presentation analysis](../02-capabilities/graphics/README.md) defines workload-contract device selection, device epochs, memory/resources, explicit submission/synchronization, bounded frame pacing, and presentation over window-owned surface generations.

The [input foundations analysis](../02-capabilities/input/README.md) separates physical/logical keyboard observations from text composition/commit, defines pointer/touch streams, focus/capture routing, event provenance, privacy, loss/reset, conformance, and latency evidence.

The [text, fonts, and layout analysis](../02-capabilities/text/README.md) defines typed revisioned Unicode positions, exact font plans, deterministic shaping and cluster maps, bidi/line layout, caret/hit-test geometry, rasterization, multilingual conformance, and performance evidence.

The [accessibility foundations analysis](../02-capabilities/accessibility/README.md) defines application-owned semantic trees, text ranges, focus/actions/events/live updates, virtualization, user preferences, privacy, native adapter mappings, assistive-technology conformance, and performance evidence.

The [clipboard and drag-and-drop analysis](../02-capabilities/data-transfer/README.md) defines typed lazy offers, bounded materialization, clipboard ownership/persistence, accessible drag negotiation, committed move semantics, file promises, cross-process trust, conformance, and performance evidence.

The [internationalization and localization analysis](../02-capabilities/internationalization/README.md) defines locale preference/context snapshots, resource and typed-message resolution, formatting/parsing, calendar/time-zone ambiguity and versioning, collation/search, pseudolocalization, live changes, conformance, and performance evidence.

The [configuration and change-notification analysis](../02-capabilities/configuration/README.md) defines typed schemas and source plans, provenance-bearing immutable snapshots, validation/reload policy, secret-reference boundaries, native invalidation reconciliation, loss/resynchronization, conformance, and performance evidence.

The [observability, diagnostics, and crash-reporting analysis](../02-capabilities/observability/README.md) defines stable structured schemas, explicit causal/time context, bounded metrics/tracing pipelines, exporter independence, diagnostic bundles, privacy governance, loss accounting, and separated minimal crash capture/symbolication.

The [application lifecycle and session-integration analysis](../02-capabilities/lifecycle/README.md) defines instance epochs, readiness, typed activation, multi-instance policy, session/power observations, cooperative termination, scoped inhibition, restoration metadata, conformance, and performance evidence.

The [networking foundations analysis](../02-capabilities/networking/README.md) defines service identities/endpoints, expiring resolution candidate sets, connection racing, streams, datagrams, listeners, path observation, secure-channel composition, authority, conformance, and performance evidence.

The [memory and mapping foundations analysis](../02-capabilities/memory/README.md) defines virtual address/backing state, file/shared mappings, protection, residency/discard, allocator boundaries, executable-memory authorization, conformance, and performance evidence.

The [plugin and module lifecycle analysis](../02-capabilities/plugins/README.md) defines package identity/provenance, metadata-only discovery, interface compatibility, isolation/authority, activation/quiescence, immutable generation updates, rollback, supply-chain evidence, conformance, and benchmarks.

The [threading and synchronization foundations analysis](../02-capabilities/threading/README.md) defines native thread lifecycle, mutex/rwlock, condition/semaphore/event waits, atomics, scheduling/QoS/affinity, realtime constraints, TLS, conformance, and performance evidence.

The [audio foundations analysis](../02-capabilities/audio/README.md) defines endpoint generations, exact PCM formats/layouts, render/capture streams, clock correlation, routing policy, XRUN recovery, restricted realtime processing, capture authority, conformance, and latency/stability benchmarks.

The [device discovery and hardware-change foundations analysis](../02-capabilities/devices/README.md) defines scoped queries, coherent snapshots, generation-bound identity evidence, typed/provenanced properties and topology, notification-driven reconciliation, privacy, class handoff, conformance, and scale/convergence benchmarks.

The [asynchronous I/O foundations analysis](../02-capabilities/async-io/README.md) defines completion-oriented operations across completion/readiness/blocking providers, exact terminal progress, cancellation lifetime, resource/registration generations, bounded backpressure/fairness, engine/executor separation, observability, conformance, and performance evidence.

The [storage volumes and removable-media foundations analysis](../02-capabilities/storage/README.md) defines device/media/region/filesystem/mount entities, namespace-aware observation, capacity, mount arbitration, staged safe removal, durability limits, security/accessibility, conformance, and performance evidence.

The [camera and media-capture foundations analysis](../02-capabilities/capture/README.md) defines permission-separated camera observation, revocable capture authority, negotiated session generations, exact raw frame/color/orientation layouts, clocks, controls, bounded delivery, privacy/accessibility, conformance, and performance evidence.

The [notifications and user-attention foundations analysis](../02-capabilities/notifications/README.md) defines typed localized content, evidence-scoped submission milestones, user-controlled attention, untrusted action activation, replacement/progress/badges, scheduling, privacy/accessibility, conformance, and performance evidence.

The [power and energy-management foundations analysis](../02-capabilities/power/README.md) defines qualified battery/source/saver/thermal observations, explicit workload adaptation, bounded sleep/display assertion leases, lifecycle reconciliation, energy measurement, privacy/accessibility, conformance, and sustained benchmarks.

The [credential and identity-session foundations analysis](../02-capabilities/identity-session/README.md) separates provider-scoped principals, login-session generations, security-context snapshots, authentication evidence, opaque credential handles, authority, and restricted delegation/impersonation.

The [printing and document-output foundations analysis](../02-capabilities/printing/README.md) defines destination/capability generations, immutable paginated sources, format-bound whole-ticket negotiation, bounded rendering/color, boundary-scoped job evidence, artifact output, privacy/accessibility, conformance, and performance evidence.

The [display and color-management foundations analysis](../02-capabilities/display-color/README.md) defines semantic image descriptions, revisioned display color evidence, generation-scoped compositor negotiation, conversion/gamut/tone mapping, profile/calibration/measurement boundaries, lifecycle, privacy/accessibility, conformance, and performance evidence.

The [still-image and image-codec foundations analysis](../02-capabilities/still-image/README.md) defines bounded evidence-bearing probe/inspection, exact immutable pixel resources, multidimensional decode limits, progressive/region/tile output, animation composition, metadata privacy/provenance, explicit encode/transcode, provider isolation, conformance corpora, and performance evidence.

The [time-based media foundations analysis](../02-capabilities/time-media/README.md) defines bounded source/container/track models, exact timeline domains, generation-scoped codec/raw resources, playback clocks and A/V/text synchronization, negotiated seek/buffer discontinuities, timed text/accessibility, encode/mux/recording, protection boundaries, conformance, and performance evidence.

The [application activation and association foundations analysis](../02-capabilities/activation/README.md) defines typed intents, handler/default association snapshots, brokered file/URI/application/reveal activation, incoming instance routing, explicit file authority and URI safety, packaging registration, boundary-scoped milestones, privacy/accessibility, conformance, and performance evidence.

The [screen and window capture foundations analysis](../02-capabilities/screen-capture/README.md) defines trusted display/window/application/region selection, revocable source-generation authority, exact raw frame/color/geometry/time, explicit cursor and audio streams, observation/protection nonclaims, bounded delivery, privacy/accessibility, conformance, and performance evidence. The [windowed desktop foundation profile](../02-capabilities/profiles/foundation-windowed-desktop.md) version 0.27.0 composes capture conditionally while preserving explicit encode/record/persist/transmit/analyze, camera/microphone, remote-input/control, renderer/UI, editing, adaptive media/licensing, federation, privileged display/system-power, plugin-interface, and product-policy gaps. Next gate is remote presentation and controlled input-injection foundations; a general graphics command model remains deferred until multiple renderer workloads justify it.
