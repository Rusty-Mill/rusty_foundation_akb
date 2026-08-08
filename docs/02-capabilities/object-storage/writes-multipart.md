# Writes, multipart uploads, copies, and composition

**RM-OBJECT-WRITE-0001:** A write binds namespace/key, create/replace/exact-generation precondition, content length or bound, media type/encoding, typed metadata/tags, checksum and optional content descriptor, encryption, storage class, retention/hold, durability/replication, deadline, and authority.

**RM-OBJECT-WRITE-0002:** Source read, local checksum/digest, request accepted, bytes/parts transferred, provider integrity validation, staged data persisted, object generation committed, response observed, visible, replicated, and event/inventory observed are separate.

**RM-OBJECT-WRITE-0003:** Single-request write failure can have unknown commit after all bytes cross the boundary. Retry uses create/exact-generation/idempotency preconditions and result lookup; unsafe unconditional overwrite retry is prohibited.

**RM-OBJECT-MULTIPART-0001:** A multipart/resumable upload session binds namespace/key intent, provider upload identity, creator/tenant, expected length/digest, part/block/chunk size and numbering, encryption/metadata/retention, expiry, precondition strategy, and resource budget.

**RM-OBJECT-MULTIPART-0002:** Each part has number/range, exact bytes/length, provider validator/checksum, attempt identity, received/stored evidence, and replacement rule. Part validators cannot be treated as full-object digest or object generation.

**RM-OBJECT-MULTIPART-0003:** Completion supplies an immutable ordered part manifest plus whole-object expectations and conditional target state. Provider completion atomically creates one object generation or fails/returns unknown; missing/duplicate/reordered/mismatched parts are rejected.

**RM-OBJECT-MULTIPART-0004:** Abort, expiry, garbage collection, and list-parts reconcile staged resources and costs but do not delete a separately committed object. Lost completion response is resolved by upload and target-generation evidence before retry/abort.

**RM-OBJECT-COPY-0001:** Server-side copy/compose binds exact source generations/ranges/descriptors and target conditional generation, metadata/encryption/retention transformation, provider/location/class, checksum semantics, atomicity, progress, and billing. It creates a new target identity.

**RM-OBJECT-COPY-0002:** Multi-object batch operations are collections of independently identified conditional attempts unless a provider profile proves atomicity. Partial success, unknown outcomes, retries, reports, and compensation remain per object.

