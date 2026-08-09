# Cross-cutting qualities

**RM-CONTENT-XCUT-0001:** Security review covers signature/magic bypass, parser differential/polyglots, malformed/nested bombs, archive traversal, external references/SSRF, active content, exploit-triggering previews, provider compromise, verdict spoofing, stale caches, origin laundering, quarantine clearing, cloud disclosure, confused deputies, and unsafe derived artifacts.

**RM-CONTENT-XCUT-0002:** Every operation bounds input/ranges/seeks, expanded/derived bytes, graph depth/nodes/edges, parser objects, strings/metadata, CPU/work, memory, allocations, storage, handles/processes, network/provider calls, concurrency, wall time, output, and diagnostics.

**RM-CONTENT-XCUT-0003:** Restricted providers use least privilege, separate identities and scratch roots, authenticated request/result framing, immutable inputs where possible, output quotas, kill deadlines, crash-loop isolation, version pinning, signed deployment, and auditable updates.

**RM-CONTENT-XCUT-0004:** Observability records stage latency, bytes/ranges, graph frontier, candidates/conflicts, provider/database/policy generations, verdict class, cache/freshness, restrictions, transformations/loss, resource limits, and failures without content, paths, URIs, credentials, or sensitive findings by default.

**RM-CONTENT-XCUT-0005:** Security warnings, evidence conflicts, password/provider needs, preview omissions, transformation loss, quarantine/override, progress, and recovery are accessible, localized, structured, non-color-only, keyboard-operable, and resistant to hostile names/content mimicking trusted UI.

**RM-CONTENT-XCUT-0006:** Locale affects display only. Detection rules, identity, hashes, byte offsets, path safety, policy keys, ordering, and reproducible transformation do not depend on user locale unless an exact textual profile says so.

**RM-CONTENT-XCUT-0007:** Fair admission prevents one tenant or hostile subject from monopolizing parsers, scanners, cloud quota, memory, storage, CPU/GPU, network, or worker processes; overload returns typed retry/unknown outcomes rather than implicit allow.
