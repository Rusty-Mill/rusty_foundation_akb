# `rm.text.font-resolution`

| Field | Value |
|---|---|
| Status | Draft |
| Contract version | 0.1.0 |

**RM-TEXT-FONT-0001:** A request declares ordered families/generic roles, weight/stretch/style, optical size, variation axes, language/script, required character/feature coverage, color-glyph policy, licensing/export constraints, source policy, and fallback limits.

**RM-TEXT-FONT-0002:** Resolution returns an ordered immutable plan of exact face instances identified by artifact digest, face/collection index, variation coordinates, synthesized attributes, source/provenance, trust status, and availability lifetime.

**RM-TEXT-FONT-0003:** Family/display names are requests and diagnostics, not stable font identity. Two files with the same names are not equivalent without artifact/face evidence.

**RM-TEXT-FONT-0004:** System font changes publish a collection revision. Existing resolved plans remain immutable or become explicitly unavailable; they never silently adopt a replacement face mid-layout.

**RM-TEXT-FONT-0005:** Fallback is deterministic within one resolution snapshot and identifies which scalar/cluster ranges selected each face. Missing coverage yields a declared missing-glyph policy rather than pretending the primary face rendered it.

**RM-TEXT-FONT-0006:** Synthetic bold/oblique, variable-axis clamping, optical sizing, bitmap strikes, color formats, and platform substitution are separately disclosed quality facts.

**RM-TEXT-FONT-0007:** Untrusted downloadable/user fonts are parsed behind resource limits and an isolation policy appropriate to the threat model. Discovery never causes undeclared network access.

**RM-TEXT-FONT-0008:** Font bytes, names, installed-set fingerprints, caches, and licensing metadata follow authority/privacy policy. Embedding/export is prohibited unless the resolved license/source policy permits it.

**RM-TEXT-FONT-0009:** Async discovery/loading supports cancellation and budgets. The sync path may use already available snapshots but does not perform hidden network or unbounded scan work.

