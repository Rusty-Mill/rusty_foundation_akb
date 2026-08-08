# Shared memory and transfer

## Capability identity

`rm.memory.shared-region` owns anonymously or named/handle-backed shared bytes and explicit transfer authority.

**RM-MEMORY-SHARED-0001:** Creation specifies size, access directions, sealing/resize policy, inheritance/transfer policy, visibility namespace, persistence/lifetime, and protection. Named global discovery is not the baseline.

**RM-MEMORY-SHARED-0002:** Transfer produces a separately owned authority with no broader access than the source grant. Process inheritance and unrelated-process transfer are explicit allowlisted operations.

**RM-MEMORY-SHARED-0003:** Shared bytes convey no synchronization, message boundaries, initialization, schema version, endianness, pointer validity, object lifetime, trust, or crash consistency.

**RM-MEMORY-SHARED-0004:** Cross-process layouts use offset-based versioned representations and atomics/synchronization whose cross-process and cross-architecture properties are separately proven. Native pointers and Rust references are prohibited in interchange layouts.

**RM-MEMORY-SHARED-0005:** Resize/seal races are explicit. A view cannot silently outlive or exceed the backing object's valid extent, and truncation/fault risk is documented.

**RM-MEMORY-SHARED-0006:** Cleanup distinguishes closing one view, closing one backing handle, unlinking/discoverability removal, and final backing reclamation. No process assumes its close destroys other mappings.

