# Knowledge ownership and trial readiness

| Field | Value |
|---|---|
| Review status | Unknown |
| Reviewed | 2026-08-10 |
| Accountable owner | David Bailey ([@baileyrd](https://github.com/baileyrd)) |
| Architecture reviewer | David Bailey ([@baileyrd](https://github.com/baileyrd)) — same person as accountable owner; see independence note below |
| Security reviewer | David Bailey ([@baileyrd](https://github.com/baileyrd)) — same person as accountable owner; see independence note below |
| Evidence reviewer | David Bailey ([@baileyrd](https://github.com/baileyrd)) — same person as accountable owner; see independence note below |
| Compatibility authority | Foundation architecture review until a dedicated compatibility council exists |

**Independence note, per [RM-TRIAL-REVIEW-0002](../../05-governance/implementation-trials/review-checklist.md) and [RFC-0004](../../rfc/0004-solo-maintainer-review-sufficiency.md):** one person filling every reviewer role is a disclosed independence limitation. Per RFC-0004's solo-maintainer mode, this satisfies the independent-reviewer expectation for every gate this document feeds — including accepting Experimental promotion and authorizing TRIAL-0003 — without a separate scoped waiver. It does not itself perform the architecture, security, or evidence review each role is responsible for, and does not change this document's Review status from Unknown: solo-maintainer mode resolves *who* may review, not *whether the review has happened*. RFC-0004 reactivates the independence requirement automatically, with no calendar expiry, the moment a second distinct person is named for any reviewer role. (This note previously cited a domain-scoped [reviewer-independence waiver](reviewer-independence-waiver.md), now superseded by RFC-0004.)

## Ownership duties

The domain owner maintains the layered-authority model, conflict-registry semantics, multi-domain-hosting requirement, and the query-surface mapping in [model.md](model.md), and is accountable for keeping [RFC-0003](../../rfc/0003-rusty-knowledge-domain-framework.md), [ADR-0164](../../adr/0164-rusty-knowledge-is-a-domain-framework.md), and [ADR-0165](../../adr/0165-knowledge-layered-authority-carries-over-as-a-requirement.md) consistent with this domain's documents as they evolve. The owner does not own the `search`, `persistence`, `networking`/`ipc`, `security`, or `observability` capability contracts this framework composes — those remain each capability's own owner's responsibility, per [ADR-0164](../../adr/0164-rusty-knowledge-is-a-domain-framework.md)'s placement decision. Actual promotion and trial records must name accountable people, exact environments, and reviewer-independence limitations before this review can resolve past Unknown.

## Bounded trial plan

[TRIAL-0003](../../05-governance/implementation-trials/rusty-knowledge-trial-proposal.md) proposes the bounded trial: re-implement `baileyrd/knowledge-mcp`'s 15 MCP tools and layered-authority/conflict-registry semantics in Rust, in [`rusty-mill/rusty_knowledge`](https://github.com/Rusty-Mill/rusty_knowledge), using the [foundation trial template](../../05-governance/implementation-trials/trial-template.md). The proposal is entry-reviewed and **not authorized**: the Subject gate fails on its own (this domain remains Draft, no accepted Experimental decision); Repository is Qualified (`rusty_knowledge` has a bootstrap commit — license, README, Draft standards profile — but the profile is Draft, not Accepted). Named people are no longer a blocker (RFC-0004's solo-maintainer mode); Cross-cutting and Bounds remain Unknown because their substantive content (assessed dimensions, selected time/effort limits) doesn't exist yet, independent of who reviews it.

The trial, once any future revision is authorized, would use a fixed comparison corpus derived from `knowledge-mcp`'s existing test fixtures and UAF 1.3 domain content, read-only comparison against the cited `knowledge-mcp` commit, no production data, and no release publication. It does not select public Rust APIs, crates/workspaces, storage engine, vector-search extension, MCP transport crate, or repository topology — those remain trial-authorization inputs, not decided here.

Stop conditions include: any commit to `rusty_knowledge` before authorization; silent flattening of the layered-authority model or dropping of the conflict registry; loss of multi-domain hosting; any claim that this ownership document or TRIAL-0003's proposal existing authorizes implementation; material drift in the cited `knowledge-mcp` commit without re-review; and any attempt to resolve this domain's promotion-review gate on the strength of RFC-0003's acceptance alone.

**RM-KNOWLEDGE-OWNER-0001:** Promotion and trial records for `knowledge` MUST name accountable people, exact `knowledge-mcp` and `rusty_knowledge` generations, reviewer independence, and unresolved limitations before authorization.

**RM-KNOWLEDGE-OWNER-0002:** Trial hypotheses MUST distinguish authority-layer labeling, conflict-registry recording, multi-domain isolation, and retrieval-mode discoverability as separate claims, per [model.md](model.md)'s draft requirements.

**RM-KNOWLEDGE-OWNER-0003:** This bounded plan is evidence only and MUST NOT authorize implementation, a first commit to `rusty_knowledge`, dependency selection, or release.

**RM-KNOWLEDGE-OWNER-0004:** Closeout MUST retain negative evidence, account for which hypotheses remain unresolved, and prevent trial artifacts from entering a release before a separate promotion decision accepts them.
