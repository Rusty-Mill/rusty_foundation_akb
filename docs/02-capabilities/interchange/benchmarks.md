# Benchmarks

**RM-INTERCHANGE-BENCH-0001:** Benchmarks publish hardware/OS/architecture, implementation/version/options, schema/format/profile, dataset/value distributions, encoded sizes, ownership/lifetime, validation/canonicalization, streaming chunks, warmup, repetitions, and uncertainty.

**RM-INTERCHANGE-BENCH-0002:** Encode/decode reports throughput and latency distributions, bytes, peak/retained memory, allocations/copies, CPU/cache/SIMD, energy, startup/schema resolution, and correctness across scalar, nested, wide, deep, repeated, map, binary/text, and unknown-heavy values.

**RM-INTERCHANGE-BENCH-0003:** Streaming trials vary chunk/frame/message size, backpressure, partial input/output, cancellation, concurrency, compression, and async/sync paths while measuring time-to-first/complete value and bounded buffering.

**RM-INTERCHANGE-BENCH-0004:** Canonicalization/transcoding reports sort/buffer/spill and multiple-pass costs, exact output, loss classes, numeric/Unicode/map distributions, unknowns/extensions, source/target sizes, and comparison verification.

**RM-INTERCHANGE-BENCH-0005:** Hostile-input trials measure bounded time/memory/diagnostics under maximum depth/length/digits/fields, duplicates/collisions, invalid UTF/tags/offsets, decompression, lazy random access, and fuzz corpora without using crashes as throughput.

**RM-INTERCHANGE-BENCH-0006:** Registry/generation trials measure cold/warm resolution, authenticated cache, compatibility checks, dependency graphs, generation, outage/failover, and large fleet schema rollout.

**RM-INTERCHANGE-BENCH-0007:** Faster results that weaken validation, unknown preservation, canonical bytes, compatibility, lifetime safety, privacy, or limits are failures and remain outside performance comparisons.
