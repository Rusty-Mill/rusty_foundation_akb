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

Release artifacts and their conformance/benchmark reports use the [signed-artifact and provenance evidence model](../02-capabilities/signed-artifacts/README.md). Signature validity, signer trust, trusted time, transparency, provenance, reproducibility, and release authorization remain separately reportable gates.

Repository-scale structural inventory and readiness claims use the [consistency, traceability, and readiness model](consistency-readiness/README.md). A conformance or benchmark file proves planned evidence structure only; direct requirement links and qualified results are required before provider, profile, release, or Stable-promotion claims.

Publication, promotion, mirroring, advisories, revocation, and emergency exercises use the [repository-operations evidence model](repository-operations/README.md). A stable release claim binds an immutable artifact digest, publication record, channel-metadata generation, required evidence, and unresolved exceptions rather than a mutable tag or web page.

Implementation change and repository evidence follow the [software development compliance model](../05-governance/software-development/compliance-evidence.md). Development-standard results identify exact rules, repository profile, source/tool/configuration generations, review/test/benchmark evidence, and exceptions; a generic “standards compliant” label is insufficient.
