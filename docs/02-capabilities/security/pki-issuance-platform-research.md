# Platform and protocol research

This research informs adapters; protocol standards, CA policy, and platform behavior remain authoritative.

## Protocol families

- ACME models accounts, orders, identifier authorizations/challenges, CSR finalization, certificate retrieval, revocation, account-key change, replay nonces, errors, and rate limits. ACME Renewal Information adds issuer-suggested renewal windows and replacement reporting.
- EST uses authenticated TLS/HTTP for CA certificates, CSR attributes, initial enroll, reenroll, full-CMC, and optional server-generated keys. SCEP and CMP provide other enrollment/polling/message-protection models and retain distinct bootstrap and resynchronization behavior.
- PKCS #10 defines one certificate-request syntax; a valid request signature is POP evidence but does not define CA authorization or issued contents.

Primary sources: [RFC 8555 ACME](https://www.rfc-editor.org/info/rfc8555/), [RFC 9773 ACME Renewal Information](https://www.rfc-editor.org/rfc/rfc9773.html), [RFC 7030 EST](https://www.rfc-editor.org/info/rfc7030/), [RFC 8894 SCEP](https://www.rfc-editor.org/rfc/rfc8894), [RFC 9480 CMP updates](https://www.rfc-editor.org/rfc/rfc9480.html), [RFC 2986 PKCS #10](https://www.rfc-editor.org/info/rfc2986/).

## Windows

Windows Certificate Enrollment exposes request creation, automatic/out-of-band/delayed enrollment, CA submission, response installation, templates, user/machine contexts, and existing/new keys. A successful enrollment call may still require status inspection to know whether the response was installed. AD CS policy and enrollment web services add enterprise-specific authorization and transport.

Primary sources: [Windows Certificate Enrollment API](https://learn.microsoft.com/en-us/windows/win32/seccertenroll/certenroll-portal), [IX509Enrollment](https://learn.microsoft.com/en-us/windows/desktop/api/CertEnroll/nn-certenroll-ix509enrollment), [AD CS enrollment web service](https://learn.microsoft.com/en-us/windows-server/identity/ad-cs/certificate-enrollment-web-service).

## Apple platforms

Managed-device enrollment can provision SCEP or ACME identities. Managed Device Attestation can bind hardware-backed keys and attested device properties into an ACME-based deployment, but the surrounding management and relying-party policy determines its security meaning.

Primary source: [Apple Managed Device Attestation deployment](https://support.apple.com/guide/deployment/deploy-managed-device-attestation-dep54e5ac1fd/web).

## Linux and portable services

Linux deployments commonly use distribution/enterprise agents, ACME clients, EST/SCEP/CMP tooling, NSS/OpenSSL stores, hardware tokens, systemd service reloads, and application-private files. Rusty Mill maps exact store/key/service behavior and never treats “Linux” as one enrollment provider.

