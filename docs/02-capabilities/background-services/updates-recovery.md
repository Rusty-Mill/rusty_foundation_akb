# Updates, rollback, removal, and recovery

**RM-BACKGROUND-UPDATE-0001:** Updates install a verified immutable package and definition generation before atomically changing admission. In-place mutation of a running executable or definition is forbidden.

**RM-BACKGROUND-UPDATE-0002:** New attempts route to the committed generation; existing attempts follow declared drain, cancel/checkpoint, terminate, or coexist policy. Endpoint and checkpoint compatibility are version-negotiated.

**RM-BACKGROUND-UPDATE-0003:** Health/readiness gates, bounded observation windows, crash/restart-loop detection, rollback authority, and last-known-good evidence MUST precede automatic promotion claims.

**RM-BACKGROUND-UPDATE-0004:** Rollback MUST NOT load newer incompatible checkpoints/configuration/results into an older generation without an accepted migration path. Data rollback is separate from executable rollback.

**RM-BACKGROUND-UPDATE-0005:** Removal closes admission and disables triggers before stopping/draining work, unregistering endpoints/definitions, releasing credentials, and deleting owned state according to retention policy.

**RM-BACKGROUND-UPDATE-0006:** Partial install/update/remove, reboot, power loss, broker restart, package quarantine/revocation, and administrative edits MUST reconcile from native registration plus signed package/definition state.

**RM-BACKGROUND-UPDATE-0007:** Shared service takeover, downgrade, rollback, and removal MUST authenticate package ownership and expected generation; one product cannot replace another's registration by label collision.
