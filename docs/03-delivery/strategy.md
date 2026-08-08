# Versioning, packaging, distribution, and updates

**Status:** Directional; details require RFCs before implementation.

## Versioning

- SemVer for independently published crates and specification packages.
- Explicit compatibility policy for behavioral contracts, not only Rust signatures.
- Capability and profile versions are recorded in conformance evidence.
- Coordinated releases may use a release-train label without forcing every repository to share a version.

## Packaging and distribution

- Rust libraries: crates.io where public distribution is appropriate, with signed/tagged source releases on GitHub.
- Tools and applications: native packages/installers per platform plus checksummed archives when useful.
- Specifications and schemas: immutable versioned artifacts suitable for offline verification.
- Debug symbols, SBOMs, licenses, provenance attestations, and checksums accompany release artifacts.

## Updates

- Libraries update through normal dependency resolution and lockfile review.
- Applications use signed manifests, authenticated transport, staged rollout, rollback, and downgrade protection where required.
- Update policy is separate from update mechanism so products can select cadence and trust roots.
- No silent weakening of capability, security, or profile requirements during update.

## Supply chain

- Pin CI actions and release tooling; minimize third-party dependencies.
- Require reproducible builds where feasible, hermetic release inputs, dependency review, license policy, vulnerability response, and least-privilege publishing credentials.
- Generate SBOMs and provenance attestations; sign releases and verify them before installation.
- Define maintainer recovery and key-rotation procedures before the first production release.

The [signed-artifact and provenance foundation](../02-capabilities/signed-artifacts/README.md) defines the exact signed-view, ceremony, trusted-time, transparency, provenance, verification-policy, lifecycle, conformance, and benchmark evidence required to make these commitments testable.

The [package installation and update-orchestration foundation](../02-capabilities/package-management/README.md) defines coherent authenticated update snapshots, package/installed state, native dependency resolution, immutable deployment plans, journaled staging/commit/reconciliation, bounded hooks and migrations, accessible rollout/health, compensating rollback, recovery, conformance, and benchmarks. Repository publication and operations remain a separate delivery responsibility.

The [repository publication and security-response foundation](../04-ecosystem/repository-operations/README.md) closes that delivery boundary with immutable release records, digest-preserving channel promotion, authenticated repository snapshots, untrusted mirrors, revisioned advisories, coordinated disclosure, revocation/emergency response, retention/backup, conformance, and operational objectives. Concrete providers and wire profiles remain RFC choices.

## Compatibility channels

`experimental`, `preview`, and `stable` channels communicate contract maturity. Channel promotion is evidence-based and never inferred from elapsed time.
