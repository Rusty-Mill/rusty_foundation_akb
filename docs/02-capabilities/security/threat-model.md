# Security foundation threat model

**Status:** Draft baseline

## Protected properties

- Authority cannot be forged, amplified, confused across namespaces, or silently broadened.
- Secret and random material is not disclosed through output, diagnostics, memory reuse, or telemetry.
- Provider claims cannot exceed native enforcement or tested evidence.
- A compromised component is limited to its explicitly granted authority where the deployment platform can enforce that boundary.

## Trust boundaries

The principal boundaries are application-to-common API, common API-to-provider, safe Rust-to-unsafe/native code, process-to-process delegation, application-to-OS enforcement, and build/release-to-installed artifact. Remote identity protocols and hostile kernels are outside this initial slice.

## Threats and required treatments

| Threat | Treatment |
|---|---|
| Confused deputy | Explicit target authority; bind requests to resource, operation, audience, and caller context |
| Ambient-authority capture | Explicit opt-in and disclosure; do not infer authority from strings or current directory |
| Authority amplification | Validate derivation as subset; fail closed on unrepresentable constraints |
| Namespace/identity confusion | Typed issuer-scoped identifiers and canonical internal comparison rules |
| TOCTOU authorization race | Enforce at operation; use handle-relative/native atomic primitives where available |
| Stale or revoked context | Snapshot timestamps, validity bounds, revocation semantics, operation-time enforcement |
| Provider substitution | Signed/provenanced provider evidence and policy-constrained selection |
| Secret leakage | Redacted diagnostics, zeroization claims only when proven, no secret serialization by default |
| Weak or repeated randomness | OS cryptographic source, exact-fill semantics, fork/snapshot test strategy, fail closed |
| Denial of service | Bounded requests, cancellation/readiness policy, quotas, and rate-aware diagnostics |

## Non-guarantees

The portable model cannot protect against a compromised kernel, physical memory attacks, platform bugs, an application that deliberately exports its authority, or rights retained through native aliases outside Rusty Mill's control. Such conditions belong in deployment threat models and provider disclosures.

