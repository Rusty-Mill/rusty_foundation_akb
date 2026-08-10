# RFC-0003: Rusty Knowledge domain framework

**Status:** Draft  
**Authors:** Rusty Mill maintainers  
**Reviewers:** Unassigned  
**Created:** 2026-08-10

## Summary

Adopt "Rusty Knowledge" as a domain framework above the search, persistence, networking, IPC, security, and observability capabilities, and authorize a bounded implementation trial that ports an existing working Python MCP server (`baileyrd/knowledge-mcp`) into Rust as evidence. This RFC does not accept a capability contract, choose a crate layout, or select final API syntax.

## Motivation

`baileyrd/knowledge-mcp` is a working, tested (119+ test functions) MCP server that answers structured domain-knowledge queries (constructs, rules, relationships, cross-domain traceability, conflicts) over a layered authority model (Standard → Tool Implementation → Conventions → Process), backed by SQLite with hybrid full-text and vector search. It is not itself an OS-capability abstraction; it is an application-oriented composition that would sit above several Rusty Mill capabilities the way [terminal emulation sits above terminal session capabilities](../adr/0019-terminal-emulation-is-a-domain-framework.md).

The foundation roadmap places domain frameworks in [Phase 5 — Ecosystem scale-out](../06-roadmap/roadmap.md), "only when explicit forcing functions appear," and the project is currently in Phase 1 (domain inventory and meta-model). This RFC treats the existing, running, evidence-backed Python implementation as that explicit forcing function: the knowledge-serving behavior already exists and is already in use, so documenting it inside a controlled framework is lower risk than leaving it undocumented and unaccountable outside the architecture model. Reviewers should treat "is this forcing function sufficient to justify an early exception" as an open question this RFC must answer, not an assumption it makes.

## Goals and non-goals

### Goals

- Give the knowledge-serving domain a stable place in the architecture pyramid and capability graph before any Rust code is authorized.
- Preserve the proven parts of the Python design (layered authority model, per-domain namespacing, hybrid FTS + vector retrieval, conflict registry) as portable semantic requirements, independent of SQLite or Python-specific implementation.
- Name the rebrand: the delivered software is "Rusty Knowledge" (crate family `rusty-knowledge`); the capability-graph domain identifier is `knowledge` (`rm.knowledge.<capability>`), consistent with existing single-word domain identifiers (`search`, `caching`).
- Scope an implementation trial, in a **new, separate repository**, that re-implements the Python server's behavior in Rust and reports back as evidence.

### Non-goals

- Define Rust traits, types, or a crate/workspace layout.
- Choose a storage engine, embedding backend, or MCP transport crate.
- Accept any individual capability contract under the `knowledge` domain.
- Migrate or deprecate the existing Python `knowledge-mcp` server; it keeps running until the trial produces comparable evidence and a separate promotion decision retires it.

## Proposed design

