# Recursive inspection graphs

**RM-CONTENT-GRAPH-0001:** Recursive inspection produces a graph, not only a tree: nodes bind byte subjects or derived streams; edges name contains, references, decodes-to, extracts-to, embeds, links, fetches, transforms-to, or aliases.

**RM-CONTENT-GRAPH-0002:** Node identity uses parent generation plus exact locator/range/entry identity and optional verified digest. Names alone cannot deduplicate or authorize access.

**RM-CONTENT-GRAPH-0003:** A shared transitive budget bounds depth, nodes, edges, bytes read/expanded/derived, ratio, references, network/provider calls, CPU, memory, storage, time, and diagnostics across archives, documents, messages, media, scripts, and nested encodings.

**RM-CONTENT-GRAPH-0004:** Cycles, repeated content, recursive self-reference, external links, missing/deferred nodes, passwords/keys, unsupported encodings, and provider failures yield explicit frontier evidence rather than silent omission.

**RM-CONTENT-GRAPH-0005:** External reference retrieval is a separate network/storage authority with URI policy, identity pinning, privacy partition, credentials, redirects, size/type limits, caching, and SSRF defenses; inspection is offline by default.

**RM-CONTENT-GRAPH-0006:** Aggregate policy distinguishes all-nodes, selected nodes, reachable-active nodes, launch-critical nodes, and incomplete frontier. A clean subset cannot be reported as a clean whole.

**RM-CONTENT-GRAPH-0007:** Findings preserve ancestry so callers can locate the containing artifact and exact nested path without treating hostile names as filesystem paths or executable links.
