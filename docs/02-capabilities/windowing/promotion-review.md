# Windowing Experimental promotion review

| Field | Value |
|---|---|
| Status | Proposed; no maturity change |
| Subject | Windowing domain 0.1.1; window, display-topology, and presentation-surface contracts 0.1.x |
| Architecture | Model 1.83.0 |
| Proposed decision | Eligible for explicit Experimental promotion review; remain Draft pending disposition |
| Implementation authority | None |

## Gate assessment

| Gate | State | Exact evidence | Qualification |
|---|---|---|---|
| Contract semantics | Pass | [window](window.md), [display topology](display-topology.md), [surface](presentation-surface.md), [coordinates](coordinate-model.md), [events](event-model.md), ADR-0020/0021 | native extension surface and supported-version frontier remain trial inputs |
| Dependencies/profile impact | Pass | [composition register](dependencies.md), [windowed desktop profile](../profiles/foundation-windowed-desktop.md) | domain relationships are explicit; stable graph extraction remains CR-002 work |
| Platform research | Pass | [platform research](platform-research.md), [source review](source-review.md) | exact Win32/compositor/X11/AppKit generations are not selected |
| Cross-cutting planning | Pass | [quality review](cross-cutting.md) | no implementation, specialist product review, or provider result exists |
| Assertions/cases | Pass | [traceability](traceability.md), [conformance](conformance.md) | cases are specified but not executed |
| Benchmark scenarios | Pass | [scenario mapping](traceability.md#benchmark-scenario-mapping), [benchmarks](benchmarks.md) | no native baseline, run, budget, or performance claim exists |
| Ownership/trial bounds | Qualified | [ownership](ownership.md), [trial governance](../../05-governance/implementation-trials/README.md) | role ownership exists; named people and independent signoffs are absent |

## Decision boundary

The generated scorecard may report planning eligibility. Windowing remains Draft until an accepted record binds named accountable people, reviewer independence, exact contract/platform/profile scope, findings/waivers, decision date, and permitted trial constraints. A valid repository standards profile and separately accepted trial record remain required before code.

**RM-WINDOWING-PROMOTION-0001:** Eligibility MUST NOT change maturity, choose native providers or graphics integration, or authorize implementation without an explicit accepted decision.

**RM-WINDOWING-PROMOTION-0002:** Promotion MUST bind exact lifecycle, snapshot, coordinate, event, display, surface, authority/security, platform, and profile claims; omitted providers/features remain unsupported or unknown.

**RM-WINDOWING-PROMOTION-0003:** Planned cases and scenarios MUST NOT be represented as passing portability, accessibility, security, native-performance, resource, or recovery evidence.

