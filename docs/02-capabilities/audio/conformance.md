# Audio conformance specification

| Area | Required evidence |
|---|---|
| Devices | add/remove/default changes, identity reuse, generation invalidation, virtual/aggregate/Bluetooth endpoints, lost-event reconciliation |
| Formats | representation vectors, channel order/layout, interleaving, overflow/alignment, exact negotiation and rejected alternatives |
| Streams | state transitions, partial transfer, cancellation, backpressure, drain/stop, invalidation/reopen, no undisclosed conversion |
| Timing | frame-position monotonicity within generation, clock correlation uncertainty/drift, reset/rate change, latency-boundary labeling |
| Reliability | injected render underrun/capture overrun, discontinuity extent, recovery policy, route and service restart |
| Realtime | allocation/blocking/lock/I/O detectors, callback budget, panic containment, bounded queue overflow and generation retirement |
| Security/privacy | capture denial/consent/revocation, loopback separation, least authority, buffer retention/redaction, indicator behavior |
| Accessibility | keyboard/AT route controls, non-auditory state/error paths, mono/balance/hearing preference observation |
| Integration | suspend/resume, power mode, hotplug, UI dispatch, observability recursion, shutdown, plugin update and clock-domain correlation |

Providers test shared and supported exclusive/direct modes across built-in, USB, wireless, virtual, and aggregate devices where available. Reports bind OS/build, hardware/driver/transport, provider version, format, effective period/buffer, scheduling policy, power state, route, conversion graph, clock source, and every quality nonclaim.

Property and model tests vary sample rates, layouts, periods, queue depth, callback load, device loss, permission state, clock drift, and concurrent control changes. Failure injection is mandatory; a clean sine-wave playback demonstration is not conformance.
