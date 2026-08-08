# `rm.graphics.resource-memory`

| Field | Value |
|---|---|
| Status | Draft |
| Contract version | 0.1.0 |

**RM-GRAPHICS-MEMORY-0001:** Every buffer, image, sampler, pipeline, and synchronization resource belongs to exactly one device epoch and carries immutable creation properties plus explicit mutable state ownership.

**RM-GRAPHICS-MEMORY-0002:** Allocation declares size, alignment, format/layout, usage, residency class, CPU visibility/coherency, sharing, initialization, exportability, protection, and budget policy. Unsupported required combinations fail without partial publication.

**RM-GRAPHICS-MEMORY-0003:** Newly allocated content is initialized, cleared, or explicitly classified undefined. Protected or cross-trust resources never expose prior allocation contents.

**RM-GRAPHICS-MEMORY-0004:** Mapping defines byte range, access direction, coherency/flush/invalidate obligations, concurrency, and behavior during device loss. A mapped pointer never outlives its lease or device epoch.

**RM-GRAPHICS-MEMORY-0005:** Resource state/layout and queue ownership transitions are explicit submission dependencies. A backend may optimize them but cannot infer correctness from incidental prior use.

**RM-GRAPHICS-MEMORY-0006:** Destruction is logically immediate but physical reclamation may wait for proven completion. The provider retains no consumer reference after reclamation and exposes bounded deferred-destruction pressure.

**RM-GRAPHICS-MEMORY-0007:** Memory-budget exhaustion, eviction, residency failure, fragmentation, and system allocation failure are distinct typed outcomes where provider evidence permits. Retryability is never inferred from `out of memory` alone.

**RM-GRAPHICS-MEMORY-0008:** Import/export is a separate advanced contract identifying handle type, ownership transfer, security boundary, synchronization, format/modifier, device compatibility, and revocation. Base resources are non-exportable.

**RM-GRAPHICS-MEMORY-0009:** Readback, capture, crash dump, and diagnostic paths enforce resource content classification. Protected resources cannot enter ordinary readback or telemetry paths.

