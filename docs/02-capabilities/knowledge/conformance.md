# Conformance specification

No capability contract is accepted yet (see [RFC-0003](../../rfc/0003-rusty-knowledge-domain-framework.md)). This plan states how the draft requirements in [model.md](model.md) would be verified if accepted, and doubles as the implementation trial's comparison plan per RFC-0002.

| Requirement | Assertion or evidence | Test class |
|---|---|---|
| RM-KNOWLEDGE-MODEL-0001 | Multi-domain fixture with at least two namespaced domains; `meta.list_domains` output contains both with no cross-domain rule/construct bleed | deterministic |
| RM-KNOWLEDGE-MODEL-0002 | Fixed lookup/search corpus; every returned rule carries a non-empty authority-layer field | deterministic |
| RM-KNOWLEDGE-MODEL-0003 | Fixture containing at least one known cross-layer contradiction; `crosscut.conflicts` reports it; the same contradiction is not silently resolved inside a `lookup.rules` response | deterministic |
| RM-KNOWLEDGE-MODEL-0004 | Attempt to register a relationship type outside the domain's declared valid-relationship set; framework rejects at validation time | deterministic |
| RM-KNOWLEDGE-MODEL-0005 | Search response schema includes a retrieval-mode field distinguishing hybrid from lexical-only; a forced-degraded-mode fixture asserts the field reflects degradation | deterministic |

- **RM-KNOWLEDGE-CONFORMANCE-0001:** Conformance evidence **MUST** be produced by comparing the Rust implementation trial's tool responses against the existing Python `knowledge-mcp` server's responses over the same fixed corpus and query set, not against a specification written after the fact.
- **RM-KNOWLEDGE-CONFORMANCE-0002:** At least one test fixture **MUST** exercise a genuine cross-layer authority conflict from real domain content (not a synthetic placeholder), per [ADR-0165](../../adr/0165-knowledge-layered-authority-carries-over-as-a-requirement.md).

## Status

Deterministic test classes above are proposed, not implemented. No conformance suite exists yet; this document is the trial's entry-review input, not evidence of a passing suite.
