# Application synchronization source review

| Field | Value |
|---|---|
| Review status | Pass |
| Reviewed | 2026-08-08 |
| Expires | On provider/standards/support-baseline change or 2027-02-08, whichever occurs first |
| Reviewer | Application synchronization capability owner |
| Open blocking findings | None for planning eligibility; provider adoption requires version-bound review |

| Source | Class and reviewed status | Proposition supported | Impact and limitation |
|---|---|---|---|
| [RFC 6578](https://www.rfc-editor.org/info/rfc6578/) | IETF Proposed Standard, March 2012; status reviewed 2026-08-08 | opaque collection-scoped tokens, incremental changes, invalid-token full resynchronization | compatible; WebDAV collection progress is not universal causal/completeness evidence |
| [RFC 6902](https://www.rfc-editor.org/info/rfc6902/) and [RFC 7396](https://www.rfc-editor.org/info/rfc7396/) | IETF Standards Track patch representations; status reviewed 2026-08-08 | ordered JSON Patch and JSON Merge Patch representations | compatible; neither defines application conflict, authorization, or convergence policy |
| [Apache CouchDB 3.5 replication protocol](https://docs.couchdb.org/en/stable/replication/protocol.html) | provider documentation, stable endpoint currently identifies version 3; reviewed 2026-08-08 | directed replication, revisions/leaves, change feed, sequence/checkpoint, filtering, unstable-network recovery | compatible with qualification; version/provider behavior is evidence, not portable semantics |
| [CRDT technical report](https://hal.inria.fr/inria-00609399/document) | research evidence, not platform authority; reviewed 2026-08-08 | convergence conditions for state- and operation-based replicated datatypes | compatible; exact algebra, delivery, causality, membership, and garbage collection remain typed policy |
| [Android offline-first guidance](https://developer.android.com/topic/architecture/data-layer/offline-first) | living platform guidance; reviewed 2026-08-08 | local/network sources, queued work, pull/push sync, conflict-resolution considerations | informative only; Android application architecture does not define cross-platform authority or convergence |
| [Apple Core Data with CloudKit guidance](https://developer.apple.com/documentation/coredata/syncing-a-core-data-store-with-cloudkit) | living provider/platform guidance; reviewed 2026-08-08 | background upload/download, local-store projection, query generations, dropped/deferred push hints | informative only; managed sync cadence and provider semantics are not portable guarantees |

**RM-APP-SYNC-SOURCE-0001:** Provider adoption MUST bind exact product/protocol/SDK/service versions, topology, account/tenant/security model, quotas, retention, availability, and documented conflict/deletion behavior.

**RM-APP-SYNC-SOURCE-0002:** Mutable provider or platform guidance MUST be snapshotted or version-recorded in trial evidence and re-reviewed on material change.

**RM-APP-SYNC-SOURCE-0003:** Research and example architectures MAY justify hypotheses but MUST NOT substitute for executable histories or provider evidence.

**RM-APP-SYNC-SOURCE-0004:** An updated source invalidates affected reviewed-current claims until impact is classified and contract/test consequences are recorded.

