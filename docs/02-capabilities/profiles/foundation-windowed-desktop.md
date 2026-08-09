# `rm.profile.foundation.windowed-desktop`

| Field | Value |
|---|---|
| Status | Draft |
| Version | 0.58.0 |
| Extends | [`rm.profile.foundation.desktop` 1.0.0](foundation-desktop.md) |
| Purpose | Add native top-level window and graphics-presentation infrastructure without claiming a complete GUI toolkit |

## Required members

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0001:** Requires `rm.windowing.window`, `rm.windowing.display-topology`, and `rm.windowing.presentation-surface` `>=0.1.0,<0.2.0`.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0002:** Requires `rm.graphics.device`, `rm.graphics.resource-memory`, and `rm.graphics.submission` `>=0.1.0,<0.2.0` plus graphics presentation service `>=0.1.0,<0.2.0`.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0003:** Window/graphics resolution is joint: the selected device must prove compatibility with the selected presentation surface, format/color policy, frame-flight bound, loss recovery, and required protection properties.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0004:** Window event delivery and frame acquisition/presentation provide async paths that do not block the UI dispatch context while waiting. Sync calls obey provider affinity and never nest a hidden event loop/runtime.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0005:** The minimum workload requires ordinary composited opaque SDR presentation, explicit scale/color observation, bounded frames in flight, resize/surface recreation, and device-loss reporting. Acceleration is preferred but not silently required; software selection is disclosed.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0006:** Exact placement, HDR, tearing/variable refresh, protected content, graphics compute, external resource sharing, and global coordinates are optional constraints, not implied features.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0007:** Requires `rm.input.keyboard`, `rm.input.pointer`, and `rm.input.touch` `>=0.1.0,<0.2.0` plus text-input service `>=0.1.0,<0.2.0`; touch is conditional on the selected product/device class.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0008:** Input events carry focus/transform revisions and provenance. Background observation, capture/lock/confinement, injection, and stable device identity are prohibited unless separately selected with authority.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0009:** Editable text targets use the text-input service for committed/provisional text and surrounding context. Mapping key events independently to text is prohibited where it can duplicate native text service output.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0010:** Requires `rm.text.font-resolution` and `rm.text.shaping` `>=0.1.0,<0.2.0`, text layout service `>=0.1.0,<0.2.0`, and a compatible glyph-rasterization adapter for user-visible text.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0011:** Text/font resolution binds exact Unicode/CLDR, font artifact/face/variation, shaping/layout, and raster provider evidence. Ambient font substitution inside shaping is prohibited.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0012:** User-facing text supports semantic copy/accessibility mappings, mixed-direction layout, IME caret geometry, scale changes, zoom, high contrast/forced colors, and missing-font disclosure under the selected workload.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0013:** Requires `rm.accessibility.semantic-tree` and `rm.accessibility.user-preferences` `>=0.1.0,<0.2.0` plus platform accessibility adapter service `>=0.1.0,<0.2.0` for every supported desktop platform.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0014:** Semantic snapshots, text ranges, geometry, focus, actions, and events bind exact domain/text/layout/window revisions. Pixels, glyphs, and native adapter state are not the semantic source of truth.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0015:** Every user action and product state is keyboard/assistive-technology reachable with equivalent domain outcome; accessibility requests use ordinary validation/authorization and cannot bypass confirmation or destructive-operation policy.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0016:** Profile evidence includes representative native assistive technologies, user preference changes, virtualization, update storms, adapter restart, text/IME, secure content, and end-to-end action/focus/state convergence—not only automated tree inspection.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0017:** Requires `rm.transfer.data-offer` `>=0.1.0,<0.2.0` plus clipboard and drag-and-drop services `>=0.1.0,<0.2.0`; file/content promises are conditional on products that export or import deferred files.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0018:** Clipboard reads/writes and drag sessions are user-action scoped by default. Background monitoring/history, remote synchronization, privileged data-control, and sensitive-content persistence are prohibited unless explicitly selected with authority and evidence.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0019:** Data enumeration is side-effect free; materialization is async, bounded, cancellable, and validates untrusted representation content. Paths/URLs do not convey ambient authority.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0020:** Copy, paste, drag, operation/target selection, progress, cancellation, and result have keyboard and assistive-technology paths with equivalent domain outcomes. Move follows target-commit/source-cleanup semantics.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0021:** Requires `rm.i18n.locale-preferences` `>=0.1.0,<0.2.0` plus locale-context, resource/typed-message, formatting, calendar/time-zone, and collation services `>=0.1.0,<0.2.0` when the product exposes corresponding localized behavior.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0022:** Locale-sensitive operations use explicit immutable contexts binding user preference, bundle, Unicode/CLDR/tzdb/provider versions, actual service locales, overrides, and fallback trace. Ambient process locale is prohibited.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0023:** Product-visible messages are complete typed translatable units; localized output is not reused as canonical data; civil-time gaps/overlaps and parsing ambiguity require explicit policy.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0024:** Every shipped UI locale passes bundle/schema/plural coverage, pseudolocalization, layout/font/input/accessibility integration, bidi isolation, and live context-change evidence under product policy.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0025:** Requires `rm.config.schema`, `rm.config.source`, and `rm.config.change-observer` `>=0.1.0,<0.2.0` plus configuration resolution service `>=0.1.0,<0.2.0` when the product consumes mutable preferences or administrator policy.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0026:** Configuration uses an explicit versioned schema and source plan. Consumers receive immutable validated snapshots with value provenance; ambient registry, preferences, environment, or file reads after construction are prohibited.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0027:** Native change notifications trigger bounded re-read and reconciliation. Snapshot replacement is atomic; invalid, restart-required, coordinated, overflowed, and unavailable states are reported without partial live mutation.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0028:** Secret material is prohibited in ordinary configuration values and diagnostics. Secret references resolve through the selected secret-store capability under separate authority, and product evidence covers external writers, replacement, loss/resynchronization, policy locks, and accessible restart/error communication.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0029:** Requires `rm.observe.event` and `rm.observe.context` `>=0.1.0,<0.2.0` plus telemetry pipeline service `>=0.1.0,<0.2.0`. Metrics, tracing, diagnostic bundles, and `rm.diagnostics.crash-capture` are conditional on declared product operational requirements.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0030:** Instrumentation uses stable typed schemas, explicit correlation, clock-domain/quality evidence, bounded cardinality and queues, aggregate loss accounting, and exporter-independent producer paths. Export failure cannot indefinitely block the UI or ordinary product work.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0031:** Product-visible diagnostic collection, dynamic tracing, bundle export, and crash upload follow explicit authority, privacy classification, retention, consent, and accessible disclosure policy. Secrets, secure text, and unrestricted user content are prohibited from ordinary telemetry.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0032:** Crash evidence uses a platform-proven minimal fatal path with bounded recursion and out-of-process symbolication/redaction. Profile evidence covers handler coexistence, missing/corrupt symbols, dump restrictions, abrupt termination, exporter outage, queue saturation, and bounded shutdown flush.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0033:** Requires `rm.lifecycle.instance`, `rm.lifecycle.activation`, `rm.lifecycle.session-observer`, and `rm.lifecycle.power-observer` `>=0.1.0,<0.2.0` plus application lifecycle and restoration services `>=0.1.0,<0.2.0`; termination inhibition is optional and separately authorized.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0034:** Launch, readiness, activation, application activity, window focus, session state, and power state remain distinct revisioned observations. Activation payloads are untrusted and do not imply authority, focus, foregrounding, or successful completion.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0035:** Cooperative termination may invoke orderly shutdown within the observed deadline, but product correctness assumes callbacks may be absent. Durable domain data is committed continuously; restoration archives are disposable versioned continuity metadata.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0036:** Lifecycle evidence covers concurrent/running-instance activation, duplicate delivery, lock/disconnect, suspend/resume reconciliation, allowed/cancelled/deferred/forced termination, missing callbacks, inhibition expiry, corrupt/stale restoration, changed displays/locales/accessibility settings, and accessible localized recovery.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0037:** Networking is conditional on product workload. When selected, `rm.network.resolve`, `rm.network.byte-stream`, and `rm.network.connectivity-observer` `>=0.1.0,<0.2.0` plus connection-establishment service `>=0.1.0,<0.2.0` are required; datagram, listener, and secure-channel services are selected independently by need.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0038:** Network operations receive explicit service intent and authority. Resolution candidates, IP endpoints, path viability, transport establishment, cryptographic security, peer authentication, and application readiness remain distinguishable and evidence bound.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0039:** Internet-facing or otherwise untrusted remote communication requires an application-appropriate secure-channel/protocol contract. Peer validation binds the original service identity; insecure fallback, early data, trust override, proxy bypass, and unrestricted wildcard listening are prohibited unless explicitly selected and evidenced.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0040:** Networking evidence covers IPv4/IPv6/DNS64, candidate racing and loser cleanup, constrained/expensive/unknown paths, proxy/VPN/network changes, partial I/O/backpressure/cancellation, suspend/resume reconciliation, certificate/name/revocation-quality failures, exporter-safe diagnostics, and accessible localized connectivity/retry states.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0041:** `rm.memory.virtual-region` is optional infrastructure selected only for workloads requiring explicit virtual-memory control. File mappings, shared regions, residency/locking, large pages, and allocator services are independent optional members; executable-memory service is prohibited unless explicitly selected by a specialized profile extension.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0042:** Memory requirements distinguish reserved address space, backing/commit, accessibility, residency, locking, shared/private dirty state, and durability. A mapping cannot be exposed as a typed safe view until bounds, alignment, initialization, representation, aliasing, mutability, and concurrency invariants are proven.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0043:** Shared-memory transfer attenuates access and uses versioned offset-based layouts with separately proven synchronization. Native pointers, Rust references, secrets-by-default, implicit inheritance, and named global discovery are prohibited.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0044:** Memory evidence covers overflow/alignment, guard/protection faults in subprocesses, file truncate/replace, flush-stage nonclaims, shared lifetime/transfer, pressure/discard, lock/no-dump limitations, OOM categories, suspend/crash diagnostics, and any executable-memory entitlement/W^X claim.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0045:** Plugin support is optional. When selected, `rm.plugin.catalog` plus plugin resolution/lifecycle/update services `>=0.1.0,<0.2.0` are required with an explicit allowed isolation-class set; arbitrary ambient native-library loading is prohibited.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0046:** In-process native plugins are restricted to fully trusted host-compatible packages under exact ABI/build/loader/signing policy. Third-party or independently recoverable plugins use restricted process or pinned portable-component isolation with attenuated capability grants and quotas.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0047:** Discovery never executes plugin code. Selection binds package digest/provenance, interface versions, platform/runtime, isolation, authority, resource budgets, and conformance evidence; duplicate identity/version with different content is rejected.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0048:** Updates install immutable generations, activate only after readiness, atomically switch routing, quiesce old work, and preserve rollback/state-migration distinctions. Evidence covers malicious packages, ABI/protocol faults, crash/restart, resource exhaustion, revocation, key rotation, safe search paths, weakened platform protection, and accessible localized plugin/recovery UI.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0049:** Requires `rm.thread.spawn` plus mutex, condition/wait, and supported Rust-atomic contracts `>=0.1.0,<0.2.0` for components that own native threads; reader/writer locks, semaphores/events, affinity/QoS, realtime, and native TLS are optional exact requirements.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0050:** UI dispatch affinity, runtime tasks, worker native threads, apartment/run-loop constraints, and blocking waits remain distinct. Generic waits never silently pump UI messages, execute callbacks, or occupy async workers without disclosed policy.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0051:** Scheduling/QoS/affinity are scoped requests with effective-state evidence, not deadline or isolation guarantees. Realtime scheduling and hard affinity are prohibited unless a specialized profile supplies privilege, bounded-code, inversion, memory, watchdog, and interference evidence.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0052:** Conformance covers happens-before, spurious/obsolete wakeups, cancellation/timeouts, panic/owner failure, starvation/fairness nonclaims, atomic ordering/widths, topology invalidation, TLS destruction variance, UI/apartment deadlocks, plugin retirement, and shutdown.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0053:** Audio is conditional on product workload. When selected, `rm.audio.device-observer` and either `rm.audio.render-stream` or `rm.audio.capture-stream` `>=0.1.0,<0.2.0` are required with exact format/layout, endpoint generation, clock, period/buffer, route, and discontinuity evidence.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0054:** Capture, loopback capture, exclusive/direct access, route override, and background monitoring are separately selected and authorized. Device enumeration does not activate capture or imply consent; sensitive buffers, diagnostics, retention, and delegation follow explicit privacy policy.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0055:** Realtime audio callbacks use a preallocated bounded data plane and MUST NOT allocate, block, perform I/O, acquire ordinary contended locks, schedule through a general executor, call UI APIs, or synchronously log. Product evidence measures deadline misses, XRUNs, callback distributions, page faults, scheduling state, and representative interference.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0056:** Product route/device controls are keyboard and assistive-technology operable, expose effective state and failures non-auditorily, and observe applicable mono, balance, hearing-device, and loudness preferences. Codecs, media containers, MIDI, speech, and spatial scene behavior require separate contracts.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0057:** `rm.device.observer` `>=0.1.0,<0.2.0` is conditional on products that expose general device selection, diagnostics, or cross-class hardware-change behavior. Class-specific endpoint observation remains sufficient when no general device model is required.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0058:** Device references are provider/scope/generation bound and convey no authority. Saved-device matching exposes evidence, confidence, ambiguity, and confirmation policy; it never silently substitutes a similar or default device where security, privacy, or data integrity could change.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0059:** Device changes publish coherent snapshot revisions after bounded reconciliation. Notification loss, overflow, source restart, suspend/resume, or incomplete enumeration forces a full rescan; native callback payloads are not treated as a complete journal.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0060:** General enumeration does not open protocols, mount media, request capture consent, or wake hardware solely for optional metadata. Sensitive identifiers/topology are explicitly projected and redacted from ordinary telemetry; class handoff revalidates generation and authority at open.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0061:** `rm.io.operation` `>=0.1.0,<0.2.0` infrastructure is required when selected filesystem, network, IPC, device, or audio contracts promise native asynchronous progress. Domain contracts remain authoritative for EOF, message boundaries, partial progress, ordering, and cancellation safety.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0062:** Portable async operations are completion-oriented. Readiness providers translate stale/duplicate/coalesced hints through bounded retries; blocking fallback is disclosed with thread, saturation, cancellation, shutdown, and quality evidence.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0063:** Cancellation and timeout race with ordinary completion. Buffers, control blocks, registrations, and resource generations remain valid until exactly one terminal result; dropped futures follow declared cancel-or-detach supervision and cannot orphan untracked work.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0064:** The I/O engine and executor are separately selected. No hidden runtime, nested UI loop, indefinite executor-worker blocking, or unbounded operation/completion/wake queue is permitted; evidence covers readiness/completion races, generation reuse, saturation, fairness, shutdown drain, and timing boundaries.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0065:** `rm.storage.volume-observer` and mount observer `>=0.1.0,<0.2.0` are conditional on products that expose volume selection, capacity, mount state, or removable-media workflows. Device, media, region, filesystem, mount, namespace, and path identities remain distinct.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0066:** Mount/unmount and removable-media coordination are optional privileged services with explicit target generation, namespace, interaction, force, and degradation policy. Observation never mounts, unlocks, repairs, executes content, or wakes media solely for optional metadata.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0067:** Safe removal reports quiesce, durability, unmount, eject/removal-request, veto, and current-observation milestones. It cannot prevent surprise removal or strengthen filesystem/device/bridge durability; force requires explicit authority and accessible data-loss acknowledgment.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0068:** Storage evidence covers namespaces/multiple mounts, duplicate/ambiguous identifiers, locked/read-only/network/virtual media, hostile metadata, capacity boundaries, permission/policy denial, busy/veto, dirty data, surprise unplug, stale-generation rejection, privacy redaction, and keyboard/assistive-technology operation.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0069:** Camera capture is conditional on product workload. When selected, `rm.capture.device-observer` and raw-frame stream `>=0.1.0,<0.2.0` are required with explicit revocable capture authority, device/session generation, exact format/color/orientation, frame timing, controls, and bounded buffer policy.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0070:** Device observation never prompts or activates capture. Permission requests are explicit accessible foreground interactions; session start revalidates native authority, privacy switch/shutter, and device generation. Revocation, interruption, competing use, and indicator inconsistency suspend or invalidate capture.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0071:** Raw frames expose self-describing planes, memory domain/lifetime, sequence/discontinuity, timestamp boundary/clock/quality, control revision, and metadata provenance. Slow consumers follow an explicit bounded drop/block/copy/degrade policy; native callbacks cannot execute arbitrary product, UI, encoding, I/O, or exporter work.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0072:** Preview, still-photo processing, encoded samples, codecs, containers, recording, transport, and storage/photo-library output are separately selected. Evidence covers permission states, hostile/malformed frames, color/orientation, timestamp drift, held buffers, drops, reconfiguration, device/privacy loss, virtual provenance, telemetry redaction, and keyboard/assistive-technology operation.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0073:** Native notification submission is conditional on product workload. When selected, `rm.notify.submit` `>=0.1.0,<0.2.0` requires typed localized content, relevance/expiry, attention intent, privacy class, replacement identity, bounded assets/actions, and provider capability/degradation evidence.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0074:** Submission acceptance is not presentation, announcement, retention, delivery, or response. User/system notification settings, focus/quiet hours, lock/shared-screen privacy, accessibility, foreground/session, rate, and power policy remain authoritative; ordinary notifications cannot emulate critical alarms/calls.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0075:** Notification taps, actions, and text input enter as untrusted lifecycle activation. Action/content revision, freshness, schema, replay/idempotency, state, authority, and confirmation are revalidated before the ordinary domain command; system UI does not pre-authorize destructive or sensitive work.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0076:** Replacement, progress, badge, withdrawal, history, and scheduling are independently selected qualities. Evidence covers truncation/localization/bidi, unsupported features, policy denial, unknown outcomes, duplicate/late activation, stale updates, service/process/reboot/clock changes, sensitive-content redaction, and keyboard/assistive-technology interaction.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0077:** `rm.power.observer` `>=0.1.0,<0.2.0` is conditional on products that adapt behavior or expose battery/power state. Snapshots preserve source, multiple-device aggregation, units, validity/age/uncertainty, saver, warning, thermal, and unknown state; estimates are not budgets or deadlines.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0078:** Workload adaptation explicitly defines deferrability, latency/quality floors, rate/concurrency/batching changes, hysteresis, checkpoint/cancellation, and recovery. Energy or thermal policy cannot weaken security, integrity, durability, accessibility, or required user feedback.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0079:** Sleep/display assertion support is optional and uses narrow attributed purpose-bound leases with maximum duration, effective state, renewal validation, automatic owner release, and denial/override/expiry handling. Correctness tolerates suspend, shutdown, lid close, critical battery, and failure despite a granted lease.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0080:** Evidence covers desktops/multi-battery/docks/UPS, source and saver transitions, volatile estimates, thermal throttling, lease leak/override, suspend/resume resource reconciliation, sustained energy/performance measurement, privacy minimization, and accessible localized degradation/blocker UX.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0081:** Local principal and session observation is conditional on products that display account/session state or react to lock, switch, remote disconnect, or logoff. When selected, provider/realm, subject and session generations, evidence stability/freshness, interaction state, context-vector dimensions, unknowns, and reconciliation are explicit; names and identifiers grant no authority.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0082:** Reauthentication is conditional on sensitive product operations. When selected, `rm.identity.authenticate` `>=0.1.0,<0.2.0` binds purpose, audience, principal/realm, freshness, method/assurance, interaction, foreground/session, cancellation, and deadline. Its result contains no reusable secret and does not authorize the operation.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0083:** Credential use, export, impersonation, and delegation are separately selected privileged features. Credentials remain opaque and purpose-bound; delegated execution is attenuated and bounded; native impersonation is fully restored before completion and never crosses `await`, plugins, callbacks, or pooled-thread reuse.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0084:** Evidence covers realm/name collision and reuse, group/privilege/label change, lock/switch/remote/headless sessions, cached/fresh/cancelled/denied authentication, prompt spoof/rate resistance, credential expiry/revocation/extraction denial, stale-generation rejection, policy races, context-leak fault injection, privacy redaction, localization/bidi, and keyboard/screen-reader operation.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0085:** Printing is conditional on product workload. When selected, `rm.print.destination-observer`, document source, ticket resolver, and submit service `>=0.1.0,<0.2.0` distinguish queue/device/destination generations, format-sensitive capability snapshots, immutable pages, whole-ticket constraints, and explicit submission authority.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0086:** Resolved plans bind exact document representation and destination generation and report every default, substitution, conflict, unsupported value, and deferred decision. Stale plans are renegotiated; required media, duplex, color, quality, finishings, privacy/release, or fidelity constraints never degrade silently.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0087:** Rendering is bounded and declares geometry, pagination/imposition owner, font/resource embedding, vector/raster/transparency fallback, and color conversion evidence. Render, transfer, spool/destination acceptance, job processing/completion, physical output, collection, and artifact durability remain separate milestones; retry exposes duplicate risk.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0088:** Evidence covers local/network/virtual/offline destinations, hostile documents/tickets/device data, capability and service changes, mixed pages/ranges/copies/duplex/color, slow spool backpressure, hold/cancel/restart/ambiguous submission, artifact atomicity/durability, spool privacy, accessible localized UI/status/recovery, and accessible-output nonclaims.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0089:** Color-managed presentation is conditional on product fidelity/HDR/WCG workload. When selected, immutable image descriptions, display color observation, transform planning, and surface negotiation `>=0.1.0,<0.2.0` bind exact component encoding, colorimetry/luminance/metadata, rendering intent, destination/surface/compositor generation, and unknowns.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0090:** `HDR`, gamut, precision, headroom, peak/reference white, profile, automatic management, calibration, and observed appearance remain independent claims. ICC is one validated representation; untagged data stays unknown unless product policy explicitly assigns semantics with provenance.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0091:** Display migration and mode/profile/reference-white/headroom/compositor changes trigger coherent re-observation, renegotiation, cache retirement, and redraw. SDR/precision/gamut/metadata/software fallbacks are explicit; presentation acceptance never claims calibrated physical appearance.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0092:** Evidence covers named/parametric/ICC descriptions, SDR/PQ/HLG/linear and RGB/YUV/range vectors, heterogeneous/remote/virtual displays, CPU/GPU numerical transforms, tone/gamut mapping, hostile profiles/metadata, change storms, privacy minimization, user color/contrast filters, semantic alternatives, and bounded luminance/flash transitions.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0093:** Still-image support is conditional on product workload. When selected, `rm.image.probe`, container inspection, and decode `>=0.1.0,<0.2.0` preserve conflicting format evidence/provider provenance, item/frame/container structure, multidimensional resource budgets, and immutable exact pixel/color/alpha/orientation/memory semantics.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0094:** Progressive, region/tile, animation composition, metadata projection, encode, and transcode are independently selected qualities. Provisional revisions replace rather than mutate; animation timing/blend/disposal and reduced-motion policy are explicit; sensitive/unknown metadata is not preserved or disclosed by default.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0095:** Native/third-party/hardware codec selection binds exact operation/format/profile subset, isolation, provenance, limits, output semantics, conversions, cancellation, and fallback. Installed codec presence, extension/MIME/magic, successful probe, or hardware decode never establishes trust or fidelity.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0096:** Evidence covers valid/malformed/truncated/fuzz/bomb corpora, overflow and frame/reference storms, exact color/alpha/range/orientation, progressive final equivalence, region cost, animation timing/disposal, metadata privacy/conflicts, encode settings/determinism/finalization, provider crashes, bounded concurrency, accessible alternatives/status, reduced motion, and flash safety.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0097:** Time-based media is conditional on product workload. When selected, source/container/track inspection, demux, codec sessions, playback, and seek/buffer services `>=0.1.0,<0.2.0` preserve exact domain-tagged timestamps/generations, typed tracks/configurations, bounded queues/resources, explicit clock/sink selection, and provider provenance/isolation.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0098:** Container/media/DTS/PTS/running/device/wall time, decode/presentation/arrival order, duration/end/live edge, and sink milestones remain distinct. Seek creates a new discontinuity generation with target/tolerance/accuracy, attainable start, flush/preroll/trim, actual result, presentation-ready evidence, and stale-output rejection.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0099:** A/V/text synchronization declares time source, mappings, skew tolerances, buffer/latency policy, video drop/repeat, audio stretch/resample, cue adjustment, rate, track/config changes, and correction evidence. Hardware/software/protected paths, encode/mux/recording, adaptive streaming, and license acquisition are separately selected.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0100:** Evidence covers hostile/malformed container/codec/text corpora, timestamp/edit/index/reorder/discontinuity cases, exact raw video/audio output, drain/flush/reset/provider loss, startup/rebuffer/live/seek, long-run clock drift and A/V sync, captions/audio description/accessible controls, metadata/history privacy, protected-path nonclaims, encode/mux finalization, and bounded sustained resources.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0101:** Application activation is conditional on products that open external files/URIs/apps or register handlers. When selected, handler/association observation and brokered activation `>=0.1.0,<0.2.0` use typed immutable intents, exact role/verb, current user/system policy, explicit file/object authority or untrusted URI, foreground/interaction context, and provider-scoped milestones.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0102:** Handler registration is eligibility, not default consent; registered/eligible/recommended/default/enforced states remain distinct and revisioned. Setting defaults uses supported accessible OS settings/chooser flows. Activation never silently invokes a shell, executable search, interpreter, installer, elevation, or direct spawn.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0103:** Incoming file/URI/reopen/notification/share/custom activation is untrusted, at-least-once lifecycle input. It revalidates schema, freshness, target generation, content/scheme policy, authority, replay/idempotency, state, and domain preconditions; startup/instance routing, readiness, foreground, open, and handled milestones remain separate.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0104:** Evidence covers layered/default association changes, install/update/uninstall, file handle/path/token/bookmark and access scope, dangerous/cloud/network/quarantine targets, hostile URI grammars/custom/web links, chooser/default/exact modes, sandbox/foreground/headless, duplicate/concurrent/new/existing instances, cancellation/unknown/retry, privacy redaction, and accessible localized chooser/status/focus/recovery.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0105:** Screen/window capture is conditional on product workload. When selected, trusted source selection and raw capture session `>=0.1.0,<0.2.0` bind a revocable purpose/application/source-generation grant to an exact display, window, application group, region, or virtual display; enumeration, labels, handles, coordinates, and restore hints are not authority.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0106:** Captured frames preserve exact plane/memory/color/alpha/content-geometry, timestamp clock/boundary/quality, sequence/discontinuity, damage, source/configuration generations, and provider transformations. They do not prove what the user saw, semantic completeness, physical appearance, secure redaction, or confidentiality.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0107:** Cursor and system/application audio are independently negotiated and authorized; microphone, camera, preview, encode, record, persist, transmit, analyze, and remote-input features remain separate. Delivery and held buffers are bounded, and source/topology/resize/color/policy/device changes visibly reconcile or invalidate rather than silently retarget.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0108:** Evidence covers trusted picker cancel/deny/restrict/revoke, indicators, source identity reuse, display/window/application/region boundaries, decorations/popups/occlusion/minimize/overlays, mixed-scale/HDR/remote/virtual displays, cursor/audio timing, protected/secure/excluded content nonclaims, slow consumers, lifecycle races, telemetry redaction, and localized keyboard/screen-reader selection and stop/change controls.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0109:** Remote presentation/control is conditional on product workload. When selected, session coordination and controlled input `>=0.1.0,<0.2.0` bind local login/security context, exact capture-source generation, authenticated participant/channel evidence, purpose, role, device/action allowlist, visibility, lifetime, and revocation. View, control, clipboard, file transfer, elevation, and unattended access remain independent.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0110:** Remote events are untrusted intent revalidated at admission and injection against participant/device/session/mapping generations, order, age, rate, focus/boundary, and local override. Native acceptance is not delivery, focus, handling, or domain success; internal attribution is retained even when target applications cannot observe origin.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0111:** Coordinate/crop/scale/rotation, keymap/layout/IME, key/button/contact state, batching/order, and reconnect are explicit. Stale events retire on incompatible changes; revocation closes admission before bounded release/cancel and reports residual ambiguity. Secure input/desktop, lock/login, permission/elevation/credential UI, and emergency stop cannot be controlled remotely.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0112:** Evidence covers view/control transitions, participant/channel replacement, multi-controller arbitration, transport loss/reorder/replay, local-input/focus races, mixed-scale/resize mapping, keyboard/layout/IME, touch/pen state, integrity/sandbox/compositor restrictions, lock/switch/secure/elevated boundaries, accessible consent/indication/emergency stop, state cleanup, and input-to-remotely-presented-response latency.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0113:** Application services and durable schedules are conditional on product workload. When selected, registration, demand activation, and scheduler service `>=0.1.0,<0.2.0` bind immutable package/definition generation, user/system/session scope, principal/security context, structured launch, trigger/schedule policy, budgets, attempts, checkpoints, updates, and removal.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0114:** Installed, registered, enabled, trigger-armed, launch-requested, running, ready, work-claimed, checkpointed, completed, broker-acknowledged, and removed are distinct. Demand endpoints bind service/interface identity and generation; background contexts cannot prompt, steal focus, present arbitrary UI, or inherit an ambient desktop/profile/environment.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0115:** Durable schedules persist intent with time domain, civil-zone/rule and ambiguity policy, earliest/deadline window, flexibility, missed/overlap/retry policy, and authority—not exact execution. Trigger payloads are untrusted at-least-once reconciliation hints; domain effects use explicit durable claims, idempotency, and effect-ambiguity recovery.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0116:** Evidence covers demand/persistent/session/task workloads, register/update/rollback/remove transactions, multiple users/sessions, restricted principals, trigger duplicate/loss/storms, DST/clock/time-zone changes, sleep/reboot/downtime, quotas/dependencies, overlaps/checkpoints/crashes, accessible background controls/status, secret redaction, and activation/schedule/recovery benchmarks.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0117:** Cryptographic operations/key management are conditional on product workload. When selected, policy resolution and opaque key-operation service `>=0.1.0,<0.2.0` bind purpose, exact suite/parameters/encoding, strength/horizon, provider/protection/certification constraints, key generation/origin/usage/export/lifetime, principal, authority, and policy/provider generations before use.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0118:** Hash, MAC, KDF/password derivation, AEAD, signature/verification, agreement/KEM, wrapping, import/export, attestation, rotation, revocation, and destruction are separately selected. Private/symmetric keys are non-exportable opaque operation capabilities by default; hardware/provider fallback cannot broaden export or weaken policy.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0119:** Exact nonce/salt/context/AAD/domain/encoding, authenticated-plaintext release, signature mode/canonicality, peer-key validation/KDF, bounded transfer parsing, buffer/copy/zeroization exposure, async/cancellation, interaction, and error-oracle policy are evidence-bearing. Provider defaults and blanket hardware/FIPS/constant-time/destruction claims are prohibited.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0120:** Evidence covers published and adversarial vectors, malformed/noncanonical inputs, invalid tags/signatures/keys/points, nonce concurrency/crash/snapshot, key usage/export/rotation/destruction, provider/hardware/remote loss and rate limits, prompting/session/lock, policy/algorithm transition, certification/attestation boundaries, secret-copy/timing review, and lifecycle/throughput benchmarks.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0121:** Certificate trust is conditional on product protocol/signing workload. When selected, certificate parse, trust observation, path construction/validation, identity matching, and status service `>=0.1.0,<0.2.0` bind exact input bytes, purpose/profile, typed reference identity, verification time/clock, trust/algorithm-policy generations, revocation/network/cache mode, provider, and bounds.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0122:** Peer-provided intermediates are an unordered untrusted candidate bag; bounded construction proves relationships and may yield multiple paths. Anchors/intermediates/trusted leaves/distrust/purpose constraints and system/enterprise/user/application sources retain provenance and precedence. Store membership, self-signing, subject/issuer text, and presentation order do not establish trust.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0123:** Trust results preserve selected path/anchor, per-certificate checks, exact identity match, status source/freshness, network/cache, overrides/pins, warnings/unknowns, expiry/dependencies, and nonclaims. Signature/path/name validity does not prove possession, account identity, authorization, issuance legitimacy, or semantic content validity.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0124:** Evidence covers adversarial DER, critical extensions, alternate/cross-signed paths, loops/ambiguity/resource bounds, basic/name/policy/KU/EKU/algorithm constraints, DNS/IP/URI/email/application identities and IDN/wildcards, CRL/OCSP/stapled/unknown/stale status, offline/proxy/redirect/SSRF/cache, trust updates/overrides/pins, privacy redaction, and staged path/status benchmarks.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0125:** Signed-artifact verification is conditional on accepting code, packages, documents, plugins, configuration, or release artifacts. It binds exact signed views and identity/intent to independently evaluated signer trust/role, timestamp, transparency, provenance/SBOM/reproducibility, platform assessment, target/channel/version, freshness, and product policy.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0126:** Interactive signing is separately conditional, authority-bearing, accessible, and auditable. Verification status distinguishes cryptographic validity from trusted signer role, trusted time, transparency, provenance, platform assessment, safety nonclaims, and action authorization; the verified bytes exactly match any later load/install/display subject.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0127:** Evidence covers native/portable signed views, code/package/document mutation and ambiguity, hostile envelopes/provenance, signer/time/log/policy lifecycle, offline/cache/emergency behavior, TOCTOU, accessible localized ceremony/status, resource bounds, and staged benchmarks.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0128:** Package deployment/update orchestration is conditional for installed or self-updating products. It binds coherent authenticated repository and installed-state generations, exact artifacts, native version/dependency semantics, immutable authority-bound plans, user/machine scope, hooks/services/configuration/data, in-use policy, restart/reboot, rollout health, and recovery.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0129:** Interactive approval exposes the complete material plan and separately communicates publisher/version/channel, downgrade/removal, privileges, service interruption, data/configuration effects, restart/reboot, progress/cancellation boundary, failure, rollback, and residual state accessibly. Installation commit is not readiness, health, or user success.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0130:** Evidence covers repository attacks, resolver conflicts, stale plans, native partial/in-use states, filesystem/archive attacks, hooks/services/config/data, crash/power/disk/reboot recovery, deterministic rollout cohorts and missing health, compensating rollback, repair/removal, privacy/accessibility, and benchmarks.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0131:** Certificate enrollment/renewal is conditional for user, device, application, client-authentication, signing, or service identities. It binds operation kind, exact opaque key/protection, request/POP/attestation, subject/identifier authority, issuer/profile/policy, protocol/account/server trust, target store/scope/principal, interaction, activation, renewal/rekey/replacement, and revocation.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0132:** Interactive flows accessibly expose requester/subject, issuer, purpose/identifiers, key protection/export/archival, validity, target store/scope, requested-versus-issued changes, public disclosure, pending/retry, user-presence, activation, expiry risk, and nonclaims. A certificate does not itself confer application authorization.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0133:** Evidence covers native user/machine stores and managed enrollment, malicious requests/protocols, authority/POP/attestation, provider interaction/lock/loss, response/public-key mismatch, installation/activation, same-key/rekey/replace, clock/sleep/offline, mass renewal/revocation, privacy/accessibility, and benchmarks.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0134:** Secure transport/channel service `>=0.2.0,<0.3.0` is conditional for networked products requiring TLS or QUIC. Policy binds original service identity, versions/suites/groups/signatures, credentials/trust/name, client authentication, ALPN, SNI/ECH/privacy, resumption/early data, exporters, limits, provider, and closure.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0135:** Application-ready follows handshake/confirmation, required authentication, original identity, compatible ALPN, and authenticated QUIC parameters. Resumption is a new channel; tickets are secret scoped credentials; early data is separately replay-authorized and never automatically retransmitted.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0136:** Evidence covers hostile handshakes, identity/client-credential interaction, downgrade/privacy, resumption/early-data replay, exporters/binding, partial I/O/key updates/truncation/close, suspend/network change, QUIC streams/datagrams/migration/loss, accessible diagnostics/overrides, provider variance, and benchmarks.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0137:** HTTP client/server service `>=0.1.0,<0.2.0` is conditional for HTTP products. It binds typed messages and original origin, HTTP/1.1-/2-/3 policy, secure/proxy route, privacy/credential pool partition, streaming/decompression bounds, redirects/challenges/replay, cache, deadlines, background/session policy, and observability.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0138:** Redirect, credential disclosure, retry, early-data fallback, hedging, download/upload, cache, and protocol fallback decisions preserve user and domain intent. Interactive decisions expose origin/destination, consequence, progress, cancellation/failure quality, and recovery accessibly and locally; no UI approval becomes domain authority beyond its declared scope.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0139:** Evidence covers shared semantics, hostile HTTP/1.1 framing, HTTP/2/3 state/flow/compression, connection coalescing, streaming/cancellation/suspend/network change, redirects/auth/replay, proxies, partitioned caches, privacy/i18n/accessibility, provider differential traces, and staged performance/energy benchmarks.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0140:** Real-time transport service `>=0.1.0,<0.2.0` is conditional for WebSocket, SSE, or WebTransport products. It binds exact protocol/profile, service/resource/origin, secure HTTP route, credentials/application authority, native message/event/stream/datagram semantics, flow/queue limits, liveness, close, foreground/background/network-cost, and reconnect policy.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0141:** Reconnect always creates a new session and revalidates current identity, origin, credentials, authorization, subprotocol/extensions, limits, and product state. Resume cursors/acknowledgments are application evidence; gaps, duplicates, stale generations, unknown effects, suspend, and network changes are surfaced through accessible localized state/recovery rather than hidden replay.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0142:** Evidence covers browser/native mediation, origins/auth, hostile WebSocket/SSE/WebTransport input, compression/bounds, flow/fairness, background/suspend/network/proxy change, liveness, drain/close, reconnect/resume/storms, privacy/i18n/accessibility, provider/draft variance, and staged latency/energy benchmarks.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0143:** Messaging/RPC service `>=0.1.0,<0.2.0` is conditional for typed calls, streams, events, pub/sub, or brokered work. It binds interaction/schema revisions, service/topic, principal/authority/tenant, deadline/cancellation, resource/delivery/order/settlement, replay/idempotency/reconciliation, transport/broker profile, session/background state, and evidence boundaries.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0144:** Remote calls stay asynchronous distributed interactions and acknowledgments do not prove domain effect. User-visible send/sync/subscription/duplicate/conflict/recovery state names the reporting boundary accessibly; cancel/offline/reconnect never silently rolls back, retries, or declares success.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0145:** Evidence covers schema evolution, unary/streaming calls, deadline/cancel/partial progress, broker delivery/order/settlement/rebalance, suspend/offline/background behavior, retry/redelivery/dedup/inbox/outbox/reconciliation, security/privacy/i18n/accessibility, provider differentials, and staged latency/energy benchmarks.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0146:** Distributed coordination `>=0.1.0,<0.2.0` is conditional only when a desktop product participates directly in replicated state, exclusive distributed work, elections/locks, or cross-node consistency/transactions. It binds exact domain/configuration/instance generations, failure model, quorum/clocks, consistency/durability, authority, fencing, offline/background policy, and recovery.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0147:** Suspend, sleep, offline operation, network change, process restart, and stale caches invalidate local membership/lease/leadership confidence. Side effects require resource-enforced fencing; conflict/staleness/uncertain transaction and recovery state remains accessible and user-controllable rather than silently merged.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0148:** Evidence covers membership/failure suspicion, paused lease holders and fencing, election/lock cancellation races, consistency histories/caches/session loss, offline convergence/conflicts, distributed transactions/compensation, restore/identity clone, upgrades, privacy/i18n/accessibility, and staged network/energy benchmarks.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0149:** Application persistence/database service `>=0.1.0,<0.2.0` is conditional for durable typed product state. It binds logical schema/query, embedded/service provider and storage/topology generations, user/tenant authority, sessions/pools, transaction/isolation/durability, migrations/change, backup/restore/sync, quotas, offline policy, and lifecycle.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0150:** Database commit, durable storage, sync/replica visibility, backup inclusion, and external effect are separate. Schema/data migration is a staged compatible rollout integrated with application update/rollback; user-visible conflicts, corruption, migration/recovery, storage pressure, and data-loss boundaries remain accessible.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0151:** Evidence covers embedded filesystem/process faults and service databases, types/query binding, session/pool identity, transaction histories/durability, mixed-version migrations/offline clients, change/sync reconciliation, encrypted backup/restore/PITR, replication/failover, privacy/i18n/accessibility, and staged latency/energy benchmarks.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0152:** Object/blob storage `>=0.1.0,<0.2.0` is conditional for remote assets, backups, collaboration payloads, or content-addressed caches. It binds namespace/key/provider generation separately from verified content descriptors, exact user/tenant authority, transfer limits, offline/background policy, encryption/retention, and lifecycle.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0153:** Downloads bind exact generations and verify declared length and digest before trusted use. Uploads, including multipart staging, become visible only through conditional completion; conflicts, archive retrieval, quota/storage pressure, interrupted transfer, recovery, retention, and deletion state remain accessible and user-controllable.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0154:** Evidence covers range/resumed and parallel transfer, local-cache corruption and privacy partitioning, multipart crash/abort/complete races, conditional conflicts, delegated URL expiry/revocation, version restore, lifecycle/legal hold, replication/failover, accessibility/i18n, and staged network/energy benchmarks.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0155:** Caching `>=0.1.0,<0.2.0` is conditional for reusable local, shared, distributed, offline, or edge representations. It binds canonical keys, user/tenant/privacy partition, representation and configuration generations, freshness/validation/invalidation policy, tiers, capacity/cost, and authority.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0156:** Entry presence does not authorize reuse. Offline and stale states, refresh conflicts, storage pressure, privacy changes, corruption, eviction, and recovery remain observable and accessible; background fill respects lifecycle, connectivity, energy, metering, and user policy.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0157:** Evidence covers key/locale/identity partitions, clock/suspend freshness, validation/ranges, cancellation-safe collapse, pressure/eviction/corruption, invalidation races, offline convergence, edge propagation, accessibility/i18n, privacy, and staged latency/energy/network benchmarks.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0158:** Search/indexing `>=0.1.0,<0.2.0` is conditional for local or service-backed product discovery. It binds source/document/index-view, schema/analyzer/model/ranking, user/tenant/security, locale, freshness/offline, capacity/energy, migration/recovery, and provider generations.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0159:** Search results are derived evidence, not current source truth or action authority. Partial/stale/approximate state, index progress/errors, zero results, filter/sort state, point-in-time pagination expiry, and recovery remain accessible and user-controllable; consequential actions revalidate source generation and authority.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0160:** Evidence covers multilingual tokenization/ranking, assistive navigation/highlights, ordered offline capture, refresh/read-your-write, deterministic cursors, ANN/hybrid evaluation, tenant privacy, suspend/network/power changes, rebuild/upgrade/recovery, and staged relevance/latency/energy benchmarks.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0161:** Analytical processing `>=0.1.0,<0.2.0` is conditional for embedded or service-backed product analysis. It binds catalog/source/schema/function/plan/provider generations, user/tenant authority, batch/stream mode, event-time/effect policy, resources/energy, offline/background lifecycle, lineage, and recovery.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0162:** Results expose source snapshot/frontier, partial/approximate/late/corrected state and reproducibility class; background work respects lifecycle, metering, storage, thermal and power policy. Analytics does not authorize product action, and exactly-once state does not imply external effects.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0163:** Evidence covers typed/columnar conversion, local files/databases and remote sources, deterministic expressions/operators, cancellation/spill/pressure, offline replay/watermarks, checkpoint/sink failures, accessible progress/results, locale/time semantics, privacy, recovery, and staged latency/energy/cost benchmarks.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0164:** Structured interchange `>=0.1.0,<0.2.0` is conditional for product configuration, documents, persistence, IPC/network messages, import/export, or signed views. It binds logical schema, format/mapping/canonical/framing, registry, limits, validation, privacy, and implementation generations.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0165:** Decoded, defaulted, unknown, redacted, lossy, noncanonical, stale-schema, and partially imported state remains distinguishable and accessible. Hostile input is bounded before allocation/construction; imports do not gain filesystem/network/domain authority; signed bytes bind exact schema and canonical profile.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0166:** Evidence covers schema evolution/offline data, every selected format and canonical vector, chunked/cancelled parsing, lazy/borrowed lifetime, hostile limits/fuzzing, unknown round trips, transcoding loss, localized accessible diagnostics, registry outage/rollback, privacy, and staged latency/memory/energy benchmarks.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0167:** Service traffic `>=0.1.0,<0.2.0` is conditional for multi-endpoint remote services. It binds service/endpoint/discovery/route/security generations, network/tenant context, health/admission/affinity, retry/effect budgets, proxy/locality/failover, lifecycle/background/metered/power policy, and providers.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0168:** Network changes create new discovery/connection generations; stale/health/degraded/offline/retry state remains accessible and user-controllable. Health does not promise success, route choice does not grant authority, and retries/hedges preserve deadline, cancellation, credentials, body replay, privacy, and effect safety.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0169:** Evidence covers DNS/native/control discovery, dual-stack/network changes, endpoint churn/readiness/drain, policy/subset/affinity, multiplexed pools, retry/hedge/admission, proxy/privacy, locality/failover, suspend/background/power, accessible recovery, and staged latency/energy/network/cost benchmarks.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0170:** Policy evaluation `>=0.1.0,<0.2.0` is conditional for authorization, validation, configuration, features, routing/admission, or product rules. It binds typed entry point/request/result, policy/schema/data/function/evaluator generations, user/tenant/context, obligations/enforcement, cache/freshness, distribution, privacy, and provider.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0171:** Policy decisions are evidence, not credentials or effects. Missing/unknown/error/deny/requirements remain accessible with localized safe reasons and recovery; offline/cached permits are bounded by identity/resource/policy/data validity; obligations require explicit product capabilities and cannot execute ambient callbacks.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0172:** Evidence covers schema/type and language semantics, every result/default/conflict, entity/data freshness, cache/partial evaluation, offline/revocation, enforcement races/obligations, policy rollout/rollback, simulation, redacted accessible explanation, hostile limits, privacy, and staged latency/memory/energy benchmarks.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0173:** Compression/archive capability `>=0.1.0,<0.2.0` is conditional for import/export, downloads, backups, documents, packages, or compressed application data. It binds exact codec/container profiles and budgets, source origin/quarantine, destination/user authority, portable metadata/path mapping, integrity/encryption/trust, interaction, and providers.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0174:** Preview/listing remains inert and accessible. Extraction presents bounded conflict/security/loss evidence, never silently overwrites or creates links/special objects, stages before commit, preserves downloaded-content trust evidence, and cannot install, mount, launch, clear quarantine, or execute embedded content.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0175:** Evidence covers hostile names and localized display, user cancellation/credential mediation, drag/open/save/download flows, cloud/removable destinations, case/Unicode/platform metadata loss, expansion/storage pressure, suspend/resume, extraction recovery, reproducibility, provider differentials, and latency/memory/energy benchmarks.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0176:** Content inspection `>=0.1.0,<0.2.0` is conditional for downloaded/shared/removable/cloud files, attachments, previews, imports, packages, or active content. It binds subject/origin/quarantine, declared/detected interpretations, purpose, user/admin policy, local/cloud disclosure, restricted provider, freshness, accessible interaction, and budgets.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0177:** Display labels and thumbnails cannot hide type conflicts, active content, incomplete inspection, stale/unavailable scanners, origin, or quarantine. Previews are inert and isolated; transformation produces a new lineage-bearing artifact and cannot clear quarantine, authorize opening/install/execution, or claim universal safety.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0178:** Evidence covers hostile names/UI mimicry, platform associations and user defaults, polyglots, nested and remote content, downloaded-origin propagation, native scan/reputation/Gatekeeper-like policy, accessible warnings/override, preview crashes/hangs, transform fidelity/loss, offline/cloud/privacy modes, and latency/memory/energy benchmarks.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0179:** Information protection `>=0.1.0,<0.2.0` is conditional for labeled documents/messages/data, managed/unmanaged sharing, rights-protected content, or clipboard/drag/file/removable/print/capture/message/upload/cloud/API/AI DLP. It binds user/session/device/app, subject/lineage, taxonomy/assertions, recipient/channel/purpose, policy/protection/provider generations, offline state, privacy, and interaction.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0180:** Users receive accessible localized label/protection state, recommendations, warnings, structured justification/approval, recipient/destination consequences, stale/offline/unsupported coverage, and safe alternatives. UI cannot fabricate consent, hide partial protection, equate labels with enforcement, or claim prevention of screenshots/retyping/alternate channels.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0181:** Evidence covers manual/default/inherited/automatic labels, cross-application/platform metadata and markings, downgrade/appeal, rights/offline/revocation, managed/unmanaged recipients and apps, every selected interactive channel, background/headless denial, batch/cancellation/partial effects, hostile UI, privacy/accessibility, and latency/energy/task benchmarks.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0182:** Privacy engineering `>=0.1.0,<0.2.0` is conditional for personal/linkable data collection, device signals, permissions, preferences/consent, sharing/processing, data-rights UI, or deidentification. It binds user/subject/agent/session/device, purpose/data actions, exact notice/choice/policy, recipients/regions, retention, lineage, provider, accessibility, and authority.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0183:** Choice is granular, unbundled, localized, accessible, and withdrawable without fabricating legal conclusions or consent in background/headless contexts. Platform permission is separate evidence. Users can inspect current purposes/preferences, initiate/track requests, securely receive exports, correct/appeal, and see partial/held/residual outcomes.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0184:** Evidence covers notice/choice versions, refuse/withdraw/device/account conflicts, permissions versus consent, offline queued actions, recipient/processor/region changes, subject/agent verification, access/export/correction/restriction/erasure cases, third-party redaction, export security, restore/no-resurrection, privacy UX/accessibility, and task/latency/energy benchmarks.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0185:** Identity governance `>=0.1.0,<0.2.0` is conditional for account administration, tenant switching, invitations/guests, group management, provisioning status, access requests/reviews, or privileged workflows. It binds exact subject/account/tenant/provider generations, purpose, authority, mapping/policy/workflow generations, freshness, and privacy mode.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0186:** Interfaces distinguish directory facts, membership, requested/approved/fulfilled assignments, current sessions/credentials, and resource-effective access; expose pending/partial/unknown propagation; make destructive or privileged scope clear; and provide accessible confirmation, cancellation, expiry, emergency revocation, and recovery.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0187:** Evidence covers ambiguous identity, tenant/guest context, group derivations, stale pages/feeds, mapping loss, approval/SoD conflicts, JML and access-review tasks, offline/provider failures, session/credential/resource residuals, no-resurrection, localization/accessibility, disclosure resistance, responsiveness, and energy.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0188:** Application authentication `>=0.1.0,<0.2.0` is conditional for sign-in, passkeys/security keys, external browser/broker federation, authenticator management/recovery, account switching, session management, or sensitive-action step-up. It binds exact account/tenant/verifier/client/provider generations, purpose/transaction, interaction, risk/assurance, and authority.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0189:** Interfaces identify the verifier/account/tenant/method/transaction, preserve platform brokers and password managers, provide adequate time and non-biometric alternatives, distinguish local user verification from RP authentication, expose fallback weakness and session/logout boundaries, and never train users to approve context-free prompts.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0190:** Evidence covers browser/broker/app return routing, cancellation/restart, passkey discovery and synced/device-bound states, security keys, password/OTP/OOB, authenticator lifecycle/recovery, federation errors, step-up, concurrent sessions/logout/revocation, offline/locked devices, accessibility/localization, disclosure resistance, responsiveness, and energy.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0191:** Application authorization `>=0.1.0,<0.2.0` is conditional for permission-aware navigation/actions, ownership/sharing, role/attribute/relation administration, access explanations/reviews, delegated work, or offline authorization state. It binds exact subject/actor/tenant/resource/action/context and policy/data/frontier generations.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0192:** Interfaces treat hidden/disabled actions as usability hints, enforce at the resource boundary, protect list/count/facet/snippet existence, explain scope/recipient/expiry/deny/unknown safely, make public/external/delegated sharing explicit, support keyboard/screen-reader flows, and expose stale/offline/revocation limits.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0193:** Evidence covers navigation/action races, multi-selection and partial results, sharing/invitation/transfer/revoke, role and relation changes, filter versus point checks, policy rollout, offline caches, effective-access explanations and redaction, tenant/account switching, native denials, confused-deputy routing, localization/accessibility, responsiveness, and energy.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0194:** Secrets lifecycle `>=0.1.0,<0.2.0` is conditional for user/application secret vaults, dynamic credentials, workload brokers, authenticator or account keys, credential injection, rotation status, privileged checkout, or incident response. It binds exact user/app/device/workload, purpose/target, provider/secret/lease generations, interaction, exposure, authority, and expiry.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0195:** Interfaces preserve native brokers and password managers, minimize reveal/copy, identify target/account/scope/expiry, warn for file/environment/clipboard exposure, provide accessible approval/quorum/break-glass and recovery, show successor-adoption/predecessor-denial residuals, and never display secret-derived identifiers.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0196:** Evidence covers locked/unavailable vaults, account/device/app switching, prompts/cancellation, dynamic lease renewal, broker routing, clipboard/file/env/child-process exposure, reload/restart, rotation overlap/failure, privileged session/JIT/emergency flows, leak containment, backup/restore, localization/accessibility, responsiveness, and energy.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0197:** Durable workflow `>=0.1.0,<0.2.0` is conditional for user-visible long-running operations, offline/resumable processes, task inboxes/forms, approvals, progress/cancellation, or repair. It binds exact instance/run/definition/history, account/tenant/actor, task/effect generations, authority, deadlines, privacy, and provider.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0198:** Interfaces display durable domain state rather than owning it; distinguish requested/accepted/running/waiting/human/compensating/completed/residual states; provide safe cancel/withdraw/retry/escalate; protect task existence; support accessible/localized forms and adequate time; and never label compensation as rollback.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0199:** Evidence covers restart/offline/reconnect, duplicate commands/signals, stale views, progress and cancellation races, task claim/delegation/conflicts/drafts/submission, approval/quorum/SoD, notifications/deadlines/calendars, partial effects/compensation, version migration, repair, privacy redaction, localization/accessibility, responsiveness, and energy.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0200:** API governance `>=0.1.0,<0.2.0` is conditional for remote service or event APIs and binds logical operation, contract/binding/deployment generations, audience, consumer identity, compatibility, authority, privacy, support, and offline/reconnect policy.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0201:** Generated SDKs remain adapters behind domain boundaries. Async operations preserve cancellation/deadlines/streaming/backpressure and complete sync counterparts do not create hidden runtimes; pagination, retries, errors, quotas, and long-running state remain explicit.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0202:** Evidence covers old/new client-provider matrices, protocol mappings, offline/retry/idempotency, partial streams, inaccessible/localized errors, privacy-safe deprecation notices and telemetry, migration/rollback, generated SDK ergonomics, responsiveness, memory, energy, and benchmarks.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0203:** Application synchronization `>=0.1.0,<0.2.0` is conditional for offline-capable application state and binds dataset/replica/device/account/object/change/schema/policy generations, selection, authority, causal context, network/storage/energy policy, privacy, and objectives.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0204:** Durable local intent and optimistic display do not prove authoritative completion. Pending/confirmed/conflicted/rejected/repaired states remain accessible; fresh or fenced authority is required for globally constrained or irreversible effects unless an RFC proves delegation.

