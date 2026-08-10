# Domain model and query surface

Derived from `baileyrd/knowledge-mcp`'s working implementation. Identifiers below are draft framework-level requirements for trial input, not an accepted `rm.knowledge.*` capability contract.

## Entities

- **Domain:** a namespaced body of knowledge (for example UAF 1.3). A server instance hosts one or more domains concurrently.
- **Construct:** a named element within a domain (an entity type, artifact, or modeling concept) with rules and relationships attached.
- **Rule:** a normative statement attached to a construct, tagged with its authority layer.
- **Relationship:** a typed, directional link between two constructs, validated against the domain's declared valid-relationship set.
- **Authority layer:** one of Standard, Tool Implementation, Conventions, Process, ordered by precedence. A "shared family" (a rule prefix shared across layers, e.g. a cross-cutting security family) may be authoritative from more than one layer for different sub-questions.
- **Conflict registry entry:** a recorded contradiction between two rules across layers, with a resolution or an explicit "unresolved" state. Presence in the registry is required before a query answer may silently prefer one layer over another.

## Query surface (carried over from the Python tool groups)

- **Lookup:** construct definition, applicable rules, relationships, valid-relationship set, domain summary.
- **Validate:** element conformance, relationship legality, completeness against declared rules.
- **Search:** hybrid lexical + vector search across constructs and rule text; construct-scoped search.
- **Cross-cutting:** traceability across constructs/domains, conflict listing, cross-domain queries.
- **Meta:** domain listing, routing guidance for selecting a domain.

## Draft requirements

- **RM-KNOWLEDGE-MODEL-0001:** A domain framework instance **MUST** be able to host more than one namespaced domain and answer `meta.list_domains` without cross-domain leakage of unrelated rules or constructs.
- **RM-KNOWLEDGE-MODEL-0002:** Every lookup or search response that includes a rule **MUST** carry that rule's authority layer alongside its content; a layer-less answer is not a conforming minimum response.
- **RM-KNOWLEDGE-MODEL-0003:** When two rules from different authority layers contradict for the same construct, the framework **MUST** expose the contradiction through the conflict registry rather than resolve it silently inside a lookup response.
- **RM-KNOWLEDGE-MODEL-0004:** Relationship validation **MUST** reject a relationship type not present in the domain's declared valid-relationship set rather than accept it and defer the error.
- **RM-KNOWLEDGE-MODEL-0005:** Search **MUST** declare whether a given response used hybrid (lexical + vector) or lexical-only retrieval; lexical-only substitution **MUST NOT** be silent.

## Open

Requirement identifiers, wording, and scope above are provisional; see [open-questions.md](open-questions.md) for what the implementation trial must resolve before these become candidate capability requirements.
