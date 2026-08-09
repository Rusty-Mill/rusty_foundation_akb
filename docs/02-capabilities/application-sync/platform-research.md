# Platform and standards research

- [RFC 6578](https://datatracker.ietf.org/doc/html/rfc6578) defines collection synchronization tokens and incremental changes, including invalid-token fallback to full synchronization. A token is scoped server evidence, not universal causality.
- Apache CouchDB's [replication protocol](https://docs.couchdb.org/en/stable/replication/protocol.html) distinguishes one-way replication, change feeds, sequence IDs, checkpoints, sessions, filtered replication, revision leaves, and common-ancestry recovery.
- [RFC 6902](https://www.rfc-editor.org/rfc/rfc6902.html) defines ordered JSON Patch operations; [RFC 7396](https://www.rfc-editor.org/rfc/rfc7396.html) defines JSON Merge Patch. Both are change representations, not application conflict policy.
- Shapiro et al.'s [Conflict-Free Replicated Data Types](https://hal.inria.fr/inria-00609399/document) establishes convergence conditions for state- and operation-based replicated data types; each datatype still requires exact algebra and delivery assumptions.
- Android's official [offline-first architecture guidance](https://developer.android.com/topic/architecture/data-layer/offline-first) distinguishes local/network sources, read/write strategies, queued work, synchronization, and conflict resolution while noting versioning complexity.
- Apple's [Core Data with CloudKit synchronization guidance](https://developer.apple.com/documentation/coredata/syncing-a-core-data-store-with-cloudkit) is an example of platform-managed local-store synchronization, not a portable semantic contract.

**RM-APP-SYNC-RESEARCH-0001:** Rusty Mill maps provider tokens, revisions, feeds, patches, and conflict facilities into the explicit model without strengthening their native guarantees.

**RM-APP-SYNC-RESEARCH-0002:** Windows, Linux, and macOS provide storage, networking, background execution, identity, and notifications, but no shared native application synchronization or merge contract; provider selection remains an RFC decision.
