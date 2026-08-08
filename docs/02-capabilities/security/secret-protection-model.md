# Secret protection claim model

**Status:** Draft

“Secure storage” is not a portable scalar. Every provider claim is a vector scoped to the exact platform, account/session state, deployment, store configuration, item policy, and operation.

## Claim dimensions

| Dimension | Example values |
|---|---|
| Persistence | Process, login session, reboot-persistent, restored/migrated, synchronized |
| Protection boundary | Application logic, separate service, OS credential boundary, hardware-backed key operation |
| Subject binding | Process, application identity, user, machine, service account, explicit access group |
| Interaction | Never prompts, may prompt, requires prompt, requires unlocked session, unavailable headless |
| Exportability | Opaque-use only, scoped reveal, owned export, provider-dependent |
| Availability | Pre-login, logged-in, unlocked, offline, recovery environment |
| Replication | Local only, backup eligible, roaming/synchronized, unknown/provider policy |
| Revocation/deletion | Logical delete, key destruction, remote revocation, delayed garbage collection |
| Assurance | Mechanism documentation, conformance evidence, independent evaluation, scoped certification |

## Rules

1. A profile constrains dimensions independently; it does not request a numeric “security level.”
2. Unknown is distinct from absent and never satisfies a required protection claim.
3. A stronger value on one dimension cannot compensate for a weaker value on another.
4. Provider discovery occurs before secret submission where possible, so unacceptable prompting, export, replication, or persistence does not occur accidentally.
5. Configuration or account-state changes that alter claims produce a new observation and may invalidate cached selection.
6. Backup, migration, and synchronization are explicit data-flow properties, not assumed benefits of persistence.

## Illustrative comparison

| Mechanism class | Useful property | Critical qualifier |
|---|---|---|
| User credential vault | User-bound persistence and managed access policy | May require interactive/unlocked user session and may roam or back up |
| Machine-protected blob | Local persistence without a separate record store | Application owns metadata, rollback, file authority, and ciphertext integrity context |
| Session keyring | Kernel-mediated lifetime and access checks | Persistence and userspace readability vary by key type and keyring |
| Hardware-backed key | Private key operation may remain inside hardware | Arbitrary application secret storage/export may not be supported |

