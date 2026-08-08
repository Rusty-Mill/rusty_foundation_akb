# `rm.windowing.window`

| Field | Value |
|---|---|
| Status | Draft |
| Contract version | 0.1.0 |
| Layer | Common API / backend contract |

## Purpose

Create and govern one owned top-level native window while exposing requests, committed state, lifecycle, and native variance without presenting a synchronous fiction.

## Contract

**RM-WINDOWING-WINDOW-0001:** Creation accepts an immutable descriptor containing semantic role, initial logical extent constraints, visibility intent, decoration preference, title policy, transparency/security policy, and optional parent/owner relationship. Unsupported required fields fail before publishing a usable resource.

**RM-WINDOWING-WINDOW-0002:** Creation completes only after a native identity exists and an initial committed snapshot is available. Providers may expose an earlier internal configuring phase but must not permit presentation against unconfigured geometry.

**RM-WINDOWING-WINDOW-0003:** Move, resize, minimize, maximize, fullscreen, visibility, activation, and title operations are requests. Success means the provider accepted or submitted the request; only a later committed snapshot/event proves effective state.

**RM-WINDOWING-WINDOW-0004:** Every committed snapshot atomically contains lifecycle, logical content extent, scale/transform, surface-pixel extent, surface generation, display associations, focus/activation, visibility, occlusion knowledge, and a monotonically increasing per-window revision.

**RM-WINDOWING-WINDOW-0005:** The portable lifecycle is `configuring -> ready -> closing -> destroyed`. Visibility, minimization, focus, activation, and occlusion are orthogonal flags, not lifecycle states. No transition leaves a usable native resource after `destroyed`.

**RM-WINDOWING-WINDOW-0006:** A user or system close gesture emits `close_requested`; it does not destroy automatically. Product policy chooses whether to cancel, save, hide, or request destruction. Forced native destruction is reported distinctly.

**RM-WINDOWING-WINDOW-0007:** Destruction is idempotent. Completion means portable event delivery is closed, presentation surfaces are invalid, backend callbacks can no longer reference consumer state, and native resources have been released or transferred under an explicit escape contract.

**RM-WINDOWING-WINDOW-0008:** Window affinity and dispatch-context requirements are declared at provider resolution. Calls from an invalid context fail or marshal only when the contract explicitly permits it; they never silently run a nested event loop.

**RM-WINDOWING-WINDOW-0009:** The async path is cancellation-safe before publication. After publication, cancellation returns the owned resource or performs fully observed cleanup. The sync path may block only where its dispatch-context contract permits and never creates a hidden runtime.

**RM-WINDOWING-WINDOW-0010:** Native callback reentrancy is contained by the backend. Portable application events are delivered non-reentrantly in per-window order through a bounded queue/stream with explicit overflow semantics.

**RM-WINDOWING-WINDOW-0011:** Titles are Unicode semantic text. Conversion loss, native truncation, privacy classification, and exposure in task switchers, logs, screenshots, accessibility, or remote sessions are explicit; sensitive content is not a default title.

**RM-WINDOWING-WINDOW-0012:** Synthetic/native event provenance, capture exclusion support, transparency/click-through behavior, always-on-top, and activation-stealing are discoverable policy-controlled features, never silently enabled defaults.

## Non-guarantees

The contract does not guarantee exact placement, focus acquisition, global coordinates, decoration geometry, occlusion knowledge, capture prevention, exclusive fullscreen, or that a compositor honors requested size/state.

## Dependencies

- Requires runtime lifecycle and monotonic event timestamps.
- Optionally uses observability and security-policy capabilities.
- Does not require graphics, widgets, terminal emulation, or input interpretation.

