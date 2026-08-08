# Memory and mapping conformance specification

| Area | Required evidence |
|---|---|
| Regions | page/granularity rounding, reserve/back/commit/decommit/release state, overflow, guard ranges |
| Protection | subranges, concurrent access coordination, inaccessible faults in subprocesses, cache synchronization |
| File maps | offsets/lengths, private/shared visibility, external write, truncate/replace, flush-stage claims |
| Shared | transfer/inheritance attenuation, independent lifetimes, seals/resize, cross-process layout/version tests |
| Residency | quota failure, lock quality, discard/reinitialize, no-dump inspection, pressure behavior |
| Large pages | required/preferred/fallback, privilege denial, size/alignment, fragmentation/resource accounting |
| Executable | default denial, W^X transitions, entitlement/policy denial, generation commit, stale writable alias checks |
| Allocator | alignment/zero/overflow/OOM/realloc, ownership mismatch defense, concurrency, recursion-safe telemetry |
| Lifecycle | process transfer, fork/spawn policy, crash-dump privacy, shutdown cleanup, suspend/pressure |

Dangerous access tests execute in sacrificial subprocesses. Reports bind OS/build, architecture, page/allocation/large-page sizes, overcommit/swap/compression policy, limits/privileges/entitlements, filesystem/backing type, security hardening, allocator/provider versions, and every degraded assertion.

