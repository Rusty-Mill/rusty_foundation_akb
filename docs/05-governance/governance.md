# Governance

The [authoritative architecture model](../01-architecture/architecture-model.md) defines the current normative architecture. ADRs preserve why it changes; RFCs propose changes; supporting documents elaborate it.

## Roles

- **Maintainers:** steward repositories and merge changes within accepted architecture.
- **Capability owners:** maintain domain contracts, dependency graphs, and verification evidence.
- **Architecture review:** evaluates cross-domain boundaries, stable contracts, and ecosystem-wide decisions.
- **Security reviewers:** approve changes to authority, isolation, unsafe boundaries, cryptography, and supply chain.
- **Release stewards:** verify gates, provenance, compatibility, and publication.

One person may hold several roles initially. Decisions and evidence remain public in the repository so governance can scale beyond its founders.

**Solo-maintainer mode**, per [RFC-0004](../rfc/0004-solo-maintainer-review-sufficiency.md): while a role or repository has exactly one accountable person, that person's own disclosed self-review satisfies this project's reviewer-independence expectations for every gate — including implementation-trial authorization and promotion-review decisions — without a separate per-decision waiver. This does not reduce what any gate substantively requires; it removes only the requirement that a second person perform the review. It reactivates automatically, with no calendar expiry, the moment a second distinct person is named for any reviewer role.

## ADRs

Use an ADR for a durable choice with meaningful alternatives or consequences. Accepted ADRs are immutable except for status and links; a new ADR supersedes an old one.

## RFCs

Use an RFC for new stable capabilities, public contracts, cross-repository changes, governance policy, compatibility changes, or significant delivery mechanisms. RFCs include an explicit review period, disposition, and unresolved questions.

## Decision principles

- Prefer evidence and explicit trade-offs.
- Seek consensus; record dissent and the deciding authority when consensus is impossible.
- Experimental work may proceed behind unstable boundaries, but cannot establish stable precedent silently.
- Security or conformance blockers prevent stable promotion.

## Change control

Every normative document names its status and owner. Pull requests link affected contracts, ADRs/RFCs, profiles, tests, benchmarks, and migration notes. Scheduled reviews identify stale or contradictory guidance.

When architecture changes, the accepted decision and the authoritative model are updated together. A draft or lower-level document cannot override the model implicitly.

## Software development governance

The [foundation software development standards](software-development/README.md) govern implementation entry, Rust/API/unsafe practices, testing, performance, cross-cutting qualities, dependencies, review/CI, releases, and exceptions. Domain promotion and an applicable repository standards profile are separate conjunctive gates; neither can substitute for the other.

The [implementation trial governance model](implementation-trials/README.md) adds the third gate: exact authorization for bounded learning. Trial code and results are evidence, not precedent; material input drift suspends affected authorization until re-review.
