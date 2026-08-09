# PKI-validation source review

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Expires | On RFC/profile update, supported OS/kernel/SDK, provider/library/store, trust program/policy, status/network behavior, or identity-profile change, or 2027-02-08, whichever occurs first |
| Reviewer | PKI validation owner |
| Open blocking findings | None for dossier reviewability; exact RFC update set, profiles, providers, platform generations, stores, policies, and network/status matrices remain trial inputs |

| Source | Class and reviewed status | Proposition supported | Impact and limitation |
|---|---|---|---|
| RFC Editor [RFC 5280](https://www.rfc-editor.org/rfc/rfc5280) and its listed update chain | IETF standards-track base plus amendments; reviewed 2026-08-08 | certificate/CRL profile, extension semantics, path validation, internationalized-name processing | `RFC 5280` alone is not a complete revision claim: the RFC Editor currently lists multiple updating RFCs. Each selected profile binds the applicable base, updates, errata, algorithms, and consumer policy; this standard does not select platform trust sources or authorize use |
| RFC Editor [RFC 6960](https://www.rfc-editor.org/rfc/rfc6960) | IETF standards-track OCSP specification; reviewed 2026-08-08 | request/response, responder authorization, signatures, status and time evidence | protocol input, not a universal revocation policy or proof of non-compromise; nonce, stapling, freshness, caching, privacy, failure, and responder trust remain selected profile concerns |
| RFC Editor [RFC 9525](https://www.rfc-editor.org/rfc/rfc9525) | IETF standards-track TLS service-identity profile; reviewed 2026-08-08 | typed service-reference identity, presented-identifier matching, wildcard and application-service rules for TLS | consumer-profile evidence, not generic certificate identity semantics; other DNS/IP/URI/mailbox/application/device purposes require their own exact current profiles |
| Microsoft [`CertGetCertificateChain`](https://learn.microsoft.com/en-us/windows/win32/api/wincrypt/nf-wincrypt-certgetcertificatechain) and [`CertVerifyCertificateChainPolicy`](https://learn.microsoft.com/en-us/windows/win32/api/wincrypt/nf-wincrypt-certverifycertificatechainpolicy) | Microsoft platform contracts; reviewed 2026-08-08 | provider chain engine/cache/additional stores, time/usage/revocation flags, and distinct policy verification | exact Windows build/engine/store scopes/disallowed roots/retrieval/cache/flags/policy and observable alternate-path/rejection evidence require testing; provider success cannot override Rusty Mill policy |
| p11-kit [trust policy module](https://p11-glue.github.io/p11-glue/p11-kit/manual/trust-module.html) and [trust tool/policy store](https://p11-glue.github.io/p11-glue/p11-kit/manual/trust.html) | project provider contracts; reviewed 2026-08-08 | anchors, blocklists, attached extensions and purpose policy exposed as PKCS #11 objects and extracted views | Linux distribution/container/library integration varies; extracted bundles can lose distrust or policy metadata, so exact provider/version/config/store view and consuming library semantics require evidence |
| Apple [`SecTrustEvaluateWithError`](https://developer.apple.com/documentation/security/sectrustevaluatewitherror(_:_:)) and [Trust](https://developer.apple.com/documentation/security/trust) | Apple platform contracts; reviewed 2026-08-08 | policy-bound trust evaluation over certificate inputs, system/keychain/explicit anchors, verification date and network behavior | exact macOS/SDK/trust settings/policy/anchors/network-fetch configuration/provider cache and blocking/async behavior require evidence; result does not establish application authorization |

**RM-PKI-SOURCE-0001:** Trial evidence MUST bind exact RFC/profile/errata/update set, OS/kernel/SDK, provider/library artifact, trust sources/store scopes/generation/precedence, policy/purpose/identity, time/clock, algorithm policy, status/network/cache, overrides/pins, toolchain/build, corpus, and artifact provenance.

**RM-PKI-SOURCE-0002:** Living sources, trust programs/stores, provider behavior, and RFC update chains MUST be release- or revision-bound where possible; a familiar API, RFC number, platform, root bundle, or `trusted` result MUST NOT prove unchanged semantics or evidence.

**RM-PKI-SOURCE-0003:** Standards/profile requirements, platform/provider documentation, observed path/result behavior, trust-program policy, corpus expected results, and Rusty Mill guarantees MUST remain separately identified.

**RM-PKI-SOURCE-0004:** General certificate/path standards MUST NOT substitute for the exact consumer identity, purpose, revocation, transparency, pinning, or authorization profile; profile absence is unsupported rather than guessed.

**RM-PKI-SOURCE-0005:** A standards/profile/errata, trust source/store/program, provider/library/platform, algorithm policy, clock, network/status/cache, pin/override, or corpus change invalidates affected evidence until parsing, construction, validation, identity, status, lifecycle, interoperability, and performance impact is classified.