**RM-PROFILE-FOUNDATION-WINDOWED-DESKTOP-0205:** Evidence covers offline/reconnect, replica reinstall/clone/restore, session/checkpoint recovery, duplicate/reorder/partition, merge policies, selective sync/revocation, tombstones/late devices, migration, attachments, account transitions, localization/accessibility, responsiveness, memory/disk/network, energy, and benchmarks.

## Whole-product gaps

This profile does not supply a rendering command model, widget/UI framework, text editing model, image/audio codecs, media containers/graphs, gestures, or translated product resources. Product-specific semantic roles/actions/content, accepted transfer formats/importers, locale coverage, audio policy/content, and accessible UX still belong to the product/framework. It cannot claim desktop-application completeness.

## Evidence gates

Profile evidence includes window/device joint resolution, mixed-scale display migration, resize/occlusion/minimize, surface and device loss/recovery, bounded frame pacing, color/alpha correctness, keyboard-only native chrome, protected-path nonclaims, software fallback disclosure, and cleanup across logout/suspend/remote-session transitions.

Input evidence additionally covers layout/IME diversity, keyboard-only operation, accessibility-originated input, pointer/touch cancellation, focus/capture races, secure-text disclosure, high-rate stream bounds, and input-to-present latency correlation.

## History

- **0.58.0:** Adds conditional offline application synchronization, explicit optimistic/authoritative milestones, causal and conflict semantics, selective state, deletion/migration, accessible status, conformance, and benchmarks.
- **0.57.0:** Adds conditional API contract governance, generated SDK boundaries, directional compatibility, client migration/deprecation evidence, conformance, and desktop performance qualities.
- **0.56.0:** Adds conditional durable user-visible workflows, resumable progress, safe cancellation/compensation status, protected task inboxes, accessible forms, approvals/quorum, migration/repair, conformance, and benchmarks.
- **0.55.0:** Adds conditional secret and credential brokerage, minimized reveal/delivery, dynamic leases, rotation adoption/denial status, privileged checkout/break-glass, incident response, recovery, conformance, and benchmarks.
- **0.54.0:** Adds conditional permission-aware UI, ownership/sharing and access administration, safe explanations, sound resource filtering, offline/revocation disclosure, point enforcement, conformance, and benchmarks.
- **0.53.0:** Adds conditional application sign-in, passkey/security-key and fallback UX, broker/federation routing, authenticator management/recovery, step-up, session/logout/revocation, conformance, and benchmarks.
- **0.52.0:** Adds conditional identity administration, tenant/guest and membership evidence, provisioning/lifecycle/access-review workflows, privileged/emergency mediation, explicit propagation/residuals, conformance, and benchmarks.
- **0.51.0:** Adds conditional privacy-purpose and consent/preference evidence, accessible rights workflows, secure exports/corrections, scoped erasure and residuals, offline/processor/region handling, conformance, and benchmarks.
- **0.50.0:** Adds conditional sensitivity labeling, lineage-aware classification, governed downgrade, independently evidenced markings/rights, cross-channel DLP, accessible user mediation, offline/revocation, conformance, and benchmarks.
- **0.49.0:** Adds conditional evidence-preserving identification, restricted recursive inspection and previews, origin/quarantine propagation, provider verdicts, explicit transformation loss, accessible mediation, conformance, and benchmarks.
- **0.48.0:** Adds conditional codec/archive processing with inert accessible preview, bounded hostile input, safe transactional extraction, explicit trust and metadata loss, recovery, conformance, and benchmarks.
- **0.47.0:** Adds conditional typed policy evaluation, immutable contexts, explicit unknown/default/composition, obligation enforcement, cached/offline validity, accessible reasons, distribution/simulation, conformance, and benchmarks.
- **0.46.0:** Adds conditional service discovery/routing/balancing, expiring health evidence, affinity, unified attempt/admission budgets, network-aware failover, accessible recovery, conformance, and benchmarks.
- **0.45.0:** Adds conditional schema-first interchange, exact format mappings, canonical signed views, bounded streaming parsers, unknown/loss handling, accessible validation, registry lifecycle, conformance, and benchmarks.
- **0.44.0:** Adds conditional typed batch/stream analytics, versioned plans, event-time/state/effects, resource governance, accessible results, lineage/privacy, recovery/reproducibility, conformance, and benchmarks.
- **0.43.0:** Adds conditional source-versioned search/indexing, explicit visibility, lexical/vector/hybrid retrieval, stable pagination, accessible results, migration/recovery, relevance evaluation, conformance, and benchmarks.
- **0.42.0:** Adds conditional policy-qualified caching, privacy partitions, freshness/validation, tiering/eviction, stampede control, invalidation/edge delivery, accessibility, conformance, and benchmarks.
- **0.41.0:** Adds conditional generation-bound object/blob storage, verified content addressing, multipart commit, delegated access, retention/recovery, accessibility, conformance, and benchmarks.
- **0.40.0:** Adds conditional typed persistence/databases, transaction/durability evidence, staged migrations, offline/change reconciliation, backup/restore, replication, accessibility, conformance, and benchmarks.
- **0.39.0:** Adds conditional distributed coordination, resource-enforced fencing, precise consistency, offline/conflict evidence, transactions/recovery, accessibility, conformance, and benchmarks.
- **0.38.0:** Adds conditional messaging/RPC, schema evolution, streaming, broker delivery/settlement, explicit replay/idempotency/reconciliation, accessible state, conformance, and benchmarks.
- **0.37.0:** Adds conditional WebSocket, SSE, and versioned WebTransport sessions, native data semantics, background-aware reconnect/resume evidence, accessibility, conformance, and benchmarks.
- **0.36.0:** Adds conditional HTTP/1.1-/2-/3 semantics, streaming, connection/proxy/cache behavior, explicit redirect/auth/replay policy, accessible interaction, conformance, and benchmarks.
- **0.35.0:** Adds conditional exact TLS/QUIC channel policy, authentication/readiness, resumption/early-data replay authority, exporters/bindings, data/closure, migration, accessibility, conformance, and benchmarks.
- **0.34.0:** Adds conditional certificate enrollment, opaque-key requests/POP, identity authority, protocol delivery/install, accessible renewal/rekey/replacement/revocation, activation, conformance, and benchmarks.
- **0.33.0:** Adds conditional authenticated repository snapshots, package state/resolution/plans, journaled native deployment, hooks/services/data, accessible rollout/health, compensating rollback, recovery, conformance, and benchmarks.
- **0.32.0:** Adds conditional exact signed code/package/document/artifact views, authority-bearing signing, timestamps, transparency, provenance/reproducibility, evidence-composing verification, lifecycle, accessibility, conformance, and benchmarks.
- **0.31.0:** Adds conditional bounded certificate parsing, trust-store evidence, candidate path construction, policy/time/identity-bound validation, revocation/network/cache quality, result lifecycle, conformance, and benchmarks.
- **0.30.0:** Adds conditional versioned cryptographic policy, opaque operation-scoped keys, exact hash/MAC/KDF/AEAD/public-key/transfer contracts, provider/hardware/attestation evidence, lifecycle, conformance, and benchmarks.
- **0.29.0:** Adds conditional immutable service/job registration, execution scopes, demand activation/readiness, durable schedules and trigger reconciliation, attempts/checkpoints/retries, budgets, generation updates, accessibility, conformance, and benchmarks.
- **0.28.0:** Adds conditional participant/session/action-scoped remote presentation and controlled input, exact mappings/state/order, secure-boundary and local-override rules, emergency stop, accessibility, conformance, and end-to-end latency evidence.
- **0.27.0:** Adds conditional trusted screen/window/application/region selection, revocable generation-scoped capture, exact frame/color/geometry/timing, cursor/audio separation, protection nonclaims, bounded delivery, privacy/accessibility, conformance, and benchmarks.
- **0.26.0:** Adds conditional typed activation, revisioned handler/default policy, safe file/URI handoff, incoming instance routing, registration, boundary-scoped completion, security/accessibility, conformance, and benchmarks.
- **0.25.0:** Adds conditional time-based source/container/track, exact timeline, codec/raw-resource, playback/sync/seek/buffer, timed-text/accessibility, encode/mux, protection, conformance, and benchmark requirements.
- **0.24.0:** Adds conditional bounded image probe/decode, exact immutable pixels, progressive/region/animation/metadata boundaries, explicit encode/transcode, provider isolation, accessibility, conformance, and benchmarks.
- **0.23.0:** Adds conditional semantic image descriptions, display color evidence, compositor negotiation, transforms/HDR/profile boundaries, dynamic lifecycle, privacy/accessibility, and measurement-qualified evidence requirements.
- **0.22.0:** Adds conditional destination discovery, format-bound whole-ticket negotiation, bounded paginated output, boundary-scoped job evidence, artifact output, security, accessibility, and benchmark requirements.
- **0.21.0:** Adds conditional principal/session observation, scoped authentication evidence, opaque credential/delegation boundaries, async-safe impersonation prohibition, privacy, accessibility, and evidence requirements.
- **0.20.0:** Adds conditional qualified power/battery/thermal observation, explicit workload adaptation, optional scoped assertion leases, energy evidence, privacy, accessibility, and lifecycle requirements.
- **0.19.0:** Adds conditional typed notification submission, attention/privacy policy, untrusted action activation, optional state/scheduling features, accessibility, and evidence requirements.
- **0.18.0:** Adds conditional consent-bound camera discovery/raw capture, exact frame/color/timing/control semantics, bounded delivery, privacy/accessibility, and evidence requirements.
- **0.17.0:** Adds conditional storage-volume/mount observation, privileged mount/removal services, staged safe-removal/durability, identity, security, accessibility, and evidence requirements.
- **0.16.0:** Adds conditional completion-oriented async-I/O infrastructure, readiness translation, cancellation lifetime, engine/executor separation, bounded-load, and shutdown evidence requirements.
- **0.15.0:** Adds conditional general device observation, generation-scoped identity evidence, snapshot reconciliation, privacy, class handoff, and hardware-change evidence requirements.
- **0.14.0:** Adds conditional device/route observation, exact PCM render/capture, sample-clock correlation, restricted realtime processing, capture authority, accessibility, and latency/reliability evidence requirements.
- **0.13.0:** Adds native-thread lifecycle, synchronization/wait, atomics, UI-affinity, scheduling-quality, realtime prohibition, TLS, and evidence requirements.
- **0.12.0:** Adds optional plugin catalog, resolution, trust/isolation, lifecycle, immutable generation update, supply-chain, and evidence requirements.
- **0.11.0:** Adds optional explicit virtual-memory, mapping, sharing, residency, allocator, typed-view, and executable-memory prohibition/evidence requirements.
- **0.10.0:** Adds conditional resolution, connection racing, stream/path observation, optional datagram/listener/secure channel, authority, security, and network-change evidence requirements.
- **0.9.0:** Adds application-instance, activation, session/power observation, cooperative termination/inhibition, readiness, and safe restoration requirements.
- **0.8.0:** Adds structured observability, explicit causal context, bounded exporter-independent pipelines, privacy governance, diagnostic bundles, and separated crash capture/analysis requirements.
- **0.7.0:** Adds typed configuration schema/source/resolution, immutable snapshots, provenance, reload classes, secret boundaries, and loss-aware change reconciliation.
- **0.6.0:** Adds locale preferences/contexts, typed resources/messages, formatting, calendar/time-zone, collation, data-version, pseudolocale, and live-change requirements.
- **0.5.0:** Adds typed lazy data offers, clipboard, drag-and-drop, conditional file promises, transfer authority, and accessible-operation requirements.
- **0.4.0:** Adds semantic-tree, accessible text/action/event, preference, native adapter, and assistive-technology evidence requirements.
- **0.3.0:** Adds exact font resolution, shaping, layout, rasterization, Unicode-version, and semantic-mapping requirements.
- **0.2.0:** Adds keyboard, pointer, conditional touch, text input/composition, provenance, and authority constraints.
- **0.1.0:** Initial windowing and graphics-presentation infrastructure profile.
