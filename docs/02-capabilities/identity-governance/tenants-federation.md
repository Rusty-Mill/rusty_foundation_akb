# Tenants, invitations, guests, and federation

**RM-IDENTITY-GOV-TENANT-0001:** A tenant is an explicit administrative and data-policy boundary with immutable generation, issuer, domains, identity sources, federation relationships, policy generation, residency, and lifecycle state.

**RM-IDENTITY-GOV-TENANT-0002:** Invitations bind inviter authority, target hint, tenant, intended role or request, nonce, expiry, redemption constraints, and single-use outcome. The hint is not a subject identity.

**RM-IDENTITY-GOV-TENANT-0003:** Guest accounts retain home issuer, host tenant, sponsor, purpose, expiry, review cadence, attribute-release policy, and locally assigned entitlements. Home authentication does not imply host authorization.

**RM-IDENTITY-GOV-TENANT-0004:** Federation relationships bind exact issuer, audience, subject-mapping rule, accepted evidence classes, attribute mapping, assurance floor, keys/metadata generation, expiry, and revocation behavior.

**RM-IDENTITY-GOV-TENANT-0005:** Tenant merge, split, transfer, suspension, and deletion are migration workflows with collision analysis, data/identity lineage, entitlement re-evaluation, session revocation, provider reconciliation, and residual reporting.
