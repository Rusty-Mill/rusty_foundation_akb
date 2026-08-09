# Deprovisioning and residual ownership

**RM-IDENTITY-GOV-DEPROVISION-0001:** Deprovisioning inventory covers accounts, directory memberships, assignments, resource-local ACLs, sessions, refresh/access tokens, API keys, certificates, SSH keys, passkeys/authenticators, secrets, devices, jobs, agents, delegates, owned data, queues, approvals, and recovery contacts.

**RM-IDENTITY-GOV-DEPROVISION-0002:** Each boundary records targeted, accepted, applied, observed, verified, failed, deferred, exempt, unmanaged, and unknown outcomes with deadlines and retry/escalation state.

**RM-IDENTITY-GOV-DEPROVISION-0003:** Session invalidation, credential revocation, directory disablement, entitlement removal, resource enforcement, ownership transfer, retention, and personal-data erasure are distinct effects and may have different completion frontiers.

**RM-IDENTITY-GOV-DEPROVISION-0004:** Offline devices, caches, replicas, downstream SaaS, federated tenants, long-lived credentials, backups, and unavailable providers remain explicit residuals; completion claims name the observed boundary and time.

**RM-IDENTITY-GOV-DEPROVISION-0005:** Restore, replay, retry, provider recovery, rehire, and identifier reuse cannot resurrect revoked assignments or credentials without a new authorized generation.
