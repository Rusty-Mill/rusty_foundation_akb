# Application federation and assertions

**RM-APP-AUTH-FEDERATION-0001:** A trust relationship binds issuer, relying party/client, endpoints and keys/metadata generations, allowed protocols/flows, subject mapping, audiences, assertion/token profiles, claims, assurance, time/skew, privacy, logout, revocation, and rollover policy.

**RM-APP-AUTH-FEDERATION-0002:** Assertions validate issuer, audience/recipient, subject, signature/MAC and algorithm, key generation, time, nonce/state/request correlation, authentication context, authorized party/client, replay rules, and critical extensions before mapping.

**RM-APP-AUTH-FEDERATION-0003:** Issuer subject identifiers remain issuer- and audience-scoped aliases. Email, display name, tenant domain, or mutable claims do not establish local account equality.

**RM-APP-AUTH-FEDERATION-0004:** Front-channel, back-channel, artifact, browser redirect, native-app loopback/app-link, and device flows retain distinct origin, redirect, client-authentication, mix-up, CSRF, interception, and privacy properties.

**RM-APP-AUTH-FEDERATION-0005:** Just-in-time account creation, linking, unlinking, invitation redemption, home-realm discovery, and claim-driven group/entitlement mapping require separate product policy and identity-governance reconciliation.

**RM-APP-AUTH-FEDERATION-0006:** Federation outage, metadata/key rollover, issuer compromise, pairwise identifier change, tenant transfer, logout failure, and deprovisioning gaps remain visible; local sessions are not assumed revoked by remote logout receipt.
