# Change, expiry, and revocation

Identity/session providers publish revisioned snapshots plus invalidation hints. They do not promise a lossless history of every authentication, group, privilege, or lock-state transition.

**RM-IDENTITY-CHANGE-0001:** Change delivery MUST expose observation revision, affected scope, known change class, loss/coalescing state, and resynchronization requirement.

**RM-IDENTITY-CHANGE-0002:** Consumers MUST re-read authoritative state after invalidation, gap, overflow, reconnect, resume, provider restart, or generation mismatch and converge idempotently.

**RM-IDENTITY-CHANGE-0003:** Authentication evidence, credential handles, session references, context snapshots, and delegated contexts each carry independent expiry/revocation semantics; revoking one MUST NOT be reported as revoking the others unless proven.

**RM-IDENTITY-CHANGE-0004:** Stale generations MUST fail before sensitive work. A provider MUST NOT silently retarget a principal, session, credential, or context after identifier reuse.

**RM-IDENTITY-CHANGE-0005:** Security-critical operations revalidate required freshness and native policy even when no change event was observed. Poll/reconciliation bounds are explicit when prompt revocation matters.

**RM-IDENTITY-CHANGE-0006:** Shutdown and logoff callbacks are not cleanup guarantees. Credential and delegated-handle lifetime is owner-bound, and durable security state is committed during ordinary operation.
