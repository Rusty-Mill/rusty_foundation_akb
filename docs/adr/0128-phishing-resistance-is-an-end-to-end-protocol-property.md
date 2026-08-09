# ADR-0128: Phishing resistance is an end-to-end protocol property

## Status

Accepted

## Context

Products often label factors or devices as phishing-resistant based on hardware, biometrics, multi-factor composition, number matching, or user training. An authenticator output that can be entered into or relayed through an impostor verifier remains phishable regardless of those labels. Conversely, verifier-name- or channel-bound cryptographic protocols can prevent useful disclosure to the impostor.

## Decision

Rusty Mill reports phishing resistance only when the complete authentication protocol cryptographically binds the authenticator output to the intended verifier name or authenticated channel and validation preserves that binding through the relying party. Factor count, user verification, device binding, attestation, hardware isolation, transaction display, and replay resistance remain separate properties.

## Consequences

- Password, OTP, recovery-code, and manually approved out-of-band methods are not phishing-resistant.
- WebAuthn can provide verifier-name binding when the complete RP/origin validation contract is satisfied.
- Fallback cannot preserve a phishing-resistant claim unless the fallback protocol independently qualifies.
- Conformance tests the entire ceremony rather than trusting provider labels.
