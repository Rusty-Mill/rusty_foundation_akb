# Knowledge domain reviewer-independence waiver

**Superseded by [RFC-0004](../../rfc/0004-solo-maintainer-review-sufficiency.md).** RFC-0004 generalizes this waiver's rationale into a standing, project-wide rule and removes the need for a scoped per-decision waiver. This record is retained for history; do not renew it or treat its expiry date below as live — `ownership.md`, `cross-cutting.md`, `promotion-review.md`, and TRIAL-0003 now cite RFC-0004 directly.

Governed exception record per [RM-DEV-EXC-0001](../../05-governance/software-development/exceptions-evolution.md), addressing the single-reviewer independence gap disclosed in [ownership.md](ownership.md), [cross-cutting.md](cross-cutting.md), [promotion-review.md](promotion-review.md), and [TRIAL-0003](../../05-governance/implementation-trials/rusty-knowledge-trial-proposal.md).

| Field | Value |
|---|---|
| Rule(s) affected | The independent-reviewer expectation underlying `ownership.md`'s Architecture/Security/Evidence reviewer roles, `cross-cutting.md`'s per-dimension review, and [RM-TRIAL-REVIEW-0002](../../05-governance/implementation-trials/review-checklist.md)'s independence-disclosure requirement |
| Exact scope | `knowledge` domain documentation review only: authoring and self-assessing `promotion-review.md`, `cross-cutting.md`, and `ownership.md` while the domain remains `Draft domain analysis`. **Does not** cover accepting an Experimental promotion decision for `knowledge`, and **does not** cover authorizing TRIAL-0003 or any successor trial — both remain excluded by this waiver's own terms, regardless of reviewer-independence status |
| Rationale | This is presently a solo-maintainer effort (David Bailey / @baileyrd). Requiring a second, independent reviewer before even Draft-stage domain documentation can be authored would block all progress on a domain framework that RFC-0003 already gave an explicit forcing function to pursue. Disclosed self-review is preferable to an indefinite stall or to silently pretending independence exists |
| Alternatives considered | (1) Block all `knowledge` documentation until a second maintainer joins — rejected, indefinite and disproportionate for Draft-stage authoring work; (2) recruit an external volunteer reviewer for this domain specifically — not currently available; (3) accept disclosed self-review for documentation only, with authorization-stage gates explicitly excluded — chosen |
| Risk | Security- and evidence-relevant judgments (the layered-authority threat model, the `RK-001`–`RK-005` hypothesis design, benchmark/conformance planning) are not independently checked at the documentation stage; author blind spots or motivated framing are not caught by a second perspective |
| Compensating controls / evidence | Hypotheses in TRIAL-0003 are written falsifiably with explicit supporting/refuting/inconclusive conditions, so errors are detectable later even without a second reviewer now. The conjunctive gate model is unaffected: Subject, Repository, and Bounds remain Fail/Unknown for reasons independent of this waiver. This waiver does not, by itself, move TRIAL-0003 any closer to Authorized or `knowledge` any closer to Accepted |
| Owner | David Bailey ([@baileyrd](https://github.com/baileyrd)) |
| Approver | David Bailey ([@baileyrd](https://github.com/baileyrd)) — **self-approved**; this waiver is itself not independently reviewed, which is the same disclosed limitation it exists to name, not a hidden one |
| Issue | None tracked; this repository has no linked issue tracker for domain-scoped exceptions at this time |
| Start | 2026-08-10 |
| Expiry / trigger | Whichever occurs first: (a) a proposal to accept Experimental promotion for `knowledge` is opened — that decision requires independent review under its own terms and cannot cite this waiver; (b) a proposal to authorize TRIAL-0003 or a successor trial is opened — same; (c) 2027-02-06 (180 days from Start), matching this repository's usual review-expiry convention |
| Closure condition | An independent reviewer (not David Bailey) is named for at least the Security and Evidence roles in `ownership.md`, **or** this waiver is explicitly renewed with fresh rationale before its expiry/trigger |
| Affected release/authority claims | None. This waiver grants no implementation authority, no trial authorization, and no promotion decision. It permits Draft-stage documentation review to proceed under disclosed single-reviewer conditions only |

**RM-KNOWLEDGE-WAIVER-0001:** This waiver covers `knowledge` domain documentation review only and MUST NOT be cited as satisfying TRIAL-0003's entry gates or any future Experimental promotion decision's independent-review requirement.

**RM-KNOWLEDGE-WAIVER-0002:** This waiver expires per its stated trigger; an expired or revoked waiver reinstates the independence finding as an open blocker, per [RM-DEV-EXC-0004](../../05-governance/software-development/exceptions-evolution.md).

**RM-KNOWLEDGE-WAIVER-0003:** Self-approval of this waiver by its own owner is a disclosed limitation; a future independent reviewer reviewing `knowledge`'s promotion path should treat this waiver's own validity, not only the domain's technical content, as open for re-examination.
