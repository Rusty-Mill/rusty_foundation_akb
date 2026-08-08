# Remote presentation and controlled input conformance specification

| Area | Required evidence |
|---|---|
| Session/authority | view/control/device separation, participant/channel binding, role changes, expiry/revoke, interactive versus unattended, multi-participant arbitration |
| Presentation | capture-to-remote generations/milestones, crop/scale/color/cursor/audio, loss/congestion/adaptation, protected-content nonclaims |
| Injection | keyboard/pointer/scroll/touch/pen/text capabilities, admission/execution validation, attribution, partial/unknown outcomes, native scope |
| Mapping | stream-relative absolute/relative coordinates, resize/crop/rotation/scale/topology revisions, keymap/layout/IME/text, stale-event rejection |
| State/order | press/release/contact machines, frames/sequences, reorder/loss/duplicate/late events, reconnect generations, bounded queues and cleanup |
| Boundaries | focus races, local input precedence, lock/switch/secure input/elevation/permission UI, integrity/sandbox/compositor denial, emergency stop |
| Security/UX | peer/channel replay defense, audit redaction, indicators, consent expansion, localized keyboard/screen-reader flows, assistive-technology coexistence |

Fixtures cover view-only/control transitions, multiple and replaced peers, mixed-scale/rotated/remote displays, rapid resize/crop, every supported input class, layout/IME/lock-state changes, key/button/contact loss, high-rate motion, congestion/reconnect, local-user conflict, lock/switch/secure/elevated surfaces, sandbox/integrity denial, capture protection, and emergency revocation.

Reports bind OS/build/session/compositor, provider/portal, local security-context generation, source/session/participant/channel/virtual-device generations, authority manifest, transport/codec/configuration, coordinate/keymap revisions, queue/rate policy, native injection scope, indicator/stop evidence, and all delivery/provenance/security nonclaims. Fault injection covers replay, forged role, stale generation, packet reorder/duplication/loss, held key/contact, focus theft, policy race, transport replacement, provider crash, and shutdown races.
