# PKI issuance conformance

Every report binds client/server/RA/CA/provider/protocol versions, profile/policy/trust generations, subject/scope, key protection, clocks/network, fixtures, and result evidence.

**RM-PKI-ISSUANCE-CONFORMANCE-0001:** Request corpora cover PKCS #10 and selected protocol formats with valid and malformed ASN.1/JSON/CMS, duplicate/conflicting/unknown extensions, Unicode/names, weak/invalid keys/algorithms/signatures, oversized inputs, canonicality, public-key substitution, and requested-versus-issued differences.

**RM-PKI-ISSUANCE-CONFORMANCE-0002:** Authority tests cover every authentication/proofing/identifier challenge/template/agent/approval route, replay/substitution, stale/revoked evidence, cross-account/tenant/profile/identifier escalation, DNS/HTTP control loss, device cloning/snapshot, and nonclaims.

**RM-PKI-ISSUANCE-CONFORMANCE-0003:** POP/attestation tests cover fresh and replayed challenges, wrong request/key/channel, signature/agreement/indirect mechanisms, exportable/software/hardware/remote keys, invalid/unknown attestation roots/firmware/properties, privacy redaction, and loss of provider.

**RM-PKI-ISSUANCE-CONFORMANCE-0004:** Issuer tests cover subject/SAN/usage/constraints/policy filtering, validity/backdating, serial uniqueness across concurrency/crash/restore, lint failures, HSM/approval/rate limits, precertificate/CT/final confusion, status publication, partial release, and duplicate issuance.

**RM-PKI-ISSUANCE-CONFORMANCE-0005:** Protocol tests cover ACME nonce/account/order/authz/challenge/finalize/key-change/ARI, EST bootstrap/enroll/reenroll/CSR attributes, SCEP/CMP pending/poll/resync, redirects/proxies/RA, malformed chains, rate/retry, offline exchange, lost responses, cancellation, and idempotent reconciliation.

**RM-PKI-ISSUANCE-CONFORMANCE-0006:** Delivery/install tests cover request/certificate/public-key mismatch, malicious candidate chains, wrong store/scope/principal, key association/access/export policy, duplicate/replaced certificates, locked/unavailable stores, transaction crash, and activation/distribution failure.

**RM-PKI-ISSUANCE-CONFORMANCE-0007:** Renewal tests cover same-key/rekey/modify/replace, old-key continuity and loss, issuer guidance, clock/sleep/offline, fleet stampede, expiring/expired/revoked credentials, algorithm/provider migration, overlap/session/cache, service reload, failed activation, mass revocation, and old-key destruction.

**RM-PKI-ISSUANCE-CONFORMANCE-0008:** CA lifecycle exercises root/intermediate/issuer/status rotation, cross-sign/path ambiguity, ledger backup/restore and serial rollback prevention, cloned issuer detection, key compromise, issuance halt, mass replacement, termination, audit/certification scope, and disaster recovery.

**RM-PKI-ISSUANCE-CONFORMANCE-0009:** Cross-platform evidence covers Windows user/machine/template and out-of-band enrollment, Apple managed SCEP/ACME/attestation where available, portable protocol clients, Linux store/service diversity, and declared unavailable/degraded features.

