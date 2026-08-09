# Security and cross-cutting qualities

**RM-ARCHIVE-XCUT-0001:** Security review covers traversal, absolute/device paths, links/reparse/mount races, overwrite, case/Unicode collisions, special objects, privilege metadata, bombs, integer/offset overflow, overlap/polyglots, parser differential, weak encryption, credential oracle, signature-coverage confusion, temporary leakage, and unsafe post-extraction execution.

**RM-ARCHIVE-XCUT-0002:** Every operation has aggregate and per-entry limits for input/output bytes, ratio, entries, name/metadata size, nesting, frames/blocks/volumes, memory, allocation count, CPU/work, wall time, concurrency, open handles, temporary storage, filesystem objects, and diagnostics.

**RM-ARCHIVE-XCUT-0003:** Performance reports codec and container parse/encode/decode separately from source/sink I/O, hashing/authentication, metadata mapping, staging, commit, and durability. Throughput never hides time-to-first-output or tail/resource behavior.

**RM-ARCHIVE-XCUT-0004:** Observability records format/profile and provider generations, stage timings, byte/entry counters, limits approached/hit, mapping losses, integrity coverage, conflict/rejection classes, cleanup residuals, and sampled errors without names/content/credentials by default.

**RM-ARCHIVE-XCUT-0005:** User-facing listing, conflicts, progress, credential requests, warnings, and recovery are keyboard/screen-reader accessible, localizable, structured, and stable under large hostile name sets.

**RM-ARCHIVE-XCUT-0006:** Names and metadata preserve raw evidence separately from display strings. Locale never changes identity, path containment, canonical ordering, duplicate detection, or reproducible bytes.

**RM-ARCHIVE-XCUT-0007:** Parallel work is admission-controlled and fair across tenants/operations; one highly compressible, sparse, nested, encrypted, remote, or corrupt entry cannot monopolize memory, CPU, storage, or worker queues.
