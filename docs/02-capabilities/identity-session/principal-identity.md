# Principal identity and evidence

`rm.identity.principal-observer` produces immutable, provider-scoped principal descriptors. A descriptor is suitable for display, correlation, or a later explicit operation only to the quality its evidence supports.

**RM-IDENTITY-PRINCIPAL-0001:** A principal reference MUST include principal kind, provider/realm identity, provider-local subject identifier, observation generation, evidence source, stability scope, and freshness.

**RM-IDENTITY-PRINCIPAL-0002:** Account name, display name, email, numeric UID/GID, SID text, home path, avatar, group membership, certificate subject, and device account MUST remain typed attributes; none alone is universal identity or authority.

**RM-IDENTITY-PRINCIPAL-0003:** Equality MUST state its scope. Cross-realm correlation requires a separate attested mapping and MUST NOT be inferred from matching human-readable attributes.

**RM-IDENTITY-PRINCIPAL-0004:** Enumeration and attribute expansion are separate, authority-checked operations. Providers expose absent, withheld, stale, ambiguous, and unsupported values without substitution.

**RM-IDENTITY-PRINCIPAL-0005:** Groups, roles, claims, privileges, entitlements, labels, and capabilities are revisioned security-context evidence. They MUST NOT be flattened into a permanent `is_admin` or trust level.

**RM-IDENTITY-PRINCIPAL-0006:** Principal references are not credentials, proof of current control, login sessions, authorization decisions, or serializable capability authority.

Principal kinds may include local account, service identity, managed account, device identity, and provider-defined extension. A product requiring people, organizations, federated subjects, or account linking selects a separate identity-domain contract.
