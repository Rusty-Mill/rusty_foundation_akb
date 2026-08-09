# Platform and standards research

## Primary standards

- [Web Authentication Level 3](https://www.w3.org/TR/webauthn-3/) defines RP-scoped public-key credential registration/authentication, client/authenticator mediation, attestation, user presence/verification, backup state, and security/privacy behavior.
- [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html) defines authenticator types, assurance levels, lifecycle, phishing/replay resistance, verifier requirements, session management, and recovery considerations.
- [NIST SP 800-63C-4](https://pages.nist.gov/800-63-4/sp800-63c.html) defines federation assurance, assertions, identity providers, relying parties, subscriber-controlled wallets, and federation transactions.
- [OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0.html) defines authentication atop OAuth using ID Tokens, UserInfo, claims, nonce, issuer, audience, and authorization flows.
- [RFC 9700](https://www.rfc-editor.org/rfc/rfc9700.html) records current OAuth 2.0 security best practice, including redirect-flow protection, token replay prevention, privilege restriction, and deprecated insecure modes.
- [RFC 7009](https://www.rfc-editor.org/rfc/rfc7009.html) and [RFC 7662](https://www.rfc-editor.org/rfc/rfc7662.html) define token revocation and introspection boundaries.

## Platform families

| Family | Relevant facilities | Architectural consequence |
|---|---|---|
| Windows | WebAuthn APIs, Windows Hello, credential providers, WAM/brokers, DPAPI/CNG | platform user verification, key protection, broker accounts, and application tokens are distinct evidence |
| Linux | browsers/libfido2, PAM, desktop secret services, hardware tokens, web/native brokers | capabilities depend on desktop, browser, device permissions, and provider; no universal native account broker exists |
| macOS | AuthenticationServices/passkeys, LocalAuthentication, Keychain/Secure Enclave, platform SSO | local user verification, passkey ceremonies, credential storage, and federated tokens remain separate services |

## Conclusion

The portable model standardizes plans, evidence, lifecycles, loss, and boundaries. Exact browser/native APIs, token formats, authenticators, brokers, and assurance policy remain provider- and product-selected.
