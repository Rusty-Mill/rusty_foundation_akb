# `rm.profile.foundation.windowed-desktop`

| Field | Value |
|---|---|
| Status | Draft |
| Version | 0.9.0 |
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

## Whole-product gaps

This profile does not supply a rendering command model, widget/UI framework, text editing model, image codecs, gestures, translated product resources, or application lifecycle/session integration. Product-specific semantic roles/actions/content, accepted transfer formats/importers, locale coverage, and accessible UX still belong to the product/framework. It cannot claim desktop-application completeness.

## Evidence gates

Profile evidence includes window/device joint resolution, mixed-scale display migration, resize/occlusion/minimize, surface and device loss/recovery, bounded frame pacing, color/alpha correctness, keyboard-only native chrome, protected-path nonclaims, software fallback disclosure, and cleanup across logout/suspend/remote-session transitions.

Input evidence additionally covers layout/IME diversity, keyboard-only operation, accessibility-originated input, pointer/touch cancellation, focus/capture races, secure-text disclosure, high-rate stream bounds, and input-to-present latency correlation.

## History

- **0.9.0:** Adds application-instance, activation, session/power observation, cooperative termination/inhibition, readiness, and safe restoration requirements.
- **0.8.0:** Adds structured observability, explicit causal context, bounded exporter-independent pipelines, privacy governance, diagnostic bundles, and separated crash capture/analysis requirements.
- **0.7.0:** Adds typed configuration schema/source/resolution, immutable snapshots, provenance, reload classes, secret boundaries, and loss-aware change reconciliation.
- **0.6.0:** Adds locale preferences/contexts, typed resources/messages, formatting, calendar/time-zone, collation, data-version, pseudolocale, and live-change requirements.
- **0.5.0:** Adds typed lazy data offers, clipboard, drag-and-drop, conditional file promises, transfer authority, and accessible-operation requirements.
- **0.4.0:** Adds semantic-tree, accessible text/action/event, preference, native adapter, and assistive-technology evidence requirements.
- **0.3.0:** Adds exact font resolution, shaping, layout, rasterization, Unicode-version, and semantic-mapping requirements.
- **0.2.0:** Adds keyboard, pointer, conditional touch, text input/composition, provenance, and authority constraints.
- **0.1.0:** Initial windowing and graphics-presentation infrastructure profile.
