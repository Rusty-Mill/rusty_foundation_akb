# IPC byte-pipe Experimental promotion review

| Field | Value |
|---|---|
| Status | Proposed; no maturity change |
| Subject | IPC foundations 0.1.1; anonymous byte-pipe contract 0.1.x |
| Architecture | Model 1.86.0 |
| Proposed decision | Eligible for explicit Experimental promotion review; remain Draft pending disposition |
| Implementation authority | None |

## Gate assessment

| Gate | State | Exact evidence | Qualification |
|---|---|---|---|
| Contract semantics | Pass | [byte-pipe](byte-pipe.md), [domain boundary](README.md) | named/duplex/message IPC, framing, terminals, authentication, handle passing, shared memory, and remote transport remain outside scope |
| Dependencies/profile impact | Pass | [composition register](dependencies.md), [CLI](../profiles/foundation-cli.md), [server](../profiles/foundation-server.md), [headless](../profiles/foundation-headless.md), [process composition](../process/dependencies.md) | optional cancellation/process edges and Q-level policies are explicit; runtime/provider selection remains open |
| Platform research | Pass | [platform research](platform-research.md), [source review](source-review.md) | exact native mechanisms, OS generations, Q-levels, signal policies, and capacity/atomicity scopes are not selected |
| Cross-cutting planning | Pass | [quality review](cross-cutting.md) | no provider execution, specialist product review, resource/signal proof, or native-performance result exists |
| Assertions/cases | Pass | [traceability](traceability.md), [conformance](conformance.md) | cases are specified but not executed |
| Benchmark scenarios | Pass | [scenario mapping](traceability.md#benchmark-scenario-mapping), [benchmarks](benchmarks.md) | no native baseline, run, numeric budget, regression conclusion, or performance claim exists |
| Ownership/trial bounds | Qualified | [ownership](ownership.md), [trial governance](../../05-governance/implementation-trials/README.md) | role ownership exists; named people, independent signoffs, artifacts, and disposable environments are absent |

## Decision boundary

The generated scorecard may report planning eligibility. IPC remains Draft until an accepted record binds named accountable people, independent reviewers, exact contract/profile/provider/runtime/process scope, Q-level, exclusions, findings/waivers, decision date, and permitted trial constraints. A valid repository standards profile and separately accepted trial record remain required before code.

**RM-IPC-PROMOTION-0001:** Eligibility MUST NOT change maturity, select native mechanisms/runtimes, resolve product policy, or authorize implementation without an explicit accepted decision.

**RM-IPC-PROMOTION-0002:** Promotion MUST bind exact endpoint, authority, inheritance, partial-progress, EOF/broken-peer, capacity/backpressure, atomicity, duplication/transfer, Q-level, cancellation, concurrency, security, platform, and profile claims.

**RM-IPC-PROMOTION-0003:** Planned cases and scenarios MUST NOT be represented as passing portability, security, accessibility, native-performance, signal containment, resource, process-integration, or recovery evidence.
