# PKI platform research

| Platform | Primary mechanisms | Architectural observations |
|---|---|---|
| Windows | CryptoAPI certificate stores, chain engines, `CertGetCertificateChain`, `CertVerifyCertificateChainPolicy`, CNG signature providers | Chain building accepts additional stores and provider-managed engines/caches; policy verification is a distinct step. Machine/user/enterprise stores, disallowed roots, automatic retrieval, revocation flags, usage policy, cache, and provider updates affect results and require exact evidence. |
| Linux | Distribution/application trust bundles, p11-kit trust module, crypto-library path validators, NSS/OpenSSL/GnuTLS ecosystems | There is no single universal trust API or store. p11-kit can expose anchors, blocklists, and purpose policy as PKCS #11 objects, but extraction formats may lose distrust/policy information. Distribution, container, enterprise, application, and library/provider generations must be explicit. |
| macOS | Security framework `SecCertificate`, `SecPolicy`, `SecTrust`, system/user keychains and trust settings | A trust object binds certificates and policies; evaluation may search keychains, explicit anchors, system sources, and network intermediates. Verification date and network fetching are configurable; evaluation can block on network, so asynchronous operation is part of the contract. |

## Standards and primary sources

- [RFC 5280: Internet X.509 PKI Certificate and CRL Profile](https://www.rfc-editor.org/rfc/rfc5280)
- [RFC 6960: Online Certificate Status Protocol](https://www.rfc-editor.org/rfc/rfc6960)
- [Microsoft: CertGetCertificateChain](https://learn.microsoft.com/en-us/windows/win32/api/wincrypt/nf-wincrypt-certgetcertificatechain)
- [Microsoft: CertVerifyCertificateChainPolicy](https://learn.microsoft.com/en-us/windows/win32/api/wincrypt/nf-wincrypt-certverifycertificatechainpolicy)
- [p11-kit trust policy module](https://p11-glue.github.io/p11-glue/p11-kit/manual/trust-module.html)
- [p11-kit trust tool and policy store](https://p11-glue.github.io/p11-glue/p11-kit/manual/trust.html)
- [Apple: SecTrustEvaluateWithError](https://developer.apple.com/documentation/security/sectrustevaluatewitherror(_:_:))
- [Apple: Trust](https://developer.apple.com/documentation/security/trust)

## Evidence gaps

- Cross-signed/alternate-path preference, name/policy constraints, purpose/EKU, critical-extension, algorithm, distrust, and anchor handling by platform/build/provider.
- System/enterprise/user/application store precedence, update notification, cache invalidation, container/sandbox views, and user override lifecycle.
- Revocation mode, stapling, OCSP/CRL cache/freshness, network retrieval/privacy/proxy/offline behavior, and hard/soft failure across profiles.
- Reference identity matching, internationalized names, wildcards, IP/URI/email/application identities, pinning, historical validation, transparency, and policy evolution.
