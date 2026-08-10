# RFC-0004: Solo-maintainer review sufficiency

**Status:** Accepted  
**Authors:** David Bailey ([@baileyrd](https://github.com/baileyrd))  
**Reviewers:** None independent of the author — see Disposition  
**Created:** 2026-08-10

## Summary

Generalize `governance.md`'s existing "one person may hold several roles initially" allowance from a role-holding permission into an explicit sufficiency rule: while a role or repository has exactly one accountable person, that person's own disclosed self-review satisfies this project's reviewer-independence expectations for every gate — including [RM-TRIAL-REVIEW-0002/0003](../05-governance/implementation-trials/review-checklist.md), [entry-gates.md](../05-governance/implementation-trials/entry-gates.md)'s Ownership gate, and any promotion-review's Ownership/trial-bounds gate. This removes the need for a fresh, scoped waiver (the pattern [filesystem's FS-EXP-W001](../02-capabilities/filesystem/promotion-review.md) and the `knowledge` domain's [reviewer-independence-waiver.md](../02-capabilities/knowledge/reviewer-independence-waiver.md) both used) every time independence would otherwise block a gate, since the underlying fact — one maintainer — does not change decision to decision.

## Motivation

Two independent decisions (filesystem's Experimental promotion, and the `knowledge` domain's Draft-stage documentation review) each separately negotiated a scoped waiver to say the same true thing: this is presently a one-person project. Re-litigating that fact per decision is friction without added safety — the risk (no second perspective) is identical every time, and repeating the negotiation does not reduce it. A single durable rule, stated once and disclosed everywhere it applies, is more honest than a growing pile of near-identical waivers.

## Goals and non-goals

### Goals

- State the self-review-sufficiency rule once, project-wide, covering every gate that currently expects an independent reviewer — including trial authorization and promotion acceptance, not only documentation-stage review.
- Define an exact, checkable reactivation trigger: independence requirements reactivate the moment a second distinct person is named for any reviewer role anywhere that role structure applies. No calendar expiry — this is a standing condition tied to project staffing, not a deadline to renew.
- Preserve the disclosure duty. Self-review remains disclosed, not hidden; this RFC removes the *requirement* for a second reviewer, not the *duty to say* there isn't one.
- Retire the per-decision waiver pattern going forward; existing waivers granted under it are superseded by this RFC, not deleted.

### Non-goals

- This RFC does not waive non-waivable gates under [RM-DEV-EXC-0003](../05-governance/software-development/exceptions-evolution.md): law/license, undeclared safety invariants, secret handling, release identity/provenance, or truthful evidence. Self-review still cannot fabricate conformance results, skip benchmark execution, or assert content that hasn't actually been produced.
- This RFC does not reduce what any gate substantively requires (a composition register still needs to exist, a benchmark still needs to run); it removes only the requirement that a second person be the one to review it.
- This RFC does not retroactively re-decide filesystem's Experimental promotion or any other closed decision; it changes the rule for gates still open or opened after acceptance.

## Proposed design

1. Amend `governance.md`'s "One person may hold several roles initially" sentence to state the sufficiency rule explicitly (see companion edit in this same change).
2. Add `RM-TRIAL-REVIEW-0004` to `review-checklist.md`: while solo-maintainer mode is active, a gate's independent-reviewer expectation is satisfied by the sole accountable person's own disclosed self-review; `RM-TRIAL-REVIEW-0002`'s disclosure duty still applies without exception.
3. Add a note to `entry-gates.md`'s Ownership row: satisfied by one person, disclosed as such, while solo-maintainer mode is active.
4. Mark `FS-EXP-W001` and the `knowledge` domain's `reviewer-independence-waiver.md` as superseded by this RFC, retained for history rather than deleted.
5. `TRIAL-0003`'s gate table is updated in this same change to reflect that independence is no longer a distinct blocker for the Ownership, Cross-cutting, and Verification gates — those gates remain Unknown/Qualified for their own substantive reasons (content not yet produced), which this RFC does not manufacture.

## Behavioral contract impact

None. This is governance process only; no capability contract, architecture layer, or platform behavior changes.

## Capability graph and profile impact

None.

## Platform behavior and variance

Not applicable.

## Security, performance, accessibility, i18n, and observability

Security is the dimension most affected in spirit: single-person review of security-relevant design decisions has no adversarial check. This RFC does not pretend otherwise — it accepts that risk explicitly as the cost of a one-person project continuing to make any progress, and mitigates it only by keeping the disclosure duty intact (a future reader always sees "reviewed by the same person who authored it," never a false appearance of independence) and by leaving the conjunctive gate model itself untouched (missing substantive evidence still blocks, regardless of who's reviewing).

## Compatibility, versioning, packaging, and migration

Not applicable to existing closed decisions (see non-goals). Open or future gate reviews apply this rule immediately upon acceptance.

## Conformance and benchmarks

Not applicable; this RFC does not itself introduce a capability requirement.

## Alternatives considered

### Keep the per-decision waiver pattern

Rejected. `FS-EXP-W001` and the `knowledge` waiver each separately reproduced the same rationale, alternatives, and risk analysis for the same static fact. A standing rule says it once.

### Calendar-based expiry (e.g., revisit in 6 or 12 months)

Rejected, per explicit maintainer direction: a fixed date measures elapsed time, not whether the project has actually grown a second reviewer. The reactivation trigger is the fact that matters — a named second person — not a date that may arrive before or long after that fact.

### Remove the independence concept entirely, including disclosure

Rejected. Disclosure costs nothing and preserves an honest record for whoever reads this later, including a future second maintainer evaluating what was and wasn't independently checked.

## Drawbacks and risks

- No adversarial check exists on any single-person review while this mode is active, project-wide.
- A future reader could mistake "solo-maintainer mode" for a general license to skip review rigor rather than specifically the independence requirement; the disclosure duty and the unchanged conjunctive gate model are the guardrails against that reading.
- Retiring the waiver pattern removes a forcing function that made someone write out the rationale each time; this RFC's own text is the one-time version of that rationale and should be revisited if circumstances change materially (not just staffing).

## Unresolved questions

- None specific to this RFC; it resolves the question it was written to resolve. Whether solo-maintainer mode should have any qualitative floor (e.g., certain security-critical gates always require a second reviewer regardless of staffing) is not addressed here and is left for a future RFC if it becomes a live concern.

## Rollout and lifecycle

Effective immediately upon acceptance. `FS-EXP-W001` and `docs/02-capabilities/knowledge/reviewer-independence-waiver.md` are marked superseded in this same change, pointing here, and retained for history. `TRIAL-0003` and the `knowledge` domain's `ownership.md`, `cross-cutting.md`, and `promotion-review.md` are updated in this same change to cite this RFC instead of the narrower waiver. Reactivation is automatic and requires no further RFC: the moment a second distinct person is named for any reviewer role, that role's independence requirement resumes for future decisions.

## Disposition

**Accepted**, self-decided by the sole accountable maintainer (David Bailey, [@baileyrd](https://github.com/baileyrd)) — which is itself the exact condition this RFC exists to make explicit rather than obscure. There is no independent reviewer for this RFC; that fact is disclosed here rather than left implicit, consistent with the disclosure duty this RFC preserves for every future gate it applies to.
