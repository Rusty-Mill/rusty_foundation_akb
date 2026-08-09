# OAuth and token lifecycle

**RM-APP-AUTH-TOKEN-0001:** Authorization grants, authorization codes, access tokens, refresh tokens, ID tokens, device codes, client credentials, and session cookies are distinct typed artifacts with exact issuer, client, audience/resource, subject, scope/authorization details, generation, issue/expiry, and proof properties.

**RM-APP-AUTH-TOKEN-0002:** OAuth authorization binds exact authorization server, client instance, redirect URI, state, PKCE verifier/challenge, requested resources/scopes/authorization details, nonce where applicable, interaction, and response mode. Authorization code substitution and mix-up are rejected.

**RM-APP-AUTH-TOKEN-0003:** Access-token consumers validate the selected profile's issuer, audience/resource, token type, signature/introspection result, time, client/subject, scopes/authorization details, proof-of-possession binding, revocation/freshness, and policy; token possession alone is not universal authority.

**RM-APP-AUTH-TOKEN-0004:** Refresh tokens are narrowly scoped, confidentially stored, sender-constrained or rotated where policy requires, replay-detected, revocable by family/generation, and never exposed to resource servers or logs.

**RM-APP-AUTH-TOKEN-0005:** Token exchange, delegation, impersonation, downscoping, and on-behalf-of flows preserve actor/subject/resource/audience chains, prevent privilege amplification, and issue new independently expiring generations.

**RM-APP-AUTH-TOKEN-0006:** Revocation, introspection, key rollover, and short expiry provide different freshness evidence. Offline validation reports its accepted staleness and cannot claim immediate revocation.
