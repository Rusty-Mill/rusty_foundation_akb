# Issuance policy and certificate construction

**RM-PKI-ISSUANCE-POLICY-0001:** Issuance policy is immutable/versioned and binds issuer/key generation, certificate profile/purpose, subject/SAN sources, required proofing and POP/attestation, algorithms/key constraints, extensions, validity/backdating, serial policy, CT/status/publication, approvals, rate/quantity, and audit.

**RM-PKI-ISSUANCE-POLICY-0002:** The CA constructs certificate fields from authoritative policy and accepted evidence. It never blindly copies a CSR subject, SAN, usage, constraints, policy OID, CA bit, name constraints, AIA/CDP, custom extension, or validity request.

**RM-PKI-ISSUANCE-POLICY-0003:** End-entity, subordinate/intermediate CA, root, cross-certificate, OCSP responder, timestamp authority, code/document signing, TLS server/client, email, device, and workload profiles are distinct and cannot be widened by request attributes.

**RM-PKI-ISSUANCE-POLICY-0004:** Certificate validity binds CA clock/quality, policy maximum, authorization/proofing freshness, issuer validity, key/provider lifetime, ecosystem limits, requested service horizon, and renewal overlap. Backdating is explicit and bounded.

**RM-PKI-ISSUANCE-POLICY-0005:** Serial allocation is issuer-unique and unpredictable where policy requires, durable across concurrency/restart/restore, bounded, and never reused. Failure after allocation may leave a documented gap.

**RM-PKI-ISSUANCE-POLICY-0006:** Before signing, the issuer revalidates request integrity/POP, authorization/approval freshness, subject/identifier control, template/profile generation, algorithm/key/attestation, duplicate/conflict/rate policy, issuer/key availability, and transparency/status obligations.

**RM-PKI-ISSUANCE-POLICY-0007:** Issuance is an auditable opaque CA key operation binding TBSCertificate bytes, issuer/key/policy generations, signing plan, transaction/authorization, ceremony, timestamp, output certificate digest, and publication/status actions.

**RM-PKI-ISSUANCE-POLICY-0008:** Post-issuance lint/structural/profile checks compare exact certificate to plan before release. A mismatch quarantines the certificate and invokes incident/revocation policy; it is not repaired in place.

**RM-PKI-ISSUANCE-POLICY-0009:** CT/precertificate and other public-log workflows explicitly prevent poisoned/final certificate confusion, SCT substitution, log privacy leaks, duplicate issuance, and release before required evidence is complete.

