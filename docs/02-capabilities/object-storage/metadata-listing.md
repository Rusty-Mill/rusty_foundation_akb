# Metadata, listing, inventory, and events

**RM-OBJECT-METADATA-0001:** System metadata, user metadata, tags/labels, content representation metadata, access policy, encryption/key evidence, retention/hold, checksums, and application-signed descriptors are separate namespaces with typed size/count/encoding/privacy rules.

**RM-OBJECT-METADATA-0002:** Metadata update binds exact object and metadata generations and declares replace/merge/remove semantics, canonicalization, reserved fields, copy-on-write/new-version behavior, cache effects, encryption/retention interaction, and audit. Data and metadata generation changes remain distinct.

**RM-OBJECT-LIST-0001:** Listing binds namespace/configuration generation, prefix/delimiter/versions/filter, ordering, consistency/snapshot semantics, page size, opaque continuation token, metadata projection, authority, and total/result nonclaims.

**RM-OBJECT-LIST-0002:** Listing is discovery evidence, not proof that omitted objects do not exist or that returned objects still exist/currently match. Mutation/deletion always uses exact object-generation preconditions.

**RM-OBJECT-LIST-0003:** Continuation tokens bind exact provider/account/namespace/query/consistency and expiry; invalid/stale/changed-policy tokens fail or restart with explicit duplicate/gap behavior. Tokens are sensitive and never portable cursors.

**RM-OBJECT-INVENTORY-0001:** Inventory binds generation, scope, creation window, source consistency, schema/version, included metadata/versions, manifest/digests, delivery completeness, encryption, retention, and lag. It is a delayed evidence set, not current authority.

**RM-OBJECT-EVENT-0001:** Object events expose provider/source, namespace/key/version, operation kind, event/attempt identity, time quality, ordering/delivery/duplicate semantics, schema, and safe metadata. Notification receipt is not object existence, transaction, or domain completion proof.

**RM-OBJECT-EVENT-0002:** Consumers reconcile events and inventory against exact versioned reads; gaps, duplicates, reordering, overwrite/delete races, lifecycle actions, replication, failed operations, and provider retries are supported outcomes.

