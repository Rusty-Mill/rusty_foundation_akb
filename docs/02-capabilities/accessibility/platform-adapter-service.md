# Platform accessibility adapter service

| Field | Value |
|---|---|
| Status | Draft platform service 0.1.0 |

**RM-ACCESSIBILITY-ADAPTER-0001:** Resolution binds semantic contract version, native API/provider version, supported role/state/property/action/text mappings, event quality, virtualization, geometry, preference integration, process boundary, and known degradations.

**RM-ACCESSIBILITY-ADAPTER-0002:** The adapter translates one immutable semantic snapshot/revision into native provider objects. Native identities remain adapter-owned and map bijectively to live semantic identities within an adapter epoch.

**RM-ACCESSIBILITY-ADAPTER-0003:** Native queries execute from a bounded immutable/cached snapshot and never synchronously call arbitrary application code. Expensive realization/text work uses native asynchronous/deferred patterns where available or bounded responses.

**RM-ACCESSIBILITY-ADAPTER-0004:** Native role/control-type/pattern/interface differences are explicit mappings. The adapter may expose a platform extension but cannot strengthen the portable semantic claim or redefine application state.

**RM-ACCESSIBILITY-ADAPTER-0005:** Event translation preserves causality and required native ordering, coalesces only permitted classes, and resynchronizes after gaps. Duplicate native notifications do not imply duplicate domain actions.

**RM-ACCESSIBILITY-ADAPTER-0006:** Adapter failure/restart creates a new epoch, invalidates native objects/ranges safely, republishes a complete root snapshot, and never terminates the application UI solely because assistive infrastructure disconnected.

**RM-ACCESSIBILITY-ADAPTER-0007:** Cross-process queries/actions are bounded against denial of service, recursion, oversized text/tree requests, and malicious clients while remaining usable by legitimate assistive technology.

**RM-ACCESSIBILITY-ADAPTER-0008:** Diagnostics redact names, values, text, relations, geometry trails, and assistive-technology identities by default. Conformance fixtures use synthetic content.

**RM-ACCESSIBILITY-ADAPTER-0009:** A provider claim requires end-to-end tests with native inspection tools and representative assistive technologies; successful semantic-model unit tests alone are insufficient.

