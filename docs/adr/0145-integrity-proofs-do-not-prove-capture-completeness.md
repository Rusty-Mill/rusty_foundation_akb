# ADR-0145: Integrity proofs do not prove capture completeness

- **Status:** Accepted
- **Date:** 2026-08-08

## Context

Hashes, signatures, chains, trusted timestamps, transparency logs, and immutable storage can detect modification or deletion within an included scope. They cannot show that an uninstrumented effect emitted an event, that a producer told the truth, or that logging was enabled before the proof chain began.

## Decision

Every integrity result states its exact artifact/range, canonicalization, origin/time/sequence claims, trust inputs, verification status, gaps, and nonclaims. Completeness is assessed separately against expected source populations, capture configurations, sequences/frontiers, pipeline health, signed empty intervals where available, and reconciliation.

## Options considered

- “Tamper-proof audit log” boolean: marketable but false and unauditable.
- Integrity only, no completeness model: detects alteration but hides omission risk.
- Scoped integrity plus independent completeness evidence: selected.

## Consequences

Verification must actually run, not merely be enabled. Dashboards and attestations expose gaps and proof coverage. Threat models include compromised producers, disabled capture, missing genesis intervals, forks, and key compromise.
