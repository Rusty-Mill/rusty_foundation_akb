# Internationalization and localization benchmark specification

**Status:** Draft

| ID | Workload | Measures |
|---|---|---|
| I18N-BENCH-001 | Preference snapshot and locale-context resolution | cold/warm latency, data touched, allocations, cache hit |
| I18N-BENCH-002 | Resource/message lookup and plural/select format | messages/s, p50/p95/p99, allocations, fallback depth |
| I18N-BENCH-003 | Number/currency/unit/date/duration format | operations/s by style/locale, output bytes, allocations |
| I18N-BENCH-004 | Strict localized parsing | operations/s, rejection cost, ambiguity diagnostics, allocations |
| I18N-BENCH-005 | Instant/civil/time-zone/calendar conversion | operations/s, transition cache, data memory, update cost |
| I18N-BENCH-006 | Collation compare/sort-key/search | text units/s, sort throughput, key size, memory, version rebuild |
| I18N-BENCH-007 | Live locale/resource change and full UI reformat | semantic/layout convergence, frame stalls, peak memory, AT update latency |

Results bind exact BCP 47 inputs, locale context, resource bundle, Unicode/CLDR/tzdb/provider/OS versions, corpus/value distribution, calendar/zone/styles, cold/warm caches, concurrency, sample method, and equivalent native baseline. Correct fallback, grammatical result, ambiguity handling, and semantic/accessibility convergence are prerequisites to performance claims.

