# ADR-0164: Rusty Knowledge is a domain framework, not a base capability

**Status:** Proposed  
**Date:** 2026-08-10  
**Deciders:** Rusty Mill maintainers

## Context

`baileyrd/knowledge-mcp` is a working Python MCP server that answers structured domain-knowledge queries (constructs, rules, relationships, cross-domain traceability, conflicts) over a layered authority model, backed by SQLite with hybrid lexical and vector retrieval. [RFC-0003](../rfc/0003-rusty-knowledge-domain-framework.md) proposes rebranding a Rust reimplementation as "Rusty Knowledge" and needs a placement in the architecture pyramid before any capability specification or trial work begins. Treating it as a single new base capability under `docs/02-capabilities` would conflate several independently evolvable concerns — retrieval, storage, transport, authentication — behind one contract, the same failure mode [ADR-0019](0019-terminal-emulation-is-a-domain-framework.md) rejected for terminal emulation.

## Decision

Rusty Knowledge is a domain framework above the `search`, `persistence`, `networking`/`ipc`, `security`, and `observability` capability domains, per [section 5.9 of the architecture model](../01-architecture/architecture-model.md). It owns the application-oriented composition: per-domain namespacing, the layered authority model (Standard → Tool Implementation → Conventions → Process), the cross-layer conflict registry, and the MCP tool surface. It does not own or redefine index construction, storage durability, transport security, or diagnostics — those remain the responsibility of the capabilities it composes.

The capability-graph domain identifier is `knowledge` (`rm.knowledge.*`), distinct from the product/crate name "Rusty Knowledge," following the existing convention that a domain framework's identifier need not match its product branding (compare the `terminal` domain and its host-framework document).

## Options considered

### One `rusty-knowledge` base capability

Rejected. It would push retrieval ranking, storage durability, and transport authentication policy into one contract, preventing each from evolving, being benchmarked, or being backend-substituted independently, and would duplicate work already scoped to `search` and `persistence`.

### Multiple independent base capabilities (construct-store, retrieval, authority-resolution) with no unifying framework

Rejected for now. Splitting immediately, before any Rust evidence exists, risks freezing boundaries the Python implementation has not yet proven are independently useful. A domain framework can compose existing capabilities today and be decomposed into new base capabilities later if evidence shows a piece is independently selectable, securable, and testable on its own — this ADR does not foreclose that.

### Application-layer product with no architecture-model placement

Rejected. Leaving a running, relied-upon knowledge server outside the architecture model means its authority semantics (which layer wins a conflict) are accountable to nothing, which is the exact gap RFC-0003 exists to close.

## Consequences

- A `knowledge` domain-analysis and capability-template pass (per the [domain-analysis method](../02-capabilities/domain-analysis.md)) becomes a future, separate contribution rather than something this ADR or RFC-0003 completes now.
- The implementation trial authorized by RFC-0003 must show its composition of `search`, `persistence`, and transport capabilities explicitly rather than reinventing retrieval or storage semantics inside [`rusty_knowledge`](https://github.com/Rusty-Mill/rusty_knowledge).
- Future promotion review for `knowledge` will need framework-level evidence (the composition holds together) in addition to whatever base-capability contracts eventually get carved out of it.

## Verification

Reviewed against RFC-0003's disposition when it closes. The placement is re-examined if the implementation trial shows the composition cannot cleanly sit above `search`/`persistence` as designed (for example, if hybrid retrieval requires storage-engine-specific behavior that `search` cannot express as a portable contract).

## Follow-up

- [ ] Add `knowledge` to `docs/02-capabilities/taxonomy.md` as a domain-framework entry — done alongside this ADR.
- [ ] Open the implementation trial record once RFC-0003 is accepted.
- [ ] Revisit this placement after the trial reports evidence.
