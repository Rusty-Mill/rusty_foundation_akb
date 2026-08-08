# Reference identity and name matching

**RM-PKI-IDENTITY-0001:** Reference identities MUST be typed by protocol and role—DNS name, IP address, URI/service identity, email/mailbox, application/package/publisher, device, account, or profile-specific identity—and validated before matching.

**RM-PKI-IDENTITY-0002:** Matching MUST use the selected protocol/profile's exact authorized identifier fields, canonicalization, wildcard, internationalized-name, case, trailing-dot, address, URI, and embedded-NUL rules. Generic string or distinguished-name comparison is forbidden.

**RM-PKI-IDENTITY-0003:** Subject alternative names, common name fallback, name constraints, service/purpose identifiers, and custom extension identities MUST follow explicit profile policy; unsupported fallback fails rather than guessing.

**RM-PKI-IDENTITY-0004:** Display names and Unicode rendering are presentation only. Security comparison uses protocol-defined locale-neutral forms and preserves original values for diagnostics under privacy policy.

**RM-PKI-IDENTITY-0005:** Wildcards and patterns MUST be bounded and profile-authorized; they MUST NOT cross label/namespace boundaries, match public suffixes or bare domains contrary to policy, or expand into general regular expressions.

**RM-PKI-IDENTITY-0006:** A successful certificate-name match does not establish that the presenter controls the private key. Channel/protocol proof-of-possession and transcript binding are separate evidence.

**RM-PKI-IDENTITY-0007:** Pinning MUST specify what is pinned (certificate, SPKI/key, issuer, anchor, policy, or application identity), scope, backup pins, validity/rotation/recovery, trust-store interaction, reporting, and failure behavior. A fingerprint string is not a complete pin policy.
