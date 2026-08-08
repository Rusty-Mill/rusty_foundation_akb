# Capture devices, authorization, and sessions

`rm.capture.device-observer` projects camera-specific capabilities from [general device discovery](../devices/README.md) when correlation is proven. Observation does not activate the camera, illuminate an indicator, prompt, or claim exclusive access.

**RM-CAPTURE-AUTH-0001:** Camera observation MUST distinguish device generation, position/facing when known, transport/virtual status, availability, and capability-summary provenance without opening a capture stream.

**RM-CAPTURE-AUTH-0002:** Permission state MUST distinguish not-determined, authorized, denied, restricted/policy-controlled, unavailable, and unknown. Observation MUST NOT itself request permission.

**RM-CAPTURE-AUTH-0003:** A permission request MUST be an explicit user-interaction operation with declared purpose, foreground/session policy, cancellation, localization, and accessible explanation.

**RM-CAPTURE-AUTH-0004:** Capture authority MUST bind principal, media class, purpose, device or selection scope, allowed outputs/metadata, lifetime, delegation, and revocation policy.

**RM-CAPTURE-AUTH-0005:** Session start MUST revalidate current device generation and native authority. Prior authorization, a `DeviceRef`, or a previously running session MUST NOT bypass current enforcement.

**RM-CAPTURE-AUTH-0006:** Revocation, privacy switch/shutter, system interruption, device loss, competing exclusive use, and policy change MUST invalidate or suspend the session with distinguishable evidence.

See [ADR-0056](../../adr/0056-capture-authority-is-session-scoped-and-revocable.md).
