# Platform and format research

This research informs adapter contracts; official platform behavior remains authoritative.

## Windows

- Authenticode uses a format-specific PE signed view with excluded/mutable regions; strict verification and exact action/provider policy matter.
- `WinVerifyTrust` invokes a selected trust-provider action. A successful provider result is not automatically the product's full artifact-acceptance policy.
- Catalog, script, package, driver, and document signatures have distinct subjects and policy providers and cannot be treated as one PE contract.

Primary sources: [WinVerifyTrust](https://learn.microsoft.com/en-us/windows/win32/api/wintrust/nf-wintrust-winverifytrust), [Microsoft Authenticode strict-verification security bulletin](https://learn.microsoft.com/en-us/security-updates/securitybulletins/2013/ms13-098).

## Apple platforms

- Code signatures seal code and resources according to bundle/format rules and carry code requirements. Nested code and post-sign mutation require format-aware verification.
- Developer ID notarization is a separate Apple service assessment applied after code signing; stapled or online evidence must remain distinguishable.
- Secure timestamps differ from an unsecured local “Signed Time.”

Primary sources: [Understanding the Code Signature](https://developer.apple.com/library/archive/documentation/Security/Conceptual/CodeSigningGuide/AboutCS/AboutCS.html), [Notary API](https://developer.apple.com/documentation/NotaryAPI), [TN3161 code-signing certificates and timestamps](https://developer.apple.com/documentation/technotes/tn3161-inside-code-signing-certificates).

## Linux and portable ecosystems

Linux distributions commonly authenticate repository metadata and packages through ecosystem-specific formats and trust policy. Rusty Mill preserves package, repository, transport, and installed-content evidence separately. Portable envelope profiles may use CMS, COSE, or DSSE/Sigstore where selected by an RFC; this analysis does not select one universal wire format.

## Standards and transparency

- CMS supports signed content and attributes, countersignatures, and nested protection.
- RFC 3161 timestamps bind a message imprint in a signed timestamp token; verifier policy must evaluate the timestamp authority and imprint.
- Sigstore-style bundles can carry signature, certificate, timestamp, and transparency materials for offline verification, while trust-root and policy selection remain local.

Primary sources: [RFC 5652 CMS](https://www.rfc-editor.org/rfc/rfc5652), [RFC 3161 Time-Stamp Protocol](https://www.rfc-editor.org/rfc/rfc3161), [Sigstore documentation](https://docs.sigstore.dev/).

