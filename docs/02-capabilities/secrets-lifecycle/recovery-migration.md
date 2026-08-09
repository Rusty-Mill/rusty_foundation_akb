# Backup, recovery, migration, and deletion

**RM-SECRETS-RECOVERY-0001:** Backup policy identifies which encrypted values, metadata, leases, revocation state, audit, provider configuration, root/key material, and recovery shares are included, their protection domains, retention, access, and restore objectives.

**RM-SECRETS-RECOVERY-0002:** Restore occurs into an isolated generation, authenticates backup/provenance, validates consistency and anti-rollback epochs, prevents duplicate active issuers/leases, reconciles targets/dependents, and requires explicit activation.

**RM-SECRETS-RECOVERY-0003:** Provider migration inventories every version, metadata/access policy, opaque/non-exportable item, lease, dependent, target, audit requirement, and semantic loss; export authority is separate and plaintext staging is minimized.

**RM-SECRETS-RECOVERY-0004:** Rewrap or re-encryption preserves secret semantic generation only when plaintext and target credential are unchanged and the contract records old/new protection; rotation creates a new credential generation.

**RM-SECRETS-RECOVERY-0005:** Deletion distinguishes issue/use disablement, target revocation, provider logical deletion, version purge, replica/cache expiry, backup expiry, cryptographic erasure, hardware destruction, and unverifiable physical residuals.

**RM-SECRETS-RECOVERY-0006:** Disaster recovery and break-glass root operations use independent custody/quorum, tested ceremonies, limited exposure, immutable evidence, immediate post-use rotation, and assurance that restored authority cannot clone an active control plane silently.
