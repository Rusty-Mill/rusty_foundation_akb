# Process Experimental promotion review

| Field | Value |
|---|---|
| Status | Proposed; no maturity change |
| Subject | Process foundations 0.1.1; executable-resolution, spawn, control, supervision, and pipeline contracts 0.1.x |
| Architecture | Model 1.85.0 |
| Proposed decision | Eligible for explicit Experimental promotion review; remain Draft pending disposition |
| Implementation authority | None |

## Gate assessment

| Gate | State | Exact evidence | Qualification |
|---|---|---|---|
| Contract semantics | Pass | [launch](launch-model.md), [environment](environment-model.md), [stdio](stdio-model.md), [resolution](executable-resolve.md), [spawn](spawn.md), [control](control.md), [supervision](supervision.md), [pipeline](pipeline.md) | shell/activation/terminal/restricted-execution/service-installation and arbitrary native controls remain outside scope |
| Dependencies/profile impact | Pass | [composition register](dependencies.md), [CLI](../profiles/foundation-cli.md), [server](../profiles/foundation-server.md), [headless](../profiles/foundation-headless.md), [source-linked graph](../../04-ecosystem/consistency-readiness/dependency-graph.md) | exact capability edges are registered; product service/containment/parser policy remains open |
| Platform research | Pass | [platform research](platform-research.md), [source review](source-review.md) | exact Windows/Linux/macOS generations, parser conventions, sandbox/service contexts, and fallback mechanisms are not selected |
| Cross-cutting planning | Pass | [quality review](cross-cutting.md) | no provider execution, specialist product review, sandbox proof, or native-performance result exists |
| Assertions/cases | Pass | [traceability](traceability.md), [conformance](conformance.md) | cases are specified but not executed |
| Benchmark scenarios | Pass | [scenario mapping](traceability.md#benchmark-scenario-mapping), [benchmarks](benchmarks.md) | no native baseline, run, numeric budget, regression conclusion, or performance claim exists |
| Ownership/trial bounds | Qualified | [ownership](ownership.md), [trial governance](../../05-governance/implementation-trials/README.md) | role ownership exists; named people, independent signoffs, artifacts, and disposable environments are absent |

## Decision boundary

The generated scorecard may report planning eligibility. Process remains Draft until an accepted record binds named accountable people, independent reviewers, exact contract/profile/provider/parser/containment scope, exclusions, findings/waivers, decision date, and permitted trial constraints. A valid repository standards profile and separately accepted trial record remain required before code.

**RM-PROCESS-PROMOTION-0001:** Eligibility MUST NOT change maturity, select native mechanisms/runtimes/service managers, resolve product policy, or authorize implementation without an explicit accepted decision.

**RM-PROCESS-PROMOTION-0002:** Promotion MUST bind exact executable, arguments/environment, inheritance, milestone, child identity, wait/control, P-level, pipeline, cancellation, error, security, platform, and profile claims; omitted features remain unsupported or unknown.

**RM-PROCESS-PROMOTION-0003:** Planned cases and scenarios MUST NOT be represented as passing portability, security, accessibility, containment, native-performance, cleanup, recovery, or resource-leak evidence.
