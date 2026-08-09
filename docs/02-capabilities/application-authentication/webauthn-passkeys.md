# WebAuthn, passkeys, and cryptographic authenticators

**RM-APP-AUTH-WEBAUTHN-0001:** Registration binds relying-party identity, user/account generation, fresh challenge, origin policy, algorithms, resident/discoverable preference, user-verification requirement, attachment hints, attestation policy, extensions, timeout, and duplicate-credential policy.

**RM-APP-AUTH-WEBAUTHN-0002:** Authentication validates client data type/challenge/origin/cross-origin state, RP ID hash, user-presence and verification flags, credential identity, public key/algorithm, signature, extension outputs, backup state, sign counter evidence, and account status under exact policy.

**RM-APP-AUTH-WEBAUTHN-0003:** Credential IDs, public keys, transports, AAGUID/attestation, backup eligibility/state, discoverability, device-bound or synced character, and counter behavior are distinct evidence. No single field proves hardware protection or a unique natural person.

**RM-APP-AUTH-WEBAUTHN-0004:** Attestation is optional issuer-qualified supply-chain evidence evaluated under a privacy-aware policy; absent, none, self, anonymized, enterprise, or untrusted attestation does not silently become a device trust decision.

**RM-APP-AUTH-WEBAUTHN-0005:** Synced passkeys and device-bound credentials use different risk and recovery properties. Product policy declares acceptable backup/export characteristics and never labels all passkeys identically.

**RM-APP-AUTH-WEBAUTHN-0006:** Credential discovery and conditional mediation preserve anti-enumeration and user control. Human-readable credential names are local presentation metadata, not credential identity.
