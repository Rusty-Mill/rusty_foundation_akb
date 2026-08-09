# Rust language, workspace, and code structure

The [Rust Reference](https://doc.rust-lang.org/reference/) is the primary language reference. Rust ships on a six-week cadence, so every repository pins its edition/toolchain policy rather than depending on an ambient “latest.” Cargo's [`rust-version`](https://doc.rust-lang.org/cargo/reference/rust-version.html) declares package MSRV support expectations.

**RM-DEV-RUST-0001:** Maintained code MUST use stable Rust unless an accepted trial explicitly requires an unstable feature, isolates it, binds a toolchain, and defines removal or stabilization criteria.

**RM-DEV-RUST-0002:** Every published package MUST declare `edition`, `rust-version`, license expression, repository, documentation, and package inclusion/exclusion policy. MSRV changes follow the accepted compatibility/versioning policy and CI verifies the declared MSRV.

**RM-DEV-RUST-0003:** Workspace boundaries MUST follow capability/domain ownership and release needs. A crate is not created solely to mirror a directory, trait, or native API; cyclic conceptual dependencies indicate a boundary defect.

**RM-DEV-RUST-0004:** Modules expose narrow explicit interfaces; domain semantics remain independent from I/O/framework/provider details through ports/adapters or equivalent composition.

**RM-DEV-RUST-0005:** Public and security-relevant surfaces MUST be fully typed. Boolean blindness, stringly typed identities/policies, invalid representable states, and unchecked unit/domain conversions require redesign or explicit justification.

**RM-DEV-RUST-0006:** Prefer immutable values and ownership transfer. Interior mutability, global state, hidden registries, and ambient configuration require stated synchronization, lifetime, testing, and shutdown semantics.

**RM-DEV-RUST-0007:** Formatting is canonical and automated. Lint policy is versioned; warnings introduced by the pinned supported toolchain block CI unless a scoped suppression includes rule, rationale, owner, and removal trigger.

**RM-DEV-RUST-0008:** No `unwrap`, `expect`, indexing panic, `todo!`, `unimplemented!`, or intentional panic is permitted on reachable library/production paths unless the invariant is locally proven and documented. Tests and disposable spikes MAY use them where failure location is the intended oracle.

**RM-DEV-RUST-0009:** Macros and code generation MUST preserve source diagnostics, deterministic output, reviewable generated diffs or schemas, hygiene, documented expansion contracts, and security provenance.

**RM-DEV-RUST-0010:** Feature flags MUST be additive or explicitly conflicting, test every supported combination strategy, avoid changing the same public symbol's semantics, and never silently remove security/correctness guarantees.
