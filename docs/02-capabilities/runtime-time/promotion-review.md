# Runtime and time Experimental promotion review

| Field | Value |
|---|---|
| Status | Proposed; no maturity change |
| Subject | Runtime/time domain 0.2.0: three capability contracts at 0.1.0 plus orderly-shutdown service 0.1.0 |
| Architecture | Model 1.80.0 |
| Proposed decision | Eligible for explicit Experimental promotion review; remain Draft pending disposition |
| Implementation authority | None |

## Gate assessment

| Gate | State | Exact evidence | Qualification |
|---|---|---|---|
| Contract semantics | Pass | [clock](monotonic-clock.md), [deadline](deadline-timer.md), [cancellation](cancellation.md), [shutdown](shutdown.md) | Open questions may narrow trial scope; none silently changes current semantics |
| Dependencies/profile impact | Pass | [domain graph](README.md#candidate-model), [source-linked graph](../../04-ecosystem/consistency-readiness/dependency-graph.md), candidate profile declarations | Profile resolution remains trial evidence rather than a current release claim |
| Platform research | Pass | [platform research](platform-research.md), [source review](source-review.md) | Exact OS/SDK/provider frontier belongs in a trial record |
| Cross-cutting planning | Pass | [quality review](cross-cutting.md) | Implementation evidence does not yet exist |
| Assertions/cases | Pass | [traceability](traceability.md), [conformance](conformance.md) | Planned cases, not passing provider results |
| Benchmark scenarios | Pass | [traceability](traceability.md#benchmark-scenario-mapping), [benchmarks](benchmarks.md) | Planned scenarios; numeric budgets deferred to measurements |
| Ownership/trial bounds | Qualified | [ownership](ownership.md), [trial governance](../../05-governance/implementation-trials/README.md) | Accountable roles exist; named people and independent signoffs are absent |

## Open-question disposition for review

- RT-Q001/Q002/Q004/Q007/Q008/Q009/Q010 affect trial matrix, hypotheses, or limits and may remain open only if the promoted subject records their constraints.
- RT-Q003 periodic timers is outside the one-shot deadline contract and does not block that subject.
- RT-Q005 cancellation callbacks affects the optional callback surface; a promotion may exclude that surface or require an explicit decision.
- RT-Q006 is closed by ADR-0005.

## Decision boundary

Generated evidence says the domain satisfies the machine-checkable eligibility model. The governance decision remains Proposed because named accountable people, reviewer independence, exact promoted scope, open-question qualifications, decision date, and accepted trial constraints have not been recorded. No repository profile or trial authorization exists.

**RM-RUNTIME-PROMOTION-0001:** Eligibility evidence MUST NOT change the subject's Draft status or authorize implementation without an explicit accepted promotion decision.

**RM-RUNTIME-PROMOTION-0002:** The accepted decision MUST bind named accountable people, exact subject/generations, gate evidence, open-question dispositions, findings/waivers, reviewer independence, date, and permitted trial constraints.

**RM-RUNTIME-PROMOTION-0003:** Promotion MAY narrow the subject, platform matrix, optional surfaces, or claims; it MUST NOT mark excluded or unknown evidence as pass.

