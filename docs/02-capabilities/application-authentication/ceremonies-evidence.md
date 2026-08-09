# Authentication plans and evidence

**RM-APP-AUTH-CEREMONY-0001:** An immutable plan binds purpose, verifier and audience, subject hint or discoverable mode, transaction context, allowed and prohibited method classes, required protocol properties, interaction policy, freshness, deadline, retry policy, and authority.

**RM-APP-AUTH-CEREMONY-0002:** Challenges are unpredictable, verifier-scoped, purpose-bound, short-lived, single-use where the protocol requires, and stored or derived so replay and cross-client substitution are detected.

**RM-APP-AUTH-CEREMONY-0003:** Method selection reports why candidates are eligible, unavailable, degraded, or prohibited. Fallback is a new policy decision and never silently weakens phishing resistance, user verification, device binding, or assurance.

**RM-APP-AUTH-CEREMONY-0004:** Verification validates exact protocol syntax, challenge, origin/verifier, audience, issuer, subject/account and credential generations, time, algorithm policy, signatures/MACs, interaction flags, replay state, and revocation before policy acceptance.

**RM-APP-AUTH-CEREMONY-0005:** Authentication evidence is audience-, purpose-, and freshness-scoped input to session or transaction policy. It is not reusable secret material, delegation, entitlement, consent, or capability authority.

**RM-APP-AUTH-CEREMONY-0006:** Reauthentication creates new evidence and does not mutate the historical ceremony. The consumer defines whether prior session context may identify the subject or whether full account selection is required.
