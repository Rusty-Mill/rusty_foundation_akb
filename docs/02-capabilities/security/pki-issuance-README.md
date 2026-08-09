# Certificate issuance, enrollment, and CA-lifecycle foundations

| Field | Value |
|---|---|
| Status | Draft domain analysis |
| Purpose | Request, authorize, issue, deliver, install, renew, rekey, revoke, and operate certificates without confusing key possession, identity evidence, or CA policy |

```mermaid
flowchart LR
    Subject["Subject / workload / device"] --> Key["Opaque key generation"]
    Key --> POP["Proof of possession"]
    Identity["Vetting · account · device · name control"] --> Authz["Enrollment authorization"]
    POP --> Request["Immutable certificate request"]
    Authz --> Policy["CA profile + issuance policy"]
    Request --> Policy
    Policy --> Issue["Audited CA signing transaction"]
    Issue --> Deliver["Certificate + chain/status evidence"]
    Deliver --> Install["Key-bound store installation"]
    Install --> Renew["Renew · rekey · replace · revoke"]
```

## Conclusions

- Identity vetting, account/device authentication, identifier control, enrollment authorization, key proof-of-possession, attestation, certificate issuance, and relying-party authorization are independent evidence.
- A certificate request is an immutable signed set of requested claims. The CA constructs the issued certificate from accepted policy; it never blindly copies request attributes.
- Initial enrollment, renewal, rekey, modification, replacement, recovery, and revocation are distinct operations with explicit continuity and authority.
- Keys remain opaque operation capabilities by default. Server-generated keys, archival, escrow, export, and recovery require separately selected high-risk profiles.
- ACME, EST, SCEP, CMP, Windows enrollment, Apple managed enrollment, and out-of-band workflows map to common states while preserving protocol-specific guarantees and gaps.

## Documents

- [Enrollment model and lifecycle](pki-issuance-enrollment.md)
- [Identity proofing and enrollment authority](pki-issuance-authority.md)
- [Requests, proof-of-possession, and attestation](pki-issuance-requests.md)
- [Issuance policy and certificate construction](pki-issuance-policy.md)
- [Protocols, delivery, and installation](pki-issuance-protocols.md)
- [Renewal, rekey, replacement, and revocation](pki-issuance-renewal.md)
- [CA operation and lifecycle](pki-issuance-ca-operations.md)
- [Security, privacy, and accessibility](pki-issuance-security-accessibility.md)
- [Platform and protocol research](pki-issuance-platform-research.md)
- [Conformance](pki-issuance-conformance.md)
- [Benchmarks](pki-issuance-benchmarks.md)
- [Assertion and benchmark traceability](pki-issuance-traceability.md)
- [Dependency and lifecycle composition](pki-issuance-dependencies.md)
- [Cross-cutting quality review](pki-issuance-cross-cutting-review.md)
- [Current source review](pki-issuance-source-review.md)
- [Ownership and bounded trial plan](pki-issuance-ownership.md)
- [Promotion-unit readiness dossier](pki-issuance-readiness-review.md)
