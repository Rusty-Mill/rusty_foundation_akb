# Reading, indexing, and multipart containers

**RM-ARCHIVE-READ-0001:** Readers declare sequential, seekable, range-readable, or materialized source requirements. Providers cannot buffer an unbounded source to simulate seeking.

**RM-ARCHIVE-READ-0002:** Indexes and central directories are untrusted acceleration structures cross-checked against local headers, extents, source length, duplicate/overlap policy, encryption coverage, and entry data when read.

**RM-ARCHIVE-READ-0003:** Random access reports whether entry decode is independent, requires prior stream state/dictionary, or triggers bounded materialization. Complexity and remote range amplification remain observable.

**RM-ARCHIVE-MULTIPART-0001:** Split/multipart identity binds ordered volume identifiers, count or terminal discovery, exact lengths/digests, naming/mapping, availability, and source generation. Mixing volumes across generations is rejected.

**RM-ARCHIVE-MULTIPART-0002:** Missing, duplicate, reordered, truncated, replaced, or inaccessible volumes fail with recoverable evidence and cannot be treated as end-of-container.

**RM-ARCHIVE-READ-0004:** Nested containers consume a shared transitive budget across depth, expanded bytes, entries, references, time, CPU, memory, storage, and provider calls.

**RM-ARCHIVE-READ-0005:** Password/key prompts, remote volume fetch, dictionary retrieval, and content hydration are mediated interactions, never hidden inside an entry-read primitive.
