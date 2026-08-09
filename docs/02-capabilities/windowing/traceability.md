# Windowing assertion traceability

**Status:** Draft assertion mapping  
**Authority:** [Windowing domain](README.md)

The semantic identities below compose the existing `WINDOW-*`, `COORD-*`, `DISPLAY-*`, and `SURFACE-*` executable cases without replacing their historical identities.

| Assertion | Covered normative source files | Verification intention |
|---|---|---|
| `rm.assertion.windowing.lifecycle@1` | `window.md`, `event-model.md` | Verify staged creation, request versus committed state, close/destroy, callback order/context, reentrancy, queue policy, and terminal event boundaries. |
| `rm.assertion.windowing.coordinates@1` | `coordinate-model.md` | Property-test typed spaces, revisioned transforms, rounding, fractional scale, rotation, negative origins, and drift resistance. |
| `rm.assertion.windowing.displays@1` | `display-topology.md` | Verify revisioned snapshots, identity generations, hot-plug/mirror/remote/headless changes, privacy denial, and subscription reconciliation. |
| `rm.assertion.windowing.presentation-surface@1` | `presentation-surface.md`, `traceability.md` | Verify surface generation/invalidation, geometry/display correlation, stale-resource rejection, security nonclaims, and traceability identity rules. |
| `rm.assertion.windowing.dependencies@1` | `dependencies.md` | Verify internal-set compatibility, consumer/peer ownership direction, profile resolution, optional runtime use, and graph qualification. |
| `rm.assertion.windowing.quality-review@1` | `cross-cutting.md` | Verify six-dimension applicability, exact evidence methods, milestone separation, provider-specific claims, and findings. |
| `rm.assertion.windowing.source-review@1` | `source-review.md` | Verify source class/status/frontier, exact provider generations, mutable-source binding, observed/documented separation, and invalidation. |
| `rm.assertion.windowing.ownership@1` | `ownership.md` | Verify provider/domain roles, trial matrix/nonclaims, stop conditions, resource/privilege cleanup, and evidence retention. |
| `rm.assertion.windowing.promotion-boundary@1` | `promotion-review.md` | Verify eligibility/decision separation, exact claim scope, named review, planned-versus-observed evidence, and downstream implementation gates. |

## Benchmark scenario mapping

| Scenario | Benchmark requirements | Legacy workload | Comparison contract |
|---|---|---|---|
| `rm.benchmark.windowing.create-ready@1` | `RM-WINDOWING-BENCH-0001`, `RM-WINDOWING-BENCH-0007` | WIN-BENCH-001 | Same descriptor, initial native/compositor state, committed-snapshot milestone, and presentation nonclaim. |
| `rm.benchmark.windowing.interactive-resize@1` | `RM-WINDOWING-BENCH-0002`, `RM-WINDOWING-BENCH-0007` | WIN-BENCH-002 | Same resize path, event time basis, queue/coalescing policy, snapshot oracle, and surface work. |
| `rm.benchmark.windowing.mixed-scale-traversal@1` | `RM-WINDOWING-BENCH-0003`, `RM-WINDOWING-BENCH-0007` | WIN-BENCH-003 | Same topology, path, scale/orientation transitions, typed conversions, and revision checks. |
| `rm.benchmark.windowing.topology-storm@1` | `RM-WINDOWING-BENCH-0004`, `RM-WINDOWING-BENCH-0007` | WIN-BENCH-004 | Same display event schedule, subscription race, gap policy, and final topology frontier. |
| `rm.benchmark.windowing.lifecycle-churn@1` | `RM-WINDOWING-BENCH-0005`, `RM-WINDOWING-BENCH-0007` | WIN-BENCH-005 | Same create/show/hide/destroy sequence, terminal guarantees, native resources, and recovery observation. |
| `rm.benchmark.windowing.surface-regeneration@1` | `RM-WINDOWING-BENCH-0006`, `RM-WINDOWING-BENCH-0007` | WIN-BENCH-006 | Same invalidation point, stale-use attempt, reacquisition milestone, and graphics/display nonclaims. |

**RM-WINDOW-TRACE-0001:** Every windowing requirement MUST map to a stable semantic assertion and an executable case/review method before Experimental promotion.

**RM-WINDOW-TRACE-0002:** Native Win32, Wayland, X11, and AppKit case adapters MUST preserve the same semantic assertion identity while reporting provider-specific setup, observations, limitations, and artifacts.

**RM-WINDOW-TRACE-0003:** Presentation success, committed window state, frame display, input focus, and accessible exposure MUST remain separate oracles.

**RM-WINDOW-TRACE-0004:** Legacy `WIN-BENCH-*` workload IDs remain suite-local and MUST map to stable semantic scenario identities before comparison or promotion use.
