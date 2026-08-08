# Camera and media-capture conformance specification

| Area | Required evidence |
|---|---|
| Discovery/authority | enumeration without activation, permission states/prompt policy, denial/revocation/restriction, indicator/shutter, device generation |
| Negotiation | exact requested/negotiated/effective format/rate, unsupported constraints, hidden conversion/processing detection |
| Frames | plane/stride/size overflow, valid region, sequence/discontinuity, corrupt/truncated, CPU/GPU memory lifetime and synchronization |
| Color/orientation | range/primaries/transfer/matrix, chroma siting, rotation/mirror/crop/clean aperture, HDR/unknown metadata |
| Timing | timestamp boundary/domain/quality, rate variability, drops/duplicates, clock correlation, restart/sleep/reconfiguration epochs |
| Controls | ranges/units/modes, clamp/override, auto/manual, transactional conflicts, application latency, concurrent external changes |
| Load | held buffers, slow/multiple consumers, drop/degrade policies, callback budget, bounded queues and memory |
| Lifecycle | start/stop, cancel, interruption, competing use, privacy switch, unplug, service/driver restart, shutdown and late callbacks |
| Security/UX | virtual provenance, frame/metadata redaction, delegation, background denial, keyboard/AT flows and nonvisual state |

Fixtures cover built-in, USB, virtual, multiple-camera, privacy-shutter, fixed/variable-rate, planar/packed, compressed-device-output, high-resolution/rate, HDR/depth where supported, sandbox/portal, remote session, and denied/revoked policy. Reports bind OS/build, device/firmware/driver/transport, provider and transformation graph, permission state, effective formats/controls, buffer mode/count, clock/timestamp source, power/thermal state, and all quality/privacy nonclaims.

Frame vectors verify plane arithmetic and color/orientation metadata. Fault injection covers delayed/duplicate/corrupt frames, buffer starvation, timestamp reset/drift, permission revocation, device loss, consumer stall, memory pressure, and shutdown races.
