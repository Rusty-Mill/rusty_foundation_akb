# Device discovery benchmark specification

| Benchmark | Measures |
|---|---|
| Enumeration | time and allocation distribution by device count, projected property set, topology depth, cold/warm cache |
| Change convergence | native hint to coherent snapshot publication under single, burst, flap, overflow, and source-restart cases |
| Diff cost | time/memory versus nodes, edges, changed properties, and generation replacements |
| Observer overhead | idle CPU/wakeups/memory/handles plus sustained burst queue behavior |
| Property retrieval | per-key latency, timeout/error rate, wake/power side effects, redaction cost |
| Scale | bounded behavior with virtual-device storms, deep topology, long/malformed values, and many subscribers |
| Shutdown | cancellation and observer-close latency with enumeration and callbacks in flight |

Reports provide p50/p95/p99/max, allocations, peak memory, native calls, dropped/coalesced hints, full rescans, time to convergence, and incomplete snapshots. Runs disclose hardware/VM/container/session context, device/class/property counts, cache state, power mode, privilege, OS/build, provider version, debounce policy, queue bounds, and injected load. Friendly-name or sensitive-property values are never benchmark labels.
