# Scope, applicability, and rule governance

## Rule hierarchy

1. Law, license, and binding security response obligations.
2. Authoritative architecture model and accepted safety/security invariants.
3. Accepted domain capability contracts and workload profiles.
4. These foundation development standards.
5. Repository-local standards profiles and tool configuration.
6. Change-specific design and review evidence.

Lower levels may strengthen a rule but cannot silently weaken or redefine higher authority.

**RM-DEV-GOV-0004:** Every normative development rule MUST have a stable identifier, owner, applicability, verification method or review evidence, severity, and evolution history.

**RM-DEV-GOV-0005:** `MUST`, `SHOULD`, and `MAY` have normative force. A `SHOULD` deviation MUST record why the general rule is unsuitable and what risk remains.

**RM-DEV-GOV-0006:** Tool configuration is an enforcement projection, not normative authority. If configuration and standards disagree, the inconsistency blocks the affected gate until reconciled.

**RM-DEV-GOV-0007:** Standards changes MUST analyze existing repositories, public contracts, MSRV/toolchain policy, supported targets, CI capacity, contributor impact, security, and migration.

## Trial classes

| Class | Purpose | Allowed persistence | Merge/release status |
|---|---|---|---|
| Research spike | Learn native behavior or contract feasibility | Disposable branch/artifacts | Cannot become a dependency or public precedent |
| Experimental provider | Exercise an approved Draft contract | Reviewed unstable boundary | May merge only under Experimental maturity and explicit support nonclaims |
| Conformance/benchmark harness | Produce specification evidence | Versioned evidence tooling | Cannot define semantics independently |
| Stable implementation | Fulfill a Stable contract/profile | Supported production path | Requires full release and compatibility gates |

**RM-DEV-GOV-0008:** A spike promoted into maintained code MUST pass ordinary review, testing, dependency, unsafe, documentation, and provenance gates; prior experimentation does not grandfather violations.
