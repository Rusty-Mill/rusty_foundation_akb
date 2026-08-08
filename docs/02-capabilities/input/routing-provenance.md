# Input routing, focus, capture, and provenance

## Provenance classes

| Class | Meaning |
|---|---|
| Hardware-associated | Native system associates event with physical/device input |
| System/accessibility | Generated or transformed by trusted OS/accessibility service |
| Remote | Originated through an identified remote-session path |
| Replay | Produced from a controlled test/recording source |
| Application synthetic | Injected by application/tooling authority |
| Unknown | Provider cannot prove a stronger origin |

Provenance is evidence, not authorization. Hardware-associated does not mean benign; synthetic does not mean prohibited.

**RM-INPUT-ROUTING-0001:** Routing binds an event to native seat/session, focused/captured window, routing revision, device epoch, and provenance before portable delivery. Application widget focus is not invented by the backend.

**RM-INPUT-ROUTING-0002:** Focus changes are ordered with affected input on the same native seat where evidence permits. Ambiguity is represented explicitly rather than assigning an event to a new target by delivery time.

**RM-INPUT-ROUTING-0003:** Capture, lock, confinement, background observation, and injection each require separate negotiated authority and effective-state observation. Capability possession for ordinary focused input does not imply them.

**RM-INPUT-ROUTING-0004:** Every event has a monotonically increasing stream sequence and monotonic timestamp domain. Native device timestamps are preserved with calibration/provenance when available.

**RM-INPUT-ROUTING-0005:** Delivery is non-reentrant and bounded. Coalescing follows event-class rules; overflow emits loss/reset before any later state-dependent event.

**RM-INPUT-ROUTING-0006:** Device identities are opaque, session-scoped by default, and minimized. Stable hardware identifiers, vendor/product/serial, and capability fingerprints require explicit purpose and authority.

**RM-INPUT-ROUTING-0007:** Accessibility-generated input follows normal focus and security policy while retaining provenance sufficient to avoid duplicate activation and to test assistive workflows.

**RM-INPUT-ROUTING-0008:** Shortcuts/commands are resolved above this layer from key/text/focus context and policy. The backend cannot reserve or consume portable commands except where the native system already did so and reports it.

