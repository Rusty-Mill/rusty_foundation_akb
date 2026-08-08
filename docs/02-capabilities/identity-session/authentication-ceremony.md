# Authentication ceremonies

`rm.identity.authenticate` asks an authorized platform broker to establish fresh evidence for one purpose. It does not ask an application to collect a particular secret.

**RM-IDENTITY-AUTH-0001:** A request MUST bind purpose, audience, acceptable principal/realm, required freshness, interaction policy, acceptable method/assurance classes, cancellation, deadline, and presentation context.

**RM-IDENTITY-AUTH-0002:** The result MUST report principal reference, ceremony/provider identity, method class, assurance claims with provenance, authentication time, expiry/freshness, audience/purpose, interaction performed, and terminal outcome.

**RM-IDENTITY-AUTH-0003:** Success is authentication evidence only. Every protected operation MUST independently validate its capability authority and native policy at use time.

**RM-IDENTITY-AUTH-0004:** Password, PIN, biometric sample/template, recovery code, private key, and device-unlock secret MUST NOT appear in a normal result, diagnostic, event, callback, or application-owned UI where a trusted native broker is available.

**RM-IDENTITY-AUTH-0005:** User cancellation, timeout, unavailable interaction, locked session, unsupported method, policy denial, provider failure, stale context, and credential failure MUST remain distinguishable without revealing account-existence or secret-validation oracles beyond policy.

**RM-IDENTITY-AUTH-0006:** Cached or silent satisfaction MUST be disclosed and MUST meet requested freshness, audience, assurance, and interaction constraints; otherwise the request fails or explicitly degrades according to caller policy.

**RM-IDENTITY-AUTH-0007:** Sync and async paths have identical terminal semantics. Cancellation requests do not prove that native UI disappeared or that secret processing stopped; the resource remains owned until terminal completion.

Method classes describe evidence, not a portable strength ordering. Password plus device policy, platform biometrics, hardware-key possession, and remote federation cannot be truthfully reduced to one integer.

See [ADR-0062](../../adr/0062-authentication-results-are-scoped-evidence.md).
