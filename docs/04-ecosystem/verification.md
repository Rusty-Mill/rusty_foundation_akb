# Conformance and benchmark architecture

Verification is a first-class product, not backend-local test code.

## Conformance suite

- Contract assertions are backend-neutral and traceable to normative requirements.
- Provider adapters supply platform-specific setup and evidence without changing expected semantics.
- Tests cover happy paths, failure paths, boundaries, cancellation, concurrency, cleanup, security, and declared degradation.
- Results identify capability version, profile, provider, OS, architecture, configuration, and environment.
- A conformance claim is an immutable, machine-readable report linked to source and build provenance.

## Benchmark suite

- Measure native baseline, abstraction path, and end-to-end workload separately.
- Track latency distributions, throughput, allocations, memory, CPU, startup, binary size, and power where relevant.
- Use statistically defensible repetitions and publish noise/environment metadata.
- Define regression budgets per capability; do not compare unlike guarantees.
- Maintain representative Windows, Linux, and macOS runners, including architecture variants as support expands.

## Release gates

Stable releases require required-profile conformance, security checks, compatibility checks, and benchmark results within accepted budgets. Exceptions require a time-bounded ADR with owner and remediation plan.
