# ADR-0013: Profiles select exact contracts, not domains

**Status:** Accepted  
**Date:** 2026-08-08  
**Deciders:** Rusty Mill founders

## Context

Seed profiles previously listed broad domains such as filesystem, security, and observability. A domain name cannot be resolved, versioned, tested, or used to determine authority and quality requirements. Declaring a “Desktop” profile before its domains are specified also risks implying completeness.

## Decision

Profiles select exact versioned capabilities and platform services with independent behavioral, quality, authority, interaction, budget, degradation, and evidence constraints. Required, conditional, optional, and prohibited members have explicit resolution behavior. Current manifests use the `foundation` family to signal known workload gaps.

Profiles do not add domain bundles to the capability graph. Services are resolved compositions, not capability nodes. A satisfied resolution produces an immutable report binding the request, deployment facts, policy, authority summary, providers, evidence, disclosures, and selection rationale.

## Options considered

### Broad domain bundles

Readable but ambiguous, overinclusive, and impossible to verify precisely.

### Feature flags tied to crates

Convenient for packaging but couples workload semantics to an implementation layout that does not yet exist.

### Exact contract manifests

More detailed, but resolvable, evidence-linked, and independent of crate and OS structure.

## Consequences

- Profile manifests grow incrementally as domains mature.
- A profile name does not imply capabilities that are not listed.
- Packaging features may later be derived from a resolved profile, never define it.
- Resolution failures can identify exact unsatisfied constraints.

## Verification

Use catalog permutation, missing/transitive requirement, prohibited-side-effect, stale-evidence, authority mismatch, interaction mismatch, and deterministic replay cases against every profile manifest.

