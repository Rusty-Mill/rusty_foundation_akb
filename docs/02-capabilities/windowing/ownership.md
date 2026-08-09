# Windowing ownership and trial readiness

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Accountable owner | Windowing capability owner, initially exercised by Foundation maintainers |
| Architecture reviewer | Foundation architecture review |
| Security reviewer | Foundation security/privacy review for native handles, titles/topology, activation, transparency, and capture claims |
| Evidence reviewer | Foundation UI-platform conformance, accessibility, and performance review |
| Compatibility authority | Foundation architecture review until a dedicated compatibility council exists |

## Ownership duties

The owner maintains the three contract generations, committed snapshot and event semantics, dependency/profile composition, platform/source frontier, quality findings, conformance adapters, benchmark scenarios, and promotion evidence. Provider ownership covers Win32, Wayland, X11, and AppKit mappings separately. Actual promotion and trial records name accountable people and disclose independence limitations.

## Bounded trial plan

A later trial may exercise one minimal native top-level window per provider, exact committed snapshots, display observation, typed coordinate transforms, ordered non-reentrant events, and generation-scoped presentation targets. The matrix includes supported Windows builds, at least two materially different Wayland compositors where practical, an X11 window manager, and supported macOS/SDK generations; remote, virtual, headless, mixed-scale, rotation, and hot-plug cases are declared rather than assumed.

The trial uses the [foundation trial template](../../05-governance/implementation-trials/trial-template.md), synthetic nonsensitive titles/content, isolated unstable APIs, no production publication, and disposable code. It does not select a graphics API, widget toolkit, input model, event-loop/runtime, accessibility framework abstraction, repository layout, or metadata serialization.

Stop conditions include post-destroy callbacks, stale surface use reported as success, mixed-revision snapshots, silent non-coalescible event loss, unsafe native-handle lifetime, activation/capture claim inflation, sensitive metadata leakage, unbounded dispatch pressure, inaccessible trial controls, provenance loss, or material input drift.

**RM-WINDOWING-OWNER-0001:** Promotion or trial records MUST name accountable people for domain and each claimed provider, exact generations, reviewer independence, and unresolved platform limitations.

**RM-WINDOWING-OWNER-0002:** Trial hypotheses MUST distinguish request acceptance, committed native/compositor state, surface readiness, graphics present completion, displayed frame, focus, and accessible exposure.

**RM-WINDOWING-OWNER-0003:** The bounded plan is evidence only and MUST NOT authorize native handles, privileged capture/activation behavior, implementation, packaging, or release.

**RM-WINDOWING-OWNER-0004:** Disposal MUST close windows/sessions, release native and graphics-facing resources, revoke privileges, account for traces/artifacts, retain negative evidence, and prevent trial artifacts from entering release channels.

