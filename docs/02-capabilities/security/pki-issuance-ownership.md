# PKI-issuance ownership and trial readiness

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Accountable owner | Certificate issuance owner, initially exercised by Foundation maintainers |
| Architecture reviewer | Foundation architecture review |
| PKI/cryptography reviewer | Independent qualified review for proofing, POP, profiles, CA/key operations, lifecycle, and authority nonclaims |
| Platform/privacy reviewer | Foundation platform enrollment, network, privacy, accessibility, and deployment review |
| Evidence reviewer | Foundation issuance conformance, interoperability, durability, recovery, and performance review |

## Ownership duties

The owner maintains enrollment states, typed intent, authority and proofing boundaries, request/POP/attestation semantics, profile and issuance policy, protocol adapters, CA ledger and signing transaction, delivery/install/activation evidence, renewal/rekey/replacement/revocation, dependencies, source and quality reviews, conformance, benchmarks, and dossier scope. CA, key-provider, platform, protocol, deployment, status/transparency, and consumer owners retain their narrower configuration and operational responsibilities.

## Bounded trial plan

A later trial may use a disposable private hierarchy, synthetic identities and names, isolated DNS/HTTP/status services, non-production accounts, software keys and explicitly approved test hardware/remote-key partitions. It may exercise ACME, EST, SCEP, CMP, Windows enrollment, Apple-managed enrollment, and out-of-band fixtures only where exact profiles and providers are pinned. Scenarios include valid and hostile requests, POP/attestation mismatch, authorization expiry, pending/denied orders, policy rewriting, duplicate/replayed messages, response-without-install, key mismatch, activation rollback, renewal windows and deadlines, revocation races, CA/HSM loss, backup/restore, clone detection, serial monotonicity, and hierarchy rotation.

The trial uses the [foundation trial template](../../05-governance/implementation-trials/trial-template.md). It makes no production CA, trust-store, DNS, device-management, service, key, HSM partition, certificate, or account change; performs no public issuance; and does not select permanent Rust APIs, crates, providers, default profiles, retry policies, performance budgets, packaging, or release support.

Stop conditions include unauthorized name/profile issuance, private-key disclosure, copied unapproved claims, POP/attestation bypass, replay acceptance, issuance without durable ledger commit, serial rollback or active clone, cross-tenant/key confusion, delivery reported as installation, installation reported as activation, stale continuity authorization, renewal storm, failed revocation reconciliation, uncontrolled network reach, sensitive log leakage, or inability to account for generated keys and certificates.

**RM-PKI-ISSUANCE-OWNER-0001:** Promotion and trial records MUST name accountable people for every claimed protocol, platform, CA, key provider, proofing, policy, installation, activation, status/transparency, and recovery context, including reviewer independence and qualifications.

**RM-PKI-ISSUANCE-OWNER-0002:** Trial hypotheses MUST distinguish intent, authentication/proofing, authorization, POP/attestation, request construction, policy evaluation, CA commit/signing, protocol delivery, verification, key-bound installation, activation, relying-party acceptance, renewal, replacement, and revocation.

**RM-PKI-ISSUANCE-OWNER-0003:** This bounded plan is evidence only and MUST NOT authorize implementation, public issuance, production trust/key/CA/HSM/device-management/service mutation, provider dependencies, packaging, or release.

**RM-PKI-ISSUANCE-OWNER-0004:** Closeout MUST account for every generated key, request, authorization, order, certificate, serial, ledger event, status/transparency object, store entry, service binding, account, network fixture, provider cache, backup, log, trace, and report; only verified disposable assets may be removed.
