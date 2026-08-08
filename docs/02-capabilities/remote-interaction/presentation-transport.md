# Presentation pipeline and transport boundary

Remote presentation composes [screen capture](../screen-capture/README.md), optional cursor/audio streams, transforms, codecs, transport, remote decoding, and presentation. No stage is hidden inside input authority.

**RM-REMOTE-INTERACTION-PRESENT-0001:** The pipeline MUST preserve source/session/configuration generations, frame sequence/discontinuity, damage, color, timing, cursor mode, transformations, codec configuration, transport loss, and remote presentation milestones.

**RM-REMOTE-INTERACTION-PRESENT-0002:** Capture, encode acceptance, packet submission, peer receipt, decode, composition, and remote presentation MUST remain distinct evidence boundaries.

**RM-REMOTE-INTERACTION-PRESENT-0003:** Transport confidentiality/integrity and peer authentication MUST be separately negotiated and bound to the participant/session. Capture authority does not authorize network disclosure.

**RM-REMOTE-INTERACTION-PRESENT-0004:** Resolution, rate, crop, color, cursor, audio, and quality adaptation MUST preserve a revisioned mapping to the controlled source; stale remote coordinates cannot be applied after an incompatible revision.

**RM-REMOTE-INTERACTION-PRESENT-0005:** Protected, secure, omitted, substituted, or unknown capture output retains every screen-capture nonclaim after encoding and transport. A black frame is not proof of confidentiality.

**RM-REMOTE-INTERACTION-PRESENT-0006:** Backpressure and congestion MUST be bounded across capture, encode, transport, decode, and presentation, with explicit drop/coalesce/degrade policy and no unbounded latency accumulation.

The base slice does not select a codec, container, signaling protocol, NAT traversal mechanism, or conferencing topology. Those are workload-specific compositions governed by media, networking, identity, and supply-chain contracts.
