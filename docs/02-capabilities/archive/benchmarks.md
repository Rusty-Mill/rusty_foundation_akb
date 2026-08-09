# Benchmarks

**RM-ARCHIVE-BENCH-0001:** Codec workloads vary corpus type/compressibility, size, frame/block/window, level/strategy, dictionary, checksum, chunking, sync/async, concurrency, cold/warm state, and hardware acceleration while reporting encode/decode latency distributions, time to first/last byte, goodput, ratio, CPU, allocations, peak memory, energy, and output correctness.

**RM-ARCHIVE-BENCH-0002:** Container workloads separately measure open/header/index/list, sequential and random entry read, remote ranges, create/finalize, metadata mapping, nested traversal, split volumes, encryption/authentication, digest/signature verification, and close/cancel.

**RM-ARCHIVE-BENCH-0003:** Extraction workloads vary entry count/size distribution, directory depth, metadata richness, duplicates/conflicts, links/sparse files, destination filesystem, free space, overwrite policy, staging topology, durability, antivirus/indexing, concurrency, and cache state.

**RM-ARCHIVE-BENCH-0004:** Adversarial trials measure bounded rejection cost for corrupt indexes, misleading sizes, high expansion, excessive nesting/entries/metadata, path collisions, unavailable volumes/dictionaries/keys, slow I/O, integrity failures, and cancellation at every milestone.

**RM-ARCHIVE-BENCH-0005:** Native/provider comparisons use identical bytes, semantic profile, budgets, integrity checks, metadata policy, staging/commit/durability boundary, and correctness assertions. Missing safety or quality is not scored as speed.

**RM-ARCHIVE-BENCH-0006:** Reports identify hardware/architecture, OS/build/filesystem/options, provider/library/version, corpus digests, format/profile, codec/dictionary/parameters, source/sink topology, memory/thread limits, warmup/repetitions, uncertainty, outliers, and telemetry overhead.
