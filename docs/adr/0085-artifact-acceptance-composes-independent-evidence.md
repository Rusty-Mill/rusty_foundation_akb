# ADR-0085: Artifact acceptance composes independent evidence

**Status:** Accepted  
**Date:** 2026-08-08

## Context

Platforms and ecosystems expose convenient “signed,” “trusted,” “notarized,” or “verified” results, but those may cover different bytes, signers, times, logs, provenance, reputation, and policy. Treating any one as authority to install, execute, load, publish, or display creates confused-deputy and stale-evidence failures.

## Decision

Artifact acceptance is a versioned product-policy decision over independently reported structural/digest integrity, signature cryptography, signer key/certificate trust and role, trusted time, transparency, provenance/SBOM/reproducibility, platform assessment, version/channel/target constraints, freshness, and action authority. Results retain inputs, generations, successes, failures, unknowns, expiry, and nonclaims. The bytes acted upon must exactly match the verified subject.

## Consequences

- Signature validity never means safe, malware-free, current, or authorized.
- Offline, unavailable, unsupported, indeterminate, and policy-rejected outcomes remain distinct.
- Cache and lifecycle rules include every material policy and evidence generation.
- Products may select different policies without weakening the common evidence model.