1. Add `knowledge` to the initial capability taxonomy as a domain-framework entry (not a base OS capability): construct/rule/relationship modeling, layered authority resolution, hybrid lexical+vector retrieval, cross-domain traceability, and conflict registries.
2. The `knowledge` domain framework composes, and does not redefine, the following existing capability domains:
   - `search` — index build/query, hybrid lexical/vector retrieval, ranking, pagination (the Python server's FTS5 + `sqlite-vec` + RRF fusion is domain-specific policy over this capability, not a new retrieval primitive).
   - `persistence` — the durable store for domains, constructs, rules, relationships, and the conflict registry.
   - `networking` / `ipc` — the MCP transport surface (currently Streamable HTTP over ASGI in Python; transport choice is deferred to the trial).
   - `security` — bearer-token authentication and rate limiting at the transport boundary.
   - `observability` — request/tool-call diagnostics.
3. A capability specification for `rm.knowledge.*` is out of scope for this RFC; domain analysis and a capability template pass follow the [domain-analysis method](../02-capabilities/domain-analysis.md) as a separate contribution once the trial reports.
4. Authorize one bounded [implementation trial](../05-governance/implementation-trials/README.md), per RFC-0002, whose subject is: re-implement the 15 MCP tools and layered-authority/conflict-registry semantics of `baileyrd/knowledge-mcp` in Rust, in a new repository, without changing observable tool behavior. The trial is evidence; it does not itself authorize a release or retire the Python server.

## Behavioral contract impact

None. No `knowledge` capability contract is accepted by this RFC.

## Capability graph and profile impact

Adds `knowledge` as a domain-framework node above `search`, `persistence`, `networking`/`ipc`, `security`, and `observability`. No existing capability's contract changes. No profile currently requires `knowledge`.

## Platform behavior and variance

The Python implementation is already platform-uniform (SQLite embeds identically on Windows/Linux/macOS; no OS-specific mechanism is involved). The trial should confirm this holds for the chosen Rust storage and vector-search crates and record any variance.

## Security, performance, accessibility, i18n, and observability

- Security: the layered authority model and conflict registry are integrity-relevant (they determine which answer Claude receives as authoritative); the trial must preserve them exactly, not just the query surface.
- Performance: the trial's benchmark plan compares Rust rebuild/query latency against the existing Python server's measured behavior as its native baseline, per [RFC-0002](0002-implementation-trial-governance.md).
- Accessibility/i18n: not applicable at the protocol layer; deferred to any future consumer surface.
- Observability: the trial preserves the existing per-tool-call diagnostics as a minimum, not a stretch goal.

## Compatibility, versioning, packaging, and migration

The Python `knowledge-mcp` server (`v0.1.0`) remains authoritative and running for the duration of the trial. No migration is authorized by this RFC. Domain content already ingested (UAF 1.3; `data_mesh`/`udra` stubs) is trial input evidence, not a contract this RFC freezes.

## Conformance and benchmarks

Deferred to the trial record per RFC-0002: the trial's entry review must state falsifiable questions (does the Rust reimplementation produce byte-for-byte-equivalent tool responses for a fixed corpus and query set?) and bind them to executable comparison cases before code is authorized.

## Alternatives considered

### Treat Rusty Knowledge as a base capability under `02-capabilities`

Rejected: it is an opinionated composition of several existing capabilities (search, persistence, transport, security), not a single cohesive, independently selectable unit of OS-adjacent behavior. This mirrors [ADR-0019](../adr/0019-terminal-emulation-is-a-domain-framework.md)'s reasoning for terminal emulation.

### Defer this proposal entirely until Phase 5

Considered and rejected as the default, but only provisionally: the working Python server already exists and is already relied upon, which is a materially different situation from a hypothetical future domain framework with no prior art. If reviewers judge that distinction insufficient, this RFC should be rejected or held rather than accepted by default.

### Skip governance and start the Rust port directly in the new repository

Rejected: it would repeat exactly the specification-before-implementation violation [RFC-0002](0002-implementation-trial-governance.md) and [ADR-0002](../adr/0002-specification-before-implementation.md) exist to prevent, and would leave the layered-authority/conflict-registry semantics undocumented as architecture.

## Drawbacks and risks

- Authorizing a domain framework ahead of the roadmap's default phase adds review burden and sets a precedent other early domain-framework proposals may cite; the disposition below should record the forcing-function reasoning explicitly so it cannot be cited as a blanket exception.
- The trial could reveal that SQLite-in-Rust or the vector-search crate ecosystem cannot cleanly satisfy the layered-authority/conflict-registry semantics, in which case the domain framework's shape may need to change before any specification work.
- Running two implementations (Python authoritative, Rust experimental) during the trial is real operational overhead.

## Unresolved questions

- Is an existing, running, external implementation a sufficient forcing function to justify a domain framework ahead of Phase 5, or should this wait?
- Should the `knowledge` domain framework expose one Rusty Mill capability (`rm.knowledge.query`) or several narrower ones (construct lookup, validation, search, cross-cutting) mirroring the Python server's four tool groups?
- Which storage and vector-search crates are credible trial candidates, and what does "byte-for-byte-equivalent" mean for hybrid-ranked search results where floating-point fusion scores are involved?
- Does the MCP transport belong under `networking`, under `ipc`, or does it need its own capability, given existing capabilities do not yet cover the Model Context Protocol specifically?

## Rollout and lifecycle

1. Review and accept or reject this RFC, resolving the Phase-1-vs-Phase-5 timing question explicitly in the disposition.
2. If accepted, record the domain-framework placement decision as an ADR (see companion ADR-0164) before the trial begins.
3. Open one implementation trial record, in the new repository, scoped to functional parity with `baileyrd/knowledge-mcp`'s 15 tools.
4. Report trial evidence back into this RFC's trial-application section per the RFC-0001 pattern; do not begin capability specification work until the trial reports.
5. A separate future RFC accepts (or declines) the `rm.knowledge.*` capability contract based on trial evidence, and a separate decision addresses retiring the Python server.

## Disposition

Pending review.
