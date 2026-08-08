# Reads, ranges, and streaming

**RM-OBJECT-READ-0001:** A read binds exact namespace/key and preferably object generation, conditional validators, byte range or whole-object intent, metadata projection, consistency/replica, decryption, checksum/content-digest verification, deadline, and output limits.

**RM-OBJECT-READ-0002:** Head/metadata lookup, read admitted, response metadata, first/last byte, provider checksum validated, caller content digest validated, stream complete, and caller consumed are distinct milestones.

**RM-OBJECT-READ-0003:** Range requests use exact inclusive/exclusive semantics, requested/effective interval, object total length/generation, satisfiable/short/changed outcomes, multipart range policy, and maximum count/bytes. Adjacent requests never assemble across different generations.

**RM-OBJECT-READ-0004:** Parallel and resumed downloads pin exact object generation, descriptor, length, range plan, completed ranges and per-range/full verification. If generation changes or evidence is missing, partial data is discarded or quarantined rather than mixed.

**RM-OBJECT-READ-0005:** Streaming applies backpressure and bounds queued bytes/chunks/time, concurrency, decompression/decryption, checksum state, spill storage, retries, and consumer stalls. Cancellation reports downloaded/verified/persisted progress and cannot prove provider nonaccess.

**RM-OBJECT-READ-0006:** Cached/CDN/intermediary reads expose cache key, object generation/validator, age/freshness, stale policy, range behavior, encryption/authorization partition, purge/invalidation, and origin evidence. Public cacheability is explicit.

**RM-OBJECT-READ-0007:** Archive-tier retrieval is a separate restore/request lifecycle with tier, cost, estimated/actual availability, expiry, copy/version identity, cancellation, and authorization; read failure cannot silently initiate billable restoration.

