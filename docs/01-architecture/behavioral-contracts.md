# Behavioral contracts

A behavioral contract is the normative source for what consumers may rely on and what providers must prove. API shape follows the contract; it does not substitute for one.

## Required sections

1. Identity, purpose, maturity, and owner.
2. Preconditions, inputs, outputs, and invariants.
3. Resource ownership, lifetime, cancellation, and cleanup.
4. Ordering, concurrency, thread-safety, and reentrancy.
5. Async and sync semantics, including blocking behavior.
6. Success, typed failures, partial completion, and recovery.
7. Security authority, privilege boundaries, and sensitive data handling.
8. Performance class, budgets, scaling characteristics, and measurement method.
9. Accessibility and internationalization effects where user interaction or text is involved.
10. Observability signals and privacy constraints.
11. Platform variance, native mapping, emulation, and degradation.
12. Compatibility and evolution rules.
13. Conformance assertions and benchmark scenarios.

Normative terms **MUST**, **SHOULD**, and **MAY** follow RFC 2119-style meanings. Every **MUST** needs a test or a documented reason it cannot be mechanically verified.

## Capability lifecycle

`Draft -> Experimental -> Stable -> Deprecated -> Retired`

Promotion to Stable requires accepted contracts, at least one conforming backend on each target platform, profile impact analysis, security review, compatibility policy, conformance coverage, and benchmark baselines.
