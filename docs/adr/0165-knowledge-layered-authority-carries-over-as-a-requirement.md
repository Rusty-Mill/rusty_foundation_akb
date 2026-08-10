# ADR-0165: Knowledge domain layered authority is a portable requirement, not a Python implementation detail

**Status:** Proposed  
**Date:** 2026-08-10  
**Deciders:** Rusty Mill maintainers

## Context

`baileyrd/knowledge-mcp`'s most load-bearing design decision is a four-layer authority model (Standard → Tool Implementation → Conventions → Process) with an explicit conflict registry for cross-layer contradictions, plus one server hosting multiple namespaced knowledge domains side by side (UAF today; `data_mesh`/`udra` as stubs) rather than one server per domain. Both properties determine which answer a query returns when sources disagree, which is semantically load-bearing, not an artifact of SQLite or Python. Without recording this, a Rust trial could "simplify" by flattening the authority model or hard-coding a single domain, silently changing observable behavior while still passing a shallow tool-response comparison.

## Decision

The implementation trial authorized by [RFC-0003](../rfc/0003-rusty-knowledge-domain-framework.md) **MUST** preserve, as portable semantic requirements independent of storage engine or language:

1. Multi-domain hosting: one server instance can serve more than one namespaced knowledge domain concurrently, matching the existing `meta.list_domains` / `meta.routing_guide` tool contract.
2. The four-layer authority model and its precedence order, including "shared families" that span multiple layers (the Python implementation's `SEC-*`-style shared prefixes in its requirement/construct registry).
3. An explicit, queryable conflict registry (`crosscut.conflicts`) rather than silent precedence resolution with no audit trail.
4. Hybrid retrieval as a declared capability of the `search` composition, not an optional enhancement: lexical-only fallback is an allowed degraded mode, but it must be discoverable as degraded, not silently substituted.

Trial evidence must include a comparison corpus and query set exercising at least one real cross-layer conflict, so "preserved the authority model" is falsifiable rather than asserted.

## Options considered

### Let the trial choose its own semantics and reconcile with the Python server afterward

Rejected. Authority/conflict-resolution semantics are exactly the kind of decision [ADR-0009](0009-identity-is-not-authority.md) and [ADR-0116](0116-policy-decisions-are-evidence-not-effect-authority.md) treat as too consequential to leave implicit; reconciling after the fact risks discovering a silent behavior change only once something downstream trusted a wrong answer.

### Require bit-identical ranking scores between Python and Rust

Rejected as the bar. Hybrid fusion (FTS5 + vector, combined by Reciprocal Rank Fusion) is float-sensitive across different vector-search crates; requiring bit-identical scores would block any implementation choice. The trial instead compares top-K result sets and conflict-registry decisions, not raw scores.

### Treat single-domain hosting as acceptable for the trial's initial scope

Rejected. Multi-domain hosting is not an incidental feature to defer — it is the reason a "unified domain knowledge server" exists instead of one server per standard. Narrowing scope to single-domain would produce evidence about a different, easier problem.

## Consequences

- The trial's entry review (per RFC-0002) must name its comparison corpus and at least one cross-layer conflict scenario before code is authorized.
- Storage-engine and vector-search-crate selection remains open; this ADR constrains observable behavior, not implementation choice.
- A future `rm.knowledge.*` capability specification inherits these four points as candidate normative requirements rather than re-deriving them from scratch.

## Verification

The trial closes successful only if its evidence bundle demonstrates all four preserved properties against the comparison corpus, per the outcome-neutral closeout process in RFC-0002. A trial that reimplements the tool surface but drops multi-domain hosting or the conflict registry closes as failed or inconclusive, not successful.

## Follow-up

- [ ] Trial entry review — name the comparison corpus and cross-layer conflict scenario (owner: trial proposer, due before trial code begins).
- [ ] Trial closeout — attach evidence for all four preserved properties (owner: trial proposer, due at trial close).
