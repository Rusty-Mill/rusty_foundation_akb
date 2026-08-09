# Async I/O Experimental promotion review

| Field | Value |
|---|---|
| Status | Proposed; no maturity change |
| Subject | Async I/O foundations 0.1.1; operation, engine, cancellation, registration, load, runtime, shutdown, and observability contracts |
| Architecture | Model 1.87.0 |
| Proposed decision | Eligible for explicit Experimental promotion review; remain Draft pending disposition |
| Implementation authority | None |

## Gate assessment

| Gate | State | Exact evidence | Qualification |
|---|---|---|---|
| Contract semantics | Pass | [operation](operation-model.md), [readiness/completion](readiness-completion.md), [cancellation/lifetime](cancellation-lifetime.md), [registration](registration-resources.md), [load](backpressure-fairness.md), [runtime](runtime-integration.md), [errors/observability](errors-observability.md) | consuming-domain operations/effects and native provider matrices remain separately owned and unselected |
| Dependencies/profile impact | Pass | [composition register](dependencies.md), [filesystem](../filesystem/dependencies.md), [IPC](../ipc/dependencies.md), [process](../process/dependencies.md) | framework relationships are explicit; no premature capability node or universal engine/runtime dependency is created |
| Platform research | Pass | [platform research](platform-research.md), [source review](source-review.md) | exact OS/provider/runtime/operation/resource generations and mechanisms are not selected |
| Cross-cutting planning | Pass | [quality review](cross-cutting.md) | no provider execution, consuming-product review, unsafe proof, power result, or native-performance evidence exists |
| Assertions/cases | Pass | [traceability](traceability.md), [conformance](conformance.md) | model/cases are specified but not executed |
| Benchmark scenarios | Pass | [scenario mapping](traceability.md#benchmark-scenario-mapping), [benchmarks](benchmarks.md) | no native baseline, run, numeric budget, regression conclusion, power, fairness, or performance claim exists |
| Ownership/trial bounds | Qualified | [ownership](ownership.md), [trial governance](../../05-governance/implementation-trials/README.md) | role ownership exists; named people, independent signoffs, provider artifacts, and disposable environments are absent |

## Decision boundary

The generated scorecard may report planning eligibility. Async I/O remains Draft until an accepted record binds named accountable people, independent reviewers, exact framework/provider/runtime/operation/resource/consumer scope, exclusions, findings/waivers, decision date, and permitted trial constraints. A valid repository standards profile and separately accepted trial record remain required before code.

**RM-ASYNC-PROMOTION-0001:** Eligibility MUST NOT change maturity, create a universal capability API, select native engines/runtimes, resolve product policy, or authorize implementation without an explicit accepted decision.

**RM-ASYNC-PROMOTION-0002:** Promotion MUST bind exact operation, lifecycle, strategy, cancellation, lifetime, registration, load/fairness, wake/runtime, shutdown, observability, platform, resource, and consuming-domain claims.

**RM-ASYNC-PROMOTION-0003:** Planned models/cases/scenarios MUST NOT be represented as passing portability, security, accessibility, native-performance, power, fairness, cancellation, resource-safety, shutdown, or recovery evidence.
