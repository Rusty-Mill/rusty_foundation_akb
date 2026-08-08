# Change observation and reload

## Capability identity

`rm.config.change-observer` converts native invalidations into portable reconciliation events.

**RM-CONFIG-CHANGE-0001:** Native notifications are treated as hints to re-read state, not a lossless portable journal of individual writes.

**RM-CONFIG-CHANGE-0002:** Events distinguish snapshot replacement, rejected candidate, pending restart, observer overflow/loss, source unavailable, permission changed, and terminal observer failure.

**RM-CONFIG-CHANGE-0003:** A replacement event carries old/new snapshot revisions, changed stable key identities, cause class, and coalescing disclosure. It never claims that every intermediate native state was observed.

**RM-CONFIG-CHANGE-0004:** On overflow, ambiguous rename/replacement, observer restart, or lost continuity, the provider emits `ResynchronizationRequired` and performs or requests a full source re-read before later replacement claims.

**RM-CONFIG-CHANGE-0005:** Delivery ordering is total per resolver instance. Duplicate invalidations and spurious wakeups are permitted internally but cannot create duplicate snapshot revisions with identical resolution evidence.

**RM-CONFIG-CHANGE-0006:** Streams have bounded buffering and explicit coalescing/backpressure. Cancellation stops future delivery and releases native registrations without invalidating already issued snapshots.

**RM-CONFIG-CHANGE-0007:** Change callbacks never run while provider-internal locks are held and never require consumers to reenter a native notification thread.

**RM-CONFIG-CHANGE-0008:** Self-writes are not assumed to be uniquely identifiable. Feedback-loop suppression uses revision/content evidence and remains bounded.

## Reload transaction

Live keys may publish directly after validation. Coordinated keys first prepare named participants, then either commit a common new revision or abort without changing active state. This is an in-process service transaction, not a claim of atomicity across unrelated processes or native stores.

