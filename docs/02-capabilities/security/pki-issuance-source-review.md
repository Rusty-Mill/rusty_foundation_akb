# PKI-issuance source review

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Expires | On applicable RFC/profile update, supported platform enrollment change, CA/provider change, or 2027-02-08, whichever occurs first |
| Reviewer | Certificate issuance owner |
| Open blocking findings | None for dossier reviewability; exact profiles, providers, platforms, proofing methods, CA policy, and deployment paths remain trial inputs |

| Source | Class and reviewed status | Proposition supported | Impact and limitation |
|---|---|---|---|
| RFC Editor [RFC 8555](https://www.rfc-editor.org/rfc/rfc8555) | IETF standards-track ACME specification; reviewed 2026-08-08 | account, order, authorization, challenge, finalize, certificate, and revocation resource lifecycle | ACME challenge success authorizes only the selected identifier/order under the selected CA policy; it does not prove general identity, application authority, installation, or activation |
| RFC Editor [RFC 9773](https://www.rfc-editor.org/rfc/rfc9773) | IETF standards-track ACME Renewal Information specification; reviewed 2026-08-08 | CA-suggested renewal windows and replacement reporting | ARI is scheduling evidence, not execution authority. The client retains applicability validation, randomized scheduling, deadline, retry, policy, key, install, activation, and rollback responsibility |
| RFC Editor [RFC 7030](https://www.rfc-editor.org/rfc/rfc7030), [RFC 8894](https://www.rfc-editor.org/rfc/rfc8894), and [RFC 9480](https://www.rfc-editor.org/rfc/rfc9480) | IETF enrollment protocol specifications; reviewed 2026-08-08 | EST, SCEP, and CMP have distinct bootstrap, authentication, proof-of-possession, pending, polling, confirmation, and recovery semantics | common lifecycle mapping must preserve protocol-specific states and weaknesses; apparent request/response similarity is not semantic equivalence |
| RFC Editor [RFC 2986](https://www.rfc-editor.org/rfc/rfc2986) | IETF informational PKCS #10 request syntax; reviewed 2026-08-08 | signed certification-request representation and proof that the requester can sign with the corresponding private key | a valid signature proves neither real-world identity nor authority for copied names, extensions, profile selection, issuance, installation, or use |
| Microsoft [Certificate Enrollment API](https://learn.microsoft.com/en-us/windows/win32/seccertenroll/certificate-enrollment-api) and [`IX509Enrollment::Enroll`](https://learn.microsoft.com/en-us/windows/win32/api/certenroll/nf-certenroll-ix509enrollment-enroll) | Microsoft platform contracts; reviewed 2026-08-08 | Windows enrollment composition, request submission, response handling, and installation status | successful method return does not necessarily establish response installation; exact disposition, enrollment status, context, store, key association, policy, and platform generation require observation |
| Apple [Managed Device Attestation](https://support.apple.com/guide/deployment/managed-device-attestation-dep28afbde6a/web) and [ACME certificate payload](https://support.apple.com/guide/deployment/acme-certificate-payload-settings-dep5d180e4bf/web) | Apple deployment contracts; reviewed 2026-08-08 | managed-device attestation evidence and declarative/device-management ACME enrollment controls | deployment scope, supported OS/device/management state, attestation claims, hardware binding, renewal, installation, and relying-party policy remain explicit; attestation is not general identity or authorization |

**RM-PKI-ISSUANCE-SOURCE-0001:** Trial evidence MUST bind exact protocol/profile/update/errata set, platform/SDK/provider/CA generation, authentication and proofing method, request and certificate profile, key provider/protection, policy, network, clock, retry, installation target, activation consumer, toolchain, and artifact provenance.

**RM-PKI-ISSUANCE-SOURCE-0002:** Standards requirements, platform documentation, CA policy, observed provider/protocol behavior, and Rusty Mill guarantees MUST remain separately identified.

**RM-PKI-ISSUANCE-SOURCE-0003:** Protocol completion, request signature validity, attestation acceptance, CA issuance, delivery, store installation, service activation, relying-party acceptance, and domain authorization MUST NOT be collapsed into one success state.

**RM-PKI-ISSUANCE-SOURCE-0004:** Renewal guidance, including ARI, MUST be treated as bounded scheduling input; it MUST NOT silently grant execution authority, waive local policy, reuse stale continuity evidence, or imply successful replacement.

**RM-PKI-ISSUANCE-SOURCE-0005:** A source, protocol, profile, CA policy, platform/provider, proofing, key-protection, trust/status/transparency, installation, or consumer change invalidates affected evidence until its semantic, security, interoperability, lifecycle, and performance impact is classified.
