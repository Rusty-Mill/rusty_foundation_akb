# Printing and document-output conformance specification

| Area | Required evidence |
|---|---|
| Destination | local/network/virtual/offline queues, duplicate names/devices, generation reuse, format-sensitive capabilities, ready/configured state, notification loss |
| Ticket | required/preferred/default/prohibited, relational conflicts, substitutions, per-page overrides, stale-plan revalidation, native extensions |
| Document | known/streamed page counts, mixed geometry/orientation, page/sheet/impression units, deterministic replay, hostile fonts/images/profiles, resource loss |
| Rendering | vector/text/raster/transparency, clipping, scaling/imposition, page ranges, color/profile conversion, preview parity, bounded cancellation/backpressure |
| Job | partial/ambiguous submission, hold/release, stop/resume, cancel races, abort, provider restart/disappearance, duplicate policy, state/reason/count evidence |
| Artifact | atomic replacement/durability, metadata, accessible structure, embedding, encryption/signing nonclaims, virtual-queue distinction |
| Security/accessibility | authority separation, spool leakage/recovery, hostile parser/driver data, privacy redaction, accessible dialog/status/error/preview and output evidence |

Test fixtures cover zero/one/large page counts, empty ranges, mixed media, simplex/duplex, copies/collation, unavailable trays/finishings, monochrome/color, extreme resolution, offline/paper-out/jam/door/toner conditions where safely reproducible, sandbox/portal/headless sessions, service/driver restart, network partition, slow destination, and cancellation at every boundary.

Reports bind OS/build, print service/driver/filter/backend, destination/queue/device and generation evidence, protocol/transport, document format/profile/digest, ticket request/effective result, renderer/color/font versions, sandbox/session/authority, job state provenance, test fixtures, and every physical-output/fidelity/durability nonclaim. Synthetic content and accounts are used; reusable release/accounting secrets and user documents never enter evidence bundles.
