# Lazy, borrowed, and zero-copy decoding

**RM-INTERCHANGE-LAZY-0001:** Decoded representations declare owned/borrowed/shared/lazy state, backing buffer and schema lifetimes, mutability, thread/send/sync constraints, validation stage, and materialization behavior.

**RM-INTERCHANGE-LAZY-0002:** Borrowed views cannot outlive, mutate, remap, decrypt-away, recycle, or race their backing bytes; ownership and pinning are enforced by types or explicit checked leases.

**RM-INTERCHANGE-LAZY-0003:** Lazy decoding defers named work but still validates framing and all bounds needed for safe navigation; deferred fields can fail later with stable context and cannot bypass global resource limits.

**RM-INTERCHANGE-LAZY-0004:** Zero-copy claims name format/layout, alignment, endianness, contiguity, lifetime, validation, encryption/compression, trust, architecture, and access operation; fallback copying remains semantically equivalent and observable.

**RM-INTERCHANGE-LAZY-0005:** Index/table-of-contents and random-access metadata are untrusted, bounds-checked against content, protected by integrity where required, and prevented from causing overlapping/aliased mutable views.

**RM-INTERCHANGE-LAZY-0006:** Partial materialization, field projection, skipping, and predicate inspection preserve unknown/canonical/signature behavior or explicitly report that exact reserialization is unavailable.

**RM-INTERCHANGE-LAZY-0007:** Arena/pool/buffer reuse clears sensitive data as classified and prevents references from one message, tenant, generation, or thread observing another.
