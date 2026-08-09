# Application sessions, logout, and revocation

**RM-APP-AUTH-SESSION-0001:** A session binds immutable session generation, subject/account/tenant, client, authentication evidence and time, assurance/risk state, issued/idle/absolute expiries, renewal and concurrency policy, device/channel context, privileges, and revocation frontier.

**RM-APP-AUTH-SESSION-0002:** Session identifiers are unpredictable bearer secrets or proof-bound handles, transported and stored with platform-appropriate protections, rotated after authentication and privilege changes, partitioned by origin/tenant, and excluded from URLs/logs.

**RM-APP-AUTH-SESSION-0003:** Renewal creates a new session or token generation after checking account/authenticator/session status, policy, risk, revocation, and expiry. Activity does not extend absolute lifetime unless product policy explicitly permits it.

**RM-APP-AUTH-SESSION-0004:** Logout distinguishes local client state, application session invalidation, authorization-server/identity-provider session, refresh/access tokens, device credentials, and other relying-party sessions. Completion reports the exact boundary.

**RM-APP-AUTH-SESSION-0005:** Revocation can target a session, subject, account, authenticator, client, device, tenant, token family, privilege, or security epoch and propagates through generation checks, push hints, introspection, cache expiry, or forced reauthentication with measured convergence.

**RM-APP-AUTH-SESSION-0006:** Concurrent-session enumeration and termination use privacy-preserving recognizable metadata, resist cross-tenant enumeration, distinguish current/other/unknown sessions, and record ambiguous offline effects.
