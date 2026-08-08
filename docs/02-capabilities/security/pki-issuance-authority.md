# Identity proofing and enrollment authority

**RM-PKI-ISSUANCE-AUTHORITY-0001:** Enrollment authenticates an account/principal/device/workload using an explicitly selected method and channel, then separately authorizes certificate profile, identifiers, purpose, validity, key properties, issuer, quantity/rate, store/scope, and renewal/revocation rights.

**RM-PKI-ISSUANCE-AUTHORITY-0002:** Human identity proofing, enterprise-directory membership, device management enrollment, hardware attestation, DNS/HTTP/email identifier control, existing certificate continuity, shared bootstrap secret, administrator approval, and workload identity remain typed evidence with issuer-specific policy.

**RM-PKI-ISSUANCE-AUTHORITY-0003:** Identifier validation binds exact typed identifier, validation method, challenge/token, responder/control point, perspective/location, authorization account, start/completion, expiry/reuse, and policy generation. DNS name control does not prove legal entity or application authorization.

**RM-PKI-ISSUANCE-AUTHORITY-0004:** Enrollment templates/profiles are policy objects, not authority by name. Resolution binds immutable template identifier/generation, allowed requester/enroller roles, subject/SAN construction, extensions, key/algorithm/attestation, validity, issuance approval, renewal, archival, export, and revocation.

**RM-PKI-ISSUANCE-AUTHORITY-0005:** On-behalf-of enrollment identifies subject, requester, enrollment agent/delegation chain, allowed profile/identifiers, proofing source, approvals, and audit. An agent cannot request its own authority into the certificate.

**RM-PKI-ISSUANCE-AUTHORITY-0006:** Automated enrollment uses noninteractive workload/device authority whose bootstrap, activation, rotation, revocation, cloning/snapshot, recovery, and rate limits are explicit. Environment variables and machine labels are not enrollment authority.

**RM-PKI-ISSUANCE-AUTHORITY-0007:** Approval decisions bind exact request/public key/claims, subject and proofing evidence, policy/profile generation, approver role, reason, expiry, and constraints. Approval of one request cannot authorize a modified CSR or replay.

**RM-PKI-ISSUANCE-AUTHORITY-0008:** Enrollment authority establishes only permission for the CA to consider issuance. It does not guarantee issuance, certificate trust by a relying party, current key possession, protocol authentication, or application authorization.

