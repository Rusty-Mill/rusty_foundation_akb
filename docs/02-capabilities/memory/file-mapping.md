# File mappings and persistence

## Capability identity

`rm.memory.file-mapping` creates a mapped view over an explicitly authorized file resource.

**RM-MEMORY-FILEMAP-0001:** Inputs include file authority, offset, requested length, shared/private visibility, access/protection, extension policy, durability intent, and truncation policy. Offset alignment and effective mapped/usable ranges are explicit.

**RM-MEMORY-FILEMAP-0002:** Mapping a file does not freeze file identity, size, content, or namespace. Providers state behavior when the file is truncated, replaced, externally modified, or storage becomes unavailable; unsafe access may fault.

**RM-MEMORY-FILEMAP-0003:** Private/copy-on-write modifications are not file writes. Shared visibility to other mappings, writeback scheduling, filesystem visibility, and durable storage are separate milestones.

**RM-MEMORY-FILEMAP-0004:** A flush request reports the strongest proven stage: requested, dirty pages submitted, mapping writeback completed, file synchronized, or directory/namespace durability composed through filesystem services.

**RM-MEMORY-FILEMAP-0005:** Concurrent mapped and ordinary file I/O follows only the coherence guarantees documented for the selected provider/filesystem. Portable code supplies synchronization and cannot assume atomic multi-byte updates.

**RM-MEMORY-FILEMAP-0006:** Safe typed views require bounds, alignment, initialized-byte, representation, aliasing, mutability, and concurrency invariants established by a higher-level adapter. The base mapping exposes bytes, not arbitrary typed objects.

