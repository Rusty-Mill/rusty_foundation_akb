# ADR-0161: Random-output tests do not certify unpredictability

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill architecture governance

## Context

Secure-random integrations must detect wrong providers, incomplete fills, fallback, lifecycle duplication, and output disclosure. It is tempting to use uniqueness checks, statistical batteries, entropy estimates, compressibility, or output fingerprints as proof that the result is cryptographically secure. Finite output samples cannot establish unpredictability, correct source selection, module boundaries, resistance to state compromise, or safe behavior across forks and VM clones. Retaining derived fingerprints also expands exposure of secret-quality output.

## Decision

Secure-random assurance is based on exact authoritative provider/module/configuration provenance, correct fail-closed API integration, lifecycle evidence, and scoped cryptographic validation claims. Output statistical tests may be used only as bounded investigation triggers for gross integration faults. They are not conformance pass criteria for unpredictability and cannot create a security or certification claim.

Conformance and benchmark artifacts must not retain random bytes or output-derived hashes, checksums, prefixes, uniqueness sets, compressibility results, or fingerprints. Functional tests may use controlled instrumented providers and buffer-state canaries that are not derived from successful cryptographic output.

## Options considered

- Treat statistical batteries as certification: intuitive but scientifically and cryptographically unsound.
- Omit all output-path diagnostics: avoids overclaiming but weakens detection of obvious integration defects.
- Use provider/provenance evidence plus bounded noncertifying diagnostics: supports defect detection without misrepresenting security.

## Consequences

- Provider/source verification and failure injection become primary conformance evidence.
- Lifecycle cases such as boot readiness, fork, clone, snapshot, and reinitialization require explicit provider evidence.
- Benchmark tooling cannot persist output-derived artifacts for convenience.
- Suspicious statistical observations block or trigger investigation but a clean observation does not prove security.

## Verification

The [secure-random traceability](../02-capabilities/security/random-traceability.md), [quality review](../02-capabilities/security/random-cross-cutting-review.md), and [bounded trial plan](../02-capabilities/security/random-ownership.md) preserve this evidence boundary.
