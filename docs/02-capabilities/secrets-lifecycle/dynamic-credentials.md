# Dynamic credentials and leases

**RM-SECRETS-LEASE-0001:** A dynamic credential request binds authenticated subject/actor/workload, target/provider, account/role/profile, actions/scope, purpose, requested lifetime, renewability, constraints, session/transaction, policy, and authority.

**RM-SECRETS-LEASE-0002:** Issuance returns credential generation, lease identity, issued/active/expiry times, renewable ceiling, target account/object identity, revocation mechanism, delivery form, target-side effect evidence, and explicit nonclaims.

**RM-SECRETS-LEASE-0003:** Provider receipt and secret return do not prove target activation. The broker verifies or later reconciles target account/key/token/certificate existence and usable policy.

**RM-SECRETS-LEASE-0004:** Renewal revalidates current subject/workload, target, policy, lease, risk, authorization, and maximum lifetime and returns a new lease or credential generation where provider semantics require.

**RM-SECRETS-LEASE-0005:** Revocation distinguishes broker lease invalidation from target account/key/token/certificate denial and retries/reconciles ambiguous or unavailable target effects.

**RM-SECRETS-LEASE-0006:** Database, cloud, API, SSH, certificate, OAuth token-exchange, and provider-native credentials retain distinct issuance, audience, proof, rotation, revocation, audit, and reuse semantics.
