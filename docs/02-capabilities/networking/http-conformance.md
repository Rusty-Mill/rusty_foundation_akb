# HTTP conformance specification

**RM-HTTP-CONFORMANCE-0001:** Reports bind client/server/provider builds, protocol versions, topology/proxies, origin and secure policy, request/response fixtures, cache/credential generations, clocks, limits, impairment, and canonical event/evidence traces.

**RM-HTTP-CONFORMANCE-0002:** Shared semantics cover methods, targets, fields, informational/final responses, content rules, trailers, negotiation, ranges/conditionals, validators, malformed/unknown extensions, and streaming bodies across all supported versions.

**RM-HTTP-CONFORMANCE-0003:** HTTP/1.1 adversarial corpora cover conflicting length/transfer coding, whitespace, obs-fold, incomplete/chunked framing, pipelining, upgrade/tunnel, premature close/reuse, and request/response smuggling differentials.

**RM-HTTP-CONFORMANCE-0004:** HTTP/2 and HTTP/3 corpora cover settings, state machines, invalid frames, flow control, header compression limits, blocked streams, reset/GOAWAY, concurrency, priority variance, connection errors, and cross-stream isolation.

**RM-HTTP-CONFORMANCE-0005:** Policy tests cover redirects, origin/proxy challenges, replayable/non-replayable bodies, retries after every send milestone, hedging, downgrade/fallback, pooling/coalescing, alternative services, and unknown-effect preservation.

**RM-HTTP-CONFORMANCE-0006:** Cache tests cover freshness/age, validators, Vary, authorization, invalidation, partial responses, stale modes, disconnected behavior, partition isolation, corruption, eviction, collapse, and clock discontinuity.

**RM-HTTP-CONFORMANCE-0007:** Resource tests enforce head/body/decompression/compression/table/stream/connection/queue/time limits under slowloris, cancellation, overload, proxy failure, loss, reorder, migration, and shutdown.

**RM-HTTP-CONFORMANCE-0008:** Differential tests compare canonical semantic traces across providers and protocol versions, permitting only declared variance and never weaker security, authority, resource, or failure-evidence guarantees.

