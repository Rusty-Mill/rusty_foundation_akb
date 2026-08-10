# Implementation trial governance

**Status:** Accepted foundation governance  
**Authority:** [RFC-0002](../../rfc/0002-implementation-trial-governance.md)

An implementation trial is a bounded experiment for resolving named architecture, provider, conformance, or performance uncertainty. It is not permission to start a product, establish a public API, publish a release, or treat trial structure as architectural precedent.

```mermaid
stateDiagram-v2
  [*] --> Proposed
  Proposed --> Authorized: every entry gate passes
  Proposed --> Rejected: gate fails or scope is unjustified
  Authorized --> Active: bound repository generation begins
  Active --> Paused: material input drift
  Paused --> Active: re-review authorizes new generation
  Active --> Closed: success / failure / inconclusive
  Closed --> Disposed: retention period ends
  Closed --> Proposed: follow-on trial
  Closed --> PromotionReview: ordinary promotion evidence is complete
  PromotionReview --> [*]
```

The lifecycle is defined by the [entry gates](entry-gates.md), [trial contract](trial-contract.md), [evidence plan](evidence-plan.md), [repository and CI rules](repository-and-ci.md), [native-provider matrix](native-provider-matrix.md), [change control](change-control.md), [closeout rules](closeout.md), and [review checklist](review-checklist.md). Authors start from the [trial template](trial-template.md).

The [security-foundation batch trial proposal](security-batch-trial-proposal.md) is the first full application of this governance model. It is intentionally blocked because its subjects remain Draft and its exact people, platforms, providers, repository, toolchain, limits, and approvals are unselected. Proposal completeness is not authorization.

The [rustils filesystem composed evidence trial proposal](rustils-trial-proposal.md) (`TRIAL-0002`, now revision 3) is a second application, citing an existing external repository ([`baileyrd/rustils`](https://github.com/baileyrd/rustils)) as candidate qualified input evidence. Revision 0 composed a four-domain tuple (filesystem, process, networking, security); revision 1 narrowed to filesystem alone after filesystem's own promotion review reached an accepted Experimental decision; revision 2 staffed Ownership (bootstrap, one person, independence explicitly waived) and defined Bounds; revision 3 bound Repository to rustils' now-Accepted standards profile and reviewed the Cross-cutting plan. `Learning value`, `Verification`, and `Ownership` remain `Qualified` — per RFC-0004, independence is no longer Ownership's open question, but the substantive review work still is — so the trial stays `Not authorized`. Per RFC-0002's rollout rule, an existing prototype cannot claim retroactive authorization regardless of how complete its own independent evidence is.

The [Rusty Knowledge implementation trial proposal](rusty-knowledge-trial-proposal.md) (TRIAL-0003) is a third application, entered per [RFC-0003](../../rfc/0003-rusty-knowledge-domain-framework.md) for the [`knowledge` domain framework](../../02-capabilities/knowledge/README.md) and citing `baileyrd/knowledge-mcp` as candidate qualified input evidence. It remains blocked: the `knowledge` domain remains Draft with no accepted Experimental decision (the Subject gate fails on its own), and the target repository ([`rusty-mill/rusty_knowledge`](https://github.com/Rusty-Mill/rusty_knowledge)) has a bootstrap commit and a Draft, not yet Accepted, standards profile.

**RM-TRIAL-MODEL-0001:** A trial MUST bind one exact authorization generation to named questions, scope, inputs, evidence, owners, limits, and closeout conditions.

**RM-TRIAL-MODEL-0002:** Trial work and results MUST NOT establish Stable API, production support, portability, provider preference, release eligibility, or repository topology by implication.

**RM-TRIAL-MODEL-0003:** Success, failure, and inconclusive outcomes are equally valid learning outcomes and MUST preserve their evidence and limitations.

**RM-TRIAL-MODEL-0004:** A trial MAY inform a later ADR, RFC, contract revision, or promotion review, but only those ordinary governance paths can change architecture or maturity.
