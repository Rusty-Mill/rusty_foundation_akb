# ADR-0149: Shared terms have canonical roles, not universal types

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Terms such as session, token, state, event, receipt, authority, and delivery recur across many domains. Treating spelling as equivalence collapses important boundaries; allowing unconstrained local meanings creates contradictions.

## Decision

The architecture defines canonical cross-domain semantic roles and nonclaims. Domains may define qualified refinements and distinct types while preserving those boundaries. Ambiguous homonyms require domain or boundary qualification.

## Alternatives considered

- One universal type per shared word: rejected because domain identity, lifecycle, authority, and data differ.
- Entirely local vocabularies: rejected because cross-domain composition would be unsafe and unreviewable.
- Automated equivalence by lexical matching: rejected because wording cannot establish semantic identity.

## Consequences

- Reviews gain a common language without forcing a universal object model.
- Public contracts should use more distinct types where substitution is dangerous.
- Vocabulary changes require contradiction impact review.
