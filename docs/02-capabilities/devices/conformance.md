# Device discovery conformance specification

| Area | Required evidence |
|---|---|
| Queries | class/state/property/topology filters, unsupported predicates, limits, cancellation, permission scope |
| Snapshots | revision/coherence bounds, completeness, partial property failures, malformed values, redaction and namespace versions |
| Identity | removal/reinsert, ID/path reuse, driver restart, identical devices, virtual/aggregate nodes, stale/ambiguous resolution |
| Properties | type/unit/encoding, missing versus unsupported/redacted/error, volatility, length limits, sensitive-value handling |
| Topology | typed planes, multi-parent/cycles/missing ancestors, provenance, endpoint generations, inferred-edge nonclaims |
| Changes | registration/enumeration race, burst/coalescing, overflow, source restart, suspend/resume, bounded convergence |
| Lifecycle | concurrent enumerate/change/close, callback teardown, cancellation, provider loss, process shutdown |
| Handoff | class/generation revalidation, denied open, no guessed correlation, attenuated cross-process delegation |
| UX/privacy | identical labels, keyboard/AT selection, nonvisual change/error, diagnostic pseudonyms and cardinality bounds |

Test fixtures include built-in, removable, hot-pluggable, virtual, composite/multifunction, disabled, faulted, permission-hidden, and rapidly flapping devices where the platform supports them. Reports bind OS/build, architecture, privilege/container/session, provider and driver versions, selected namespaces/classes/properties, power state, and known virtualization or remote-session effects.

Model-based tests compare each published diff with fresh enumeration and verify eventual convergence after arbitrary duplicated, reordered, coalesced, or lost hints. Hardware-dependent claims require captured raw snapshots and change traces with sensitive identifiers redacted reproducibly.
