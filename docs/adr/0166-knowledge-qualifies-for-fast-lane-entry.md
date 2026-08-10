# ADR-0166: Knowledge qualifies for RFC-0005 fast-lane entry

**Status:** Accepted  
**Date:** 2026-08-10  
**Deciders:** David Bailey ([@baileyrd](https://github.com/baileyrd)) — solo, per [RFC-0004](../rfc/0004-solo-maintainer-review-sufficiency.md)

## Context

[RFC-0005](../rfc/0005-fast-lane-implementation-entry.md) defines a fast lane for domains that don't touch unsafe/FFI authorship, native platform backends, or authority/credential/crypto primitives: a single Accepted ADR is sufficient to begin implementation, in place of [RFC-0002](../rfc/0002-implementation-trial-governance.md)'s full eight-gate trial-entry process. `knowledge` (the domain framework specified in [RFC-0003](../rfc/0003-rusty-knowledge-domain-framework.md), [ADR-0164](0164-rusty-knowledge-is-a-domain-framework.md), [ADR-0165](0165-knowledge-layered-authority-carries-over-as-a-requirement.md)) has been going through that full process — [TRIAL-0003](../05-governance/implementation-trials/rusty-knowledge-trial-proposal.md) is currently `Not authorized`, blocked on Subject (no accepted Experimental promotion) despite real crate research, a composition register, and a repository bootstrap already existing. This ADR decides whether `knowledge` actually needs that machinery.

## Decision

`knowledge` qualifies for RFC-0005's fast lane. Implementation may begin in [`rusty-mill/rusty_knowledge`](https://github.com/Rusty-Mill/rusty_knowledge) on the strength of this ADR alone, without waiting for TRIAL-0003 to reach Authorized or for `knowledge`'s own promotion-review to reach Accepted.

**Against each qualification-test criterion:**

- **(a) No new unsafe/FFI authorship.** `knowledge`'s implementation consumes `rusqlite` and `sqlite-vec` (researched in [platform-research.md](../02-capabilities/knowledge/platform-research.md)) as ordinary Cargo dependencies exposing safe-Rust-facing APIs over their own internal unsafe/FFI. `knowledge` does not write new `unsafe` blocks or FFI bindings of its own; it calls safe functions those crates already publish and maintain.
- **(b) No native OS platform backend.** `knowledge` is a database-backed server (SQLite via `rusqlite`) with an HTTP-ish MCP transport (`rmcp`). It does not touch raw syscalls, native handles, or platform-specific mechanism code — `rusqlite`'s `bundled` feature and `rmcp`'s transport implementations already handle whatever platform variance exists, and `knowledge` does not reimplement or bypass that layer.
- **(c) No authority/credential/crypto primitives.** `knowledge`'s layered authority model (Standard → Tool Implementation → Conventions → Process, per [ADR-0165](0165-knowledge-layered-authority-carries-over-as-a-requirement.md)) is a data-modeling and precedence concept — which rule wins when two sources disagree — not an authentication, authorization, or cryptographic primitive. Transport-level authentication (bearer tokens, matching the Python prior art) is explicitly composed from the `security` capability per [`dependencies.md`](../02-capabilities/knowledge/dependencies.md), not implemented inside `knowledge`.

## Options considered

### Keep grinding through TRIAL-0003's full entry review

Rejected. TRIAL-0003's own gate table already shows the remaining blockers (Subject: no accepted Experimental promotion; assertions/benchmarks: not executed) are downstream of *specifying `knowledge` fully before writing any code* — exactly the ordering RFC-0005 exists to relax for non-security work. Continuing would mean writing a capability specification, conformance plan, and benchmark plan for a system that doesn't exist yet, based entirely on reading someone else's Python source, before finding out through building whether that specification is even right.

### Fast-lane only part of `knowledge` (e.g., storage layer) and keep the rest gated

Rejected as premature narrowing. Nothing about `knowledge` as scoped touches the three excluded criteria; splitting it without a concrete reason to distrust part of it would just reintroduce the same overhead RFC-0005 is meant to remove, for no disclosed benefit.

### Treat RFC-0005's acceptance alone as sufficient, skip a domain-specific ADR

Rejected — RFC-0005 itself requires a per-domain ADR (its step 2) precisely so "fast lane" isn't a blanket declaration that silently covers everything going forward without anyone having actually checked the three criteria for that specific domain. This ADR is that check, done and recorded.

## Consequences

- Implementation may begin in `rusty_knowledge` immediately: a Cargo workspace, the researched dependencies (`rusqlite`, `sqlite-vec`, `rmcp`), and a first working slice.
- `TRIAL-0003` is not deleted or declared wrong — it remains the historical record of what full-process entry review looked like for this domain, and is marked superseded-in-practice by this ADR in a follow-up edit, not silently abandoned.
- `knowledge`'s eventual capability specification (the `docs/02-capabilities/knowledge/` template pass RFC-0003 deferred) is now expected to happen *after* a working implementation exists, informed by what building it actually revealed — not before, as originally planned.
- Ordinary development standards still apply once code exists: this ADR does not exempt `knowledge` from testing, dependency hygiene, or CI — only from the pre-code trial-authorization ceremony.
- If `knowledge` later needs its own unsafe code, a native backend, or authority/crypto primitives (none currently anticipated), RFC-0005's exit condition reactivates full RFC-0002 governance for that part automatically.

## Verification

Reviewed against RFC-0005's three criteria above, all satisfied as of this decision. If a future contributor or the maintainer finds `knowledge`'s actual implementation drifting into any excluded category, that's this ADR's own trigger to reopen — not a violation to hide, per the same evidence-disclosure culture the rest of this project's governance already uses.

## Follow-up

- [ ] Mark `TRIAL-0003` superseded-in-practice by this ADR for `knowledge`'s implementation path, retained for history (owner: David Bailey, due: next `rusty_foundation_akb` change touching that file).
- [ ] Scaffold a Cargo workspace in `rusty_knowledge` with the researched dependencies (owner: David Bailey, due: immediately, this session).
- [ ] Write `knowledge`'s capability specification once a working slice exists, informed by what building it revealed (owner: David Bailey, due: unscheduled — post-implementation, per RFC-0005).
