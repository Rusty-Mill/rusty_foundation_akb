# Allocator service boundary

An allocator service composes virtual regions, policy, bookkeeping, and workload-specific allocation semantics. The architecture does not standardize a global allocator implementation before measured workloads justify it.

**RM-MEMORY-ALLOCATOR-0001:** An allocator contract states size/alignment limits, zero-size behavior, initialization, reallocation, failure policy, thread safety, ownership/deallocation pairing, fragmentation expectations, and observability.

**RM-MEMORY-ALLOCATOR-0002:** Allocation returns owned storage or a typed failure; library paths do not abort or invoke process-global OOM behavior unless the selected profile explicitly requires that policy.

**RM-MEMORY-ALLOCATOR-0003:** Memory obtained from one allocator is released only through its compatible owner. Crossing module/FFI boundaries uses explicit ownership functions and ABI/version identity.

**RM-MEMORY-ALLOCATOR-0004:** Secure, realtime, arena, executable, graphics, shared, and ordinary heap allocation are distinct workload contracts. One scalar “fast allocator” quality is prohibited.

**RM-MEMORY-ALLOCATOR-0005:** Allocation telemetry is bounded, recursion-safe, and privacy aware. Diagnostics do not inspect payload bytes by default.

