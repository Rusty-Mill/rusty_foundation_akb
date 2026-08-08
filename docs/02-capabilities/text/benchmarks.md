# Text, fonts, and layout benchmark specification

**Status:** Draft

| ID | Workload | Measures |
|---|---|---|
| TEXT-BENCH-001 | Cold/warm font collection snapshot and match | latency, files/bytes touched, allocations, cache size |
| TEXT-BENCH-002 | Shaping by script and run length | scalars/glyphs per second, p50/p95/p99, allocations, cache hit |
| TEXT-BENCH-003 | Fallback-heavy and emoji/color text | face switches, shaping/raster latency, memory, glyph expansion |
| TEXT-BENCH-004 | Paragraph bidi/line layout | text per second, line count, memory, tail latency |
| TEXT-BENCH-005 | Incremental edit/reflow versus full | affected range, latency, cache invalidation, equality |
| TEXT-BENCH-006 | Hit testing/caret/selection geometry | queries per second, tail latency, allocation-free rate |
| TEXT-BENCH-007 | Glyph raster/cache at mixed scale | glyphs per second, upload bytes, cache hit/eviction, CPU/GPU/power |
| TEXT-BENCH-008 | Terminal grid shaping/damage workload | frame preparation, fallback runs, allocations, input-to-present contribution |

Results bind the exact corpus, Unicode/CLDR data, font artifacts, features, provider/library versions, CPU/GPU, OS, scale/raster policy, cold/warm cache state, sample method, and native baseline with equivalent semantics. Correct mappings and layout invariants are prerequisites to speed claims.

