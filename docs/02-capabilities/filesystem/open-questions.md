# Filesystem foundations open questions

**Status:** Active register

| ID | Question | Why it matters | Evidence or decision needed |
|---|---|---|---|
| FS-Q001 | ~~What minimum containment strength is required for Stable `rm.filesystem.resolve`?~~ **Partially resolved:** providers use R0–R3; security-sensitive profiles must select R1+. | Platform strength varies. | [Resolution quality levels](resolution-quality.md); exact profile minima remain open |
| FS-Q002 | ~~Is a directory resource part of `resolve` or a separate capability?~~ **Closed: separate capability.** | Directory authority is independently useful for enumeration, mutation, and sync. | [`rm.filesystem.directory`](directory.md) |
| FS-Q003 | Should append be a file capability quality or a separate operation contract? | Atomic append and positioned-write semantics vary. | Platform/filesystem matrix |
| FS-Q004 | ~~What durability levels are portable?~~ **Partially resolved:** D0–D3 model adopted for trial. | Exact provider support remains evidence-driven. | [Durability model](durability-model.md) |
| FS-Q005 | Which metadata fields belong in the base snapshot? | Too many fields create false portability; too few force platform branching. | CLI/server/desktop scenarios |
| FS-Q006 | How is Windows share/delete policy represented without infecting portable callers? | It materially affects open, rename, and replacement. | Policy model RFC |
| FS-Q007 | ~~Is atomic replacement a capability or a platform service?~~ **Closed: capability.** | Native atomic transition is independently selectable and testable; durable publication may be a service. | [ADR-0008](../../adr/0008-atomic-replacement-is-a-capability.md) |
| FS-Q008 | ~~What is the portable error taxonomy?~~ **Closed for the foundation slice.** | Categories plus native evidence support recovery without raw-code coupling. | [Filesystem error model](error-model.md) |
| FS-Q009 | How should path values serialize across platform families? | Lossless native representation may not be meaningful elsewhere. | Packaging/configuration scenarios |
| FS-Q010 | ~~Which filesystem families are required for conformance?~~ **Partially resolved:** Core-local tier is mandatory; exact Linux primary and extended matrix remain open. | Claims cannot inherit across filesystem families. | [Provider support matrix](support-matrix.md) |
| FS-Q011 | Is filesystem watching a journal, invalidation stream, or multiple quality levels? | Native services differ in granularity, persistence, and loss behavior. | Dedicated watch domain analysis |
| FS-Q012 | How are sandbox/bookmark/capability authorities represented on macOS and other platforms? | Path access may not equal durable authority. | Security model research |
