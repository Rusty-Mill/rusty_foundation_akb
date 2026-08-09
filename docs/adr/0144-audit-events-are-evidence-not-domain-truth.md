# ADR-0144: Audit events are evidence, not domain truth

- **Status:** Accepted
- **Date:** 2026-08-08

## Context

Audit trails are often called immutable ledgers and later treated as event-sourced domain state. Yet audit events may be delayed, duplicated, minimized, sampled where allowed, corrected, redacted, produced at different effect boundaries, or absent during capture failures. Replaying them can repeat no authority and may omit required domain data.

## Decision

Audit events are immutable, provenance-bearing evidence about decisions and effects. Authoritative domain state and effect receipts remain separate. Audit events can support investigation, reconciliation, assessment, and recovery validation but cannot independently recreate authorization, repeat effects, or become domain truth unless a separately specified event-sourced domain contract proves that role.

## Options considered

- Treat audit as the universal event store: one pipeline, but mismatched privacy, completeness, and replay semantics.
- Treat audit as disposable diagnostics: insufficient for accountability and evidence.
- Separate evidence ledger with explicit links: selected.

## Consequences

Capture boundaries and reconciliation are explicit. Corrections append rather than rewrite. Products may deliberately select event sourcing elsewhere, but must not infer it from the audit facility.
