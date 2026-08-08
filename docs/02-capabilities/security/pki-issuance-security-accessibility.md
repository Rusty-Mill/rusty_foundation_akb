# Security, privacy, and accessibility

**RM-PKI-ISSUANCE-CROSS-0001:** Requests, names, extensions, attestation, protocol messages, CA chains, status, errors, redirects, templates, enrollment attributes, logs, and imported packages are hostile input with strict size/depth/count/ASN.1/text/network/polling bounds.

**RM-PKI-ISSUANCE-CROSS-0002:** Enrollment endpoints prevent SSRF, challenge delegation/substitution, DNS rebinding, redirect credential leakage, replay, confused account/tenant, cross-origin response mix-up, arbitrary template selection, and request/public-key substitution.

**RM-PKI-ISSUANCE-CROSS-0003:** Bootstrap secrets, account keys, private keys, recovery material, administrator credentials, challenges, reports, and pending-request identifiers are purpose-bound, minimally exposed, redacted, rotated, and never logged in reusable form.

**RM-PKI-ISSUANCE-CROSS-0004:** Identity/identifier/attestation/enrollment telemetry is privacy-classified and minimized. Public transparency or directory publication is explicit before issuance and exposes only policy-approved claims.

**RM-PKI-ISSUANCE-CROSS-0005:** Interactive enrollment/approval shows subject/requester, issuer, certificate purpose and identifiers, key protection/provider, validity, export/archival, target store/scope, requested-versus-issued changes, privacy/publication, and warnings accessibly.

**RM-PKI-ISSUANCE-CROSS-0006:** Prompts are keyboard and assistive-technology operable, focus-stable, localized, safe under bidi/untrusted names, non-color-dependent, and do not imply that a certificate makes a party trusted or authorized.

**RM-PKI-ISSUANCE-CROSS-0007:** Noninteractive failures distinguish authentication, authorization, POP/attestation, policy, pending, rate limit, network, issuer, delivery, installation, activation, renewal deadline, and recovery states through accessible administrative surfaces.

**RM-PKI-ISSUANCE-CROSS-0008:** Observability correlates intent/request/order/authorization/issuance/certificate/store/activation/renewal/revocation generations while hashing or suppressing subject identifiers and certificate contents according to policy.

