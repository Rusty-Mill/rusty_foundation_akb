# Governance

The [authoritative architecture model](../01-architecture/architecture-model.md) defines the current normative architecture. ADRs preserve why it changes; RFCs propose changes; supporting documents elaborate it.

## Roles

- **Maintainers:** steward repositories and merge changes within accepted architecture.
- **Capability owners:** maintain domain contracts, dependency graphs, and verification evidence.
- **Architecture review:** evaluates cross-domain boundaries, stable contracts, and ecosystem-wide decisions.
- **Security reviewers:** approve changes to authority, isolation, unsafe boundaries, cryptography, and supply chain.
- **Release stewards:** verify gates, provenance, compatibility, and publication.

One person may hold several roles initially. Decisions and evidence remain public in the repository so governance can scale beyond its founders.

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
