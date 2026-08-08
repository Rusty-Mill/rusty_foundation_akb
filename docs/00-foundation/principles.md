# Architecture principles

## 1. Abstract capabilities, not operating systems

Model what an application needs to accomplish. OS APIs are backend mechanisms, not the public conceptual model.

## 2. Spec before implementation

Define vocabulary, semantics, guarantees, failure modes, platform variance, and verification before stabilizing APIs or creating crates.

## 3. Rust-native and zero-cost where feasible

Public interfaces should use Rust's ownership, type, error, and concurrency models. Abstraction cost must be visible and justified.

## 4. Async-first, sync-complete

Potentially blocking operations must compose naturally with async execution. Every stable capability must also have a documented synchronous use path; sync must not be a naive nested-runtime wrapper.

## 5. Native performance

Use the strongest appropriate native mechanism per backend. Avoid avoidable copies, allocations, context switches, and indirection. Claims require benchmarks.

## 6. Secure by default

Least privilege, explicit authority, safe defaults, boundary validation, and auditable sensitive operations are part of every contract.

## 7. Explicit variance and degradation

Do not silently emulate, weaken, or ignore behavior. Availability, emulation, degradation, and unsupported states must be inspectable.

## 8. Testable and observable

Normative guarantees must map to conformance tests. Operations must support consistent diagnostics without requiring a particular telemetry vendor.

## 9. Layer integrity

Dependencies flow downward through declared interfaces. Cross-layer shortcuts require an ADR and must not leak backend details upward.

## 10. Deliberate evolution

Compatibility, deprecation, migration, and lifecycle rules are designed alongside features.
