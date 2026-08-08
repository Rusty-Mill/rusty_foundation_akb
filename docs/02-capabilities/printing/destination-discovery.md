# Destination discovery and capability snapshots

`rm.print.destination-observer` exposes queues and virtual/file destinations visible within an explicit user/session/network scope. Observation neither connects to a device nor grants submission.

**RM-PRINT-DESTINATION-0001:** A reference MUST include provider, queue/destination identity, generation, observation scope/revision, kind, availability, provenance, and stability claim.

**RM-PRINT-DESTINATION-0002:** Queue identity, physical device identity, URI, display name, driver, endpoint, and location MUST remain distinct. Matching names, addresses, serials, or capabilities do not prove sameness.

**RM-PRINT-DESTINATION-0003:** A capability snapshot MUST bind destination generation, query time, provider, selected document format, supported/default ticket dimensions, ready/configured distinctions, constraint relationships, state/reasons, and unknown or withheld values.

**RM-PRINT-DESTINATION-0004:** Media, trays, finishings, duplex, copies, page ranges, orientation, scaling, resolution, color, quality, collation, output bin, accounting, authentication, and secure-release support are independent typed dimensions. Providers MUST NOT invent defaults for unavailable dimensions.

**RM-PRINT-DESTINATION-0005:** Discovery and state notifications are invalidation hints. Loss, coalescing, reconnect, driver/service restart, configuration change, and generation mismatch require full snapshot reconciliation.

**RM-PRINT-DESTINATION-0006:** Optional status collection MUST avoid waking sleeping devices, network scanning, credential prompts, or disclosure of sensitive queue/job state unless explicitly selected and authorized.

See [ADR-0064](../../adr/0064-print-plans-bind-destination-generation-and-format.md).
