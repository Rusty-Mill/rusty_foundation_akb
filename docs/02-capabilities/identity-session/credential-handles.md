# Credential handles and brokers

Credential material belongs behind a native or product-specific broker. The portable layer carries constrained handles and secret-value resources, not casually clonable strings.

**RM-IDENTITY-CREDENTIAL-0001:** A credential handle MUST declare provider, credential class, subject/realm hints under disclosure policy, allowed purposes/audiences/operations, interaction requirement, exportability, persistence, expiry, revocation support, owner scope, and assurance evidence.

**RM-IDENTITY-CREDENTIAL-0002:** Handles MUST be opaque, non-serializable by default, generation-scoped, least-authority, and unusable after close, expiry, revocation, provider restart, or owner retirement.

**RM-IDENTITY-CREDENTIAL-0003:** Raw-secret import/export is a separate explicitly authorized operation using `rm.security.secret-value`; non-exportability, hardware confinement, user presence, and broker-only use MUST be preserved.

**RM-IDENTITY-CREDENTIAL-0004:** Credential selection MUST bind purpose and audience and MUST NOT silently choose a broader credential because it is cached, default, or belongs to the same display account.

**RM-IDENTITY-CREDENTIAL-0005:** Storage uses the selected `rm.security.secret-store` protection vector. A credential handle does not imply persistence, synchronization, backup, recovery, deletion assurance, or cross-device availability.

**RM-IDENTITY-CREDENTIAL-0006:** Applications MUST NOT place credentials in command lines, environment blocks, ordinary configuration, URLs, logs, crash metadata, clipboard offers, notification payloads, or unclassified IPC.

Web/OAuth tokens, Kerberos tickets, client certificates, SSH agents, passkeys, and application passwords require protocol-specific contracts above this broker because refresh, audience, proof-of-possession, delegation, and revocation semantics differ.
