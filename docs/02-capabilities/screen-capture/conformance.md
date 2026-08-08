# Screen and window capture conformance specification

| Area | Required evidence |
|---|---|
| Selection/authority | trusted picker, cancel/deny/restrict, exact source kind/generation, enumeration separation, grant attenuation, revocation and indicator |
| Source boundary | display/window/application/region, decorations/popups/children/shadows, occlusion/minimized/offscreen, overlays, remote/virtual provenance |
| Frames | exact plane/stride/extent/alpha/memory/synchronization, valid content, stale padding, sequence/discontinuity, damage and immutable lifetime |
| Color/timing | SDR/HDR, color/range/reference white, provider transforms, timestamp boundary/domain/quality, correlation and drift |
| Cursor/audio | hidden/embedded/metadata cursor, shape/hotspot/scale/timing; system/app audio scope, PCM/clock/discontinuity; microphone separation |
| Change/load | resize/migration/topology/color/source changes, held buffers, slow/multiple consumers, bounded drop/degrade/copy policy |
| Protection | secure UI, protected media, capture exclusion, blank/substituted/denied output, explicit confidentiality and completeness nonclaims |
| Lifecycle/UX | start/suspend/resume/revoke/stop, lock/switch/sleep/provider/device loss, late callback rejection, accessible localized selection/indicator/control |

Fixtures include single/mixed-scale/HDR displays, rotated/mirrored/virtual/remote displays, decorated/transparent/minimized/offscreen/occluded windows, owned popups, rapid resize/migration, dynamic cursor shapes, system/app/protected audio, secure/protected surfaces, sandbox/portal flows, and denied/revoked policy.

Reports bind OS/build/session/compositor/portal, provider and GPU/driver, source kind and opaque generation, authority and indicator evidence, selection path, effective frame/color/cursor/audio configuration, queue/pool policy, clock sources, transformations, remote/virtual state, and every completeness/confidentiality nonclaim. Fault injection covers source reuse, topology loss, stale frames, timestamp reset, buffer starvation, consumer stalls, revocation, device/provider restart, and teardown races.
