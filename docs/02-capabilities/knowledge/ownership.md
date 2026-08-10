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

**Independence note, per [RM-TRIAL-REVIEW-0002](../../05-governance/implementation-trials/review-checklist.md):** one person filling every reviewer role is a disclosed independence limitation, not a resolved review. Naming an accountable owner unblocks the "named people absent" finding; it does not itself perform the architecture, security, or evidence review each role is responsible for, and does not change this document's Review status from Unknown. The single-reviewer gap for **this domain's Draft-stage documentation review** is covered by the [reviewer-independence waiver](reviewer-independence-waiver.md) — but that waiver explicitly excludes accepting Experimental promotion and authorizing TRIAL-0003, both of which still need either an independent reviewer for the security and evidence roles or a separate, renewed waiver decision made at that time.

## Ownership duties

The domain owner maintains the layered-authority model, conflict-registry semantics, multi-domain-hosting requirement, and the query-surface mapping in [model.md](model.md), and is accountable for keeping [RFC-0003](../../rfc/0003-rusty-knowledge-domain-framework.md), [ADR-0164](../../adr/0164-rusty-knowledge-is-a-domain-framework.md), and [ADR-0165](../../adr/0165-knowledge-layered-authority-carries-over-as-a-requirement.md) consistent with this domain's documents as they evolve. The owner does not own the `search`, `persistence`, `networking`/`ipc`, `security`, or `observability` capability contracts this framework composes — those remain each capability's own owner's responsibility, per [ADR-0164](../../adr/0164-rusty-knowledge-is-a-domain-framework.md)'s placement decision. Actual promotion and trial records must name accountable people, exact environments, and reviewer-independence limitations before this review can resolve past Unknown.

## Bounded trial plan

[TRIAL-0003](../../05-governance/implementation-trials/rusty-knowledge-trial-proposal.md) proposes the bounded trial: re-implement `baileyrd/knowledge-mcp`'s 15 MCP tools and layered-authority/conflict-registry semantics in Rust, in [`rusty-mill/rusty_knowledge`](https://github.com/Rusty-Mill/rusty_knowledge), using the [foundation trial template](../../05-governance/implementation-trials/trial-template.md). The proposal is entry-reviewed and **not authorized**: the Subject and Repository gates both fail (this domain remains Draft; `rusty_knowledge` has no commits or standards profile), and Ownership, Cross-cutting, and Bounds are Unknown pending named people.

The trial, once any future revision is authorized, would use a fixed comparison corpus derived from `knowledge-mcp`'s existing test fixtures and UAF 1.3 domain content, read-only comparison against the cited `knowledge-mcp` commit, no production data, and no release publication. It does not select public Rust APIs, crates/workspaces, storage engine, vector-search extension, MCP transport crate, or repository topology — those remain trial-authorization inputs, not decided here.

Stop conditions include: any commit to `rusty_knowledge` before authorization; silent flattening of the layered-authority model or dropping of the conflict registry; loss of multi-domain hosting; any claim that this ownership document or TRIAL-0003's proposal existing authorizes implementation; material drift in the cited `knowledge-mcp` commit without re-review; and any attempt to resolve this domain's promotion-review gate on the strength of RFC-0003's acceptance alone.

**RM-KNOWLEDGE-OWNER-0001:** Promotion and trial records for `knowledge` MUST name accountable people, exact `knowledge-mcp` and `rusty_knowledge` generations, reviewer independence, and unresolved limitations before authorization.

**RM-KNOWLEDGE-OWNER-0002:** Trial hypotheses MUST distinguish authority-layer labeling, conflict-registry recording, multi-domain isolation, and retrieval-mode discoverability as separate claims, per [model.md](model.md)'s draft requirements.

**RM-KNOWLEDGE-OWNER-0003:** This bounded plan is evidence only and MUST NOT authorize implementation, a first commit to `rusty_knowledge`, dependency selection, or release.

**RM-KNOWLEDGE-OWNER-0004:** Closeout MUST retain negative evidence, account for which hypotheses remain unresolved, and prevent trial artifacts from entering a release before a separate promotion decision accepts them.
