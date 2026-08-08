# CA operation and lifecycle

**RM-PKI-CA-0001:** CA identity binds hierarchy/namespace, legal/organizational owner, certificate-policy/practice documents, root/intermediate/RA/status/log services, issuer certificate/key generations, profiles, trust distributions, and operating environment.

**RM-PKI-CA-0002:** Root, intermediate/subordinate, issuing, registration authority, validation authority, OCSP/status, CRL, timestamp, CT/log, audit, and recovery roles are separately attenuated with quorum and offline/online boundaries.

**RM-PKI-CA-0003:** CA key ceremonies specify generation/import, algorithm/parameters, hardware/module and attestation/certification, quorum/roles, environment, entropy, backup/escrow where allowed, public-key verification, certificate construction/signing, activation, audit, and destruction.

**RM-PKI-CA-0004:** The issuance ledger durably records accepted/rejected/pending transactions, serials, exact certificates/requests/authorization/profile, signer key generation, timestamps, revocation/status, and audit correlation. Restore prevents serial/transaction rollback and duplicate issuance.

**RM-PKI-CA-0005:** Issuance services enforce rate/quantity, namespace, duplicate, high-risk profile, approval, policy, HSM/provider, lint, CT/status, and anomaly controls before release; failover cannot bypass them.

**RM-PKI-CA-0006:** Intermediate/root rotation and hierarchy migration define old/new trust distribution, cross-signing constraints, path ambiguity, issuance cutover, overlap, relying-party compatibility, status/AIA/CDP, algorithm transition, rollback limits, and end-of-life.

**RM-PKI-CA-0007:** CA backup/recovery protects key material and ledger/config/audit separately, uses split knowledge/quorum where selected, prevents cloned active issuers and serial rollback, and proves recovery in isolated drills.

**RM-PKI-CA-0008:** Compromise response identifies suspected key/service/time/scope, halts issuance, preserves evidence, rotates/revokes/distrusts, republishes status/metadata, replaces affected certificates, coordinates relying parties, communicates unknowns, and conducts review.

**RM-PKI-CA-0009:** CA termination defines issuance stop, final CRL/status service lifetime, key destruction/archival, repository and audit retention, customer/subject notification, trust-store removal, successor/escrow if any, and legal/policy obligations.

**RM-PKI-CA-0010:** External audits, certification, CPS conformance, and provider attestations are scoped dated evidence, not blanket proof that every issuance followed policy.

