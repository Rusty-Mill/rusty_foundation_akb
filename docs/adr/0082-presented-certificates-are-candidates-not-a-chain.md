# ADR-0082: Presented certificates are candidates, not a chain

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Peers and files commonly provide a leaf plus intermediates in an expected order, but inputs may be unordered, duplicated, unrelated, malicious, incomplete, or contain cross-signed alternatives. Trust stores and caches can supply other issuers and anchors. Treating presentation order as a validated chain permits issuer confusion and hides alternate policy outcomes.

## Decision

Rusty Mill treats the leaf separately and all supplied non-leaf certificates as an untrusted candidate bag. Bounded path construction proves issuer relationships, signatures, constraints, algorithm policy, and connection to explicit trust anchors while retaining candidate provenance. It may produce zero, one, or multiple candidate paths; deterministic selection and rejected alternatives are evidence. No supplied terminal certificate becomes an anchor implicitly.

## Consequences

- Construction and validation remain separate but composable phases.
- Cross-signs, alternate anchors, loops, duplicates, and same-subject keys are normal test cases.
- Network and store intermediates remain untrusted candidates.
- Resource bounds can yield an explicit indeterminate result rather than a false untrusted/trusted claim.
