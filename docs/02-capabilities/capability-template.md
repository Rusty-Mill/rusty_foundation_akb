# Capability specification template

Copy this file to the future domain location and replace all instructional text. A capability specification is normative only after its governing RFC is accepted.

---

# `rm.<domain>.<capability>` — Capability name

**Status:** Draft  
**Contract version:** 0.1.0  
**Domain:** Domain  
**Owner:** Unassigned  
**Profiles:** None yet

## Purpose

What application outcome does this capability enable?

## Scope

### Goals

### Non-goals

## Vocabulary

Define terms whose meanings affect conformance.

## Scenarios

Include ordinary, boundary, failure, concurrent, cancellation, recovery, and shutdown scenarios.

## Semantic model

Describe state, resources, authorities, events, operations, and invariants without prescribing Rust API syntax.

## Requirements

Use stable identifiers and normative language.

- **RM-DOMAIN-CAPABILITY-0001:** A provider **MUST** ...
- **RM-DOMAIN-CAPABILITY-0002:** A consumer **MAY** ...

## Lifecycle and ownership

Creation, borrowing, transfer, closure, cancellation, cleanup, and behavior after failure.

## Concurrency and ordering

Thread-safety, reentrancy, ordering, atomicity, backpressure, fairness, and race behavior.

## Async and sync semantics

Completion model, cancellation safety, blocking guarantees, synchronous path, and interactions with executors or threads.

## Errors and recovery

Typed failure categories, partial completion, retry safety, idempotency, and diagnostic context. Do not expose raw platform error codes as the portable semantic model.

## Authority and security

Required authority, least-privilege defaults, sensitive data, trust boundaries, threat assumptions, and audit events.

## Quality requirements

### Performance

### Accessibility

### Internationalization

### Observability

## Dependencies

| Relationship | Capability | Reason |
|---|---|---|
| requires / optionally-uses / conflicts-with | `rm.example.name` | Why |

## Platform realization

| Platform | State | Candidate native mechanisms | Known variance |
|---|---|---|---|
| Windows | Unknown | Research required | None recorded |
| Linux | Unknown | Research required | None recorded |
| macOS | Unknown | Research required | None recorded |

## Degradation and emulation

Define allowed quality levels and how they are discovered. Anything not stated here is not an allowed silent fallback.

## Compatibility and evolution

State what constitutes compatible additive change, breaking semantic change, deprecation, and retirement.

## Conformance plan

| Requirement | Assertion or evidence | Test class |
|---|---|---|
| RM-DOMAIN-CAPABILITY-0001 | TBD | deterministic / environment / manual review |

## Benchmark plan

Define native baseline, abstraction measurement, representative workload, environment controls, metrics, and provisional regression budget.

## Open questions

- Unresolved question and the evidence needed to answer it.

## History

| Version | Date | Change | Decision |
|---|---|---|---|
| 0.1.0 | YYYY-MM-DD | Initial draft | RFC-NNNN |
