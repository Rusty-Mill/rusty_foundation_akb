# RFC-0005: Fast-lane implementation entry for non-security domain frameworks

**Status:** Accepted  
**Authors:** David Bailey ([@baileyrd](https://github.com/baileyrd))  
**Reviewers:** None independent — see Disposition, consistent with [RFC-0004](0004-solo-maintainer-review-sufficiency.md)  
**Created:** 2026-08-10

## Summary

Amend [RFC-0002](0002-implementation-trial-governance.md)'s implementation-trial governance with a fast lane: a domain or domain framework that does not implement new unsafe/FFI code, does not implement a native OS platform backend, and does not implement authority/credential/cryptographic primitives may begin implementation once a single Accepted ADR names the subject, states why it qualifies, and binds a target repository — skipping the eight-gate conjunctive entry review, the ownership/cross-cutting/promotion-review document set, and the trial-record lifecycle entirely for that work. The full RFC-0002 model remains mandatory for anything that does touch those three excluded categories.

## Motivation

RFC-0002's trial-governance model was built for a platform whose core risk is native, unsafe, cross-OS code: memory safety, authority boundaries, ABI mismatches across Windows/Linux/macOS. Eight conjunctive gates, named independent reviewers, and formal evidence plans earn their cost there — a bug is a real vulnerability across three operating systems.

Applying that same machinery to `knowledge` — a domain framework porting a working Python MCP server (SQLite + hybrid search + an HTTP-ish transport) to Rust, using well-established safe-Rust-facing crates — produced disproportionate overhead: an RFC, two ADRs, a domain-analysis document set, a blocked trial proposal, a promotion review, ownership and cross-cutting documents, a reviewer-independence waiver, RFC-0004 generalizing that waiver, real crate research, a composition register, and a repository bootstrap — all before one line of Rust existed. For a solo maintainer trying to get a working thing off the ground, that ordering (specification-and-governance-before-implementation, applied uniformly) actively worked against the goal RFC-0002 exists to serve: learning by building, safely.

## Goals and non-goals

### Goals

- Distinguish security-and-native-code risk (where heavy gates are proportionate) from everything else (where they aren't), and gate proportionately to which one applies.
- Let a solo maintainer start writing code for non-security domain frameworks after one ADR, not eight gates and a document set.
- Keep the full RFC-0002 model fully intact and mandatory for anything touching unsafe/FFI authorship, native platform backends, or authority/credential/crypto primitives — this RFC narrows applicability, it does not weaken the model where it applies.
- Make the fast lane's exit condition explicit and automatic, mirroring RFC-0004's pattern, rather than a one-time exemption that quietly becomes precedent for everything.

### Non-goals

- This RFC does not exempt security, unsafe/FFI-authoring, or native-platform-backend work from RFC-0002. `TRIAL-0001` (security-foundation) and the native-platform-backend portions of `TRIAL-0002` (rustils/filesystem) are explicitly unaffected and remain under the full model.
- This RFC does not retroactively re-decide any closed gate state on `TRIAL-0002` or `TRIAL-0001`.
- This RFC does not authorize any specific domain's fast-lane entry by itself — a separate ADR is required per domain, naming exactly why that domain qualifies. This RFC defines the lane; it does not drive anything through it.
- This RFC does not remove the standards-development process ([`docs/05-governance/software-development/`](../05-governance/software-development/README.md)) — ordinary Rust/testing/dependency/CI hygiene still applies to fast-laned code once it exists. What's removed is the *pre-code authorization ceremony*, not post-code quality practice.

## Proposed design

1. **Qualification test.** A domain or domain framework qualifies for the fast lane if, and only if, its implementation will not: (a) author new `unsafe` Rust code or FFI bindings beyond depending on existing, independently-published crates that already provide safe-Rust-facing APIs over their own unsafe/FFI internals; (b) implement a native OS platform backend (raw syscalls, native handle management, platform-specific mechanism code); (c) implement authority, credential, cryptographic, or sandboxing primitives — consuming an existing `security` capability's eventual contract is fine, *building* one is not.
2. **Entry instrument.** A single ADR, in the ordinary [ADR process](../05-governance/governance.md#adrs), stating: the subject domain/framework, an explicit statement against each of the three qualification-test criteria, the target repository, and a one-paragraph scope statement (what's being built, not a full specification). No RFC, no trial proposal, no promotion-review/ownership/cross-cutting document set, and no entry-gate table are required to begin implementation. Accepting the ADR is itself the authorization — under RFC-0004's solo-maintainer mode, a solo-authored, self-accepted ADR is sufficient, same as any other ADR.
3. **What still applies once code exists.** Ordinary software-development standards (testing, dependency hygiene, CI) apply immediately per `docs/05-governance/software-development/`. A capability specification (the `docs/02-capabilities/<domain>/` template) is still expected once the domain's shape stabilizes through building it — this RFC changes *when* specification work happens relative to code, not whether it happens at all. Fast-laned work still cannot claim Stable maturity, a public release, or a conformance/certification claim without separately satisfying whatever those require.
4. **Exit condition — automatic, not a deadline.** A fast-laned domain's future work reverts to full RFC-0002 governance the moment any of the following becomes true, whichever comes first: (a) the domain's actual scope grows to touch unsafe/FFI authorship, a native platform backend, or authority/credential/crypto primitives; (b) the project gains a second contributor with a stake in that domain; (c) the domain has real external users beyond the maintainer; (d) the domain seeks Stable maturity or a public release claim. No calendar expiry — same reasoning as RFC-0004: a date measures elapsed time, not whether the actual risk changed.
5. **Retroactive scope.** Existing trial proposals are not silently reclassified. `TRIAL-0001` and the native/filesystem-touching portions of `TRIAL-0002` remain under full RFC-0002 governance, since they genuinely touch the excluded categories. `TRIAL-0003` (`knowledge`) is a plausible fast-lane candidate and is addressed by a companion ADR in this same change, not by this RFC's own text — this RFC defines the mechanism, the companion ADR applies it.

## Behavioral contract impact

None directly — this is process governance. Indirectly, it changes *when* a capability contract gets written relative to when code exists for fast-laned domains: after a working prototype, not before.

## Capability graph and profile impact

None. Fast-laned code is not thereby added to the capability graph or any profile; that remains a separate, later decision once a capability specification exists.

## Platform behavior and variance

Not applicable to this RFC directly. Fast-laned domains, by qualification-test criterion (b), are precisely the ones *not* implementing platform-specific backend code, so platform variance is expected to be low-stakes for anything that qualifies — which is itself part of why the fast lane is safe to offer them.

## Security, performance, accessibility, i18n, and observability

Security is the dimension this RFC is built around excluding from the fast lane by design (criterion (c) and the native-backend exclusion (b), since native platform mechanisms are often where security-relevant behavior lives). Performance, accessibility, i18n, and observability are not gated pre-code by this RFC either way; they remain ordinary engineering concerns addressed as the code is written and reviewed under standard development practice, not pre-authorized via a trial evidence plan.

## Compatibility, versioning, packaging, and migration

Not applicable pre-code. Once fast-laned code reaches a point where release/versioning matters, ordinary Rusty Mill compatibility and packaging rules apply unchanged — this RFC only affects the pre-implementation gate, not post-implementation obligations.

## Conformance and benchmarks

Not required before fast-lane implementation begins (that's the point). Expected once the implementation exists and the domain moves toward any maturity claim beyond "exists and works for the maintainer."

## Alternatives considered

### Keep RFC-0002 uniform for all domains

Rejected — this is the status quo this RFC exists to change, and its cost was demonstrated directly on `knowledge` before any code existed.

### Blanket exemption for all pre-Stable work, no qualification test

Rejected. A blanket exemption would also exempt security and native-platform work, which is exactly where the heavy gates are proportionate to real risk. The three-criterion test targets the actual risk driver, not maturity level alone.

### Per-domain waiver instead of a standing fast lane

Rejected for the same reason RFC-0004 rejected per-decision waivers over a standing rule: the underlying fact (this class of work doesn't carry the risk RFC-0002 was built for) doesn't change domain to domain, so re-litigating it per domain is the same avoidable overhead this RFC is trying to remove. A single ADR per domain (step 2 above) is the minimum necessary per-domain step, not a full waiver negotiation.

### Time-boxed fast lane (e.g., "for the first 6 months")

Rejected, consistent with RFC-0004: a calendar date doesn't track whether the actual triggering conditions (a second contributor, real users, scope creeping into excluded categories) have occurred.

## Drawbacks and risks

- A domain could grow into the excluded categories gradually enough that the exit condition isn't noticed in time; mitigated only by the maintainer's own vigilance, since no automated check enforces criterion (a)/(b)/(c) drift — this is a real, disclosed limitation, not a solved problem.
- Skipping the domain-analysis document set pre-code means less structured thinking happens before code than RFC-0002's model intends; the tradeoff accepted here is that for non-security work, learning by building is an acceptable substitute for learning by specifying first.
- A future contributor could misread "fast lane" as "no standards apply" rather than "no *pre-code authorization* ceremony applies" — the Non-goals section and this RFC's continued reference to ordinary development standards are the guardrail against that reading.

## Unresolved questions

- Should a fast-laned domain's *first* capability specification (once written, post-code) require anything beyond the ordinary [domain-analysis method](../02-capabilities/domain-analysis.md), given it will be written with working code already in hand rather than before it? Left for whoever writes that specification to judge against the ordinary process as it stands.

## Rollout and lifecycle

Effective immediately upon acceptance. A companion ADR in this same change applies the fast lane to `knowledge` specifically. Future fast-lane qualifications for other domains follow step 2 above — one ADR each, not a repeat of this RFC.

## Disposition

**Accepted**, self-decided by the sole accountable maintainer (David Bailey, [@baileyrd](https://github.com/baileyrd)), per [RFC-0004](0004-solo-maintainer-review-sufficiency.md)'s solo-maintainer mode — disclosed here rather than treated as a problem. This RFC is itself an instance of the judgment call RFC-0004 was written to make explicit: the maintainer decided the existing process was miscalibrated for this class of work and changed it, rather than working around it silently or grinding through ceremony that wasn't earning its cost.
