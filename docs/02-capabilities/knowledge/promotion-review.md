# Knowledge Experimental promotion review

| Field | Value |
|---|---|
| Status | Proposed; no maturity change |
| Subject | Knowledge domain framework, Draft domain analysis; `rm.knowledge.*` has no accepted capability contract |
| Architecture | Model 1.99.0 |
| Proposed decision | Not yet eligible for Experimental promotion; remain Draft pending the substantive gates below (reviewer independence is resolved by RFC-0004, not a remaining blocker) |
| Implementation authority | None |

## Gate assessment

| Gate | State | Exact evidence | Qualification |
|---|---|---|---|
| Contract semantics | Qualified | [model.md](model.md)'s draft requirements RM-KNOWLEDGE-MODEL-0001–0005, [RFC-0003](../../rfc/0003-rusty-knowledge-domain-framework.md), [ADR-0164](../../adr/0164-rusty-knowledge-is-a-domain-framework.md), [ADR-0165](../../adr/0165-knowledge-layered-authority-carries-over-as-a-requirement.md) | Requirements are derived entirely from one external Python implementation and have not been exercised as a Rust vertical slice; no `rm.knowledge.*` capability contract is accepted |
| Dependencies/profile impact | Fail | none | No composition register (`dependencies.md`) exists naming exact `requires`/`optionally-uses` edges into `search`, `persistence`, `networking`/`ipc`, `security`, `observability`; no profile references `knowledge` |
| Platform research | Fail | [platform-research.md](platform-research.md) | Document explicitly states "No research has been executed against real Rust crates yet"; every platform-variance cell is marked Unevaluated in [TRIAL-0003](../../05-governance/implementation-trials/rusty-knowledge-trial-proposal.md) |
| Cross-cutting planning | Qualified | [cross-cutting.md](cross-cutting.md) | Review status Unknown; dimensions are planned, not yet assessed; accountable owner is named (David Bailey, [@baileyrd](https://github.com/baileyrd)), and per [RFC-0004](../../rfc/0004-solo-maintainer-review-sufficiency.md) being the sole reviewer no longer blocks this gate on independence grounds — the assessment itself still needs to happen |
| Assertions/cases | Fail | [conformance.md](conformance.md) | Test classes are proposed, not implemented; no `traceability.md` exists mapping requirements to executed assertions |
| Benchmark scenarios | Fail | [benchmarks.md](benchmarks.md) | Document explicitly states "No benchmarks have been run"; no regression budget exists |
| Ownership/trial bounds | Qualified | [ownership.md](ownership.md), [TRIAL-0003](../../05-governance/implementation-trials/rusty-knowledge-trial-proposal.md) | Review status Unknown; every reviewer role is named (David Bailey, [@baileyrd](https://github.com/baileyrd)); RFC-0004's solo-maintainer mode resolves the independence question, but TRIAL-0003's entry review is still Not authorized for its own reasons (Subject and Repository gates Fail) |

## Decision boundary

`knowledge` is not eligible for Experimental promotion. Unlike a domain approaching promotion eligibility (compare [filesystem](../filesystem/promotion-review.md), whose planning gates are mostly Pass after a completed platform-research and cross-cutting pass), `knowledge` currently fails three of seven gates outright (dependencies/profile impact, platform research, assertions/cases, benchmark scenarios — four, not three) and qualifies the remaining three only because the required documents now exist, not because their content has been reviewed to a decision. An accountable owner (David Bailey, [@baileyrd](https://github.com/baileyrd)) is now named, resolving the "no named person" finding, and per [RFC-0004](../../rfc/0004-solo-maintainer-review-sufficiency.md)'s solo-maintainer mode, that same person holding every reviewer role now satisfies this project's independence expectation for every gate, including accepting Experimental promotion — no separate waiver needed. What still blocks advancing past Draft is unrelated to reviewer independence: a composition register binding exact graph edges into `search`/`persistence`/`networking`/`security`/`observability`; real platform/crate research replacing every "Unevaluated" cell; an executed (not merely planned) conformance comparison against `knowledge-mcp`; the cross-cutting dimensions actually being assessed, not just planned; and TRIAL-0003 reaching an authorized state or a documented reason it need not.

**RM-KNOWLEDGE-PROMOTION-0001:** This review MUST NOT change `knowledge`'s maturity, select a storage/vector-search/transport crate, or authorize implementation without a separate accepted decision naming exact people, generations, and evidence.

**RM-KNOWLEDGE-PROMOTION-0002:** Promotion MUST bind exact authority-layer, conflict-registry, multi-domain-isolation, and retrieval-mode claims from [model.md](model.md); omitted claims remain unsupported or unknown, not assumed to hold.

**RM-KNOWLEDGE-PROMOTION-0003:** Existence of this promotion-review, cross-cutting, or ownership document MUST NOT be represented as satisfying TRIAL-0003's Subject or Repository gates; those require an accepted Experimental decision and a `rusty_knowledge` standards profile respectively, neither of which this record creates.

**RM-KNOWLEDGE-PROMOTION-0004:** Per [RFC-0004](../../rfc/0004-solo-maintainer-review-sufficiency.md), a single accountable reviewer satisfies this review's independence expectation while solo-maintainer mode is active; this does not substitute for the substantive content each gate above still requires.
