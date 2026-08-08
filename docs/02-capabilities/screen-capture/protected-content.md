# Protected content and capture exclusion

**RM-SCREEN-CAPTURE-PROTECTION-0001:** Protected media, secure desktop/UI, password surfaces, capture-exclusion requests, hardware overlays, rights policy, and provider filtering MUST be reported as separate mechanisms and evidence states.

**RM-SCREEN-CAPTURE-PROTECTION-0002:** Black, transparent, frozen, substituted, missing, or denied output MUST be distinguishable where the provider exposes the cause; otherwise the cause is unknown.

**RM-SCREEN-CAPTURE-PROTECTION-0003:** Successful capture MUST NOT claim completeness, and failed/blank capture MUST NOT claim confidentiality, secure redaction, or absence of sensitive content.

**RM-SCREEN-CAPTURE-PROTECTION-0004:** An application's capture-exclusion request is policy advice unless an end-to-end provider path proves enforcement across every supported capture mechanism, remote session, camera, plugin, and privileged observer.

**RM-SCREEN-CAPTURE-PROTECTION-0005:** Protected-path support MUST be negotiated across source, compositor, capture provider, memory, transform, encoder, transport, and sink. Any unproven link terminates the confidentiality claim.

**RM-SCREEN-CAPTURE-PROTECTION-0006:** Applications MUST NOT use screen capture as the sole mechanism for secret extraction prevention, DRM enforcement, trusted UI verification, or detection of hostile observation.

## Required reporting

Reports identify requested exclusion/protection, effective provider evidence, affected regions/streams when knowable, transition time, downgrade, and nonclaims. Security-sensitive workflows prevent secret display through domain policy and trusted boundaries instead of relying on capture behavior.
